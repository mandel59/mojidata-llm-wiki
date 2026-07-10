---
type: Topic
title: CJK Strokes Variation Sequences
description: "CJK Strokes characters に standardized variation sequences を追加し、StandardizedVariants.txt と code charts に反映する議論。"
slug: cjk-strokes-variation-sequences
bodies: [UTC]
documents: [utc-l2-26-073r, utc-l2-26-099]
topics: [unicode-18-change-sources]
status: accepted-for-unicode-18
tags: [cjk, strokes, variation-sequences, standardizedvariants, unicode-18]
timestamp: 2026-07-07T21:45:00+09:00
---

# CJK Strokes Variation Sequences

## 概要

CJK Strokes Variation Sequences は、CJK Strokes characters に standardized variation sequences を追加し、Unicode Version 18.0 の data files、code charts、Core Specification Appendix F に反映する議論である。

この topic は CJK Unified Ideographs 本体の source data ではなく、CJK Strokes block の character presentation と `StandardizedVariants.txt` の保守に関わる。`L2/26-099` では、CJK & Unihan Working Group recommendations の一項目として扱われた。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2026-03-04 | UTC | [L2/26-073R](../documents/utc-l2-26-073r.md) | Night Koo が CJK Strokes characters 向け standardized variation sequences の revised proposal を提出した。 |
| 2026-04-11 | UTC | [L2/26-099](../documents/utc-l2-26-099.md) | CJK & Unihan Working Group が 17 standardized variation sequences を Unicode Version 18.0 target で受け入れ、Pipeline、`StandardizedVariants.txt`、code charts、Core Specification Appendix F を更新する action item を置いた。 |

## 主な論点

### StandardizedVariants.txt への反映

`L2/26-099` は、CJK Strokes の variation sequences を actual data update として扱い、`StandardizedVariants.txt` additions と code chart / core spec update を並行して進める。したがって、この議論は proposal 文書だけでなく Unicode 18.0 beta data の確認対象でもある。

### CJK / Unihan Working Group recommendations との関係

CJK Strokes は Unihan property そのものではないが、`L2/26-099` では UAX \#38、UAX \#45、UTS \#39、IRG follow-up と同じ recommendation bundle に含まれる。Unicode 18.0 の CJK 関連変更点を追う場合、CJK Unified Ideographs 以外の CJK-adjacent data update として確認する必要がある。

## 関連文書

- [L2/26-073R](../documents/utc-l2-26-073r.md) - CJK Strokes standardized variation sequences proposal。
- [L2/26-099](../documents/utc-l2-26-099.md) - UTC \#187 向け CJK & Unihan Working Group recommendations。

## 関連トピック

- [Han Ideographic Scripts](../families/han-ideographic-scripts.md)
- [Unicode 18.0 Change Sources](unicode-18-change-sources.md)

## 出典

- `utc-l2-26-073r` - <https://www.unicode.org/L2/L2026/26073r-strokes-svs-with-attachment.pdf>
- `utc-l2-26-099` - <https://www.unicode.org/L2/L2026/26099-cjk-unihan-wg-utc187.pdf>
