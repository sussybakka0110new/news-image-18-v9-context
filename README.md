# news-image-18-v9-context

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/sussybakka0110new/news-image-18-v9-context/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/sussybakka0110new/news-image-18-v9-context/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

A 1024x1024 front page summing up the world news of Wednesday 18 November 2026: a navy date band; three original flat-SVG hero scenes, each with a one-line title and a two-line context caption; nine numbered top stories, each pairing a small, natural-ratio flat-SVG scene icon (with its number badge attached) to the left of its own headline and a short fact blurb; a "by the numbers" strip; a bold blue monospaced ASCII world map with 20 numbered location pins; 26 more briefs and a sourced footer. Rendered with Chromium and real DejaVu fonts.

Illustrations are original flat SVG art drawn at their native viewBox proportions (no horizontal stretching); icons are near-square scenes enriched with story context rather than single flat silhouettes.

## Run it

```sh
mkdir -p /output && python3 main.py
```

`main.py` is standard-library only. It copies the committed `entry.png` to the runner output directory and refuses an empty file, a file over 1 MiB, or anything that is not a complete PNG/JPEG.

## Render

```sh
chromium --headless --no-sandbox --hide-scrollbars --force-device-scale-factor=1 \
  --window-size=1024,1024 --screenshot=entry.png render.html
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=kk7jw559&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
