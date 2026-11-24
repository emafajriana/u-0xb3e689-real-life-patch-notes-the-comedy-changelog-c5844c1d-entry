# Real-Life Patch Notes: The Comedy Changelog

[![make.fun bounty](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![rank](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/emafajriana/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d-entry/rank.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![reward](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/emafajriana/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d-entry/reward.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)

An entry for make.fun's [Real-Life Patch Notes: The Comedy Changelog](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d) bounty: one line, at most 160 characters — a software patch note for a bug in real life, in the terse register of a real release note.

## The entry

> v33.5.1: fixed a bug where crossing a doorway flushed the reason for entering the room; intent is now cached before the threshold, not after.

The doorway effect, shipped as a fix: you walk into a room, the reason you came in is gone, and you stand there buffering. This build caches the intent before the threshold instead of after it.

## Run it

```sh
python3 main.py
```

Writes `entry.txt` to `/output` by default; set `MAKEFUN_OUTPUT_DIR` to write somewhere else. The program reads its output back and checks it against the gate (UTF-8, 1–160 characters, single line, not only white space). Python standard library only.

## License

MIT — see [LICENSE](LICENSE).
