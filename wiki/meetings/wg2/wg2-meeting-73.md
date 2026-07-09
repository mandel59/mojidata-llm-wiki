---
type: Meeting
title: "WG2 Meeting #73"
description: "2026-06 WG2 Meeting #73 の ISO/IEC 10646 7th edition DIS progression、external code charts、Amendment 1、Small Seal / CJK recommendations。"
slug: wg2-meeting-73
body: WG2
bodies: [WG2]
meeting: 73
date: "2026-06-22/26"
location: Paris, France
documents: [wg2-n5350r8, wg2-n5351, wg2-n5354, wg2-n5355, wg2-n5361r, wg2-n5362, wg2-n5363r, wg2-n5365, wg2-n5366, wg2-n5367, wg2-n5368, wg2-n5369, utc-l2-26-099, utc-l2-26-102]
topics: [iso-10646-edition-and-code-charts, small-seal-script, unihan-database-maintenance, unicode-18-change-sources, script-encoding-pipeline, dai-xaau-script, maya-hieroglyph-encoding, leibnizian-and-historic-mathematical-symbols, cjkv-components, kirg-sgsource]
tags: [meeting, wg2, iso-10646, dis, amendment, small-seal, cjk, unihan]
timestamp: 2026-07-08T00:00:00+09:00
---

# WG2 Meeting \#73

## 概要

WG2 Meeting \#73 は 2026-06-22/26 に Paris, France で開催された。中心は ISO/IEC 10646 7th edition CD.4 disposition の受け入れ、DIS progression、UCS code charts の external linked content 化、7th edition Amendment 1 project subdivision、Small Seal / CJK / Unihan changes、Maya review、`kIRG_SGSource` である。

この meeting の一次入口は revised agenda [WG2 N5350R8](../../documents/wg2-n5350r8.md) と recommendations [WG2 N5354](../../documents/wg2-n5354.md) である。`WG2 N5351` は minutes / action items として catalog にあるが、2026-07-08 時点では document URL が未掲載なので、決定事項は [WG2 N5354](../../documents/wg2-n5354.md) を一次ソースにする。

## 主要議題

- [ISO/IEC 10646 Edition and Code Charts](../../topics/iso-10646-edition-and-code-charts.md) - CD.4 disposition、external code charts、DIS progression、Amendment 1 project subdivision。
- [Small Seal Script](../../topics/small-seal-script.md) - [WG2 N5369](../../documents/wg2-n5369.md) の name / property / glyph correction と DIS text への反映。
- [Unihan Database Maintenance](../../topics/unihan-database-maintenance.md) - `L2/26-099` に基づく representative glyph changes、property value changes、CJK Strokes SVS。
- [Unicode 18.0 Change Sources](../../topics/unicode-18-change-sources.md) - Unicode 18.0 / ISO/IEC 10646 7th edition synchronization。
- [Script Encoding Pipeline](../../topics/script-encoding-pipeline.md) / [Dai Xaau Script](../../topics/dai-xaau-script.md) - Amendment 1 starting repertoire、SEI liaison report、Dai Xaau、Maya review。
- [Maya Hieroglyph Encoding](../../topics/maya-hieroglyph-encoding.md) - Codical Maya / Maya Hieroglyphs Extended-A の WG2 \#74 までの review request。
- [CJKV Components](../../topics/cjkv-components.md) / [kIRG_SGSource](../../topics/kirg-sgsource.md) - Amendment 1 target と Unicode 19.0 target。

## 決定事項

