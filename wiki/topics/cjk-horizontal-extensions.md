---
type: Topic
title: CJK Horizontal Extensions
description: 既存 CJK Unified Ideographs に JMJ / G / UK / U source data を追加する horizontal extension 提案。
slug: cjk-horizontal-extensions
bodies: [IRG, WG2, UTC]
documents: [wg2-n5221, irg-n2721, irg-n2722, irg-n2369r, utc-l2-24-012, irg-n2909, irg-n2923r, irg-n2929, irg-n2935, irg-n2960, utc-l2-26-147]
topics: [jmj-horizontal-extension-review-path, uax45-u-source-ideographs, irg-source-data-and-representative-glyphs]
status: active
tags: [irg, cjk, horizontal-extension, source-data]
timestamp: 2026-07-08T00:00:00+09:00
---

# CJK Horizontal Extensions

## 概要

CJK horizontal extension は、既に encoded されている CJK Unified Ideographs に対して、member body source の source reference と representative glyph を追加する作業である。新しい code point を追加する proposal ではなく、既存文字への source data / glyph data の追加・更新として扱われる。

近年の例には、Japan NB の JMJ references、China の `G-source` 9156 characters、UK の 2 characters、UTC の `U-source` 40 characters がある。大規模 source addition は、単なる property 追加ではなく、source owner の review、representative glyph、Unihan source property maintenance に接続する。

## 経緯

| 年月 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2019-05 | IRG / WG2 | `IRG N2369R` / `WG2 N5085` | UAX \#45 にあるが U-source identifiers を欠く encoded ideographs へ U-source references を付ける precedent。 |
| 2023-04 | WG2 | [WG2 N5221](../documents/wg2-n5221.md) | Japan NB が MOJI-JOHO-KIBAN IDEOGRAPHS-2018 の JMJ references を J-column へ追加する large horizontal extension request を提出。 |
| 2024-01 | UTC | [L2/24-012](../documents/utc-l2-24-012.md) | CJK & Unihan Group が U+3150D へ UTC-00420 を `kIRG_USource` として追加する U-source horizontal extension を勧告した。 |
| 2024-09 | IRG / WG2 | [IRG N2721](../documents/irg-n2721.md) / `WG2 N5284` | IRG Convenor が、`WG2 N5221` 規模の horizontal extension は IRG review に向くとして Japan の IRG active participation を求めた。 |
| 2024-09 | IRG | [IRG N2722](../documents/irg-n2722.md) | JMJ horizontal extension 後の source reference / glyph correspondence issue を指摘。 |
| 2026-03 | IRG | [IRG N2929](../documents/irg-n2929.md) | China が 9156 characters の `G-source` horizontal extension を提出。source は `GCW-Source`。 |
| 2026-03 | IRG | [IRG N2923R](../documents/irg-n2923r.md) | Dong Wenjie が GGH-source 6 characters と GXC-source 3 characters の horizontal extension candidates を Appendix B に示した。 |
| 2026-03 | IRG | `IRG N2909` | M66.09 が `IRG N2929` の review と revised document `IRG N2929R` の準備を action item 化。 |
| 2026-06 | IRG | [IRG N2960](../documents/irg-n2960.md) | UK が WS2024 review で既存 CJK Unified Ideographs に unified された 2 characters の horizontal extension を提案。 |
| 2026-07 | IRG / UTC | `IRG N2961` / `L2/26-147` | UTC が 40 CJK Unified Ideographs への `kIRG_USource` value と U-source representative glyph 追加を提案。 |
| 2026-07 | IRG | `IRG N2935` | Meeting \#67 agenda Section 8 に G-source、UK、U-source horizontal extension が載った。 |

## 主な論点

### JMJ horizontal extension

[WG2 N5221](../documents/wg2-n5221.md) は、MOJI-JOHO-KIBAN IDEOGRAPHS-2018 に関係する JMJ references を ISO/IEC 10646 の J-source column へ追加する proposal である。registry subject は 36,422 horizontal extensions とし、関連 chart PDF が別リンクで提供された。

[IRG N2721](../documents/irg-n2721.md) / `WG2 N5284` は、同規模の horizontal extension は WG2 より IRG に提出し、CJK experts が早い段階で review するべきだったと位置づける。詳細な review path は [JMJ Horizontal Extension Review Path](jmj-horizontal-extension-review-path.md) に分ける。

### G-source 9156 characters

[IRG N2929](../documents/irg-n2929.md) は、中国の official geographical names、personal names、philological monographs、dictionaries、periodicals、local gazetteers などを根拠に、G-source reference を持たない 9156 encoded characters へ `GCW-Source` を追加する提案である。内訳は URO 18、Extension A 162、Extension B 3069、Extension C 421、Extension D 27、Extension E 378、Extension F 2796、Extension G 1543、Extension H 359、Extension J 383 とされる。

