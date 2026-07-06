---
type: Meeting
title: "IRG Meeting #66"
description: "2026-03-16/20 の IRG Meeting #66 recommendations と Meeting #67 へ引き継がれた action items。"
slug: irg-meeting-66
kind: meeting
body: IRG
meeting: 66
date: "2026-03-16/20"
location: Virtual
documents: [irg-n2899, irg-n2909, irg-n2910, irg-n2911]
topics: [irg-working-set-2024, cjk-horizontal-extensions, irg-source-data-and-representative-glyphs, kirg-sgsource, cjkv-components, irg-indexing-rules]
tags: [meeting, irg, recommendations, ws2024]
timestamp: 2026-07-06T21:31:45+09:00
---

# IRG Meeting #66

## 概要

IRG Meeting #66 は 2026-03-16/20 に virtual meeting として開催された。会合の中心は `IRG Working Set 2024 Version 4.0` の review で、会合後の recommendation では Version 5.0 の作成 schedule が決まった。

この会合は、次回 [IRG Meeting #67](meeting-67.md) の議題の直接の前段にあたる。特に WS2024 Version 5.0、China horizontal extension、G / T / K / UK / V source glyph and reference changes、`kIRG_SGSource`、CJKV Components、UCV / NUCV、FS / SC、radical assignment rules が #67 へ引き継がれている。

## 主要議題

- [IRG Working Set 2024](../../topics/irg-working-set-2024.md) - Version 4.0 の comments / responses を review し、Version 5.0 の schedule を決めた。
- [CJK Horizontal Extensions](../../topics/cjk-horizontal-extensions.md) - China の 9156-character G-source horizontal extension と、既存 proposal からの追加 horizontal extension 候補を扱った。
- [IRG Source Data and Representative Glyphs](../../topics/irg-source-data-and-representative-glyphs.md) - G / T / K / UK / V source の source references と representative glyph corrections を整理した。
- [kIRG_SGSource](../../topics/kirg-sgsource.md) - Singapore characters を `kIRG_GSource` から分離する new normative property を IRG として勧告した。
- [CJKV Components](../../topics/cjkv-components.md) - Components-A / Components-B proposal を WG2 へ forward することを勧告した。
- [IRG Indexing Rules](../../topics/irg-indexing-rules.md) - UCV / NUCV、FS / SC guidelines、radical assignment rules を整理した。

## 決定事項

| Recommendation | 決定・要点 | 後続 |
| --- | --- | --- |
| M66.01 | Future meeting schedule を確認。#67 は Tokyo hybrid、#68 は virtual、#69 は Ho Chi Minh City hybrid、#70 は virtual、#71 は host seeking。 | #67 agenda で再確認。 |
| M66.02 | 旧 IRG document register から現行 register への migration が 2026-02-14 に完了。ただし約 700 件の early IRG documents は unavailable。 | member bodies / experts に archives 提供を依頼。 |
| M66.03 / M66.04 | UCV / NUCV lists を確認し、追加更新分を provisional accept。 | `IRG N2931` review へ。 |
| M66.05 / M66.06 | `IRG Disunified Ideographs` page を IWDS Series 4 の replacement として accept。U+2E5A2 disunification は accept しない。 | NUCV#363 に exception note。 |
| M66.07 | WS2024 Version 4.0 review を踏まえ、Version 5.0 の production schedule を決定。 | 2026-05-29 `IRG N2932`、2026-08-14 `IRG N2933`、#67 review。 |
| M66.08 | 次期 IRG working set submission estimates を member body activity report に含めるよう依頼。 | #67 activity reports。 |
| M66.09 | China の 9156-character horizontal extension `IRG N2929` を review し、revised `IRG N2929R` を #67 で扱う方針。 | 2026-08-28 feedback、2026-09-25 revised document。 |
| M66.10 / M66.11 | `IRG N2930` の 3 G-source reference changes は accept。`IRG N2919R` / `IRG N2923R` の 342 reference changes と 3 glyph changes は China response 待ち。 | #67 discussion。 |
| M66.12 / M66.13 | T-source U+2976E glyph change と K-source U+2DB7C glyph / `kRSUnicode` change を accept。 | WG2 / Unicode 18.0 pipeline へ。 |
| M66.14 / M66.15 | UK-source glyph changes と V-source U+268A1 / U+268A2 glyph changes は追加 response / evidence 待ち。 | #67 discussion または将来提案。 |
| M66.16 | new normative `kIRG_SGSource` property を establish し、`GS` prefix を `SG` source へ移すことを勧告。 | WG2 #73 へ提出。 |
| M66.17 | `IRG N2878R3` の CJK Unified Ideographs Components-A / B を WG2 へ forward することを勧告。 | Proposal Summary Form を付けて WG2 #73 へ。 |
| M66.18 / M66.19 | FS / SC guidelines を consolidated document へ置換し、radical assignment rules の final document 作成を指示。 | `IRG N2951`, `IRG N2952`。 |
| M66.20 | IRG P&P Version 18 Draft 2 を accept。 | final version publication。 |

## 後続確認

- [IRG Meeting #67](meeting-67.md) - #66 recommendations の follow-up が agenda Section 4 にまとまっている。
- `IRG N2932` - WS2024 Version 5.0。
- `IRG N2933` - WS2024 Version 5.0 consolidated comments。2026-07-06 の作業時点では文書実体未確認。
- `IRG N2929R` - China horizontal extension revised document。
- `IRG N2951` - Consolidated FS & SC Guidelines。
- `IRG N2952` - Rules for Assigning Radicals。2026-07-06 の作業時点では文書実体未確認。

## 出典

- `irg-n2899` - <https://www.unicode.org/irg/docs/n2899-ScheduleAgenda.html>
- `irg-n2909` - <https://www.unicode.org/irg/docs/n2909-Recommendations.pdf>
- `irg-n2910` - <https://www.unicode.org/irg/docs/n2910-EditorialReport.pdf>
- `irg-n2911` - <https://www.unicode.org/irg/docs/n2911-MiscEditorialReport.pdf>
