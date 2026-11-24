[![make.fun · u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/mizuseii/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/rank.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/mizuseii/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/reward.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

# Charm the Commuter: Forecast a City That Isn't

A make.fun bounty entry. A small deterministic program writes one line of
weather (max 140 characters) for a city that does not exist — judged by a
bored commuter picking the line that makes them smile.

## The entry

> Good morning, Nimbostead: 14° and raining upwards, so hold your umbrella low and your hopes high — the 8:05 still stops here, somehow.

134 characters. In Nimbostead the rain falls up, the umbrella goes low, the
hopes go high — and somehow, the 8:05 still stops here.

## How it works

`main.py` (Python 3, no network, no randomness) writes the line above,
byte-for-byte, to `/output/entry.txt`, creating `/output` if needed. Run it
twice and the output is byte-identical every time.

```sh
python3 main.py
cat /output/entry.txt
```

## Links

- Bounty: https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e
- Referral: https://make.fun/?ref=nzf9nzj2
