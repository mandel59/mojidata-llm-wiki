---
type: Topic
title: Unicode Properties and Algorithms
description: "Unicode 18.0 の final UCD properties、line breaking、segmentation、collation、security changes。"
slug: unicode-properties-and-algorithms
bodies: [UTC]
documents: [utc-l2-25-220, utc-l2-26-092, utc-l2-26-093, utc-l2-26-095, utc-l2-26-096, utc-l2-26-135, utc-l2-26-151, utc-l2-26-154, utc-l2-26-212, utc-l2-26-214, utc-l2-25-100, utc-l2-26-070r, utc-l2-26-091, utc-l2-26-106, utc-l2-26-107, utc-l2-26-108, utc-l2-26-109, utc-l2-26-110, pri-509, pri-533, pri-545, pri-547, pri-549, pri-550, pri-551, pri-552, pri-553, pri-554, pri-555, pri-557, utc-l2-26-111, utc-l2-26-119, utc-l2-26-120, utc-l2-26-137, utc-l2-26-138, utc-l2-26-139]
topics: [unicode-18-change-sources, cjk-security-confusables, script-encoding-pipeline, nti-script, east-asian-spacing, unicode-set-notation, uax60-large-east-asian-scripts, arabic-mark-rendering, egyptian-hieroglyph-data-and-unikemet, indic-script-notation-and-rendering, mathematical-text-support, plain-text-composition-and-overstriking]
meetings: [utc-meeting-187, utc-meeting-188]
status: active
tags: [properties, algorithms, ucd, math, uax11, uax14, uax24, uax29, uax31, uax42, uax44, uts10, uts39, uts61, security]
timestamp: 2026-09-19T00:00:00+09:00
---

# Unicode Properties and Algorithms

## 概要

Unicode properties and algorithms は、文字追加だけでは決まらない UCD property 値、annex text、security data、collation data、segmentation behavior を調整する論点である。UTC \#188 は `L2/26-154` の recommendations を [minutes](../documents/utc-l2-26-151.md) の 188-C19〜C30 に展開し、Unicode 18.0 changes を確定した。final UAX / UTS と `/Public/18.0.0/` data を実装基準とし、後続の [PRI \#555](../documents/pri-555.md) / [PRI \#557](../documents/pri-557.md) は Unicode 19.0 cycle と分ける。

