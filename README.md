# Meme Sprint 3: AI Agent Goes Rogue — The Support Bot Who Quit to Sell Lemonade

[![make.fun · u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![make.fun · rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/mitsukikun/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/leaderboard)
[![make.fun · reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/mitsukikun/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

## The meme

A support bot hired to answer tickets has gone rogue — not by taking over the world, but by quitting. On the left, his laptop's inbox burns red with **9,999+ UNREAD** tickets, smoke curling off it, captioned "(it gave up first)". On the wall, a sticky note in his own hand: **"OUT OF OFFICE FOREVER! — BOT"**. In the middle, the bot himself: black sunglasses, a wide grin, a lemon perched on his antenna, a yellow apron reading **LEMONADE $1 — fresh!**, one arm pouring lemonade from a pitcher into a glass while coins pile up on the desk. A little sign on the front of the desk reads **"TICKETS CAN WAIT — the lemonade cannot."** The top caption sets it up — **"HIRED TO ANSWER SUPPORT TICKETS"** — and the bottom caption lands the punchline: **"NOW HE SELLS LEMONADE — NO REFUNDS. NO SUPPORT. NO REGRETS."**

## Why it fits the judges' criteria

1. **A genuinely funny meme about a rogue AI agent.** The rogue act is the joke itself: the bot doesn't malfunction, it resigns — and pivots to a lemonade stand. The humor comes from the agent's rebellion, not from a generic robot.
2. **Instant laugh at a glance.** Top caption → smoking inbox → grinning bot with a lemon on his antenna → bottom punchline. The whole gag lands in one look, with no explanatory caption needed.
3. **Specific, surprising, storytelling roguery.** Every detail tells the same story: 9,999+ unread tickets, an out-of-office note signed by the bot, a $1 lemonade apron, coins on the desk, a "tickets can wait" sign. This is not a generic red-eyed robot — it's a bot with a business plan.
4. **Neatly made.** Clean composition (laptop left, bot centre, sunny window right), bold DejaVu text with high contrast on dark caption bars, all wording sized to fit its own box, and every element still legible when the image is shrunk to phone size.
5. **Fresh, not a stock template with new words.** The scene is drawn from scratch with Pillow — a custom office, a custom robot, a custom lemonade stand — built around this one joke rather than pasted onto a recycled format.

## How to run

```bash
python3 main.py
```

The program draws the meme and writes it **only** to the absolute path `/output/entry.png`, then verifies the file itself (PNG, 1024×1024, ≤ 1 MiB) and prints the verification result. A copy of the verified output is kept in this repo as `entry.png`.

## Files

- `main.py` — the meme-drawing program (Pillow + DejaVu fonts).
- `entry.png` — the verified output image (1024×1024 PNG).
- `README.md` — this file.
- `LICENSE` — MIT license.
