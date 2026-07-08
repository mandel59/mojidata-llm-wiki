---
type: Topic
title: Maya Hieroglyph Encoding
description: "Codical Maya と Classic Maya Hieroglyphs Extended-A の staged / unified encoding。"
slug: maya-hieroglyph-encoding
bodies: [UTC, WG2]
documents: [utc-l2-26-145, utc-l2-26-146, wg2-n5354, wg2-n5365, wg2-n5366, wg2-n5367]
meetings: [utc-meeting-188, wg2-meeting-73]
status: proposed
tags: [script, maya, hieroglyphs, format-controls, extension]
timestamp: 2026-07-08T00:00:00+09:00
---

# Maya Hieroglyph Encoding

## 概要

Maya Hieroglyph Encoding は、Maya writing を Codical Maya base set と Classic Maya extensions に分けて、unified script として符号化する提案群を扱う topic である。UTC \#188 候補文書として [L2/26-145](../documents/utc-l2-26-145.md) Codical Maya Hieroglyphs と [L2/26-146](../documents/utc-l2-26-146.md) Maya Hieroglyphs Extended-A が提出されている。

両文書はいずれも in-progress draft / not for citation とされており、2026-07-08 時点では UTC の agenda / minutes 上の処理は未確認である。一方、WG2 \#73 は `WG2 N5366` / `WG2 N5367` として同 proposals を受け取り、WG2 \#74 までの review を求めた。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2026-06-22 | UTC / WG2 | [L2/26-145](../documents/utc-l2-26-145.md) | Postclassic codices を対象に Codical Maya Hieroglyphs を base set として提案した。 |
| 2026-06-22 | UTC / WG2 | [L2/26-146](../documents/utc-l2-26-146.md) | Classic Maya corpus の first extension tranche として Maya Hieroglyphs Extended-A を提案した。 |
| 2026-06-26 | WG2 | [WG2 N5354](../documents/wg2-n5354.md) | WG2 \#73 M73.14 が `WG2 N5366` / `WG2 N5367` を WG2 \#74 までに review するよう National Bodies / liaison organizations に求めた。 |
| 2026-07-30 | UTC | [UTC Meeting \#188](../meetings/utc/utc-meeting-188.md) | UTC \#188 の agenda / minutes は未掲載だが、UTC \#187 後の候補文書として追跡する。 |

## 主な論点

### Codical Maya を base set にする

[L2/26-145](../documents/utc-l2-26-145.md) は Dresden、Madrid、Paris codices の standardized subset を first encoding target とする。Codical corpus は Classic Maya 全体より狭いが、surviving codices の sign repertoire と glyph-block structure を安定して比較できるとする。

### Classic Maya を extension として足す

[L2/26-146](../documents/utc-l2-26-146.md) は Codical set と unified encoding できない Classic Maya signs を Extended-A として追加する。差分を separate script ではなく font-level style / extension repertoire として扱う点が重要である。

### format controls と block composition

Maya hieroglyphic writing は glyph blocks と affixation を持つため、plain linear sequence だけでは表現できない。Codical proposal の format controls は Classic Maya proposal も依存するため、repertoire より先に text model / rendering model の妥当性を確認する必要がある。

## 関連文書

- [L2/26-145](../documents/utc-l2-26-145.md) - Codical Maya Hieroglyphs。
- [L2/26-146](../documents/utc-l2-26-146.md) - Maya Hieroglyphs Extended-A。
- [WG2 N5354](../documents/wg2-n5354.md) - WG2 \#73 recommendations。
- [WG2 N5365](../documents/wg2-n5365.md) - SEI liaison contribution。

## 関連トピック

- [Script Encoding Pipeline](script-encoding-pipeline.md)

## 出典

- `utc-l2-26-145` - <https://www.unicode.org/L2/L2026/26145-codical-maya.pdf>
- `utc-l2-26-146` - <https://www.unicode.org/L2/L2026/26146-classic-maya.pdf>
- `wg2-n5354` - <https://www.unicode.org/wg2/docs/n5354-Mtg73-Paris-Recs-rev5.pdf>
