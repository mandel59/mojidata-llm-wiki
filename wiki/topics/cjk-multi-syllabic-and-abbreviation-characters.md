---
type: Topic
title: CJK Multi-Syllabic and Abbreviation Characters
description: Han-only の multi-syllabic / abbreviation characters と script-hybrid characters を区別する IRG 議論。
slug: cjk-multi-syllabic-and-abbreviation-characters
bodies: [IRG, WG2, UTC]
documents: [irg-n2867r, irg-n2866r2, irg-n2885r, irg-n2828, irg-n2826, utc-l2-26-057, utc-l2-26-064, utc-l2-26-071, utc-l2-26-083, utc-l2-26-085, utc-l2-26-099]
topics: [cjk-hybrid-characters, cjk-abbreviated-and-simplified-ideographs, unihan-database-maintenance, irg-indexing-rules]
events: [irg-m65-24-cjk-hybrid-characters, utc-187-uax45-futurews-additions]
status: active
tags: [cjk, abbreviation, multi-syllabic, hybrid, irg]
timestamp: 2026-07-08T00:00:00+09:00
---

# CJK Multi-Syllabic and Abbreviation Characters

## 概要

CJK multi-syllabic / abbreviation characters は、複数音節の語・単位・固有名などを 1 つの graph に圧縮する文字をどう扱うかという論点である。[IRG N2867R](../documents/irg-n2867r.md) は、機能として abbreviation であっても、components がすべて Han であれば script-hybrid character とは別に扱うべきだと整理した。

この topic は [CJK Hybrid Characters](cjk-hybrid-characters.md) の subtopic として、script boundary ではなく abbreviation function によって生じる分類問題を扱う。`⿸广K` のように Latin / Kana / Hangul / Bopomofo などを component として意図する場合は script-hybrid 側、兛・粁・糎・U+2EDEE のように Han components だけで構成される場合は通常の CJKUI review 側に寄せる、という境界が中心である。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2025-10-11 | IRG | [IRG N2885R](../documents/irg-n2885r.md) | Kim Kyongsok が `IRG N2866R` に対し、CJK Hybrid Characters の IRG P&P、terminology、legacy mapping、member body ごとの候補数見積もりを質問した。 |
| 2025-10-15 | IRG | [IRG N2866R2](../documents/irg-n2866r2.md) | Witty Wen が script-hybrid characters を CJKUI とは別 block に置く案を提示し、all-Katakana / all-hiragana 形や legacy cases の扱いも論点化した。 |
| 2025-10-15 | IRG | [IRG N2867R](../documents/irg-n2867r.md) | Witty Wen が multi-syllabic characters / abbreviation characters の分類を整理し、Han-only abbreviation characters は script-hybrid と区別して CJKUI で扱えると提案した。 |
| 2025-10-16 | IRG | [IRG N2828](../documents/irg-n2828.md) | CJK Editorial Group report が [IRG N2867R](../documents/irg-n2867r.md) を CJK Hybrid Characters 関連文書群に含め、Han-Hangul hybrid を除く hybrid characters は別 block とする提案にまとめた。 |
| 2025-10-16 | IRG | [IRG N2826](../documents/irg-n2826.md) | IRG Meeting \#65 Recommendation M65.24 が、CJK Hybrid Characters の encoding を WG2 に委ねつつ IRG oversight を残す方針を記録した。 |

## 主な論点

### abbreviation function と script identity

[IRG N2867R](../documents/irg-n2867r.md) は、「abbreviation characters」を広い機能 category とし、その中に Han-only の multi-syllabic characters と script-hybrid characters があると整理する。たとえば 兛 は 千克、粁 は kilometer、糎 は centimeter などを 1 graph に圧縮するが、components は Han script domain に留まる。

一方、`⿸广K` や `⿸广O` のように Latin letter を component として意図する場合、機能としては abbreviation でも script-hybrid character であり、CJKUI ではなく [CJK Hybrid Characters](cjk-hybrid-characters.md) 側に寄せるべきとする。

### Han-only abbreviation の CJKUI inclusion

[IRG N2867R](../documents/irg-n2867r.md) は、components がすべて Han radicals / components で、Han-based sources により実使用が裏付けられる multi-syllabic abbreviation characters は、通常の ideograph として IRG review に載せられるとする。例として、unit abbreviations や compound surname ligature U+2EDEE が挙げられる。

