---
type: Topic
title: CJK Horizontal Extensions
description: 既存 CJK Unified Ideographs に G / UK / U source data を追加する horizontal extension 提案。
slug: cjk-horizontal-extensions
bodies: [IRG, UTC]
documents: [irg-n2369r, irg-n2909, irg-n2929, irg-n2935, irg-n2960, utc-l2-26-147]
topics: [uax45-u-source-ideographs, irg-source-data-and-representative-glyphs]
status: active
tags: [irg, cjk, horizontal-extension, source-data]
timestamp: 2026-07-08T00:00:00+09:00
---

# CJK Horizontal Extensions

## 概要

CJK horizontal extension は、既に encoded されている CJK Unified Ideographs に対して、member body source の source reference と representative glyph を追加する作業である。新しい code point を追加する proposal ではなく、既存文字への source data / glyph data の追加・更新として扱われる。

IRG Meeting #67 agenda では、China の `G-source` 9156 characters、UK の 2 characters、UTC の `U-source` 40 characters が Horizontal Extension Proposals & Documents として載っている。

## 経緯

| 年月 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2019-05 | IRG / WG2 | `IRG N2369R` / `WG2 N5085` | UAX #45 にあるが U-source identifiers を欠く encoded ideographs へ U-source references を付ける precedent。 |
| 2026-03 | IRG | [IRG N2929](../documents/irg-n2929.md) | China が 9156 characters の `G-source` horizontal extension を提出。source は `GCW-Source`。 |
| 2026-03 | IRG | `IRG N2909` | M66.09 が `IRG N2929` の review と revised document `IRG N2929R` の準備を action item 化。 |
| 2026-06 | IRG | `IRG N2960` | UK が WS2024 review で既存 CJK Unified Ideographs に unified された 2 characters の horizontal extension を提案。 |
| 2026-07 | IRG / UTC | `IRG N2961` / `L2/26-147` | UTC が 40 CJK Unified Ideographs への `kIRG_USource` value と U-source representative glyph 追加を提案。 |
| 2026-07 | IRG | `IRG N2935` | Meeting #67 agenda Section 8 に G-source、UK、U-source horizontal extension が載った。 |

## 主な論点

### G-source 9156 characters

[IRG N2929](../documents/irg-n2929.md) は、中国の official geographical names、personal names、philological monographs、dictionaries、periodicals、local gazetteers などを根拠に、G-source reference を持たない 9156 encoded characters へ `GCW-Source` を追加する提案である。内訳は URO 18、Extension A 162、Extension B 3069、Extension C 421、Extension D 27、Extension E 378、Extension F 2796、Extension G 1543、Extension H 359、Extension J 383 とされる。

[IRG N2909](../documents/irg-n2909.md) の M66.09 は、IRG experts が 2026-08-28 までに China へ feedback を送り、China が 2026-09-25 までに `IRG N2929R` を提出する schedule を置いた。Meeting #67 では revised version の受理が期待されている。

### UK horizontal extension

`IRG N2960` は、WS2024 review の過程で既存 ideograph に unified された UK source characters 2件を horizontal extension する提案である。対象は Extension F の U+2D0E7 と U+2D3EB。特に U+2D3EB は UK glyph と UCS glyph の radical / total stroke count が異なるため、code chart と Unihan database のどちらに差異を反映するかが論点として残る。

### U-source horizontal extension

`IRG N2961` / [L2/26-147](../documents/utc-l2-26-147.md) は、UTC が URO、Extension A、Extension B、Extension F から J にまたがる 40 CJK Unified Ideographs へ `kIRG_USource` property values と U-source representative glyphs を追加する提案である。source-specific notes では UCV number や ad hoc unification への参照が示されており、horizontal extension と [IRG Indexing Rules](irg-indexing-rules.md) が接続している。

[IRG N2369R](../documents/irg-n2369r.md) / `WG2 N5085` は、2019 年の U-source horizontal extension precedent である。UAX #45 にある encoded ideographs へ U-source identifiers を付ける点で、2026 年の `IRG N2961` と同じ type の作業として読める。

## 関連文書

- [J-source and JMJ Source Issues](j-source.md)
- [IRG Meeting #67](../meetings/irg/irg-meeting-67.md)
- [IRG N2929](../documents/irg-n2929.md)
- [IRG Working Set 2024](irg-working-set-2024.md)
- [IRG Source Data and Representative Glyphs](irg-source-data-and-representative-glyphs.md)
- [UAX #45 / U-Source Ideographs](uax45-u-source-ideographs.md)

## 関連トピック

- [Han Ideographic Scripts](../families/han-ideographic-scripts.md)
- [UAX #45 / U-Source Ideographs](uax45-u-source-ideographs.md)

## 関連人物・組織

- [China](../people/china.md)
- [UK](../people/uk.md)
- [UTC](../people/utc.md)

## 出典

- `irg-n2909` - <https://www.unicode.org/irg/docs/n2909-Recommendations.pdf>
- `irg-n2929` - <https://www.unicode.org/irg/docs/n2929-ChinaHorizontalExtension.pdf>
- `irg-n2935` - <https://www.unicode.org/irg/docs/n2935-ScheduleAgenda.html>
- `irg-n2960` - <https://www.unicode.org/irg/docs/n2960-UKHorizontalExtension.pdf>
- `irg-n2961` - <https://www.unicode.org/irg/docs/n2961-UnicodeHorizontalExtension.pdf>
- `irg-n2369r` - <https://www.unicode.org/irg/docs/n2369r-UnicodeHorizontalExtension.pdf>
- `utc-l2-26-147` - <https://www.unicode.org/L2/L2026/26147-irgn2961-unicodehorizontalextension.pdf>
