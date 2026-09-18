---
type: Topic
title: Maya Hieroglyph Encoding
description: "Codical Maya と Classic Maya Hieroglyphs Extended-A の staged / unified encoding。"
slug: maya-hieroglyph-encoding
bodies: [UTC, WG2]
documents: [utc-l2-26-145, utc-l2-26-145r, utc-l2-26-146, utc-l2-26-151, utc-l2-26-158, wg2-n5354, wg2-n5365, wg2-n5366, wg2-n5367]
meetings: [utc-meeting-188, wg2-meeting-73]
status: proposed
tags: [script, maya, hieroglyphs, format-controls, extension]
timestamp: 2026-07-08T00:00:00+09:00
---

# Maya Hieroglyph Encoding

## 概要

Maya Hieroglyph Encoding は、Maya writing を Codical Maya base set と Classic Maya extensions に分けて、unified script として符号化する提案群を扱う topic である。[L2/26-145R](../documents/utc-l2-26-145.md) Codical Maya Hieroglyphs と [L2/26-146](../documents/utc-l2-26-146.md) Maya Hieroglyphs Extended-A が提出されている。

両文書はいずれも in-progress draft / not for citation とされる。WG2 \#73 は `WG2 N5366` / `WG2 N5367` として同 proposals を受け取り、WG2 \#74 までの review を求めた。UTC \#188 minutes は採択 consensus を置いておらず、Codical proposal は会合後に Version 1.2 へ改訂された。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2026-06-19 | WG2 | [WG2 N5366](../documents/utc-l2-26-145.md) | Postclassic codices を対象に Codical Maya Hieroglyphs Version 1.0 を base set として提出した。 |
| 2026-06-19 | WG2 | [WG2 N5367](../documents/utc-l2-26-146.md) | Classic Maya corpus の first extension tranche、Version 0.61 を提出した。 |
| 2026-06-22 | UTC | [L2/26-145](../documents/utc-l2-26-145.md) / [L2/26-146](../documents/utc-l2-26-146.md) | 同じ2提案を UTC Document Registry に登録した。 |
| 2026-06-26 | WG2 | [WG2 N5354](../documents/wg2-n5354.md) | WG2 \#73 M73.14 が [WG2 N5366](../documents/utc-l2-26-145.md) / [WG2 N5367](../documents/utc-l2-26-146.md) を WG2 \#74 までに review するよう National Bodies / liaison organizations に求めた。 |
| 2026-07-28/30 | UTC | [UTC Meeting \#188](../meetings/utc/utc-meeting-188.md) | `L2/26-158` の references には入ったが、minutes は Maya proposals の採択 consensus / action item を置かなかった。 |
| 2026-09-01 | UTC | [L2/26-145R](../documents/utc-l2-26-145.md) | Codical proposal Version 1.2 が property tables を含む改訂版として作成された。 |

## 主な論点

### Codical Maya を base set にする

[L2/26-145](../documents/utc-l2-26-145.md) は Dresden、Madrid、Paris codices の standardized subset を first encoding target とする。Codical corpus は Classic Maya 全体より狭いが、surviving codices の sign repertoire と glyph-block structure を安定して比較できるとする。

### Classic Maya を extension として足す

[L2/26-146](../documents/utc-l2-26-146.md) は Codical set と unified encoding できない Classic Maya signs を Extended-A として追加する。差分を separate script ではなく font-level style / extension repertoire として扱う点が重要である。

### format controls と block composition

Maya hieroglyphic writing は glyph blocks と affixation を持つため、plain linear sequence だけでは表現できない。Codical proposal の format controls は Classic Maya proposal も依存するため、repertoire より先に text model / rendering model の妥当性を確認する必要がある。

Codical Version 1.2 は joiners、appearance modifiers、segment delimiters、compression controls、damage modifiers と proposed property values を示す。Extended-A draft はこの control set に依存する一方、`Properties` section が placeholder のままである。したがって両案は同時に review する必要があるが、仕様成熟度は同一ではない。

## 関連文書

- [L2/26-145](../documents/utc-l2-26-145.md) - Codical Maya Hieroglyphs。
- [L2/26-146](../documents/utc-l2-26-146.md) - Maya Hieroglyphs Extended-A。
- [WG2 N5354](../documents/wg2-n5354.md) - WG2 \#73 recommendations。
- [WG2 N5365](../documents/wg2-n5365.md) - SEI liaison contribution。

## 関連トピック

- [Script Encoding Pipeline](script-encoding-pipeline.md)

## 出典

- `utc-l2-26-145r` - <https://www.unicode.org/L2/L2026/26145r-codical-maya.pdf>
- `utc-l2-26-146` - <https://www.unicode.org/L2/L2026/26146-classic-maya.pdf>
- `wg2-n5366` - <https://www.unicode.org/wg2/docs/n5366-Codical_Maya_20260619.pdf>
- `wg2-n5367` - <https://www.unicode.org/wg2/docs/n5367-Classic_Maya_20260619.pdf>
- `wg2-n5354` - <https://www.unicode.org/wg2/docs/n5354-Mtg73-Paris-Recs-rev5.pdf>
