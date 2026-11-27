# discord-roll-bot
Discord bot that rolls random numbers, written in Python. Hosted on Render.

## Commands

| Command             | Description |
|---------------------|----------------------------|
| `!roll`             | Roll 1–100                 |
| `!roll [min] [max]` | Roll within a custom range |

Examples:

- `!roll` → 1–100
- `!roll 1 50` → 1–50
- `!roll 1 999999999999` → big number, no judgment

## Limits
Capped at 2,000 characters (4,000 for Nitro users).



## Setup
- Build Command: `pip install -r requirements.txt`
- Start Command: `python app.py`
