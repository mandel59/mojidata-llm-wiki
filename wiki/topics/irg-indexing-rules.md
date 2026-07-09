---
type: Topic
title: IRG Indexing Rules
description: UCV / NUCV、FS / SC、radical assignment rules の IRG 運用論点。
slug: irg-indexing-rules
bodies: [IRG]
documents: [irg-n1105, irg-n2171, irg-n2221, irg-n2826, irg-n2862r2, irg-n2909, irg-n2915, irg-n2925, irg-n2931, irg-n2935, irg-n2951, irg-n2952, utc-l2-26-134, utc-l2-26-148]
topics: [unihan-data-format-and-property-syntax, ucv-nucv-lists, cjk-hybrid-characters, cjk-multi-syllabic-and-abbreviation-characters]
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
| 2005-01 | IRG | [IRG N1105](../documents/irg-n1105.md) | `IRG N954AR` の first stroke / stroke count amendments を示し、後続 stroke counting guideline の predecessor になった。 |
| 2017-06 | IRG | [IRG N2171](../documents/irg-n2171.md) | Chen Zhuang が UCS 内の stroke counting differences を整理し、Henry Chan / KR feedback を含む draft guideline として共有した。 |
| 2017-07 | IRG | [IRG N2221](../documents/irg-n2221.md) | `IRG N954AR`、N1105、N2171 の SC entries を consolidate し、future IRG Working Set で使う guideline とした。 |
| 2025-11 | IRG | [IRG N2915](../documents/irg-n2915.md) | Kim Kyongsok が `IRG N2862` の FS values について、radical 情報と FS value 選択原理の明示を求めた。 |
| 2026-01 | IRG | [IRG N2862R2](../documents/irg-n2862r2.md) | Eiso Chan が N2862 への feedback を受けて SC / FS guideline R2 を提出し、N2915 への response も記録した。 |
| 2026-03 | IRG | [IRG N2909](../documents/irg-n2909.md) | M66.04 が updated UCV / NUCV examples を provisionally accept し、[IRG N2931](../documents/irg-n2931.md) の準備と review schedule を置いた。 |
| 2026-03 | IRG | [IRG N2909](../documents/irg-n2909.md) | M66.18 が [IRG N2862R2](../documents/irg-n2862r2.md) を previous FS / SC documents の replacement として accept し、final [IRG N2951](../documents/irg-n2951.md) の準備を求めた。 |
| 2026-03 | IRG | `IRG N2909` | M66.19 が [IRG N2925](../documents/irg-n2925.md) をもとに condensed rules を含む `IRG N2952` を準備するよう求めた。 |
| 2026-04 | IRG | [IRG N2951](../documents/irg-n2951.md) | Consolidated FS & SC Guidelines が提出され、138 entries の structure と values を示した。 |
| 2026-07 | IRG | `IRG N2935` | Meeting \#67 agenda が UCV / NUCV comments due 2026-07-24、FS / SC final document、radical assignment follow-up を載せた。 |

## 主な論点

### UCV / NUCV lists

[IRG N2931](../documents/irg-n2931.md) は `UCS Ideograph Unifiable Component Variations Summary List (UCV)` と `Non-Unifiable Component Variations Summary List (NUCV)` をまとめる。Meeting \#67 agenda では、IRG experts が `IRG N2931` を review し、comments を 2026-07-24 までに出すことになっている。詳細は [UCV and NUCV Lists](ucv-nucv-lists.md) に集約する。

### FS / SC guidelines

[IRG N1105](../documents/irg-n1105.md) は `IRG N954AR` への amendments、[IRG N2171](../documents/irg-n2171.md) は UCS 内の stroke counting differences と expert feedback、[IRG N2221](../documents/irg-n2221.md) はそれらの consolidated SC entries である。N2221 は existing UCS code charts と異なる stroke count を future IRG Working Set で使う場合があることを明示しており、後続 guideline の predecessor になる。

[IRG N2862R2](../documents/irg-n2862r2.md) は、N2862 への feedback を反映した SC / FS guideline revision であり、entry syntax、Shape / Variants columns、dotted circle を含む不確定 values を整理した。[IRG N2915](../documents/irg-n2915.md) は、FS values の根拠を理解するには radical 情報と選択原理の明示が必要だとする KR feedback である。N2862R2 は N2915 に基づく変更は入れていないが、response として radical / non-radical distinction を不要とする理由を記録した。

