import fs from "node:fs/promises";
import path from "node:path";
import { pathToFileURL } from "node:url";
import { createRequire } from "node:module";

const requireFromWorkspace = createRequire(path.join(process.cwd(), "package.json"));
const { chromium } = requireFromWorkspace("playwright");
const pptxgen = requireFromWorkspace("pptxgenjs");

const DEFAULT_WIDTH = 1920;
const DEFAULT_HEIGHT = 1080;
const DEFAULT_SLIDE_W = 13.333333;
const DEFAULT_SLIDE_H = 7.5;

function parseArgs(argv) {
  const args = {
    width: DEFAULT_WIDTH,
    height: DEFAULT_HEIGHT,
    includeNotes: true,
  };

  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    const next = argv[i + 1];
    if (arg === "--topic") args.topic = next, i += 1;
    else if (arg === "--overview") args.overview = next, i += 1;
    else if (arg === "--out") args.out = next, i += 1;
    else if (arg === "--screens-dir") args.screensDir = next, i += 1;
    else if (arg === "--expected-slides") args.expectedSlides = Number(next), i += 1;
    else if (arg === "--width") args.width = Number(next), i += 1;
    else if (arg === "--height") args.height = Number(next), i += 1;
    else if (arg === "--no-notes") args.includeNotes = false;
    else if (arg === "--help" || arg === "-h") args.help = true;
    else throw new Error(`Unknown argument: ${arg}`);
  }

  return args;
}

function printHelp() {
  console.log(`Usage:
  node export_overview_to_pptx.mjs --topic <topic-name> [--expected-slides 34]
  node export_overview_to_pptx.mjs --overview <path> --out <path>

Options:
  --topic <name>              Uses topics/<name>/overview.html
  --overview <path>           Direct path to overview.html
  --out <path>                Output .pptx path
  --screens-dir <path>        Screenshot output directory
  --expected-slides <number>  Fail when data-slide count differs
  --width <px>                Capture width, default 1920
  --height <px>               Capture height, default 1080
  --no-notes                  Skip speaker notes`);
}

function resolveConfig(args) {
  const root = process.cwd();
  if (!args.topic && !args.overview) {
    throw new Error("Provide --topic or --overview.");
  }

  const topicDir = args.topic ? path.join(root, "topics", args.topic) : path.dirname(path.resolve(args.overview));
  const overview = path.resolve(args.overview || path.join(topicDir, "overview.html"));
  const inferredTopic = args.topic || path.basename(topicDir);
  const outDir = path.join(topicDir, "exports", "pptx");

  return {
    root,
    topic: inferredTopic,
    topicDir,
    overview,
    out: path.resolve(args.out || path.join(outDir, `${inferredTopic}.pptx`)),
    screensDir: path.resolve(args.screensDir || path.join(outDir, "slides")),
    expectedSlides: Number.isFinite(args.expectedSlides) ? args.expectedSlides : null,
    width: Number.isFinite(args.width) ? args.width : DEFAULT_WIDTH,
    height: Number.isFinite(args.height) ? args.height : DEFAULT_HEIGHT,
    includeNotes: args.includeNotes,
  };
}

async function ensureInput(config) {
  await fs.access(config.overview);
  await fs.mkdir(config.screensDir, { recursive: true });
  await fs.mkdir(path.dirname(config.out), { recursive: true });
}

async function waitForAssets(page) {
  await page.evaluate(async () => {
    if (document.fonts?.ready) await document.fonts.ready;
    await Promise.all(
      Array.from(document.images)
        .filter((img) => !img.complete)
        .map((img) => new Promise((resolve) => {
          img.addEventListener("load", resolve, { once: true });
          img.addEventListener("error", resolve, { once: true });
        }))
    );
  });
}

async function getSlideNumbers(page) {
  return page.evaluate(() => {
    const numbers = Array.from(document.querySelectorAll("#detail-frame .scene[data-slide]"))
      .map((scene) => Number(scene.dataset.slide))
      .filter((n) => Number.isFinite(n));
    return [...new Set(numbers)].sort((a, b) => a - b);
  });
}

