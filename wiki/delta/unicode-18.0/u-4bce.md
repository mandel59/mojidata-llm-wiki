---
type: Character Delta
title: "Unicode 18.0 glyph delta: U+4BCE 䯎"
description: "U+4BCE 䯎のUnicode 18.0における字形更新、その根拠と審議経緯を整理する。"
slug: u-4bce
codepoint: "U+4BCE"
character: "䯎"
unicode_version: "18.0"
change_type: "T-source mapping exchange"
documents: [irg-n2860, irg-n2861, utc-l2-26-099]
topics: [unicode-18-change-sources, irg-source-data-and-representative-glyphs, unihan-database-maintenance]
tags: [unicode-18, glyph-delta, cjk-ideograph]
timestamp: 2026-07-12T00:00:00+09:00
---

# U+4BCE 䯎

## 要約

Unicode 18.0 delta chartではExtension AのU+4BCEが**T-source mapping exchange**の対象になっている。T-sourceを`T3-4F78`から`T7-2B55`へ移し、U+2FA08との割当てを交換する。内部componentの`八`/`人`系の差をsource evidenceに合わせる。

## 変更内容

T-sourceを`T3-4F78`から`T7-2B55`へ移し、U+2FA08との割当てを交換する。内部componentの`八`/`人`系の差をsource evidenceに合わせる。

## Unihan dataの差分

| Property | Unicode 17.0 | Unicode 18.0 beta |
| --- | --- | --- |
| `kIRG_TSource` | `T3-4F78` | `T7-2B55` |

表はmojidataが固定しているUnicode 17.0 UnihanとUnicode 18.0 beta Unihanの比較である。値が不変でもchart fontの字形変更は別途存在しうる。

## 経緯

IRG N2861がmapping changeと結論し、UTC \#187が受理した。

## 影響

- plain textのcode pointはU+4BCEのままであり、文字列の置換を要求する変更ではない。
- source property、IDS、地域別glyphを単一の「標準字形」と混同しない。
- 実装ではUnicode 18.0 chartとUnihan beta dataを同じ版として更新する。

## 関連文書

- [IRG-N2860](../../documents/irg-n2860.md)
- [IRG-N2861](../../documents/irg-n2861.md)
- [UTC-L2-26-099](../../documents/utc-l2-26-099.md)
- [Unicode 18.0 Change Sources](../../topics/unicode-18-change-sources.md)

## 出典

- Unicode 18.0 Delta Charts Index - <https://www.unicode.org/charts/PDF/Unicode-18.0/>
- Unicode 18.0 beta code charts - <https://www.unicode.org/Public/18.0.0/charts/>
- Unicode 18.0 beta Unihan data - <https://www.unicode.org/Public/18.0.0/ucd/Unihan.zip>