[IRG N2951](../documents/irg-n2951.md) は、previous documents `IRG N954AR`、`IRG N1105`、`IRG N2171`、`IRG N2221`、[IRG N2862R2](../documents/irg-n2862r2.md) を置き換える consolidated FS & SC guidelines である。entry syntax は stroke count、first stroke value、ordering letter を組み合わせる形式で、FS は Annex K の values と dotted circle を使う。agenda は、この document が 2026-04-02 に posted され、IWDS Series 1 に追加されたと記録している。

[L2/26-148](../documents/utc-l2-26-148.md) は、IRG N2951 の conventions と ORT metadata checking に合わせて 458 ideographs の `kTotalStrokes` values を変更する proposal である。IRG rule そのものではなく、IRG review data を Unihan property values へ接続する変更として [Unihan Data Format and Property Syntax](unihan-data-format-and-property-syntax.md) でも扱う。

### radical assignment rules

[IRG N2925](../documents/irg-n2925.md) は Primary / Secondary Radical assignment rules の更新提案であり、WS2017 / WS2021 で続いた radical assignment の議論を背景にしている。論点は、semantic radical が discoverability を妨げる場合に primary radical を直感的に選び、technically correct radical を secondary radical とする運用と、その secondary radical の追加が ORT manager と会合時間の負担を増やしている点である。

[IRG N2925](../documents/irg-n2925.md) は、lookup 目的の追加 radical は一般利用者には有用でも IRG の encoding review の scope から外れ得るため、CJK & Unihan Working Group 側で扱う選択肢を示している。IRG \#66 は、この proposal をもとに condensed version を含む `IRG N2952` を準備するよう求めた。Meeting \#67 agenda と catalog には `IRG N2952` が載っているが、2026-07-08 の取得時点で registry URL は 404 だったため、内容の精読は後続確認とする。

## 関連文書

- [IRG Meeting \#67](../meetings/irg/irg-meeting-67.md)
- [IRG N1105](../documents/irg-n1105.md)
- [IRG N2171](../documents/irg-n2171.md)
- [IRG N2221](../documents/irg-n2221.md)
- [IRG N2862R2](../documents/irg-n2862r2.md)
- [IRG N2915](../documents/irg-n2915.md)
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
- [CJK Hybrid Characters](cjk-hybrid-characters.md)
- [CJK Multi-Syllabic and Abbreviation Characters](cjk-multi-syllabic-and-abbreviation-characters.md)

## 関連人物・組織

- [Eiso Chan](../people/eiso-chan.md)
- [Kim Kyongsok](../people/kim-kyongsok.md)
- [Henry Chan](../people/henry-chan.md)
- [IRG](../people/irg.md)

## 出典

- `irg-n2862r2` - <https://www.unicode.org/irg/docs/n2862r2-SCFS.pdf>
- `irg-n1105` - <https://www.unicode.org/irg/docs/n1105-IRGN954AR-Amendment.pdf>
- `irg-n2171` - <https://www.unicode.org/irg/docs/n2171-StrokeCountingGuidelines.pdf>
- `irg-n2221` - <https://www.unicode.org/irg/docs/n2221-StrokeCountingGuidelines.pdf>
- `irg-n2915` - <https://www.unicode.org/irg/docs/n2915-IRGN2862Feedback.pdf>
- `irg-n2909` - <https://www.unicode.org/irg/docs/n2909-Recommendations.pdf>
- `irg-n2925` - <https://www.unicode.org/irg/docs/n2925-RadicalAssignments.pdf>
- `irg-n2931` - <https://www.unicode.org/irg/docs/n2931-Complete.pdf>
- `irg-n2935` - <https://www.unicode.org/irg/docs/n2935-ScheduleAgenda.html>
- `irg-n2951` - <https://www.unicode.org/irg/docs/n2951-FSSC.pdf>
- `irg-n2952` - <https://www.unicode.org/irg/docs/n2952-RadicalAssignments.pdf>（2026-07-08 取得時点で 404）
- `utc-l2-26-134` - <https://www.unicode.org/L2/L2026/26134-rsindex-syntax-change.pdf>
- `utc-l2-26-148` - <https://www.unicode.org/L2/L2026/26148-ktotalstrokes-changes.pdf>
