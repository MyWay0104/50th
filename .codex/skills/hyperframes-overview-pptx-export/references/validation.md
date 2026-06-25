# Validation Reference

Use these checks after exporting a HyperFrames overview deck to PPTX.

## Count screenshots

```powershell
$screens = "topics\<topic>\exports\pptx\slides"
(Get-ChildItem $screens -Filter "slide-*.png").Count
```

## Check PPT internals

```powershell
Add-Type -AssemblyName System.IO.Compression.FileSystem
$ppt = "topics\<topic>\exports\pptx\<topic>.pptx"
$zip = [System.IO.Compression.ZipFile]::OpenRead((Resolve-Path $ppt))
try {
  $slides = ($zip.Entries | Where-Object { $_.FullName -match '^ppt/slides/slide\d+\.xml$' }).Count
  $notes = ($zip.Entries | Where-Object { $_.FullName -match '^ppt/notesSlides/notesSlide\d+\.xml$' }).Count
  $media = ($zip.Entries | Where-Object { $_.FullName -match '^ppt/media/' }).Count
  [pscustomobject]@{ Slides = $slides; Notes = $notes; Media = $media }
} finally {
  $zip.Dispose()
}
```

## Check PNG dimensions with Node

```powershell
node -e "const fs=require('fs'); for (const f of process.argv.slice(1)) { const b=fs.readFileSync(f); console.log(f, b.readUInt32BE(16)+'x'+b.readUInt32BE(20), b.length); }" `
  topics\<topic>\exports\pptx\slides\slide-01.png `
  topics\<topic>\exports\pptx\slides\slide-19.png `
  topics\<topic>\exports\pptx\slides\slide-34.png
```
