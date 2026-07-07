---
type: Synthesis
title: Han Ideographic Scripts
description: Han / ideographic 系の script、source data、component、indexing rules を束ねる synthesis。
slug: han-ideographic-scripts
members: [small-seal-script, uax45-u-source-ideographs, unihan-data-format-and-property-syntax, irg-working-set-2024, cjk-horizontal-extensions, jmj-horizontal-extension-review-path, cjk-hybrid-characters, cjk-multi-syllabic-and-abbreviation-characters, irg-source-data-and-representative-glyphs, g-source-glyph-and-reference-issues, kirg-sgsource, cjkv-components, irg-indexing-rules, ucv-nucv-lists]
topics: [small-seal-script, uax45-u-source-ideographs, unihan-data-format-and-property-syntax, irg-working-set-2024, cjk-horizontal-extensions, jmj-horizontal-extension-review-path, cjk-hybrid-characters, cjk-multi-syllabic-and-abbreviation-characters, irg-source-data-and-representative-glyphs, g-source-glyph-and-reference-issues, kirg-sgsource, cjkv-components, irg-indexing-rules, ucv-nucv-lists]
tags: [family, han, ideographic]
timestamp: 2026-07-06T21:31:45+09:00
---

# Han Ideographic Scripts

## 概要

Han / ideographic 系の script、block、source data、variation database にまたがる議論を束ねる family。Small Seal Script のような独立 script 提案と、IRG Working Set / source data / component / indexing rules のような CJK ideograph 運用論点をまとめる。

## メンバー

| Topic | 状態 | 一言 |
| --- | --- | --- |
| [Small Seal Script](../topics/small-seal-script.md) | in-ballot-pipeline | `Shuowen Jiezi` に基づく小篆を独立 script として符号化する提案。 |
| [UAX \#45 / U-Source Ideographs](../topics/uax45-u-source-ideographs.md) | active | UTC の U-source database、FutureWS records、`kIRG_USource`、horizontal extension の保守論点。 |
| [Unihan Data Format and Property Syntax](../topics/unihan-data-format-and-property-syntax.md) | active | UAX \#38 / UTS \#37 / RSIndex.txt / `kTotalStrokes` など Unihan 周辺 data format と property syntax の更新。 |
| [IRG Working Set 2024](../topics/irg-working-set-2024.md) | active | IRG Meeting \#67 の中心議題である WS2024 Version 5.0 review。 |
| [CJK Horizontal Extensions](../topics/cjk-horizontal-extensions.md) | active | 既存 CJK Unified Ideographs に JMJ / G / UK / U source data を追加する提案群。 |
| [JMJ Horizontal Extension Review Path](../topics/jmj-horizontal-extension-review-path.md) | active | JMJ references の J-column horizontal extension と IRG review path。 |
| [CJK Hybrid Characters](../topics/cjk-hybrid-characters.md) | active | 非 Han script components を含む Han-like characters の CJKUI / 別 block policy。 |
| [CJK Multi-Syllabic and Abbreviation Characters](../topics/cjk-multi-syllabic-and-abbreviation-characters.md) | active | Han-only abbreviation characters と script-hybrid characters の分類境界。 |
| [IRG Source Data and Representative Glyphs](../topics/irg-source-data-and-representative-glyphs.md) | active | member body source reference、representative glyph、Unihan property の修正論点。 |
| [G-source Glyph and Source Reference Issues](../topics/g-source-glyph-and-reference-issues.md) | active | G-source representative glyph と source reference correction の個別論点。 |
| [kIRG_SGSource](../topics/kirg-sgsource.md) | accepted-for-future-version | Singapore characters を `kIRG_GSource` から分離する normative source property。 |
| [CJKV Components](../topics/cjkv-components.md) | accepted-for-future-version | CJK Unified Ideographs Components-A/B の encoding proposal。 |
| [IRG Indexing Rules](../topics/irg-indexing-rules.md) | active | UCV / NUCV、FS / SC、radical assignment rules の review。 |
| [UCV and NUCV Lists](../topics/ucv-nucv-lists.md) | active | component variation の unification / disunification 境界を整理する IRG reference lists。 |

## 横断テーマ

- source references が character identity を支えるか。
- modern CJK equivalents を normative data とするか、informative / indexing data とするか。
- IRG UNC、horizontal extension、UAX \#38 / UTS \#37 との接続。
- code charts と large data files を規格本文からどう分離するか。
- component と ideograph、component と input-method fragment をどう区別するか。
- representative glyph 修正を source evidence、member body convention、Unihan property のどこで表現するか。

## 関連 family

現時点では未作成。