この方針は、CJKUI に非 Han scripts を直接 component として含めないという boundary を守りつつ、Han-only の abbreviation character まで hybrid block に送らないための分類である。

[CJK Abbreviated and Simplified Ideographs](cjk-abbreviated-and-simplified-ideographs.md) は、この分類境界の UTC / UAX \#45 側の実例として扱う。2026 年の UTC \#187 では、`L2/26-057`、`064`、`071`、`083`、`085` のような略字・俗簡字・simplified forms を含む proposals が UAX \#45 FutureWS additions として処理されたが、非 Han script component を含む script-hybrid 問題とは分けて追跡する。

### source prioritization と GB 18030

文書は、Han-only abbreviation characters について、China、Hong Kong SAR、Macao SAR、TCA などの Han-based sources に基づく proposals を優先すべきとする。十分な Han usage がある場合、GB 18030 で code-point gap を残すのではなく、mapping / encoding を検討できるという観点が示されている。

逆に、non-Han-based sources だけに由来し Han usage との関連が薄い abbreviation characters は、GB 18030 mapping を空ける判断もありうるとする。この点は encoding と national implementation の境界に関わる。

### Goryaku-gana と legacy oversight

[IRG N2867R](../documents/irg-n2867r.md) は、合略仮名（Goryaku-gana）を condensed readings として機能する abbreviation characters としつつ、CJK Unified Ideographs に入れるべきではなく独立 block が適切だと述べる。既に encoded された all-Katakana / all-hiragana shaped cases は oversight と位置づけられる。

[IRG N2866R2](../documents/irg-n2866r2.md) の U+323BF 例と同様、すでに CJKUI に入った legacy cases を移動するという決定ではなく、今後の分類・mapping・property handling の課題として扱う。

## 現状

2025-10-16 の IRG Meeting \#65 時点で、multi-syllabic / abbreviation characters だけを独立 block とする consensus は記録されていない。整理されたのは、Han-only abbreviation characters と script-hybrid characters を混同しないこと、CJK hybrid characters の broad policy は M65.24 で WG2 / IRG oversight に委ねること、property assignment rules は IRG で後続議論することまでである。

このため、この topic は [CJK Hybrid Characters](cjk-hybrid-characters.md) の subclass-specific follow-up として維持し、正式な encoding path や block proposal が出たら Source Document page と event に分離する。

## 関連文書

- [IRG N2867R](../documents/irg-n2867r.md) - Multi-Syllabic Characters and Abbreviation Characters。
- [IRG N2866R2](../documents/irg-n2866r2.md) - Script-Hybrid Characters and GB 18030。
- [IRG N2885R](../documents/irg-n2885r.md) - comments on `IRG N2866R`。
- [IRG N2828](../documents/irg-n2828.md) - Editorial Report on Miscellaneous Issues。
- [IRG N2826](../documents/irg-n2826.md) - IRG Meeting \#65 recommendations; M65.24。
- [L2/26-099](../documents/utc-l2-26-099.md) - UTC \#187 CJK & Unihan WG recommendations; UAX \#45 FutureWS additions。

## 関連トピック

- [CJK Hybrid Characters](cjk-hybrid-characters.md)
- [CJK Abbreviated and Simplified Ideographs](cjk-abbreviated-and-simplified-ideographs.md)
- [Unihan Database Maintenance](unihan-database-maintenance.md)
- [IRG Indexing Rules](irg-indexing-rules.md)

## 出典

- `irg-n2867r` - <https://www.unicode.org/irg/docs/n2867r-MultiSyllabicCharacters.pdf>
- `irg-n2866r2` - <https://www.unicode.org/irg/docs/n2866r2-ScriptHybridFeedback.pdf>
- `irg-n2885r` - <https://www.unicode.org/irg/docs/n2885r-IRGN2866RFeedback.pdf>
- `irg-n2828` - <https://www.unicode.org/irg/docs/n2828-MiscEditorialReport.pdf>
- `irg-n2826` - <https://www.unicode.org/irg/docs/n2826-Recommendations.pdf>
- `utc-l2-26-099` - <https://www.unicode.org/L2/L2026/26099.htm>