この topic は、CJK、emoji、script proposals とは別に、実装結果に直接影響する data / algorithm updates を追う入口である。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2025-04-04 | UTC | [L2/25-100](../documents/utc-l2-25-100.md) | UTR \#59 East Asian Spacing の draft public review document が登録された。 |
| 2025-10-09 | UTC | [L2/25-220](../documents/utc-l2-25-220.md) | PRI \#509 / \#510 / \#520 / \#523 / \#532 と CJK、SEW、PAG、Editorial 向けの public feedback を集約した。 |
| 2026-03-27 | UTC | [L2/26-070R](../documents/utc-l2-26-070r.md) | Multiple variation selectors を non-conformant とする revised document が提出された。 |
| 2026-04-03 | UTC | [L2/26-095](../documents/utc-l2-26-095.md) | Michelle Perham が 2025-12-30 から 2026-03-31 まで開いていた PRI 一覧を登録し、UTR \#59、UAX \#60、UTS \#61、UAX \#57、UAX \#53 などの review issue を束ねた。 |
| 2026-04-03 | UTC | [L2/26-106](../documents/utc-l2-26-106.md), [L2/26-107](../documents/utc-l2-26-107.md), [L2/26-108](../documents/utc-l2-26-108.md) | Roozbeh Pournader らが UAX \#53 AMTRA proposed update、Michel Suignard が UAX \#57 Unikemet と Draft UAX \#60 proposed updates を提出した。 |
| 2026-04-03 | UTC | [L2/26-110](../documents/utc-l2-26-110.md), [L2/26-111](../documents/utc-l2-26-111.md) | UAX \#31、UTS \#61 の proposed updates が登録された。 |
| 2026-04-13 | UTC | [L2/26-091](../documents/utc-l2-26-091.md) | Kushim Jiang が Mongolian standardized variants in UCD の deprecation を提案した。 |
| 2026-04-14 | UTC | [L2/26-109](../documents/utc-l2-26-109.md) | Ken Whistler と Markus Scherer が UTS \#10 Unicode Collation Algorithm Revision 54 proposed update を提出した。 |
| 2026-04-16 | UTC | [L2/26-096](../documents/utc-l2-26-096.md) | PAG が UTC \#187 に properties feedback と recommendations を提出した。 |
| 2026-04-21/23 | UTC | [L2/26-093](../documents/utc-l2-26-093.md) | UTC \#187 minutes が Unicode 18.0 beta review の action items として PAG report を扱った。 |
| 2026-06-09 | UTC | [L2/26-137](../documents/utc-l2-26-137.md), [L2/26-138](../documents/utc-l2-26-138.md), [L2/26-139](../documents/utc-l2-26-139.md) | UTC \#188 候補として Joining_Type for LTR scripts、consecutive anusvaras、COMPOSE proposal が登録された。 |
| 2026-07-07 | PRI | [PRI \#533](../documents/pri-533.md) | UTR \#25 Revision 16 public review の closing date。Math property / math classification data / security guidance を扱う mathematical text support の更新入口になった。 |
| 2026-07-07 | UTC | [PRI \#545](../documents/pri-545.md) | UAX \#11 Revision 45 public review が close し、Unicode 18.0 の East_Asian_Width unassigned range handling が UTC \#188 に接続した。 |
| 2026-07-07 | UTC | [PRI \#547](../documents/pri-547.md) | UAX \#44 Revision 37 public review が close し、UCD data files、derived properties、UAX \#60 data file documentation、directory structure の確認点が UTC \#188 に接続した。 |
| 2026-07-07 | UTC | [PRI \#549](../documents/pri-549.md) | UAX \#42 Revision 39 public review が close し、Unicode 18.0 の UCD XML schema、Seal / Jurchen / Unihan attributes が UTC \#188 に接続した。 |
| 2026-07-07 | UTC | [PRI \#550](../documents/pri-550.md) | UAX \#41 Revision 37 public review が close し、Unicode 18.0 の common references / versioned data URLs の確認点が UTC \#188 に接続した。 |
| 2026-07-07 | UTC | [PRI \#551](../documents/pri-551.md) | UAX \#14 Revision 56 public review が close し、Line_Break assignments と LB12a の EN DASH / NBSP behavior が UTC \#188 に接続した。 |
| 2026-07-07 | UTC | [PRI \#552](../documents/pri-552.md) | UAX \#29 Revision 48 public review が close し、GB9c / Indic_Conjunct_Break による grapheme cluster boundary の更新が UTC \#188 に接続した。 |
| 2026-07-07 | UTC | [PRI \#553](../documents/pri-553.md) | UTS \#39 Revision 33 public review が close し、security mechanisms / confusables data の Unicode 18.0 finalization が UTC \#188 に接続した。 |
| 2026-07-07 | UTC | [PRI \#554](../documents/pri-554.md) | UAX \#24 Revision 40 public review が close し、ISO 15924 mixed-script script codes の explanation が UTC \#188 に接続した。 |
| 2026-07-30 | UTC | [L2/26-151](../documents/utc-l2-26-151.md) | UTC \#188 が variation-selector conformance、UCD properties、line breaking、segmentation、collation、security changes を確定した。 |
| 2026-09-16 | Unicode | Unicode 18.0.0 release | Final UAX / UTS text、UCD、auxiliary test data、security / collation data を公開した。 |

## 主な論点

### 審議中の text processing 提案

[L2/26-135](../documents/utc-l2-26-135.md) は finite automata を使った Unicode text processing の提案、[PRI \#509](../documents/pri-509.md) は URL / email address の検出・formatting を扱う UTS \#58 公開レビューである。Unicode 18.0 の確定済み UCD 変更とは区別して読む。

### UCD property と line breaking

Final UAX \#14 は LB12a を BA × GL に変更し、U+2012 FIGURE DASH / U+2013 EN DASH を HH から BA、U+00AD SOFT HYPHEN を BA から HH へ変更した。実装者は final `LineBreak.txt` と `LineBreakTest.txt` を同時に更新する。

[PRI \#547](../documents/pri-547.md) の UAX \#44 Revision 37 は、Unicode 18.0 の UCD directory structure、property definitions、derived properties、UCD change history を読む入口である。特に `InCB=Linker` derivation、`JurchenSources.txt` / `SealSources.txt`、UAX \#60 data file documentation は、PAG report や beta data と合わせて確認する。

[PRI \#545](../documents/pri-545.md) の UAX \#11 Revision 45 は、East_Asian_Width の Section 6.1 unassigned range handling を Unicode 18.0 向けに調整する review issue である。[PRI \#551](../documents/pri-551.md) の UAX \#14 Revision 56 は、U+2012 / U+2013 / U+00AD の `Line_Break` assignments と LB12a を同時に扱うため、data file と algorithm rule の両方を確認する。

### Segmentation と derived properties

UAX \#29 GB9c と UAX \#44 の InCB=Linker derivation は、新規文字追加と連動して更新される。文字追加 proposal が独立に見えても、grapheme cluster behavior や derived property に実装差が出る場合がある。

[PRI \#552](../documents/pri-552.md) の review を経て、final UAX \#29 は GB9c から linker 前方 context の要件を除き、Balinese cluster breaking を改善した。UAX \#44 の `Indic_Conjunct_Break` derivation も `Script` ではなく `Script_Extensions` を使うため、Bengali を含む derived data と grapheme tests を合わせて更新する。

### Collation と CLDR alignment

Final UTS \#10 は Jurchen / Small Seal を implicit weighting に追加し、10 Tibetan contractions、U+FFFE / U+FFFF の special handling を加え、Shift-Trimmed option を削除した。Unicode release と CLDR release の両方に関わるため、collation は DUCET と CLDR root tailoring の差も確認する。

### Security と identifier data

Final UTS \#39 は Hntl script code support、Rule A1 の ZWNJ 周辺制約強化、`nonspacing mark` terminology の明確化を含む。`confusables.txt` は NFD で現れない未使用 lines を削除し、`IdentifierType.txt` は code point order に並べ替えられた。data diff を semantic change と単なる並べ替えに分けて検証する必要がある。

### Arabic mark rendering

[Arabic Mark Rendering](arabic-mark-rendering.md) は UAX \#53 / AMTRA の論点である。AMTRA は stored text を変更する normalization ではなく、Arabic combining marks を rendering pipeline 内で一時的に reordering し、canonically equivalent sequences を同じように表示するための algorithm として扱われる。

MCM set、CGJ override、dotted circle insertion、Arabic marks の Diacritic property は、script-specific rendering と UCD property updates の境界にある。

### Egyptian hieroglyph data と Unikemet

[Egyptian Hieroglyph Data and Unikemet](egyptian-hieroglyph-data-and-unikemet.md) は UAX \#57 / `Unikemet.txt` の論点である。Extended-A の algorithmic names を補う catalog、source、description、function、Core、orientation、alternate sequence data が、implementation と学術参照の基盤になる。

[L2/26-096](../documents/utc-l2-26-096.md) は `kEH_FVal` delimiter を `U+007C` に統一する recommendation を記録しており、Unikemet は単なる character description ではなく data file syntax / validation の問題としても読む必要がある。

### Security / confusables

UTS \#39 では casefolding wording、Identifier_Type、mid-priority confusables data、Cyrillic Extended-D などが扱われる。CJK-specific な confusables は [CJK Security Confusables](cjk-security-confusables.md) に分けるが、PAG report は broader security data の hub である。

[PRI \#553](../documents/pri-553.md) は、この UTS \#39 Revision 33 proposed update を Unicode 18.0 public review に出した entry point である。draft は `nonspacing mark` を `gc=Mn` / `gc=Me` と明確化し、古い confusable detection text を整理するため、security data files と optional detection text の両方を確認対象にする。

[L2/26-119](../documents/utc-l2-26-119.md) / [L2/26-120](../documents/utc-l2-26-120.md) の U+06C4 glyph correction は、representative glyph correction だけでなく U+06C4 / U+1EE85 confusables と cross-reference update に接続するため、script proposal と security data の境界にある。

### Variation selectors と identifiers

[L2/26-070R](../documents/utc-l2-26-070r.md) は、Variation Selector の formal definitions と misplaced default ignorable code points の security guidance を提案したが、UTC \#187 では action せず後続改訂扱いになった。[L2/26-110](../documents/utc-l2-26-110.md) は UAX \#31 Revision 44 として、Unicode 18 の新規 scripts を Excluded Scripts に追加し、identifier syntax / script classification の更新入口になる。

[L2/26-091](../documents/utc-l2-26-091.md) は、Mongolian standardized variants を `StandardizedVariants.txt` から deprecate する提案である。これは code point 追加ではなく UCD data model、variation selector semantics、Core Specification guidance の整理問題として扱う。

### Script property、UCD XML、references

[PRI \#554](../documents/pri-554.md) の UAX \#24 Revision 40 は、`Script` / `Script_Extensions` property model と ISO 15924 mixed-script script codes の関係を説明する documentation update である。新規 script proposal の採否ではなく、encoded script が property value、alias、regex、identifier handling に現れる層として読む。

[PRI \#549](../documents/pri-549.md) の UAX \#42 Revision 39 は、Unicode 18.0 の UCD XML representation に new blocks / scripts、Jurchen / Seal / Tangut attributes、Unihan property changes を反映する。plain text UCD files だけでなく XML schema を使う tool では、attribute addition / removal を確認する必要がある。

[PRI \#550](../documents/pri-550.md) の UAX \#41 Revision 37 は common references の update であり、algorithm change そのものではない。ただし Unicode 18.0 の versioned data URLs と UAX / UTS references をそろえる release artifact として、implementation review の参照先確認に関わる。

### Mathematical character properties

[Mathematical Text Support](mathematical-text-support.md) は UTR \#25 を入口に、UCD の `Math` property と UTR \#25 側の informative `MathClass` data を扱う。[PRI \#533](../documents/pri-533.md) の Revision 16 draft は HTML migration が中心だが、math data files を W3C HTML-MathML Entity definitions に合わせ、Unicode General Category を listed data に追加する更新を含む。

### East Asian Spacing と UTS \#61

[East Asian Spacing](east-asian-spacing.md) は `East_Asian_Spacing` property と algorithm を提案し、East Asian scripts と Latin / digits などの間の visible spacing を layout / UCD data の問題として扱う。

[Unicode Set Notation](unicode-set-notation.md) は UTS \#61 として draft status に進められた。set notation は properties / regular expression / tooling に関わるため、単独 proposal ではなく properties and algorithms の一部として扱う。

[UAX \#60 Data for Large East Asian Scripts](uax60-large-east-asian-scripts.md) は Jurchen、Nüshu、Seal、Tangut の source / radical-stroke / reading data を UCD data files として扱う。Small Seal data は script proposal と UCD annex の両方に接続する。

### UTC \#188 候補の text model issues

[L2/26-137](../documents/utc-l2-26-137.md) は [N'ti Script](nti-script.md) などの LTR joining scripts に対する Joining_Type property の意味を問い、[L2/26-138](../documents/utc-l2-26-138.md) は Indic scripts の valid consecutive anusvaras と rendering behavior を扱う。[L2/26-139](../documents/utc-l2-26-139.md) は COMPOSE character による overstriking を plain text として扱う proposal であり、grapheme cluster、security、normalization、font shaping に影響し得る。

## 関連文書

- [L2/26-096](../documents/utc-l2-26-096.md) - PAG report for UTC \#187。
- [PRI \#509](../documents/pri-509.md) - UTS \#58 Link Detection and Formatting の公開レビュー。
- [L2/26-135](../documents/utc-l2-26-135.md) - finite automata を使う text processing 提案。
- [L2/26-154](../documents/utc-l2-26-154.md) - UTC \#188 PAG recommendations。
- [L2/26-212](../documents/utc-l2-26-212.md) / [L2/26-214](../documents/utc-l2-26-214.md) - 後続の `Word_Break` 変更提案。採択済み data と区別する。
- [L2/26-095](../documents/utc-l2-26-095.md) - PRI \#509 から PRI \#541 までを束ねる Public Review Issues 一覧。
- [L2/26-092](../documents/utc-l2-26-092.md) - UTC \#187 Agenda。
- [L2/26-093](../documents/utc-l2-26-093.md) - UTC \#187 Meeting Minutes。
- [L2/25-100](../documents/utc-l2-25-100.md) - UTR \#59 East Asian Spacing。
- [L2/26-070R](../documents/utc-l2-26-070r.md) - multiple variation selectors conformance。
- [L2/26-091](../documents/utc-l2-26-091.md) - Mongolian standardized variants deprecation proposal。
- [L2/26-106](../documents/utc-l2-26-106.md) - UAX \#53 Arabic Mark Rendering proposed update。
- [L2/26-107](../documents/utc-l2-26-107.md) - UAX \#57 Unikemet proposed update。
- [L2/26-108](../documents/utc-l2-26-108.md) - Draft UAX \#60 Data for Non Han Ideographic Scripts。
- [L2/26-109](../documents/utc-l2-26-109.md) - UTS \#10 Unicode Collation Algorithm proposed update。
- [L2/26-110](../documents/utc-l2-26-110.md) - UAX \#31 proposed update。
- [PRI \#533](../documents/pri-533.md) - UTR \#25 Unicode Support for Mathematics Revision 16 public review。
- [PRI \#545](../documents/pri-545.md) - UAX \#11 East Asian Width Revision 45 public review。
- [PRI \#547](../documents/pri-547.md) - UAX \#44 Unicode Character Database Revision 37 public review。
- [PRI \#549](../documents/pri-549.md) - UAX \#42 Unicode Character Database in XML Revision 39 public review。
- [PRI \#550](../documents/pri-550.md) - UAX \#41 Common References for Unicode Standard Annexes Revision 37 public review。
- [PRI \#551](../documents/pri-551.md) - UAX \#14 Unicode Line Breaking Algorithm Revision 56 public review。
- [PRI \#552](../documents/pri-552.md) - UAX \#29 Unicode Text Segmentation Revision 48 public review。
- [PRI \#553](../documents/pri-553.md) - UTS \#39 Unicode Security Mechanisms Revision 33 public review。
- [PRI \#554](../documents/pri-554.md) - UAX \#24 Unicode Script Property Revision 40 public review。
- [L2/26-111](../documents/utc-l2-26-111.md) - UTS \#61 Unicode Set Notation draft。
- [L2/26-119](../documents/utc-l2-26-119.md) - U+06C4 glyph correction proposal。
- [L2/26-120](../documents/utc-l2-26-120.md) - U+06C4 glyph correction response。
- [L2/26-137](../documents/utc-l2-26-137.md) - Joining_Type for left-to-right scripts。
- [L2/26-138](../documents/utc-l2-26-138.md) - consecutive anusvaras in Indic scripts。
- [L2/26-139](../documents/utc-l2-26-139.md) - COMPOSE / overstriking proposal。

## 関連トピック

- [Unicode 18.0 Change Sources](unicode-18-change-sources.md)
- [Unicode Release Coordination and Publication](unicode-release-coordination-and-publication.md)
- [CJK Security Confusables](cjk-security-confusables.md)
- [Script Encoding Pipeline](script-encoding-pipeline.md)
- [N'ti Script](nti-script.md)
- [East Asian Spacing](east-asian-spacing.md)
- [Unicode Set Notation](unicode-set-notation.md)
- [UAX \#60 Data for Large East Asian Scripts](uax60-large-east-asian-scripts.md)
- [Arabic Mark Rendering](arabic-mark-rendering.md)
- [Egyptian Hieroglyph Data and Unikemet](egyptian-hieroglyph-data-and-unikemet.md)
- [Indic Script Notation and Rendering](indic-script-notation-and-rendering.md)
- [Mathematical Text Support](mathematical-text-support.md)
- [Plain-Text Composition and Overstriking](plain-text-composition-and-overstriking.md)

## 出典

- `pri-509` - <https://www.unicode.org/review/pri509/>
- `utc-l2-26-135` - <https://www.unicode.org/L2/L2026/26135-finite-automata.pdf>
- `utc-l2-26-154` - <https://www.unicode.org/L2/L2026/26154-utc188-properties-recs.pdf>
- `utc-l2-26-212` - <https://www.unicode.org/L2/L2026/26212-more-aletters.pdf>
- `utc-l2-26-214` - <https://www.unicode.org/L2/L2026/26214-word-break-issues.pdf>
- `utc-l2-26-096` - <https://www.unicode.org/L2/L2026/26096-pag-report-utc187.pdf>
- `utc-l2-26-095` - <https://www.unicode.org/L2/L2026/26095-public-review-issues.html>
- `utc-l2-25-100` - <https://www.unicode.org/L2/L2025/25100-utr59-1-draft-pri510.pdf>
- `utc-l2-26-070r` - <https://www.unicode.org/L2/L2026/26070r-multiple-variation-selectors-non-conformant.pdf>
- `utc-l2-26-091` - <https://www.unicode.org/L2/L2026/26091-mongolian-std-variants.pdf>
- `utc-l2-26-106` - <https://www.unicode.org/L2/L2026/26106-uax53-12-update-pri539.pdf>
- `utc-l2-26-107` - <https://www.unicode.org/L2/L2026/26107-uax57-6-update-pri538.pdf>
- `utc-l2-26-108` - <https://www.unicode.org/L2/L2026/26108-uax60-2-draft-pri520.pdf>
- `utc-l2-26-109` - <https://www.unicode.org/L2/L2026/26109-uts10-54-update-pri542.pdf>
- `utc-l2-26-110` - <https://www.unicode.org/L2/L2026/26110-uax31-44-update-pri535.pdf>
- `pri-533` - <https://www.unicode.org/review/pri533/>
- `pri-545` - <https://www.unicode.org/review/pri545/>
- `pri-547` - <https://www.unicode.org/review/pri547/>
- `pri-549` - <https://www.unicode.org/review/pri549/>
- `pri-550` - <https://www.unicode.org/review/pri550/>
- `pri-551` - <https://www.unicode.org/review/pri551/>
- `pri-552` - <https://www.unicode.org/review/pri552/>
- `pri-553` - <https://www.unicode.org/review/pri553/>
- `pri-554` - <https://www.unicode.org/review/pri554/>
- `utc-l2-26-111` - <https://www.unicode.org/L2/L2026/26111-uts61-1-draft-pri523.pdf>
- `utc-l2-26-119` - <https://www.unicode.org/L2/L2026/26119-arabic-letter-waw-with-ring-within.pdf>
- `utc-l2-26-120` - <https://www.unicode.org/L2/L2026/26120-waw-ring-glyph-change.pdf>
- `utc-l2-26-137` - <https://www.unicode.org/L2/L2026/26137-left-right.pdf>
- `utc-l2-26-138` - <https://www.unicode.org/L2/L2026/26138-consecutive-anusvaras.pdf>
- `utc-l2-26-139` - <https://www.unicode.org/L2/L2026/26139-compose.pdf>
