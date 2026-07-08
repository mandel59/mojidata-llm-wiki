---
type: Topic
title: Emoji Repertoire Proposals
description: "Emoji 18.0 / 19.0 に向けた個別 emoji proposal、ESR short list、final candidate name の整理。"
slug: emoji-repertoire-proposals
bodies: [UTC]
documents: [utc-l2-25-230r, utc-l2-25-252, utc-l2-25-253, utc-l2-25-254, utc-l2-25-255, utc-l2-25-256, utc-l2-25-257, utc-l2-25-258, utc-l2-25-259, utc-l2-26-008r, utc-l2-26-048, utc-l2-26-098, utc-l2-26-104]
topics: [emoji-interoperability-and-intake, unicode-18-change-sources, unicode-release-coordination-and-publication, unicode-properties-and-algorithms]
status: active
tags: [emoji, repertoire, proposal, unicode-18, esr]
timestamp: 2026-07-08T00:00:00+09:00
---

# Emoji Repertoire Proposals

## 概要

Emoji Repertoire Proposals は、個別 emoji proposal が ESR review を通って Unicode / Emoji version の candidate list に入る過程を追う topic である。[Emoji Interoperability and Intake](emoji-interoperability-and-intake.md) が process / CLDR / interoperability を扱うのに対し、この topic では concrete repertoire、code point、final character name、replaced candidate を整理する。

Unicode 18.0 では [L2/25-230R](../documents/utc-l2-25-230r.md) が 9 new emoji characters を推薦し、[L2/26-008R](../documents/utc-l2-26-008r.md) が FACE WITH SQUINTING EYES を CRACKING FACE に置き換えた。Emoji 19.0 については、[L2/26-098](../documents/utc-l2-26-098.md) が intake window と review priorities を示す。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2025-10-21 | UTC | [L2/25-252](../documents/utc-l2-25-252.md), [L2/25-253](../documents/utc-l2-25-253.md), [L2/25-254](../documents/utc-l2-25-254.md), [L2/25-255](../documents/utc-l2-25-255.md), [L2/25-256](../documents/utc-l2-25-256.md), [L2/25-257](../documents/utc-l2-25-257.md), [L2/25-258](../documents/utc-l2-25-258.md), [L2/25-259](../documents/utc-l2-25-259.md) | Emoji 18.0 candidate proposal batch が registry に登録された。 |
| 2025-10-29 | UTC | [L2/25-230R](../documents/utc-l2-25-230r.md) | ESR が U+1FADD APPLE CORE を外し、9 new emoji characters を Unicode 18.0 向けに推薦した。 |
| 2026-01-15 | UTC | [L2/26-048](../documents/utc-l2-26-048.md) | Jennifer Daniel が CRACKING FACE / cracked smiling face proposal を提出した。 |
| 2026-01-21 | UTC | [L2/26-008R](../documents/utc-l2-26-008r.md) | ESR が U+1FAEB FACE WITH SQUINTING EYES を CRACKING FACE に変更し、Unicode 18.0 final emoji candidates を更新した。 |
| 2026-04-03 | UTC | [L2/26-104](../documents/utc-l2-26-104.md) | UTS \#51 Revision 30 draft が Emoji 18.0 の specification / data layer を更新した。 |
| 2026-04-14 | UTC | [L2/26-098](../documents/utc-l2-26-098.md) | ESR が monarch butterfly feedback、Emoji 19.0 intake、CLDR keyword intake を UTC \#187 に報告した。 |

## Unicode 18.0 final emoji candidates

