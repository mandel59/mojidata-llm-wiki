---
type: Synthesis
title: Han Ideographic Scripts
description: Han / ideographic 系の script、source data、component、indexing rules、関連 data / symbols を束ねる synthesis。
slug: han-ideographic-scripts
members: [small-seal-script, uax60-large-east-asian-scripts, uax45-u-source-ideographs, japanese-place-name-ideographs, japanese-historical-ideographs, unihan-database-maintenance, unihan-data-format-and-property-syntax, irg-working-set-2024, cjk-horizontal-extensions, jmj-horizontal-extension-review-path, j-source, cjk-hybrid-characters, cjk-multi-syllabic-and-abbreviation-characters, irg-source-data-and-representative-glyphs, g-source-glyph-and-reference-issues, kirg-sgsource, cjkv-components, cjk-strokes-variation-sequences, irg-indexing-rules, ucv-nucv-lists, cjk-security-confusables, ideographic-punctuation-proposals]
topics: [small-seal-script, uax60-large-east-asian-scripts, uax45-u-source-ideographs, japanese-place-name-ideographs, japanese-historical-ideographs, unihan-database-maintenance, unihan-data-format-and-property-syntax, irg-working-set-2024, cjk-horizontal-extensions, jmj-horizontal-extension-review-path, j-source, cjk-hybrid-characters, cjk-multi-syllabic-and-abbreviation-characters, irg-source-data-and-representative-glyphs, g-source-glyph-and-reference-issues, kirg-sgsource, cjkv-components, cjk-strokes-variation-sequences, irg-indexing-rules, ucv-nucv-lists, cjk-security-confusables, ideographic-punctuation-proposals]
tags: [family, han, ideographic]
timestamp: 2026-07-08T00:00:00+09:00
---

# Han Ideographic Scripts

## 概要

Han / ideographic 系の script、block、source data、variation database、関連 data / symbols にまたがる議論を束ねる family。Small Seal Script のような独立 script 提案と、IRG Working Set / source data / component / indexing rules のような CJK ideograph 運用論点をまとめる。

## メンバー

| Topic | 状態 | 一言 |
| --- | --- | --- |
| [Small Seal Script](../topics/small-seal-script.md) | in-ballot-pipeline | `Shuowen Jiezi` に基づく小篆を独立 script として符号化する提案。 |
| [UAX \#60 Data for Large East Asian Scripts](../topics/uax60-large-east-asian-scripts.md) | active | Small Seal など large East Asian scripts 向け data annex の title / syntax / description 保守。 |
| [UAX \#45 / U-Source Ideographs](../topics/uax45-u-source-ideographs.md) | active | UTC の U-source database、FutureWS records、`kIRG_USource`、horizontal extension の保守論点。 |
| [Japanese Place-Name Ideographs](../topics/japanese-place-name-ideographs.md) | active | 日本の地名・登記資料に現れる未符号化漢字を UAX \#45 / FutureWS records として扱う proposals。 |
| [Japanese Historical Ideographs](../topics/japanese-historical-ideographs.md) | active | 日本古典籍・近世近代資料に現れる未符号化漢字を UTC / CJK 標準化候補として扱う proposal chain。 |
| [Unihan Database Maintenance](../topics/unihan-database-maintenance.md) | active | Unihan database、`k*` properties、release updates、property value 追加・変更・削除の umbrella。 |
| [Unihan Data Format and Property Syntax](../topics/unihan-data-format-and-property-syntax.md) | active | UAX \#38 / UTS \#37 / RSIndex.txt / `kTotalStrokes` など Unihan 周辺 data format と property syntax の更新。 |
| [IRG Working Set 2024](../topics/irg-working-set-2024.md) | active | IRG Meeting \#67 の中心議題である WS2024 Version 5.0 review。 |
| [CJK Horizontal Extensions](../topics/cjk-horizontal-extensions.md) | active | 既存 CJK Unified Ideographs に JMJ / G / UK / U source data を追加する提案群。 |
| [JMJ Horizontal Extension Review Path](../topics/jmj-horizontal-extension-review-path.md) | active | JMJ references の J-column horizontal extension と IRG review path。 |
| [J-source and JMJ Source Issues](../topics/j-source.md) | active | JMJ-source expansion 後の J-source representative glyph、source reference、`kIRG_JSource` disposition。 |
| [CJK Hybrid Characters](../topics/cjk-hybrid-characters.md) | active | 非 Han script components を含む Han-like characters の CJKUI / 別 block policy。 |
| [CJK Multi-Syllabic and Abbreviation Characters](../topics/cjk-multi-syllabic-and-abbreviation-characters.md) | active | Han-only abbreviation characters と script-hybrid characters の分類境界。 |
| [IRG Source Data and Representative Glyphs](../topics/irg-source-data-and-representative-glyphs.md) | active | member body source reference、representative glyph、Unihan property の修正論点。 |
| [G-source Glyph and Source Reference Issues](../topics/g-source-glyph-and-reference-issues.md) | active | G-source representative glyph と source reference correction の個別論点。 |
| [kIRG_SGSource](../topics/kirg-sgsource.md) | accepted-for-future-version | Singapore characters を `kIRG_GSource` から分離する normative source property。 |
| [CJKV Components](../topics/cjkv-components.md) | accepted-for-future-version | CJK Unified Ideographs Components-A/B の encoding proposal。 |
| [CJK Strokes Variation Sequences](../topics/cjk-strokes-variation-sequences.md) | accepted-for-unicode-18 | CJK Strokes characters の standardized variation sequences と `StandardizedVariants.txt` 更新。 |
| [IRG Indexing Rules](../topics/irg-indexing-rules.md) | active | UCV / NUCV、FS / SC、radical assignment rules の review。 |
| [UCV and NUCV Lists](../topics/ucv-nucv-lists.md) | active | component variation の unification / disunification 境界を整理する IRG reference lists。 |
| [CJK Security Confusables](../topics/cjk-security-confusables.md) | active | UTS \#39 security data、Unihan `kSpoofingVariant` / `kZVariant`、Han identifier policy の CJK confusables。 |
| [Ideographic Punctuation Proposals](../topics/ideographic-punctuation-proposals.md) | active | Ideographic Symbols and Punctuation block 周辺の句読点・記号追加提案。 |

## 横断テーマ

- source references が character identity を支えるか。
- modern CJK equivalents を normative data とするか、informative / indexing data とするか。
- IRG UNC、horizontal extension、UAX \#38 / UTS \#37 との接続。
- code charts と large data files を規格本文からどう分離するか。
- component と ideograph、component と input-method fragment をどう区別するか。
- representative glyph 修正を source evidence、member body convention、Unihan property のどこで表現するか。
- CJK-adjacent data / symbols を Han ideograph 本体からどこまで分け、どこで同じ review discipline に接続するか。

## 周辺だがメンバー外

- [East Asian Quotation Marks](../topics/east-asian-quotation-marks.md) - CJK text と縦横組に関わるが、主対象は quotation mark の core spec guidance であり、Han / ideographic script data ではない。
- [Unicode 18.0 Change Sources](../topics/unicode-18-change-sources.md) - release tracking の umbrella であり、この family の member topics を横断参照する入口として扱う。

## 関連 family

現時点では未作成。