async function injectExportCss(page, config) {
  await page.addStyleTag({
    content: `
      html, body {
        width: ${config.width}px !important;
        height: ${config.height}px !important;
        margin: 0 !important;
        padding: 0 !important;
        overflow: hidden !important;
        background: #ffffff !important;
      }
      .strip, .main-header, .aim-overlay, .aim-tooltip, .aim-toast {
        display: none !important;
      }
      .main, .detail, .detail-frame {
        position: fixed !important;
        inset: 0 !important;
        width: ${config.width}px !important;
        height: ${config.height}px !important;
        min-width: ${config.width}px !important;
        min-height: ${config.height}px !important;
        max-width: ${config.width}px !important;
        max-height: ${config.height}px !important;
        margin: 0 !important;
        padding: 0 !important;
        border: 0 !important;
        border-radius: 0 !important;
        box-shadow: none !important;
        overflow: hidden !important;
        background: #ffffff !important;
        display: block !important;
        transform: none !important;
        container-type: normal !important;
      }
      #detail-frame > .scene {
        position: absolute !important;
        inset: 0 auto auto 0 !important;
        width: ${config.width}px !important;
        height: ${config.height}px !important;
        transform: none !important;
        transform-origin: top left !important;
        display: none !important;
      }
      #detail-frame > .scene.export-active {
        display: flex !important;
      }
      #detail-frame > .scene.export-active .speaker-note {
        display: none !important;
      }
    `,
  });
}

async function activateSlide(page, slideNumber) {
  await page.evaluate((n) => {
    document.querySelectorAll("#detail-frame .scene").forEach((scene) => {
      scene.classList.remove("active", "export-active");
      if (Number(scene.dataset.slide) === n) {
        scene.classList.add("active", "export-active");
      }
    });
  }, slideNumber);
  await page.waitForTimeout(160);
}

async function captureSlides(config) {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({
    viewport: { width: config.width, height: config.height },
    deviceScaleFactor: 1,
  });
  page.setDefaultTimeout(30000);

  await page.goto(pathToFileURL(config.overview).href, { waitUntil: "networkidle" });
  await waitForAssets(page);
  await injectExportCss(page, config);

  const slideNumbers = await getSlideNumbers(page);
  if (config.expectedSlides !== null && slideNumbers.length !== config.expectedSlides) {
    throw new Error(`Expected ${config.expectedSlides} slides, found ${slideNumbers.length}: ${slideNumbers.join(", ")}`);
  }

  const captures = [];
  for (const slideNumber of slideNumbers) {
    await activateSlide(page, slideNumber);
    const screenshotPath = path.join(config.screensDir, `slide-${String(slideNumber).padStart(2, "0")}.png`);
    await page.locator("#detail-frame").screenshot({ path: screenshotPath, animations: "disabled" });
    const note = config.includeNotes ? await page.evaluate((n) => {
      const scene = Array.from(document.querySelectorAll("#detail-frame .scene"))
        .find((el) => Number(el.dataset.slide) === n);
      return scene?.querySelector(".speaker-note")?.textContent?.trim() || "";
    }, slideNumber) : "";
    captures.push({ slideNumber, screenshotPath, note });
    console.log(`captured slide ${String(slideNumber).padStart(2, "0")}`);
  }

  await browser.close();
  return captures;
}

async function buildPptx(config, captures) {
  const pptx = new pptxgen();
  pptx.layout = "LAYOUT_WIDE";
  pptx.author = "Codex";
  pptx.company = "LSW_Coding";
  pptx.subject = config.topic;
  pptx.title = config.topic;
  pptx.lang = "ko-KR";
  pptx.theme = {
    headFontFace: "Pretendard",
    bodyFontFace: "Pretendard",
    lang: "ko-KR",
  };

  for (const capture of captures) {
    const slide = pptx.addSlide();
    slide.background = { color: "FFFFFF" };
    slide.addImage({
      path: capture.screenshotPath,
      x: 0,
      y: 0,
      w: DEFAULT_SLIDE_W,
      h: DEFAULT_SLIDE_H,
    });
    if (capture.note) slide.addNotes(capture.note);
  }

  await pptx.writeFile({ fileName: config.out });
  return config.out;
}

const args = parseArgs(process.argv.slice(2));
if (args.help) {
  printHelp();
  process.exit(0);
}

const config = resolveConfig(args);
await ensureInput(config);
const captures = await captureSlides(config);
const output = await buildPptx(config, captures);
console.log(`pptx: ${output}`);
