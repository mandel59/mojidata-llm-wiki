---
type: Topic
title: CJK Security Confusables
description: "UTS #39 security data における CJK confusable pairs と CJK 専門 review。"
slug: cjk-security-confusables
kind: topic
bodies: [UTC]
documents: [utc-l2-26-082, utc-l2-26-099, utc-l2-26-127]
status: active
tags: [cjk, security, confusables, uts39]
timestamp: 2026-07-07T00:00:00+09:00
---

# CJK Security Confusables

## 概要

CJK Security Confusables は、UTS #39 security data の `confusables.txt` と、CJK glyph / source data の専門判断が交差する topic である。CJK ideographs では、視覚的類似性、source separation、semantic distinction、variant property が重なるため、単純な glyph comparison だけでは confusable pair を決めにくい。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2026-03-18 | UTC | `L2/26-082` | CJK confusables の review request が提出された。 |
| 2026-04-11 | UTC | `L2/26-099` | CJK & Unihan Working Group は U+3A36 / U+6440 を除き、新しい CJK confusable pairs を UTS #39 に追加する action item を置いた。 |
| 2026-05-04 | UTC | `L2/26-127` | Properties and Algorithms WG が CJK confusables data の second review request を提出した。 |

## 主な論点

### CJK WG review の必要性

`L2/26-127` は、候補 pairs を `EquivalentUnifiedIdeograph.txt`、`kSpoofingVariant`、`kZVariant`、Windows / Android glyph comparison などから作るが、最終判断には CJK Working Group review が必要であることを示す。CJK ideograph の security data は、glyph shape だけでなく、CJK source data と既存 variant relationships を踏まえる必要がある。

### one-stroke difference の扱い

`L2/26-099` Section 33 は、`L2/26-082` の候補のうち U+3A36 / U+6440 pair を除外した。理由は、U+9CE5 鳥と U+70CF 烏が一画差でも区別されるように、この pair も distinct と判断されたためである。

## 関連文書

- [L2/26-099](../documents/utc-l2-26-099.md)
- `L2/26-082` - Request for review of CJK confusables。
- `L2/26-127` - second request for review of CJK confusables。

## 関連トピック

- [Unihan Database Maintenance](unihan-database-maintenance.md)
- [IRG Source Data and Representative Glyphs](irg-source-data-and-representative-glyphs.md)

## 出典

- `utc-l2-26-082` - <https://www.unicode.org/L2/L2026/26082-review-cjk-confusables.pdf>
- `utc-l2-26-099` - <https://www.unicode.org/L2/L2026/26099-cjk-unihan-wg-utc187.pdf>
- `utc-l2-26-127` - <https://www.unicode.org/L2/L2026/26127-2nd-cjk-confusables.pdf>
