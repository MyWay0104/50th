# Ex2 Success Pattern

Use this reference when reproducing the successful `ex2` result from `why-ai-49th-oxxodok-airbnb`.

## Source Split

For the updated `ex2.jpg` source at `751x1497`, the successful crops were:

- question box: `275,42,745,692`
- answer box: `38,710,728,1430`
- question output: `470x650`
- answer output: `690x720`

The exact command:

```powershell
python <skill-dir>\scripts\split_capture.py `
  --source topics\why-ai-49th-oxxodok-airbnb\pictures\ex2.jpg `
  --question-out topics\why-ai-49th-oxxodok-airbnb\pictures\ex2-question.jpg `
  --answer-out topics\why-ai-49th-oxxodok-airbnb\pictures\ex2-answer.jpg `
  --question-box 275,42,745,692 `
  --answer-box 38,710,728,1430 `
  --question-size 470x650 `
  --answer-size 690x720
```

## Successful Layout Measurements

In the overview renderer, the successful layout had approximately:

- placeholder right gap: `26px`
- placeholder bottom gap: `21px`
- answer image left/right internal whitespace: `1px / 1px`
- question image fully inside frame: true
- answer image fully inside frame: true
- overlap width: about `28px`

Treat these as targets, not hard rules. Preserve readability over matching exact numbers.
