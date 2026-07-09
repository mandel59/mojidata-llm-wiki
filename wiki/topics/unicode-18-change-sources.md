---
type: Topic
title: Unicode 18.0 Change Sources
description: "Unicode 18.0 の変更点を調べるための公式資料と関連 UTC / WG2 / IRG 文書。"
slug: unicode-18-change-sources
bodies: [UTC, WG2, IRG]
documents: [utc-l2-25-230r, utc-l2-26-008r, utc-l2-26-092, utc-l2-26-093, utc-l2-26-073r, utc-l2-26-074, utc-l2-26-084, utc-l2-26-095, utc-l2-26-096, utc-l2-26-097, utc-l2-26-098, utc-l2-26-099, utc-l2-26-100, utc-l2-26-101, utc-l2-26-102, pri-547, pri-548, pri-552, pri-553, utc-l2-26-104, utc-l2-26-105, utc-l2-26-106, utc-l2-26-107, utc-l2-26-108, utc-l2-26-109, utc-l2-26-112, utc-l2-26-126, utc-l2-26-134, utc-l2-26-148, utc-l2-26-149, wg2-n5354, irg-n2916, irg-n2927r, irg-n2930, irg-n2935]
topics: [unicode-release-coordination-and-publication, unicode-properties-and-algorithms, script-encoding-pipeline, emoji-interoperability-and-intake, emoji-repertoire-proposals, leibnizian-and-historic-mathematical-symbols, unihan-data-format-and-property-syntax, cjk-strokes-variation-sequences, uax60-large-east-asian-scripts, t-source-representative-glyph-issues, arabic-mark-rendering, egyptian-hieroglyph-data-and-unikemet]
status: draft-release
tags: [unicode-18, release, beta, ucd, migration]
timestamp: 2026-07-07T00:00:00+09:00
---

# Unicode 18.0 Change Sources

## 概要

Unicode 18.0 の変更点は、単一の提案文書ではなく、release summary、beta review page、UCD / UAX / UTS の proposed updates、UTC Release Management Group report、WG2 recommendations、IRG / CJK & Unihan Working Group documents に分散している。2026-07-07 時点では Unicode 18.0 は draft / beta review 段階であり、公式 beta page は release planned date を 2026-09-16 としている。`L2/26-102` の RMG schedule は 2026-09-15 release を予定していたため、最終的な日付は release page / beta page を優先して確認する。

## 経緯

