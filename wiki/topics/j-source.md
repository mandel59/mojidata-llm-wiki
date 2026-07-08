---
type: Topic
title: J-source and JMJ Source Issues
description: JMJ-source expansion 後の J-source representative glyph、source reference、kIRG_JSource disposition の議論。
slug: j-source
bodies: [WG2, IRG, UTC]
documents: [irg-n2722, wg2-n5296, wg2-n5301, wg2-n5304, irg-n2859, irg-n2870]
topics: [jmj-horizontal-extension-review-path, irg-source-data-and-representative-glyphs, cjk-horizontal-extensions]
events: [wg2-m72-07-j-source-glyph-revert, irg-n2859-j-source-disposition-request, irg-n2870-japan-feedback-on-j-source-disposition]
status: active
tags: [cjk, source-data, j-source, jmj, unihan]
timestamp: 2026-07-08T00:00:00+09:00
---

# J-source and JMJ Source Issues

## 概要

J-source は、ISO/IEC 10646 / Unicode の CJK Unified Ideographs における Japan source reference 群である。この topic は、JMJ-source expansion 後に表面化した representative glyph、source reference、`kIRG_JSource` / related Unihan data の correction and disposition を扱う。

大規模な JMJ references の J-column 追加 request と、その review body を WG2 から IRG に接続する議論は [JMJ Horizontal Extension Review Path](jmj-horizontal-extension-review-path.md) に分ける。この page では、追加後に見つかった glyph / source correspondence issue と、WG2 / IRG での処理を追う。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2024-09-18 | IRG | [IRG N2722](../documents/irg-n2722.md) | Yi Bai と Eiso Chan が JMJ horizontal extension 後の source reference / glyph correspondence issues を指摘した。 |
| 2025-02-18 | WG2 | [WG2 N5296](../documents/wg2-n5296.md) | CheonHyeong Sim が JMJ-source related glyph issues を提出し、code chart generation の font selection により既存 J-source / JK-source glyphs が変わって見える問題を指摘した。 |
| 2025-06-23/27 | WG2 | [WG2 N5301](../documents/wg2-n5301.md), [WG2 N5304](../documents/wg2-n5304.md) | [WG2 M72.07 J-source glyph revert recommendation](../events/wg2-m72-07-j-source-glyph-revert.md)。WG2 側で chart glyph stability の問題として処理された。 |
| 2025-08-13 | IRG | [IRG N2859](../documents/irg-n2859.md) | [IRG N2859 J-source disposition request](../events/irg-n2859-j-source-disposition-request.md)。IRG 側で source reference / Unihan data maintenance を含む disposition 案に進んだ。 |
| 2025-09-25 | IRG | [IRG N2870](../documents/irg-n2870.md) | [IRG N2870 Japan feedback on J-source disposition](../events/irg-n2870-japan-feedback-on-j-source-disposition.md)。Japan NB が符号化済み文字の current status 維持を求めた。 |

## 主な論点

### JMJ reference と code point / glyph の対応

[IRG N2722](../documents/irg-n2722.md) は、JMJ horizontal extension 後に、glyph shape と code point 対応に問題がある例を挙げる。JMJ-016916 / JMJ-016917 と U+72CA / U+3094D、JMJ-046312 / JMJ-046313 と U+26B20 / U+26B07、JMJ-043941 と U+25CBB / U+7BF9 などが中心である。

[IRG N2859](../documents/irg-n2859.md) はこれらを disposition 案に落とし込み、U+72CA の `kIRG_JSource` を JMJ-016916 から JMJ-016917 に変え、U+3094D に JMJ-016916 を horizontal extension する案などを示した。一方、U+7BF9 / U+25CBB や JMJ-055359 / JMJ-055360 については no action を勧告している。

### font selection と representative glyph

[WG2 N5296](../documents/wg2-n5296.md) は、code chart generation における font selection の変更が J-source representative glyph の見え方を変えた問題を扱う。CJK Extension C の JK-source characters と compatibility block の J-source characters で、HeiseiMincho / MS Mincho から IPAmjMincho へ変わった例があり、文書は Japan NB の明確な position を求めている。

