# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/shin9898/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/shin9898/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A one-page "front page" of the world's news on **Friday 20 November 2026**: a Russian missile
landing in Poland during one of the war's largest air attacks on Ukraine, the AI-led sell-off on
Wall Street, the UK–EU post-Brexit reset deal, COP31 running into overtime, Trump's threatened tax
on US data centres abroad and a claimed AI-assisted proof of the Riemann hypothesis.

![entry](assets/entry.png)

- `main.py` (Python 3.13, standard library only) copies `assets/entry.png` to `/output/entry.png`.
  The copy is byte-for-byte, so every run writes the same file.
- `build/render.py` draws the page with Pillow at build time; `build/stories.py` holds every
  headline and figure with the reports it was checked against (BBC, DW, Al Jazeera, France 24, CNBC).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png (/output in the grader)
```

Rebuild the image (macOS system fonts, Pillow):

```sh
python3 -m venv .venv && .venv/bin/pip install pillow && .venv/bin/python build/render.py
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
