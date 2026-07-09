---
type: Topic
title: T-source Representative Glyph Issues
description: "IRG N2860 / N2861 / N2927R による T-source representative glyph と source mapping correction の整理。"
slug: t-source-representative-glyph-issues
bodies: [IRG, UTC, WG2]
documents: [irg-n2860, irg-n2861, irg-n2927r, irg-n2909, irg-n2911, utc-l2-26-099, wg2-n5354]
topics: [irg-source-data-and-representative-glyphs, unihan-database-maintenance, unicode-18-change-sources]
people: [ma-shijie, tca, irg]
meetings: [irg-meeting-66, utc-meeting-187, wg2-meeting-73]
status: active
tags: [irg, t-source, source-reference, representative-glyphs]
timestamp: 2026-07-09T00:00:00+09:00
---

# T-source Representative Glyph Issues

## 概要

T-source representative glyph issues は、TCA が担当する T-source code chart glyph と source mapping を、MOE `Dictionary of Variants`、TCA character tables、documented source evidence、standard form に照らして見直す IRG の論点である。

このページでは、Ma Shijie の [IRG N2860](../documents/irg-n2860.md)、TCA response の [IRG N2861](../documents/irg-n2861.md)、pending characters を解消した [IRG N2927R](../documents/irg-n2927r.md) をひとまとまりに扱う。親 topic の [IRG Source Data and Representative Glyphs](irg-source-data-and-representative-glyphs.md) は、G / K / T / UK / V / SAT source 全体の update queue を扱う。

## 経緯

| 年月日 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2025-08-13 | IRG | [IRG N2860](../documents/irg-n2860.md) | Ma Shijie が 25 T-source glyphs の revision request を提出し、TCA に検討を求めた。 |
| 2025-10-16 | IRG | [IRG N2861](../documents/irg-n2861.md) | TCA が MOE と協議した response として、8 no change、3 mapping change、12 modification、2 pending に分類した。 |
| 2026-03-16 | IRG | [IRG N2927R](../documents/irg-n2927r.md) | TCA が pending だった U+2976E と U+20885 を整理し、U+2976E は glyph change、U+20885 は current glyph 維持とした。 |
| 2026-03-16/20 | IRG | [IRG N2909](../documents/irg-n2909.md), [IRG N2911](../documents/irg-n2911.md) | IRG Meeting \#66 が U+2976E の T-source glyph change と U+20885 no-change を受け入れた。 |
| 2026-04-11 | UTC | [L2/26-099](../documents/utc-l2-26-099.md) | CJK & Unihan Working Group が IRG \#66 follow-up を Unicode Version 18.0 target の data / chart action に接続した。 |
| 2026-06-26 | WG2 | [WG2 N5354](../documents/wg2-n5354.md) | WG2 \#73 M73.02 が selected CJK additions and changes を ISO/IEC 10646 CD へ接続した。 |

## 主な論点

### evidence と standard form

[IRG N2860](../documents/irg-n2860.md) は、MOE `Dictionary of Variants` や original evidence に見える forms をもとに glyph revision を求めた。一方、[IRG N2861](../documents/irg-n2861.md) は、TCA character table や documented source と一致している場合、または TCA / MOE が standard form と見る場合、別 evidence があっても no change としている。

### mapping change と glyph modification

TCA response は、U+43DE、U+4BCE、U+3862 のように T-source reference を移す cases と、U+201DC、U+2697A、U+20268 などの glyph component を修正する cases を分けた。この分類は、source evidence mismatch を見つけたときに `kIRG_TSource` 相当の source reference を変えるのか、representative glyph を変えるのかを区別するために重要である。

### pending 2 characters

U+2976E と U+20885 は [IRG N2861](../documents/irg-n2861.md) では pending だった。[IRG N2927R](../documents/irg-n2927r.md) は、U+2976E について MOE が right part を 已 から 巳 に戻すことに同意したとし、U+20885 については Variants Dictionary に複数 forms があるものの current glyph を維持するとした。

## 関連文書

- [IRG N2860](../documents/irg-n2860.md) - 25 T-source glyphs の revision request。
- [IRG N2861](../documents/irg-n2861.md) - `IRG N2860` への TCA response。
- [IRG N2927R](../documents/irg-n2927r.md) - pending 2 characters の follow-up。
- [IRG N2909](../documents/irg-n2909.md), [IRG N2911](../documents/irg-n2911.md) - IRG Meeting \#66 recommendations / editorial report。
- [L2/26-099](../documents/utc-l2-26-099.md) - UTC \#187 CJK & Unihan recommendations。
- [WG2 N5354](../documents/wg2-n5354.md) - WG2 \#73 recommendations。

## 関連トピック

- [IRG Source Data and Representative Glyphs](irg-source-data-and-representative-glyphs.md)
- [Unihan Database Maintenance](unihan-database-maintenance.md)
- [Unicode 18.0 Change Sources](unicode-18-change-sources.md)

## 出典

- `irg-n2860` - <https://www.unicode.org/irg/docs/n2860-TSourceGlyphIssues.pdf>
- `irg-n2861` - <https://www.unicode.org/irg/docs/n2861-IRGN2860Feedback.pdf>
- `irg-n2927r` - <https://www.unicode.org/irg/docs/n2927r-TSourceGlyphChanges.pdf>
- `irg-n2909` - <https://www.unicode.org/irg/docs/n2909-Recommendations.pdf>
- `irg-n2911` - <https://www.unicode.org/irg/docs/n2911-MiscEditorialReport.pdf>
- `utc-l2-26-099` - <https://www.unicode.org/L2/L2026/26099-cjk-unihan-wg-utc187.pdf>
- `wg2-n5354` - <https://www.unicode.org/wg2/docs/n5354-Mtg73-Paris-Recs-rev5.pdf>
