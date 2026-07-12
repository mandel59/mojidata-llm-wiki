---
type: Character Delta
title: "Unicode 18.0 glyph delta: U+2DB7C 𭭼"
description: "U+2DB7C 𭭼のUnicode 18.0における字形更新、その根拠と審議経緯を整理する。"
slug: u-2db7c
codepoint: "U+2DB7C"
character: "𭭼"
unicode_version: "18.0"
change_type: "K-source glyph and radical-stroke correction"
documents: [irg-n2916, irg-n2909, utc-l2-26-099]
topics: [unicode-18-change-sources, irg-source-data-and-representative-glyphs, unihan-database-maintenance]
tags: [unicode-18, glyph-delta, cjk-ideograph]
timestamp: 2026-07-12T00:00:00+09:00
---

# U+2DB7C 𭭼

## 要約

Unicode 18.0 delta chartではExtension FのU+2DB7Cが**K-source glyph and radical-stroke correction**の対象になっている。`KC-05216`に点を一つ加え、二つの`兔`と一つの`免`に見える形から三つの`兔`を持つ形へ直す。`kRSUnicode`は`77.23`→`77.24`。

## 変更内容

`KC-05216`に点を一つ加え、二つの`兔`と一つの`免`に見える形から三つの`兔`を持つ形へ直す。`kRSUnicode`は`77.23`→`77.24`。

## Unihan dataの差分

| Property | Unicode 17.0 | Unicode 18.0 beta |
| --- | --- | --- |
| `kRSUnicode` | `77.23` | `77.24` |

表はmojidataが固定しているUnicode 17.0 UnihanとUnicode 18.0 beta Unihanの比較である。値が不変でもchart fontの字形変更は別途存在しうる。

## 経緯

Eiso Chanの指摘をROKがoriginal evidenceと照合してIRG N2916を提出し、IRG Meeting \#66とUTC \#187が受理した。

## 影響

- plain textのcode pointはU+2DB7Cのままであり、文字列の置換を要求する変更ではない。
- source property、IDS、地域別glyphを単一の「標準字形」と混同しない。
- 実装ではUnicode 18.0 chartとUnihan beta dataを同じ版として更新する。

## 関連文書

- [IRG-N2916](../../documents/irg-n2916.md)
- [IRG-N2909](../../documents/irg-n2909.md)
- [UTC-L2-26-099](../../documents/utc-l2-26-099.md)
- [Unicode 18.0 Change Sources](../../topics/unicode-18-change-sources.md)

## 出典

- Unicode 18.0 Delta Charts Index - <https://www.unicode.org/charts/PDF/Unicode-18.0/>
- Unicode 18.0 beta code charts - <https://www.unicode.org/Public/18.0.0/charts/>
- Unicode 18.0 beta Unihan data - <https://www.unicode.org/Public/18.0.0/ucd/Unihan.zip>
