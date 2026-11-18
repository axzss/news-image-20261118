[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/axzss/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/axzss/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

# news-image-20261118 — The World, Wednesday 18 November 2026

A one-page newspaper-style summary of the world's news of Wednesday 18 November 2026, as a single 1024×1024 PNG. `main.py` copies the bundled image to `/output/entry.png` — deterministic, no network, no randomness.

Built early on 18 November (around 02:20 UTC) from what had been reported so far that day; the day's later news is not in it.

## The seven stories

1. **Top story — Middle East / Gulf:** Iran drones target a U.S. radar in Bahrain; Bahrain intercepts them and Kuwait reports its own interceptions. *(Reuters)*
2. **Ukraine / War:** Ukraine hits the Crimea bridge for a second day as Russia keeps pounding Kyiv's bridges. *(The Times of India)*
3. **Business / Tech:** Nvidia revenue jumps 103% to $115.8 billion in quarterly sales; the firm will not reinstate ex-CEO Jensen Huang. *(AppiSToS, UK press)*
4. **Asia / Diplomacy:** Trump in Manila for Quad talks ahead of his China trip; praises Australia's Albanese before the APEC summit in Shenzhen. *(AP, The West Australian)*
5. **Middle East / Sanctions:** Britain and Australia sanction firms building Israeli settlements in the West Bank. *(AP, The West Australian)*
6. **Trade — China / Canada:** Canada and China extend trade deals as Xi meets Carney ahead of APEC. *(The Times of India)*
7. **Space:** Voyager 1 nears one light-day from Earth — the first human-made object that far. *(The West Australian)*

The image is drawn programmatically with Pillow (`render.py`) from verified reporting on the day — every word is real text, no AI-generated imagery, so nothing is garbled.

## Run

```sh
python3 main.py
# writes /output/entry.png (1024x1024 PNG, ~121 KB)
```

Run it twice and the output bytes are identical (`sha256sum` matches).

## Bounty

Built for the make.fun bounty: https://make.fun/bounty/news-image-20261118

Optional: earn referral rewards, a second way to make money — join make.fun with referral code `1409h78a`: https://make.fun/r/1409h78a