| 日付 | Body | 文書・資料 | できごと |
| --- | --- | --- | --- |
| 2026-03-31 | UTC | `L2/26-102` | Unicode 18.0 alpha feedback snapshot。 |
| 2026-04-03 | UTC | [L2/26-095](../documents/utc-l2-26-095.md), [L2/26-106](../documents/utc-l2-26-106.md), [L2/26-107](../documents/utc-l2-26-107.md), [L2/26-108](../documents/utc-l2-26-108.md) | Public Review Issues 一覧と、UAX \#53 Arabic Mark Rendering、UAX \#57 Unikemet、Draft UAX \#60 の proposed updates が登録された。 |
| 2026-04-11 | UTC | `L2/26-099` | CJK & Unihan Working Group が Unicode 18.0 target の Unihan / UAX \#45 / UAX \#60 / UTS \#39 / chart updates を勧告。 |
| 2026-04-14 | UTC | [L2/26-109](../documents/utc-l2-26-109.md) | UTS \#10 Unicode Collation Algorithm Revision 54 proposed update が登録された。 |
| 2026-04-15 | UTC | `L2/26-102` | RMG が UTC \#187 に Unicode 18.0 timeline、beta deliverables、ISO/IEC 10646 7th edition との同期上の変更を報告。 |
| 2026-04-16 | UTC | `L2/26-096` | PAG が properties、algorithms、security、confusables、UTS \#61 の Unicode 18.0 向け recommendations を提出。 |
| 2025-10-29/2026-01-21 | UTC | [L2/25-230R](../documents/utc-l2-25-230r.md), [L2/26-008R](../documents/utc-l2-26-008r.md) | ESR が Unicode 18.0 emoji additions と final candidate names を整理した。 |
| 2026-04-17/22 | UTC | `L2/26-097`, `098`, `100`, `101`, `126` | Editorial、Emoji、Script Encoding、Charts、ICU4X / TC39 liaison の reports が UTC \#187 の Unicode 18.0 beta review 準備に接続。 |
| 2026-04-21/23 | UTC | `L2/26-092`, `L2/26-093` | [UTC Meeting \#187](../meetings/utc/utc-meeting-187.md)。Agenda / minutes が Unicode 18.0 beta review authorization と WG reports を束ねる。 |
| 2026-04-23 | UTC | `L2/26-102` | UTC \#187 で beta content を finalize する予定。 |
| 2026-05-26 | UTC | Unicode 18.0 beta review page | Beta review 開始。beta UCD、delta charts、annex proposed updates、notable issues を公開。 |
| 2026-07-05 | UTC | [L2/26-149](../documents/utc-l2-26-149.md) | Leibnizian variation sequences と Unicode 18.0 delta charts への corrections / recommendations が提出された。 |
| 2026-07-07 | UTC | [PRI \#547](../documents/pri-547.md) | UAX \#44 Revision 37 public review が close し、UCD directory structure と release data file documentation の確認点が UTC \#188 へ接続した。 |
| 2026-07-07 | UTC | [PRI \#548](../documents/pri-548.md) | Unicode 18.0.0 Beta public review が close し、UTC \#188 content finalize に向けた feedback snapshot になった。 |
| 2026-07-07 | UTC | [PRI \#552](../documents/pri-552.md) | UAX \#29 Revision 48 public review が close し、Unicode 18.0 の text segmentation / GB9c 更新に接続した。 |
| 2026-07-07 | UTC | [PRI \#553](../documents/pri-553.md) | UTS \#39 Revision 33 public review が close し、Unicode 18.0 の security mechanisms / confusables data finalization に接続した。 |
| 2026-07-30 | UTC | `L2/26-102` | [UTC Meeting \#188](../meetings/utc/utc-meeting-188.md) で 18.0 content finalize 予定。2026-07-07 時点で agenda / minutes は未掲載。 |
| 2026-09-16 | UTC | Unicode 18.0 beta page | 公式 beta page 上の planned release date。 |

## 主な論点

### まず見るべき公式資料

Unicode 18.0 の全体像は `Unicode 18.0.0` draft release page が入口になる。このページは、character additions、new blocks、UAX / UTS changes、UCD files、UAX \#38 / UAX \#45 / UAX \#60 data files、migration implications へのリンクを持つ。正式リリース前は draft warning があるため、変更点の最終確認には beta page と UCD data directory も併用する。

Beta review page は、reviewer 向けに beta UCD、single-block delta charts、all-block charts、emoji charts、auxiliary HTML charts、annex proposed updates、related UTS updates、notable issues をまとめる。実装者が変更点を機械的に確認する場合は、summary description だけでなく beta UCD と delta charts を直接見る必要がある。

### Unicode 18.0 の大枠

Draft release page は、Unicode 18.0 が 13,047 characters を追加し、総文字数が 172,848 characters になると説明している。新 script は Chisoi、Proto-Cuneiform numerals、Jurchen、Seal の 4 つである。新 block は Bengali Supplement、Archaic Cuneiform Numerals、Chisoi、Jurchen、Jurchen Radicals、Musical Symbols Supplement、Miscellaneous Symbols and Arrows Extended、Seal である。

### CJK / Unihan / ideographic scripts の確認点

Beta review page の notable issues は、Unihan properties の review を強調している。主な確認点は、`kIRGDaeJaweon` / `kIRGKangXi` removal、`kJapaneseNewVariant` / `kJapaneseOldVariant` addition、23 properties の delimiter changes、`kGB5` / `kIRG_GSource` syntax changes、U+2B81E / U+2EA07 に関係する disunification、約 1,800 IRG source references changes、`kRSUnicode` / `kTotalStrokes` changes、G / H / K / T / U source horizontal extensions である。

`L2/26-099` は、このうち UTC \#187 における CJK & Unihan Working Group の action items をまとめる。[L2/26-074](../documents/utc-l2-26-074.md) は `kJapaneseNewVariant` / `kJapaneseOldVariant`、[L2/26-084](../documents/utc-l2-26-084.md) は `kMandarin` feedback、[L2/26-105](../documents/utc-l2-26-105.md) は UAX \#38、[L2/26-112](../documents/utc-l2-26-112.md) は UTS \#37、[L2/26-134](../documents/utc-l2-26-134.md) は `RSIndex.txt` syntax、[L2/26-148](../documents/utc-l2-26-148.md) は `kTotalStrokes` values の大規模修正を扱う。これらの data format / syntax 層は [Unihan Data Format and Property Syntax](unihan-data-format-and-property-syntax.md) に分けて読む。

### ISO/IEC 10646 7th edition との同期

`L2/26-102` は、Unicode 18.0 が ISO/IEC 10646 7th edition と同期する必要がある一方、10646 側は 2026-04 時点で committee draft stage にあり、DIS ballot は Unicode 18.0 release 前には完了しない可能性があると説明する。このため、Unicode 18.0 beta に入れる新規内容は、June 2026 の SC2 / WG2 meetings で national body concerns を解決できるように調整する必要がある。

WG2 \#73 の `WG2 N5354` は、Small Seal、CJK additions and changes、UAX \#60 title / script naming などの一部を ISO/IEC 10646 CD / DIS progression に接続する。したがって Unicode 18.0 の変更点を追うには、UTC release pages だけでなく WG2 \#73 recommendations も見る必要がある。

### UTC \#187 WG reports

UTC \#187 の重要な change source は RMG と CJK & Unihan だけではない。[L2/26-095](../documents/utc-l2-26-095.md) は 2026-03-31 時点の PRI / feedback entry point、[L2/26-096](../documents/utc-l2-26-096.md) は UCD properties、line breaking、segmentation、collation、security data を扱う。[L2/26-106](../documents/utc-l2-26-106.md)、[L2/26-107](../documents/utc-l2-26-107.md)、[L2/26-108](../documents/utc-l2-26-108.md)、[L2/26-109](../documents/utc-l2-26-109.md) は UAX \#53、UAX \#57、UAX \#60、UTS \#10 の proposed updates として、PAG report だけでは見えにくい specification text / data file の詳細を示す。

[L2/26-100](../documents/utc-l2-26-100.md) は script proposal progression と stability issues を扱う。[L2/26-097](../documents/utc-l2-26-097.md) と [L2/26-101](../documents/utc-l2-26-101.md) は core spec text、charts、NamesList、publication artifacts を扱う。[L2/25-230R](../documents/utc-l2-25-230r.md) / [L2/26-008R](../documents/utc-l2-26-008r.md) は Emoji 18.0 candidate list、[L2/26-098](../documents/utc-l2-26-098.md) は Emoji 18.0 / 19.0 の interoperability と intake を扱い、[L2/26-126](../documents/utc-l2-26-126.md) は ICU4X / TC39 実装側の接続を示す。

### 実装者が見るべき data

実装影響は UCD と synchronized UTS の data files に現れる。draft release page は UCD 18.0.0 directory、Unihan.zip、USourceData.txt / USourceGlyphs.pdf / USourceRSChart.pdf、JurchenSources.txt、SealSources.txt、NushuSources.txt、TangutSources.txt、StandardizedVariants.txt、security data、emoji data などを list of components として示している。

UAX \#57 の `Unikemet.txt` と UAX \#60 の Jurchen / Nüshu / Seal / Tangut data files は、character names だけでは追えない script-specific identity data を UCD component として扱う。UAX \#53 の AMTRA、[PRI \#552](../documents/pri-552.md) の UAX \#29 GB9c update、UTS \#10 の DUCET changes、[PRI \#553](../documents/pri-553.md) の UTS \#39 security mechanisms update は、data file だけでなく algorithm / guidance text の更新として確認する必要がある。

### Delta charts feedback

[L2/26-149](../documents/utc-l2-26-149.md) は、Leibnizian ambiguous variation sequences の descriptive names と Unicode 18.0 delta charts の wording consistency に関する feedback である。これは新規 repertoire proposal ではなく、beta / delta review artifact の correction として読む。

## 関連文書

- [L2/26-099](../documents/utc-l2-26-099.md) - CJK & Unihan Working Group Recommendations for UTC \#187。
- [L2/26-074](../documents/utc-l2-26-074.md) - `kJapaneseNewVariant` / `kJapaneseOldVariant` proposal。
- [L2/26-084](../documents/utc-l2-26-084.md) - `kMandarin` additions / changes feedback。
- [L2/26-102](../documents/utc-l2-26-102.md) - Release Management Group Report to UTC \#187。
- [PRI \#547](../documents/pri-547.md) - UAX \#44 Unicode Character Database Revision 37 public review。
- [PRI \#548](../documents/pri-548.md) - Unicode 18.0.0 Beta public review。
- [PRI \#552](../documents/pri-552.md) - UAX \#29 Unicode Text Segmentation Revision 48 public review。
- [PRI \#553](../documents/pri-553.md) - UTS \#39 Unicode Security Mechanisms Revision 33 public review。
- [L2/26-095](../documents/utc-l2-26-095.md) - Public Review Issues 一覧。
- [L2/26-096](../documents/utc-l2-26-096.md) - Properties & Algorithms Group recommendations。
- [L2/26-097](../documents/utc-l2-26-097.md) - Editorial WG report。
- [L2/26-098](../documents/utc-l2-26-098.md) - Emoji Standard & Research WG report。
- [L2/25-230R](../documents/utc-l2-25-230r.md) - UTC \#185 ESR report and Unicode 18.0 emoji short list。
- [L2/26-008R](../documents/utc-l2-26-008r.md) - UTC \#186 ESR report and CRACKING FACE name change。
- [L2/26-104](../documents/utc-l2-26-104.md) - UTS \#51 Revision 30 proposed update。
- [L2/26-106](../documents/utc-l2-26-106.md) - UAX \#53 Arabic Mark Rendering proposed update。
- [L2/26-107](../documents/utc-l2-26-107.md) - UAX \#57 Unikemet proposed update。
- [L2/26-108](../documents/utc-l2-26-108.md) - Draft UAX \#60 Revision 2。
- [L2/26-109](../documents/utc-l2-26-109.md) - UTS \#10 Unicode Collation Algorithm proposed update。
- [L2/26-100](../documents/utc-l2-26-100.md) - Script Encoding WG recommendations。
- [L2/26-101](../documents/utc-l2-26-101.md) - Charts WG report。
- [L2/26-126](../documents/utc-l2-26-126.md) - ICU4X / TC39 liaison update。
- [UTC Meeting \#187](../meetings/utc/utc-meeting-187.md) - Unicode 18.0 beta review authorization と working group reports。
- [UTC Meeting \#188](../meetings/utc/utc-meeting-188.md) - Unicode 18.0 content finalize 予定の tracking page。
- [CJK Strokes Variation Sequences](cjk-strokes-variation-sequences.md)
- [UAX \#60 Data for Large East Asian Scripts](uax60-large-east-asian-scripts.md)
- [L2/26-105](../documents/utc-l2-26-105.md) - Proposed Update UAX \#38。
- [L2/26-112](../documents/utc-l2-26-112.md) - Proposed Update UTS \#37。
- [L2/26-134](../documents/utc-l2-26-134.md) - `RSIndex.txt` syntax enhancement。
- [L2/26-148](../documents/utc-l2-26-148.md) - `kTotalStrokes` changes。
- [L2/26-149](../documents/utc-l2-26-149.md) - Leibnizian VS names and Unicode 18.0 delta charts feedback。
- `WG2 N5354` - WG2 \#73 recommendations。
- [IRG N2916](../documents/irg-n2916.md) - K-source U+2DB7C glyph / `kRSUnicode` change。
- [IRG N2927R](../documents/irg-n2927r.md) - T-source U+2976E glyph clarification。
- [IRG N2930](../documents/irg-n2930.md) - G-source reference changes。
- `IRG N2935` - IRG Meeting \#67 agenda。Unicode 18.0 Beta review 反映済みの CJK source data status を含む。

## 関連トピック

- [Unihan Database Maintenance](unihan-database-maintenance.md)
- [Unicode Release Coordination and Publication](unicode-release-coordination-and-publication.md)
- [Unicode Properties and Algorithms](unicode-properties-and-algorithms.md)
- [Script Encoding Pipeline](script-encoding-pipeline.md)
- [Emoji Interoperability and Intake](emoji-interoperability-and-intake.md)
- [Emoji Repertoire Proposals](emoji-repertoire-proposals.md)
- [Leibnizian and Historic Mathematical Symbols](leibnizian-and-historic-mathematical-symbols.md)
- [Unihan Data Format and Property Syntax](unihan-data-format-and-property-syntax.md)
- [Small Seal Script](small-seal-script.md)
- [UAX \#45 / U-Source Ideographs](uax45-u-source-ideographs.md)
- [IRG Source Data and Representative Glyphs](irg-source-data-and-representative-glyphs.md)
- [T-source Representative Glyph Issues](t-source-representative-glyph-issues.md)
- [CJK Horizontal Extensions](cjk-horizontal-extensions.md)
- [Arabic Mark Rendering](arabic-mark-rendering.md)
- [Egyptian Hieroglyph Data and Unikemet](egyptian-hieroglyph-data-and-unikemet.md)
- [UAX \#60 Data for Large East Asian Scripts](uax60-large-east-asian-scripts.md)

## 出典

- Unicode 18.0.0 draft release page - <https://www.unicode.org/versions/Unicode18.0.0/>
- Unicode 18.0.0 beta review page - <https://www.unicode.org/versions/beta-18.0.0.html>
- `pri-547` - <https://www.unicode.org/review/pri547/>
- `pri-548` - <https://www.unicode.org/review/pri548/>
- `pri-552` - <https://www.unicode.org/review/pri552/>
- `pri-553` - <https://www.unicode.org/review/pri553/>
- `utc-l2-26-099` - <https://www.unicode.org/L2/L2026/26099-cjk-unihan-wg-utc187.pdf>
- `utc-l2-26-074` - <https://www.unicode.org/L2/L2026/26074-two-new-unihan-properties.pdf>
- `utc-l2-26-084` - <https://www.unicode.org/L2/L2026/26084-kMan-feedback.pdf>
- `utc-l2-26-102` - <https://www.unicode.org/L2/L2026/26102-rmg-report-utc187.pdf>
- `utc-l2-26-095` - <https://www.unicode.org/L2/L2026/26095-public-review-issues.html>
- `utc-l2-26-092` - <https://www.unicode.org/L2/L2026/26092.htm>
- `utc-l2-26-093` - <https://www.unicode.org/L2/L2026/26093.htm>
- `utc-l2-26-096` - <https://www.unicode.org/L2/L2026/26096-pag-report-utc187.pdf>
- `utc-l2-26-097` - <https://www.unicode.org/L2/L2026/26097-edc-report-utc187.html>
- `utc-l2-26-098` - <https://www.unicode.org/L2/L2026/26098-esr-report-utc187.pdf>
- `utc-l2-25-230r` - <https://www.unicode.org/L2/L2025/25230r-esr-report-utc185.pdf>
- `utc-l2-26-008r` - <https://www.unicode.org/L2/L2026/26008r-esr-report-utc186.pdf>
- `utc-l2-26-104` - <https://www.unicode.org/L2/L2026/26104-uts51-30-update-pri543.pdf>
- `utc-l2-26-106` - <https://www.unicode.org/L2/L2026/26106-uax53-12-update-pri539.pdf>
- `utc-l2-26-107` - <https://www.unicode.org/L2/L2026/26107-uax57-6-update-pri538.pdf>
- `utc-l2-26-108` - <https://www.unicode.org/L2/L2026/26108-uax60-2-draft-pri520.pdf>
- `utc-l2-26-109` - <https://www.unicode.org/L2/L2026/26109-uts10-54-update-pri542.pdf>
- `utc-l2-26-100` - <https://www.unicode.org/L2/L2026/26100-sew-report-utc187.pdf>
- `utc-l2-26-101` - <https://www.unicode.org/L2/L2026/26101-charts-wg-rept-utc187.pdf>
- `utc-l2-26-126` - <https://www.unicode.org/L2/L2026/26126-icu4x-and-tc39-liason-report.pdf>
- `utc-l2-26-105` - <https://www.unicode.org/L2/L2026/26105-uax38-40-update-pri534.pdf>
- `utc-l2-26-112` - <https://www.unicode.org/L2/L2026/26112-uts37-15-update-pri541.pdf>
- `utc-l2-26-149` - <https://www.unicode.org/L2/L2026/26149-leibniz.pdf>
- `wg2-n5354` - <https://www.unicode.org/wg2/docs/n5354-Mtg73-Paris-Recs-rev5.pdf>
- `irg-n2916` - <https://www.unicode.org/irg/docs/n2916-KSourceChange.pdf>
- `irg-n2927r` - <https://www.unicode.org/irg/docs/n2927r-TSourceGlyphChanges.pdf>
- `irg-n2930` - <https://www.unicode.org/irg/docs/n2930-GSourceChanges.pdf>
- `irg-n2935` - <https://www.unicode.org/irg/docs/n2935-ScheduleAgenda.html>