[WG2 N5301](../documents/wg2-n5301.md) と [WG2 N5304](../documents/wg2-n5304.md) は、M72.07 として `WG2 N5296` に記載された J-source glyph changes を revert するよう Project Editor に勧告した。この outcome は [WG2 M72.07 J-source glyph revert recommendation](../events/wg2-m72-07-j-source-glyph-revert.md) に集約する。

### disunification と published encoded characters

[IRG N2859](../documents/irg-n2859.md) の disposition request と [IRG N2870](../documents/irg-n2870.md) の Japan NB feedback は、それぞれ [IRG N2859 J-source disposition request](../events/irg-n2859-j-source-disposition-request.md) と [IRG N2870 Japan feedback on J-source disposition](../events/irg-n2870-japan-feedback-on-j-source-disposition.md) に集約する。この topic の未決点は「J-source data の整合性を高める変更」と「符号化済み文字の安定性」の衝突である。

## 現状

2025-09-25 の [IRG N2870](../documents/irg-n2870.md) 時点では、Japan NB は [IRG N2859](../documents/irg-n2859.md) の変更案に対し、current status 維持を求める立場を明示した。WG2 側では [WG2 N5296](../documents/wg2-n5296.md) に対して M72.07 が採択され、J-source glyph changes の revert が勧告済みである。

一方、IRG 側の J-source disposition が Unicode 18.0 / ISO/IEC 10646 Seventh Edition の data にどう反映されるかは、Japan NB の回答と IRG / WG2 / UTC 側の後続処理を追う必要がある。大規模 JMJ horizontal extension request そのものの review path は [JMJ Horizontal Extension Review Path](jmj-horizontal-extension-review-path.md) から辿る。

## 関連文書

- [IRG N2722](../documents/irg-n2722.md) - JMJ horizontal extension issue report。
- [WG2 N5296](../documents/wg2-n5296.md) - JMJ-source related glyph issues。
- [WG2 N5301](../documents/wg2-n5301.md) - WG2 Meeting \#72 minutes; Section 11 と M72.07。
- [WG2 N5304](../documents/wg2-n5304.md) - WG2 Meeting \#72 recommendations。
- [IRG N2859](../documents/irg-n2859.md) - J-source disposition recommendations。
- [IRG N2870](../documents/irg-n2870.md) - Japan NB comment on `IRG N2859`。

## 関連出来事

- [WG2 M72.07 J-source glyph revert recommendation](../events/wg2-m72-07-j-source-glyph-revert.md)
- [IRG N2859 J-source disposition request](../events/irg-n2859-j-source-disposition-request.md)
- [IRG N2870 Japan feedback on J-source disposition](../events/irg-n2870-japan-feedback-on-j-source-disposition.md)

## 関連トピック

- [Han Ideographic Scripts](../families/han-ideographic-scripts.md)
- [JMJ Horizontal Extension Review Path](jmj-horizontal-extension-review-path.md)
- [IRG Source Data and Representative Glyphs](irg-source-data-and-representative-glyphs.md)
- [CJK Horizontal Extensions](cjk-horizontal-extensions.md)

## 関連人物・組織

- [Japan](../people/japan.md)
- [WG2](../people/wg2.md)
- [IRG](../people/irg.md)

## 出典

- `irg-n2722` - <https://www.unicode.org/irg/docs/n2722-JSourceIssues.pdf>
- `wg2-n5296` - <https://www.unicode.org/wg2/docs/n5296-JMJ-source%20related%20glyph%20issues.pdf>
- `wg2-n5301` - <https://www.unicode.org/wg2/docs/n5301-M72minutes-JP-2025-rev5.pdf>
- `wg2-n5304` - <https://www.unicode.org/wg2/docs/n5304-Mtg72-Niigata-Recs-rev5-final.pdf>
- `irg-n2859` - <https://www.unicode.org/irg/docs/n2859-JapanRecommendations.pdf>
- `irg-n2870` - <https://www.unicode.org/irg/docs/n2870-IRGN2859Feedback.pdf>
