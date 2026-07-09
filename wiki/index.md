---
okf_version: "0.1"
---

# Unicode LLM Wiki

この wiki は UTC、WG2、IRG の公開文書を読み、Unicode 標準化の議論を後から辿るための OKF bundle です。

## Sections

- [Topics](topics/) - script、block、property、proposal、論点ごとの精読ページ
- [Documents](documents/) - 重要文書の要約
- [Events](events/) - 勧告、action item、状態変更などの出来事
- [Meetings](meetings/) - UTC/WG2/IRG 会合単位の要約
- [People](people/) - 人物、組織、member body
- [Families](families/) - 関連 topic を束ねる横断ページ

## Current Topics

- [Small Seal Script](topics/small-seal-script.md) - `Shuowen Jiezi` に基づく小篆を UCS / Unicode に独立 script として符号化する議論。
- [IRG Working Set 2024](topics/irg-working-set-2024.md) - IRG Meeting \#67 の中心議題である WS2024 Version 5.0 review。
- [CJK Horizontal Extensions](topics/cjk-horizontal-extensions.md) - G / UK / U source の horizontal extension 提案。
- [JMJ Horizontal Extension Review Path](topics/jmj-horizontal-extension-review-path.md) - JMJ references の J-column horizontal extension と IRG review path。
- [IRG Source Data and Representative Glyphs](topics/irg-source-data-and-representative-glyphs.md) - IRG source reference、representative glyph、Unihan property 修正の論点。
- [G-source Glyph and Source Reference Issues](topics/g-source-glyph-and-reference-issues.md) - G-source representative glyph と source reference correction の個別論点。
- [T-source Representative Glyph Issues](topics/t-source-representative-glyph-issues.md) - T-source representative glyph と source mapping correction の個別論点。
- [V-source Representative Glyph Issues](topics/v-source-representative-glyph-issues.md) - V-source / Nom evidence に基づく representative glyph と Unihan property update。
- [kIRG_SGSource](topics/kirg-sgsource.md) - Singapore characters を独立した normative IRG source property として扱う提案。
- [CJKV Components](topics/cjkv-components.md) - CJK Unified Ideographs Components-A/B の標準化提案。
- [IRG Indexing Rules](topics/irg-indexing-rules.md) - UCV / NUCV、FS / SC、radical assignment の運用 rule。
- [UCV and NUCV Lists](topics/ucv-nucv-lists.md) - component variation の unification / disunification 境界を整理する IRG reference lists。
- [CJK Strokes Variation Sequences](topics/cjk-strokes-variation-sequences.md) - CJK Strokes characters の standardized variation sequences と StandardizedVariants.txt 更新。
- [UAX \#60 Data for Large East Asian Scripts](topics/uax60-large-east-asian-scripts.md) - UAX \#60 の title / data model と Small Seal data の保守。
- [CJK Security Confusables](topics/cjk-security-confusables.md) - UTS \#39 security data における CJK confusable pairs と CJK WG review。
- [Kana](topics/kana.md) - 仮名の追加符号化、歴史的仮名、変体仮名、小書き仮名、合略仮名。
- [Japanese Place-Name Ideographs](topics/japanese-place-name-ideographs.md) - 日本の地名・登記資料に現れる未符号化漢字の UAX \#45 / FutureWS proposals。
- [Japanese Historical Ideographs](topics/japanese-historical-ideographs.md) - 日本古典籍・近世近代資料に現れる未符号化漢字の proposal。
- [CJK Hybrid Characters](topics/cjk-hybrid-characters.md) - 仮名・Bopomofo・Latin・Hangul などを部品に含む Han-like characters の CJKUI / 別 block policy。
- [CJK Multi-Syllabic and Abbreviation Characters](topics/cjk-multi-syllabic-and-abbreviation-characters.md) - Han-only abbreviation characters と script-hybrid characters の分類境界。
- [Ideographic Punctuation Proposals](topics/ideographic-punctuation-proposals.md) - Ideographic Symbols and Punctuation block 周辺の句読点追加提案。
- [J-source and JMJ Source Issues](topics/j-source.md) - JMJ-source expansion 後の glyph、source reference、`kIRG_JSource` disposition。
- [UAX \#45 / U-Source Ideographs](topics/uax45-u-source-ideographs.md) - UAX \#45 の U-source database、`kIRG_USource`、FutureWS、horizontal extension の保守論点。
- [Unicode 18.0 Change Sources](topics/unicode-18-change-sources.md) - Unicode 18.0 の変更点を調べるための公式資料と関連文書。
- [Unihan Database Maintenance](topics/unihan-database-maintenance.md) - Unihan database、UAX \#38、UTS \#37、関連 k* properties の保守論点。
- [Unihan Data Format and Property Syntax](topics/unihan-data-format-and-property-syntax.md) - UAX \#38 / UTS \#37 / RSIndex.txt / kTotalStrokes など Unihan 周辺 data format と property syntax の更新論点。
- [ISO/IEC 10646 Edition and Code Charts](topics/iso-10646-edition-and-code-charts.md) - WG2 / SC2 における ISO/IEC 10646 7th edition、DIS progression、code charts、Amendment 1 project。
- [Emoji Interoperability and Intake](topics/emoji-interoperability-and-intake.md) - UTC \#187 ESR report を入口にした emoji interoperability、CLDR keyword、intake process。
- [Emoji Repertoire Proposals](topics/emoji-repertoire-proposals.md) - Emoji 18.0 / 19.0 に向けた個別 emoji proposal、ESR short list、final candidate name の整理。
- [Script Encoding Pipeline](topics/script-encoding-pipeline.md) - UTC \#187 SEW report を入口にした script proposal の progression、保留、安定性論点。
- [Shaaldaa Script](topics/shaaldaa-script.md) - Oromo 用 Shaaldaa script の UCS 符号化提案と ISO/IEC 10646 Amendment 1 candidate としての扱い。
- [Unicode Properties and Algorithms](topics/unicode-properties-and-algorithms.md) - UTC \#187 PAG report を中心にした properties、algorithms、security data の更新論点。
- [East Asian Spacing](topics/east-asian-spacing.md) - UTR \#59 draft の East Asian visible spacing algorithm と property data。
- [Unicode Set Notation](topics/unicode-set-notation.md) - UTS \#61 draft の machine-readable Unicode set notation。
- [Arabic Mark Rendering](topics/arabic-mark-rendering.md) - UAX \#53 / AMTRA による Arabic combining marks の rendering order と property data。
- [Egyptian Hieroglyph Data and Unikemet](topics/egyptian-hieroglyph-data-and-unikemet.md) - UAX \#57 / Unikemet.txt による Egyptian hieroglyphs の catalog、source、function、Core data。
- [Unicode Release Coordination and Publication](topics/unicode-release-coordination-and-publication.md) - Unicode 18.0 beta review に向けた release、charts、editorial、liaison coordination。
- [East Asian Quotation Marks](topics/east-asian-quotation-marks.md) - East Asian text における quotation marks の core spec guidance、縦横組、地域差。
- [Chinese Folk Music Notation](topics/chinese-folk-music-notation.md) - Chinese folk music / Xiqu / Quyi notation の musical symbols と format controls。
- [Indic Script Notation and Rendering](topics/indic-script-notation-and-rendering.md) - Indic scripts における Vedic notation、combining marks、rendering guidance。
- [Leibnizian and Historic Mathematical Symbols](topics/leibnizian-and-historic-mathematical-symbols.md) - Leibnizian ambiguous signs と historic mathematical sources 用 symbols。
- [Maya Hieroglyph Encoding](topics/maya-hieroglyph-encoding.md) - Codical Maya と Classic Maya Hieroglyphs Extended-A の staged / unified encoding。
- [Plain-Text Composition and Overstriking](topics/plain-text-composition-and-overstriking.md) - COMPOSE character、overstriking、format controls と Unicode text model の境界。

## Current Families

- [Han Ideographic Scripts](families/han-ideographic-scripts.md) - Han / ideographic 系の script、source data、component、indexing rules を束ねる synthesis。
- [Emoji](families/emoji.md) - Emoji repertoire、UTS \#51、ESR intake、CLDR keyword / RGI data、interoperability を束ねる synthesis。
- [Script and Notation Proposals](families/script-and-notation-proposals.md) - Han / emoji 以外の script proposal、historic / technical symbols、notation characters、proposal pipeline を束ねる synthesis。
- [Text Model and Core Specification](families/text-model-and-core-specification.md) - Unicode text model、core specification guidance、UTR / UTS draft、ISO/IEC 10646 publication flow を束ねる synthesis。

## Source Entry Points

- [UTC Document Register](https://www.unicode.org/L2/L-curdoc.htm) - UTC Document Registry の current documents
- [WG2 Current Documents](https://www.unicode.org/wg2/WG2-curdoc.html) - WG2 Document Registry の current documents
- [IRG Current Documents](https://www.unicode.org/irg/IRG-curdoc.html) - IRG Document Register の current documents