| Code point | Final name | 主 proposal / rationale | 備考 |
| --- | --- | --- | --- |
| U+1F6D9 | LIGHTHOUSE | [L2/25-256](../documents/utc-l2-25-256.md) | navigation、safety、guidance、heritage の symbol。 |
| U+1FA8B | METEOR | [L2/25-257](../documents/utc-l2-25-257.md) | vendor interoperability と comet との差別化。 |
| U+1FA8C | ERASER | [L2/25-255](../documents/utc-l2-25-255.md) | stationery と erase / cancel metaphor。 |
| U+1FA8D | NET WITH HANDLE | [L2/25-258](../documents/utc-l2-25-258.md) | handheld net / catch metaphor。 |
| U+1FACC | MONARCH BUTTERFLY | [L2/25-254](../documents/utc-l2-25-254.md) | U+1F98B BUTTERFLY の vendor design divergence を解く interoperability case。 |
| U+1FADD | PICKLE | [L2/25-253](../documents/utc-l2-25-253.md) | cucumber との差別化、idiom、pickleball など。 |
| U+1FAEB | CRACKING FACE | [L2/26-048](../documents/utc-l2-26-048.md) | [L2/25-259](../documents/utc-l2-25-259.md) の FACE WITH SQUINTING EYES から置換。 |
| U+1FAF9 | LEFTWARDS THUMB SIGN | [L2/25-252](../documents/utc-l2-25-252.md) | skin tone modifier sequences を伴う。 |
| U+1FAFA | RIGHTWARDS THUMB SIGN | [L2/25-252](../documents/utc-l2-25-252.md) | skin tone modifier sequences を伴う。 |

## 主な論点

### proposal と final name の差分

Unicode 18.0 では `L2/25-259` の Squinting Face が UTC \#185 の short list に入り、その後 UTC \#186 で CRACKING FACE に変更された。Emoji proposal は「提出文書の title」「ESR short list name」「final character name」がずれる場合があるため、topic では最終 list と proposal lineage を分けて読む。

### interoperability-driven additions

MONARCH BUTTERFLY と METEOR は、単に新しい絵柄を増やすだけでなく、既存 emoji の vendor design divergence を整理する目的を持つ。これは emoji repertoire が、既存 character の semantics を安定させるためにも拡張されることを示す。

### CLDR names / keywords との接続

Final character name が決まっても、user-facing search は CLDR short names / keywords に依存する。[L2/26-008R](../documents/utc-l2-26-008r.md) と [L2/26-098](../documents/utc-l2-26-098.md) は、keyword intake を ESR / CLDR process として扱う必要を示している。

### UTS \#51 data layer

[L2/26-104](../documents/utc-l2-26-104.md) は、Emoji 18.0 の proposed UTS \#51 update として、RGI sets、emoji sequences、ZWJ / tag sequence、design guidance を定義する。Repertoire proposal の採択後は、code point だけでなく `emoji-data.txt` や CLDR data への反映を追う必要がある。

## 関連文書

- [L2/25-230R](../documents/utc-l2-25-230r.md) - ESR report for UTC \#185。
- [L2/26-008R](../documents/utc-l2-26-008r.md) - ESR report for UTC \#186。
- [L2/26-098](../documents/utc-l2-26-098.md) - ESR report for UTC \#187。
- [L2/26-104](../documents/utc-l2-26-104.md) - UTS \#51 Revision 30 proposed update。

## 関連トピック

- [Emoji Interoperability and Intake](emoji-interoperability-and-intake.md)
- [Unicode 18.0 Change Sources](unicode-18-change-sources.md)
- [Unicode Release Coordination and Publication](unicode-release-coordination-and-publication.md)
- [Unicode Properties and Algorithms](unicode-properties-and-algorithms.md)

## 出典

- `utc-l2-25-230r` - <https://www.unicode.org/L2/L2025/25230r-esr-report-utc185.pdf>
- `utc-l2-26-008r` - <https://www.unicode.org/L2/L2026/26008r-esr-report-utc186.pdf>
- `utc-l2-26-098` - <https://www.unicode.org/L2/L2026/26098-esr-report-utc187.pdf>
- `utc-l2-26-104` - <https://www.unicode.org/L2/L2026/26104-uts51-30-update-pri543.pdf>

