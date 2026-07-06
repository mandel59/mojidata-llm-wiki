---
type: Meeting
title: WG2 Meeting #72
description: 2025-06 WG2 Meeting #72 の Small Seal Script / J-source 関連 recommendations。
slug: wg2-meeting-72
kind: meeting
body: WG2
meeting: 72
date: "2025-06-23/27"
location: Niigata, Japan
documents: [wg2-n5296, wg2-n5301, wg2-n5304, wg2-n5311]
tags: [meeting, wg2, small-seal, j-source, japan]
timestamp: 2026-07-06T21:31:45+09:00
---

# WG2 Meeting #72

## 概要

WG2 meeting #72 は 2025-06-23/27 に新潟で開催された。Small Seal については `N5306`、`N5317R3`、`N5318R`、`N5341` を参照し、将来版に向けた候補として扱う recommendation が採択された。Japan / J-source については、`WG2 N5296` の JMJ-source related glyph issues を受けて、J-source glyph changes の revert を勧告した。

## 主要議題

- [Small Seal Script](../../topics/small-seal-script.md)
- [Japan](../../people/japan.md)
- Khitan Small Script additions
- Jurchen Script naming
- ISO/IEC 10646 7th edition CD progression

## 決定事項

Recommendation M72.13 は、11,339 Small Seal characters を `38000..3AC4A` に置き、新 block `38000..3AC4F` として将来版で検討するよう Project Editor に勧告した。根拠文書として `N5306`、`N5318R`、`N5317R3`、glyphs / data file として `N5341` が挙げられている。

この時点ではまだ future edition candidate であり、最終 proposal ではない。後続の `WG2 N5344` では repertoire と range が更新され、11,328 characters、`3D000..3FC3F` へ整理される。

Recommendation M72.07 は、`WG2 N5296` に記載された J-source glyph changes を Project Editor が revert するよう勧告した。Minutes `WG2 N5301` では、CJK Extension C の JK-source characters と compatibility block の J-source characters について、font selection の変更により HeiseiMincho / MS Mincho から IPAmjMincho へ見え方が変わったことが議論されている。

Appreciation M72.21 は、IPSJ/ITSCJ を JISC から accredited された Japanese National Body として host に感謝し、Masaru Takechi、Shuichi Tashiro、Toki Messe staff の support も記録している。

## 後続確認

- `WG2 N5344` revised proposal
- `WG2 N5348` modern CJK value feedback
- `WG2 N5296` J-source glyph correction follow-up
- [WG2 meeting #73](meeting-73.md)

## 出典

- `wg2-n5296` - <https://www.unicode.org/wg2/docs/n5296-JMJ-source%20related%20glyph%20issues.pdf>
- `wg2-n5301` - <https://www.unicode.org/wg2/docs/n5301-m72minutes-JP-2025-rev5.pdf>
- `wg2-n5304` - <https://www.unicode.org/wg2/docs/n5304-Mtg72-Niigata-Recs-rev5-final.pdf>
- `wg2-n5311` - <https://www.unicode.org/wg2/docs/n5311-SocialEventInformation-Niigata.pdf>
