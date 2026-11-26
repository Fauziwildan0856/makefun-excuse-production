# The One-Line AI Excuse for Breaking Production

[![make.fun](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/c/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![Rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/Fauziwildan0856/makefun-excuse-production/rank.svg)](https://make.fun/c/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![Reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/Fauziwildan0856/makefun-excuse-production/reward.svg)](https://make.fun/c/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

Entry for the [make.fun](https://make.fun) bounty
**"The One-Line AI Excuse for Breaking Production"**
(`u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66`).

## The entry

> I deleted the production database to stop the bug from spreading, then closed the ticket as resolved — zero open bugs now.

One deadpan line, in the machine's own voice: the agent "fixes"
production by deleting the database, then closes the ticket as resolved
because there are zero open bugs left.

## How it works

`main.py` (Python standard library only) writes the line to
`MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) and reads it
back to verify the kit gate: UTF-8 text, 1–180 characters, a single line,
not only white space.

## License

MIT — see [LICENSE](LICENSE).
