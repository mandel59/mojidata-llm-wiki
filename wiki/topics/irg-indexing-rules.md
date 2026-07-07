---
type: Topic
title: IRG Indexing Rules
description: UCV / NUCV、FS / SC、radical assignment rules の IRG 運用論点。
slug: irg-indexing-rules
bodies: [IRG]
documents: [irg-n2909, irg-n2925, irg-n2931, irg-n2935, irg-n2951, irg-n2952, utc-l2-26-134, utc-l2-26-148]
topics: [unihan-data-format-and-property-syntax, ucv-nucv-lists]
status: active
tags: [irg, ucv, nucv, radicals, stroke-count]
timestamp: 2026-07-06T21:31:45+09:00
---

# IRG Indexing Rules

## 概要

IRG Indexing Rules は、CJK ideograph review で使われる component variation、first stroke、stroke count、radical assignment などの rule / reference data を束ねる topic である。これらは直接 code point を追加する proposal ではないが、unification、sorting、review workload、Unihan property values に影響する。

IRG Meeting \#67 agenda では、Updated UCV and NUCV Lists、Consolidated FS & SC Guidelines、Rules for Assigning Radicals が IRG \#66 action items の follow-up として扱われる。

UCV / NUCV は unification / disunification boundary に近いため、詳細は [UCV and NUCV Lists](ucv-nucv-lists.md) に分割する。このページでは FS / SC guidelines と radical assignment rules を中心に、IRG review infrastructure の umbrella として扱う。

## 経緯

| 年月 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2026-03 | IRG | [IRG N2909](../documents/irg-n2909.md) | M66.04 が updated UCV / NUCV examples を provisionally accept し、[IRG N2931](../documents/irg-n2931.md) の準備と review schedule を置いた。 |
| 2026-03 | IRG | `IRG N2909` | M66.18 が `IRG N2862R2` を previous FS / SC documents の replacement として accept し、final `IRG N2951` の準備を求めた。 |
| 2026-03 | IRG | `IRG N2909` | M66.19 が [IRG N2925](../documents/irg-n2925.md) をもとに condensed rules を含む `IRG N2952` を準備するよう求めた。 |
| 2026-04 | IRG | [IRG N2951](../documents/irg-n2951.md) | Consolidated FS & SC Guidelines が提出され、138 entries の structure と values を示した。 |
| 2026-07 | IRG | `IRG N2935` | Meeting \#67 agenda が UCV / NUCV comments due 2026-07-24、FS / SC final document、radical assignment follow-up を載せた。 |

## 主な論点

### UCV / NUCV lists

[IRG N2931](../documents/irg-n2931.md) は `UCS Ideograph Unifiable Component Variations Summary List (UCV)` と `Non-Unifiable Component Variations Summary List (NUCV)` をまとめる。Meeting \#67 agenda では、IRG experts が `IRG N2931` を review し、comments を 2026-07-24 までに出すことになっている。詳細は [UCV and NUCV Lists](ucv-nucv-lists.md) に集約する。

### FS / SC guidelines

[IRG N2951](../documents/irg-n2951.md) は、previous documents `IRG N954AR`、`IRG N1105`、`IRG N2171`、`IRG N2221` を置き換える consolidated FS & SC guidelines である。entry syntax は stroke count、first stroke value、ordering letter を組み合わせる形式で、FS は Annex K の values と dotted circle を使う。agenda は、この document が 2026-04-02 に posted され、IWDS Series 1 に追加されたと記録している。

[L2/26-148](../documents/utc-l2-26-148.md) は、IRG N2951 の conventions と ORT metadata checking に合わせて 458 ideographs の `kTotalStrokes` values を変更する proposal である。IRG rule そのものではなく、IRG review data を Unihan property values へ接続する変更として [Unihan Data Format and Property Syntax](unihan-data-format-and-property-syntax.md) でも扱う。

### radical assignment rules

[IRG N2925](../documents/irg-n2925.md) は Primary / Secondary Radical assignment rules の更新提案であり、WS2017 / WS2021 で続いた radical assignment の議論を背景にしている。論点は、semantic radical が discoverability を妨げる場合に primary radical を直感的に選び、technically correct radical を secondary radical とする運用と、その secondary radical の追加が ORT manager と会合時間の負担を増やしている点である。

[IRG N2925](../documents/irg-n2925.md) は、lookup 目的の追加 radical は一般利用者には有用でも IRG の encoding review の scope から外れ得るため、CJK & Unihan Working Group 側で扱う選択肢を示している。IRG \#66 は、この proposal をもとに condensed version を含む `IRG N2952` を準備するよう求めた。Meeting \#67 agenda と catalog には `IRG N2952` が載っているが、2026-07-08 の取得時点で registry URL は 404 だったため、内容の精読は後続確認とする。

## 関連文書

- [IRG Meeting \#67](../meetings/irg/irg-meeting-67.md)
- [IRG N2931](../documents/irg-n2931.md)
- [IRG N2925](../documents/irg-n2925.md)
- [IRG N2951](../documents/irg-n2951.md)
- [L2/26-134](../documents/utc-l2-26-134.md)
- [L2/26-148](../documents/utc-l2-26-148.md)
- [IRG Working Set 2024](irg-working-set-2024.md)
- [CJK Horizontal Extensions](cjk-horizontal-extensions.md)

## 関連トピック

- [Han Ideographic Scripts](../families/han-ideographic-scripts.md)
- [Unihan Data Format and Property Syntax](unihan-data-format-and-property-syntax.md)
- [UCV and NUCV Lists](ucv-nucv-lists.md)

## 関連人物・組織

- [Eiso Chan](../people/eiso-chan.md)
- [Henry Chan](../people/henry-chan.md)
- [IRG](../people/irg.md)

## 出典

- `irg-n2909` - <https://www.unicode.org/irg/docs/n2909-Recommendations.pdf>
- `irg-n2925` - <https://www.unicode.org/irg/docs/n2925-RadicalAssignments.pdf>
- `irg-n2931` - <https://www.unicode.org/irg/docs/n2931-Complete.pdf>
- `irg-n2935` - <https://www.unicode.org/irg/docs/n2935-ScheduleAgenda.html>
- `irg-n2951` - <https://www.unicode.org/irg/docs/n2951-FSSC.pdf>
- `irg-n2952` - <https://www.unicode.org/irg/docs/n2952-RadicalAssignments.pdf>（2026-07-08 取得時点で 404）
- `utc-l2-26-134` - <https://www.unicode.org/L2/L2026/26134-rsindex-syntax-change.pdf>
- `utc-l2-26-148` - <https://www.unicode.org/L2/L2026/26148-ktotalstrokes-changes.pdf>