[IRG N2909](../documents/irg-n2909.md) の M66.09 は、IRG experts が 2026-08-28 までに China へ feedback を送り、China が 2026-09-25 までに `IRG N2929R` を提出する schedule を置いた。Meeting \#67 では revised version の受理が期待されている。

[IRG N2923R](../documents/irg-n2923r.md) Appendix B は、GGH-source 6 characters と GXC-source 3 characters を horizontal extension candidates として示す。IRG Meeting \#66 editorial report は、China がこれらを separate proposal にするか、`IRG N2929R` に merge することを検討するよう求めた。

### UK horizontal extension

[IRG N2960](../documents/irg-n2960.md) は、WS2024 review の過程で既存 ideograph に unified された UK source characters 2件を horizontal extension する提案である。対象は Extension F の U+2D0E7 と U+2D3EB。特に U+2D3EB は UK glyph と UCS glyph の radical / total stroke count が異なるため、code chart と Unihan database のどちらに差異を反映するかが論点として残る。

### U-source horizontal extension

`IRG N2961` / [L2/26-147](../documents/utc-l2-26-147.md) は、UTC が URO、Extension A、Extension B、Extension F から J にまたがる 40 CJK Unified Ideographs へ `kIRG_USource` property values と U-source representative glyphs を追加する提案である。source-specific notes では UCV number や ad hoc unification への参照が示されており、horizontal extension と [IRG Indexing Rules](irg-indexing-rules.md) が接続している。

[IRG N2369R](../documents/irg-n2369r.md) / `WG2 N5085` は、2019 年の U-source horizontal extension precedent である。[L2/24-012](../documents/utc-l2-24-012.md) の U+3150D / UTC-00420 追加は小規模な同型作業で、UAX \#45 にある encoded ideographs へ U-source identifiers を付ける点で、2026 年の `IRG N2961` と同じ type の作業として読める。

## 関連文書

- [JMJ Horizontal Extension Review Path](jmj-horizontal-extension-review-path.md)
- [J-source and JMJ Source Issues](j-source.md)
- [WG2 N5221](../documents/wg2-n5221.md)
- [IRG N2721](../documents/irg-n2721.md)
- [IRG N2722](../documents/irg-n2722.md)
- [L2/24-012](../documents/utc-l2-24-012.md)
- [IRG Meeting \#67](../meetings/irg/irg-meeting-67.md)
- [IRG N2929](../documents/irg-n2929.md)
- [IRG N2923R](../documents/irg-n2923r.md)
- [IRG N2960](../documents/irg-n2960.md)
- [IRG Working Set 2024](irg-working-set-2024.md)
- [IRG Source Data and Representative Glyphs](irg-source-data-and-representative-glyphs.md)
- [UAX \#45 / U-Source Ideographs](uax45-u-source-ideographs.md)

## 関連トピック

- [Han Ideographic Scripts](../families/han-ideographic-scripts.md)
- [JMJ Horizontal Extension Review Path](jmj-horizontal-extension-review-path.md)
- [UAX \#45 / U-Source Ideographs](uax45-u-source-ideographs.md)

## 関連人物・組織

- [Japan](../people/japan.md)
- [China](../people/china.md)
- [UK](../people/uk.md)
- [UTC](../people/utc.md)

## 出典

- `wg2-n5221` - <https://www.unicode.org/wg2/docs/n5221-JNB_contribution_2304.pdf>
- `irg-n2721` - <https://www.unicode.org/irg/docs/n2721-JapanIRGParticipation.pdf>
- `irg-n2722` - <https://www.unicode.org/irg/docs/n2722-JSourceIssues.pdf>
- `utc-l2-24-012` - <https://www.unicode.org/L2/L2024/24012-cjk-unihan-group-utc178.pdf>
- `irg-n2909` - <https://www.unicode.org/irg/docs/n2909-Recommendations.pdf>
- `irg-n2929` - <https://www.unicode.org/irg/docs/n2929-ChinaHorizontalExtension.pdf>
- `irg-n2923r` - <https://www.unicode.org/irg/docs/n2923r-GSourceChanges.pdf>
- `irg-n2935` - <https://www.unicode.org/irg/docs/n2935-ScheduleAgenda.html>
- `irg-n2960` - <https://www.unicode.org/irg/docs/n2960-UKHorizontalExtension.pdf>
- `irg-n2961` - <https://www.unicode.org/irg/docs/n2961-UnicodeHorizontalExtension.pdf>
- `irg-n2369r` - <https://www.unicode.org/irg/docs/n2369r-UnicodeHorizontalExtension.pdf>
- `utc-l2-26-147` - <https://www.unicode.org/L2/L2026/26147-irgn2961-unicodehorizontalextension.pdf>