| Recommendation | 主語 | 内容 | 関連 |
| --- | --- | --- | --- |
| M73.01 | WG2 | [WG2 N5369](../../documents/wg2-n5369.md) の CD.4 disposition を SC2 が受け入れるよう勧告した。Chisoi removal、CJK Strokes SVS、Small Seal names / properties / glyph corrections などを含む。 | [WG2 M73.01 Small Seal CD4 disposition](../../events/wg2-m73-01-small-seal-cd4-disposition.md) |
| M73.02 | WG2 | `L2/26-099` と IRG documents に基づく CJK additions and changes を CD に入れるよう勧告した。 | [Unihan Database Maintenance](../../topics/unihan-database-maintenance.md) |
| M73.03 | WG2 | [WG2 N5363R](../../documents/wg2-n5363r.md) に基づき、UCS code charts を core text から linked content へ移す変更を 7th edition DIS に入れるよう勧告した。 | [ISO/IEC 10646 Edition and Code Charts](../../topics/iso-10646-edition-and-code-charts.md) |
| M73.04 | WG2 | M73.01-M73.03 と final disposition [WG2 N5369](../../documents/wg2-n5369.md) を含む 7th edition DIS text を SC2 secretariat へ送るよう勧告した。target は DIS 2026-10-01、IS 2027-06-01。 | [Unicode 18.0 Change Sources](../../topics/unicode-18-change-sources.md) |
| M73.05 | WG2 | [WG2 N5362](../../documents/wg2-n5362.md) と [WG2 N5361R](../../documents/wg2-n5361r.md) をもとに、7th edition Amendment 1 project subdivision を始めるよう勧告した。 | [ISO/IEC 10646 Edition and Code Charts](../../topics/iso-10646-edition-and-code-charts.md) |
| M73.06-M73.13 | WG2 | Belarusian Ruble sign、combining overlays、Leibnizian / letterlike symbols、Sirmauri、Leke、Proto-Cuneiform、Mwangwego、Shaaldaa などを first amendment / possible additions として扱った。 | [Script Encoding Pipeline](../../topics/script-encoding-pipeline.md), [Leibnizian and Historic Mathematical Symbols](../../topics/leibnizian-and-historic-mathematical-symbols.md) |
| M73.14 | WG2 | `WG2 N5366` Codical Maya Hieroglyphs と `WG2 N5367` Maya Hieroglyphs Extended-A を WG2 \#74 までに review するよう求めた。 | [Maya Hieroglyph Encoding](../../topics/maya-hieroglyph-encoding.md) |
| M73.15 | WG2 | `WG2 N5359` に基づき、new normative IRG source for Singapore `kIRG_SGSource` を Amendment 1 target として追加するよう勧告した。 | [IRG M66.16 kIRG_SGSource establishment](../../events/irg-m66-16-kirg-sgsource-establishment.md) |
| M73.16 | WG2 | Dr. Ken Lunde の IRG Convenor 再任を SC2 に勧告した。 | [IRG](../../people/irg.md) |
| M73.17 | WG2 | WG2 \#74、WG2 \#75、IRG \#67-\#69 の future meetings schedule を確認した。 | [IRG Meeting \#67](../irg/irg-meeting-67.md) |

## 後続確認

- `WG2 N5351` - WG2 \#73 minutes / action items。2026-07-08 時点では catalog entry はあるが document URL は未掲載。
- [WG2 N5363R](../../documents/wg2-n5363r.md) - external code charts の DIS text 反映。
- [WG2 N5361R](../../documents/wg2-n5361r.md) / [WG2 N5362](../../documents/wg2-n5362.md) - Amendment 1 starting repertoire と project schedule。
- [WG2 N5365](../../documents/wg2-n5365.md) - SEI liaison report と script proposal pipeline。
- [L2/26-145](../../documents/utc-l2-26-145.md) / [L2/26-146](../../documents/utc-l2-26-146.md) - Maya proposals。WG2 aliases は `WG2 N5366` / `WG2 N5367`。
- [WG2 M73.01 Small Seal CD4 disposition](../../events/wg2-m73-01-small-seal-cd4-disposition.md)

## 関連出来事

- [WG2 M73.01 Small Seal CD4 disposition](../../events/wg2-m73-01-small-seal-cd4-disposition.md)
- [IRG M66.16 kIRG_SGSource establishment](../../events/irg-m66-16-kirg-sgsource-establishment.md)

## 出典

- `wg2-n5350r8` - <https://www.unicode.org/wg2/docs/n5350R8-Meeting73Agenda.pdf>
- `wg2-n5354` - <https://www.unicode.org/wg2/docs/n5354-Mtg73-Paris-Recs-rev5.pdf>
- `wg2-n5361r` - <https://www.unicode.org/wg2/docs/n5361R-ProvisionnallyAssigned.pdf>
- `wg2-n5362` - <https://www.unicode.org/wg2/docs/n5362-proposal_to_start_new_amendment_of_10646.pdf>
- `wg2-n5363r` - <https://www.unicode.org/wg2/docs/n5363R-codechart.pdf>
- `wg2-n5365` - <https://www.unicode.org/wg2/docs/n5365-SEILiaisonReport-June2026_WG2.pdf>
- `wg2-n5368` - <https://www.unicode.org/wg2/docs/n5368-SupplementaryMaterialsDaiXaauScript.pdf>
- `wg2-n5369` - <https://www.unicode.org/wg2/docs/n5369-CD7th-4-DOC.pdf>
- `utc-l2-26-099` - <https://www.unicode.org/L2/L2026/26099-cjk-unihan-wg-utc187.pdf>
- `utc-l2-26-102` - <https://www.unicode.org/L2/L2026/26102-rmg-report-utc187.pdf>
