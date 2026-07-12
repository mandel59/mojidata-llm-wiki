---
type: Character Delta
title: "Unicode 18.0 glyph delta: U+FACB 頋"
description: "U+FACB 頋のUnicode 18.0における字形更新、その根拠と審議経緯を整理する。"
slug: u-facb
codepoint: "U+FACB"
character: "頋"
unicode_version: "18.0"
change_type: "Disunification and source migration"
documents: [irg-n2765, irg-n2834, irg-n2826]
topics: [unicode-18-change-sources, irg-source-data-and-representative-glyphs, unihan-database-maintenance]
tags: [unicode-18, glyph-delta, cjk-ideograph]
timestamp: 2026-07-12T00:00:00+09:00
---

# U+FACB 頋

## 要約

Unicode 18.0 delta chartではCompatibility IdeographsのU+FACBが**Disunification and source migration**の対象になっている。`KP1-869A`をU+2EA07へ移し、U+FACBには内部用`KPU-0FACB`を置く。compatibility mapping `U+980B`は維持する。

## 変更内容

`KP1-869A`をU+2EA07へ移し、U+FACBには内部用`KPU-0FACB`を置く。compatibility mapping `U+980B`は維持する。

## Unihan dataの差分

| Property | Unicode 17.0 | Unicode 18.0 beta |
| --- | --- | --- |
| `kIRG_KPSource` | `KP1-869A` | `KPU-0FACB` |

表はmojidataが固定しているUnicode 17.0 UnihanとUnicode 18.0 beta Unihanの比較である。値が不変でもchart fontの字形変更は別途存在しうる。

## 経緯

IRGのdisunification reviewでKP glyphはU+980B系ではなくU+2EA07の歴史的字形に属すると判断された。

## 影響

- plain textのcode pointはU+FACBのままであり、文字列の置換を要求する変更ではない。
- source property、IDS、地域別glyphを単一の「標準字形」と混同しない。
- 実装ではUnicode 18.0 chartとUnihan beta dataを同じ版として更新する。

## 関連文書

- [IRG-N2765](../../documents/irg-n2765.md)
- `IRG-N2834`
- [IRG-N2826](../../documents/irg-n2826.md)
- [Unicode 18.0 Change Sources](../../topics/unicode-18-change-sources.md)

## 出典

- Unicode 18.0 Delta Charts Index - <https://www.unicode.org/charts/PDF/Unicode-18.0/>
- Unicode 18.0 beta code charts - <https://www.unicode.org/Public/18.0.0/charts/>
- Unicode 18.0 beta Unihan data - <https://www.unicode.org/Public/18.0.0/ucd/Unihan.zip>
