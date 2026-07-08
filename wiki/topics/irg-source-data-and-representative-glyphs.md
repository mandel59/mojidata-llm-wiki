---
type: Topic
title: IRG Source Data and Representative Glyphs
description: IRG source references、representative glyphs、Unihan properties の修正論点。
slug: irg-source-data-and-representative-glyphs
bodies: [IRG, UTC, WG2]
documents: [irg-n2909, irg-n2916, irg-n2918, irg-n2919r, irg-n2923r, irg-n2927r, irg-n2928, irg-n2930, irg-n2935, irg-n2953, irg-n2954, irg-n2955, irg-n2956, irg-n2957, irg-n2958, irg-n2959, irg-n2962, utc-l2-26-099, wg2-n5354]
topics: [g-source-glyph-and-reference-issues]
status: active
tags: [irg, unihan, source-data, representative-glyphs]
timestamp: 2026-07-06T21:31:45+09:00
---

# IRG Source Data and Representative Glyphs

## 概要

IRG source data は、CJK Unified Ideographs の code chart、Unihan properties、member body source references を結びつける基盤である。representative glyph の修正、source reference の変更、`kIRG_*Source` property の追加・移動は、既に encoded された文字の identity、検索、chart rendering に影響する。

IRG Meeting \#67 agenda では、IRG \#66 の action items として持ち越された source reference / representative glyph 修正に加え、[IRG N2928](../documents/irg-n2928.md) / [IRG N2953](../documents/irg-n2953.md) 以降の個別 issue documents が Section 9.1 "Representative Glyph & Source Reference Issues" として束ねられている。

G-source に集中する `IRG N2954` から `IRG N2962` までの proposal / feedback chain は、[G-source Glyph and Source Reference Issues](g-source-glyph-and-reference-issues.md) に分割して追う。

## 経緯

| 年月 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2026-03 | IRG | [IRG N2928](../documents/irg-n2928.md) | U+268A1 / U+268A2 の V-source glyph について、現行 component が意図されたものか、U+810A 脊 に戻すべきかが照会された。 |
| 2026-03 | IRG | `IRG N2909` | M66.10 から M66.15 が G / T / K / UK / V source の reference と representative glyph 修正を扱った。 |
| 2026-03 | IRG | [IRG N2953](../documents/irg-n2953.md) | `IRG N2928` の follow-up として、U+268A1 / U+268A2 の V-source glyph 変更を検討する追加 evidence が提示された。 |
| 2026-04 | UTC | `L2/26-099` | CJK & Unihan Working Group が IRG \#66 recommendations と PRI feedback を UTC \#187 向け data / chart updates に変換した。 |
| 2026-04 | IRG | [IRG N2954](../documents/irg-n2954.md), [IRG N2955](../documents/irg-n2955.md) | U+2CCA3 の G-source representative glyph が original evidence と合わない問題について、修正提案と feedback が出た。 |
| 2026-05 | IRG | [IRG N2956](../documents/irg-n2956.md), [IRG N2957](../documents/irg-n2957.md) | Extension C の GBK-source 5 characters について、glyph / source reference 修正案と feedback が出た。 |
| 2026-06 | IRG | [IRG N2958](../documents/irg-n2958.md), [IRG N2959](../documents/irg-n2959.md) | G-source glyph revision と SAT-source glyph issue が提出された。 |
| 2026-06 | WG2 | `WG2 N5354` | Recommendation M73.02 が `L2/26-099` の selected sections を CJK additions and changes として ISO/IEC 10646 CD に取り込むよう勧告した。 |
| 2026-07 | IRG | [IRG N2962](../documents/irg-n2962.md) | 9 G-source glyphs の revision request が提出された。 |
| 2026-07 | IRG | `IRG N2935` | Meeting \#67 agenda Section 9.1 に representative glyph / source reference issues がまとまった。 |

## 主な論点

### source reference を変えるか、representative glyph を変えるか

`IRG N2954` は、U+2CCA3 の current glyph が `Hanyu Fangyan Dacidian` の original evidence と一致しないとして、glyph normalization か `GU` source reference への変更を選択肢にした。`IRG N2955` は、original evidence に合わせて glyph を変更し、source reference は維持する方向を支持している。

`IRG N2956` は Extension C の GBK-source 5 characters について、glyph 更新と source reference 更新を混在させた提案である。`IRG N2957` は、それぞれの文字について、glyph を変えるべきもの、reference を変えるだけでよいものを分けて feedback している。

これらの G-source specific issue は [G-source Glyph and Source Reference Issues](g-source-glyph-and-reference-issues.md) に詳細を集約する。

### evidence の強さ

[IRG N2928](../documents/irg-n2928.md) は、U+268A1 / U+268A2 の現行 V-source glyph component が意図されたものか、U+810A 脊 に戻すべきかを Vietnam NB と IRG に照会した。[IRG N2953](../documents/irg-n2953.md) は、従来 glyph を支持する evidence がある一方で、別資料に normalized form が見つかったことを示し、Vietnam NB が glyph 変更を再検討する根拠としている。`IRG N2909` の M66.15 は、Vietnam の確認では current representative glyph が意図通りであるものの、additional supporting evidence があれば将来変更提案があり得る、と整理している。

