---
type: Event
title: IRG N2870 Japan feedback on J-source disposition
description: Japan NB が IRG N2859 へ回答し、published encoded characters の current status 維持を求めた出来事。
slug: irg-n2870-japan-feedback-on-j-source-disposition
date: "2025-09-25"
bodies: [IRG]
documents: [irg-n2722, irg-n2859, irg-n2870]
topics: [j-source, jmj-horizontal-extension-review-path, irg-source-data-and-representative-glyphs]
people: [japan, irg]
status: feedback-submitted
tags: [event, j-source, disunification, source-data]
timestamp: 2026-07-06T23:30:00+09:00
---

# IRG N2870 Japan feedback on J-source disposition

## 概要

[IRG N2870](../documents/irg-n2870.md) は、Japan NB が [IRG N2859](../documents/irg-n2859.md) の J-source disposition recommendations に回答した出来事である。Japan NB は、published encoded characters には disunification を適用しないという原則を再確認し、複数の code point について current status を維持すべきと述べた。

## 背景

[IRG N2859](../documents/irg-n2859.md) は、J-source representative glyph と source reference の整合性を改善するため、`kIRG_JSource` value や関連 Unihan properties の変更案を示していた。これに対し、Japan NB は符号化済み文字の安定性を優先する立場から回答した。

## 結果

Japan NB は、U+2A50D、U+5CC0、U+72CA、U+7BF9、U+26B20、U+2F93B、U+21694 について current status 維持を求めた。この回答により、J-source 関連の未決点は source data の整合性改善と published encoded characters の安定性の調整として残った。

## 影響範囲

この event は、Japan NB の J-source disposition に対する最新の明示的 position として扱う。WG2 M72.07 の chart glyph revert とは異なり、source reference、Unihan data、disunification の境界に関わる。

## 関連ページ

- [J-source and JMJ Source Issues](../topics/j-source.md)
- [JMJ Horizontal Extension Review Path](../topics/jmj-horizontal-extension-review-path.md)
- [IRG Source Data and Representative Glyphs](../topics/irg-source-data-and-representative-glyphs.md)
- [Japan](../people/japan.md)
- [IRG](../people/irg.md)

## 出典

- `irg-n2722` - <https://www.unicode.org/irg/docs/n2722-JSourceIssues.pdf>
- `irg-n2859` - <https://www.unicode.org/irg/docs/n2859-JapanRecommendations.pdf>
- `irg-n2870` - <https://www.unicode.org/irg/docs/n2870-IRGN2859Feedback.pdf>