### chart glyph convention と source convention

`IRG N2958` と `IRG N2962` は、original evidence、normal form、taboo form、G-source glyph convention、GB/T 11460-2025 などを根拠に G-source glyph 修正を求める。これは「source evidence に忠実な glyph」と「member body chart convention に合わせた glyph」の間で判断が必要になる領域である。

### Unicode / ISO progression との接続

`IRG N2935` は、G-source reference の一部、T-source representative glyph、K-source representative glyph と `kRSUnicode` property change が UTC CJK & Unihan Working Group と UTC Meeting \#187 を経て Unicode Version 18.0 Beta review に反映された、と記録している。一方、Meeting \#67 に残る G / UK / V / SAT の案件は、まだ IRG 側の検討・追加 evidence・member body response が必要である。

[`L2/26-099`](../documents/utc-l2-26-099.md) は、この接続を具体的な action item に分解する文書である。`IRG N2909` の M66.10、M66.12、M66.13 などに基づき、K / T / G source の representative glyph changes、`kIRG_GSource` changes、`kRSUnicode` changes を Unihan database / code charts の更新として扱う。さらに WG2 \#73 の `WG2 N5354` Recommendation M73.02 は、その一部を ISO/IEC 10646 CD の CJK additions and changes に含めるよう勧告した。

## 関連文書

- [J-source and JMJ Source Issues](j-source.md)
- [IRG Meeting \#67](../meetings/irg/irg-meeting-67.md)
- [IRG N2928](../documents/irg-n2928.md) - U+268A1 / U+268A2 V-source glyph enquiry。
- [IRG N2953](../documents/irg-n2953.md) - `IRG N2928` follow-up evidence。
- [Unihan Database Maintenance](unihan-database-maintenance.md)
- [IRG Working Set 2024](irg-working-set-2024.md)
- [CJK Horizontal Extensions](cjk-horizontal-extensions.md)
- [kIRG_SGSource](kirg-sgsource.md)

## 関連トピック

- [G-source Glyph and Source Reference Issues](g-source-glyph-and-reference-issues.md)
- [Han Ideographic Scripts](../families/han-ideographic-scripts.md)

## 関連人物・組織

- [IRG](../people/irg.md)
- [China](../people/china.md)
- [TCA](../people/tca.md)
- [UK](../people/uk.md)
- [Vietnam](../people/vietnam.md)
- [SAT](../people/sat.md)
- [Ng Koon Hang](../people/ng-koon-hang.md)
- [Roy Wang](../people/roy-wang.md)
- [Kushim Jiang](../people/kushim-jiang.md)
- [Ma Shijie](../people/ma-shijie.md)
- [Lin Anning](../people/lin-anning.md)

## 出典

- `irg-n2909` - <https://www.unicode.org/irg/docs/n2909-Recommendations.pdf>
- `irg-n2916` - <https://www.unicode.org/irg/docs/n2916-KSourceChange.pdf>
- `irg-n2918` - <https://www.unicode.org/irg/docs/n2918-UKSourceGlyphIssues.pdf>
- `irg-n2919r` - <https://www.unicode.org/irg/docs/n2919r-GSourceChanges.pdf>
- `irg-n2923r` - <https://www.unicode.org/irg/docs/n2923r-GSourceChanges.pdf>
- `irg-n2927r` - <https://www.unicode.org/irg/docs/n2927r-TSourceGlyphChanges.pdf>
- `irg-n2928` - <https://www.unicode.org/irg/docs/n2928-VSourceGlyphIssues.pdf>
- `irg-n2930` - <https://www.unicode.org/irg/docs/n2930-GSourceChanges.pdf>
- `irg-n2935` - <https://www.unicode.org/irg/docs/n2935-ScheduleAgenda.html>
- `irg-n2953` - <https://www.unicode.org/irg/docs/n2953-IRGN2928Followup.pdf>
- `irg-n2954` - <https://www.unicode.org/irg/docs/n2954-GSourceIssue.pdf>
- `irg-n2955` - <https://www.unicode.org/irg/docs/n2955-IRGN2954Feedback.pdf>
- `irg-n2956` - <https://www.unicode.org/irg/docs/n2956-GSourceIssues.pdf>
- `irg-n2957` - <https://www.unicode.org/irg/docs/n2957-IRGN2956Feedback.pdf>
- `irg-n2958` - <https://www.unicode.org/irg/docs/n2958-GSourceGlyphIssues.pdf>
- `irg-n2959` - <https://www.unicode.org/irg/docs/n2959-SSourceGlyphIssues.pdf>
- `irg-n2962` - <https://www.unicode.org/irg/docs/n2962-GSourceGlyphIssues.pdf>
- `utc-l2-26-099` - <https://www.unicode.org/L2/L2026/26099-cjk-unihan-wg-utc187.pdf>
- `wg2-n5354` - <https://www.unicode.org/wg2/docs/n5354-Mtg73-Paris-Recs-rev5.pdf>
