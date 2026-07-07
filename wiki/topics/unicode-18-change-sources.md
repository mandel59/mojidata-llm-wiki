---
type: Topic
title: Unicode 18.0 Change Sources
description: "Unicode 18.0 の変更点を調べるための公式資料と関連 UTC / WG2 / IRG 文書。"
slug: unicode-18-change-sources
bodies: [UTC, WG2, IRG]
documents: [utc-l2-26-092, utc-l2-26-093, utc-l2-26-073r, utc-l2-26-099, utc-l2-26-102, utc-l2-26-105, utc-l2-26-112, wg2-n5354, irg-n2935]
topics: [cjk-strokes-variation-sequences, uax60-large-east-asian-scripts]
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
| 2026-04-23 | UTC | `L2/26-102` | UTC #187 で beta content を finalize する予定。 |
| 2026-04-11 | UTC | `L2/26-099` | CJK & Unihan Working Group が Unicode 18.0 target の Unihan / UAX #45 / UAX #60 / UTS #39 / chart updates を勧告。 |
| 2026-04-15 | UTC | `L2/26-102` | RMG が UTC #187 に Unicode 18.0 timeline、beta deliverables、ISO/IEC 10646 7th edition との同期上の変更を報告。 |
| 2026-04-21/23 | UTC | `L2/26-092`, `L2/26-093` | [UTC Meeting #187](../meetings/utc/utc-meeting-187.md)。Agenda / minutes が Unicode 18.0 beta review authorization と WG reports を束ねる。 |
| 2026-05-26 | UTC | Unicode 18.0 beta review page | Beta review 開始。beta UCD、delta charts、annex proposed updates、notable issues を公開。 |
| 2026-07-07 | UTC | Unicode 18.0 beta review page | Beta public review close / feedback snapshot。 |
| 2026-07-30 | UTC | `L2/26-102` | [UTC Meeting #188](../meetings/utc/utc-meeting-188.md) で 18.0 content finalize 予定。2026-07-07 時点で agenda / minutes は未掲載。 |
| 2026-09-16 | UTC | Unicode 18.0 beta page | 公式 beta page 上の planned release date。 |

## 主な論点

### まず見るべき公式資料

Unicode 18.0 の全体像は `Unicode 18.0.0` draft release page が入口になる。このページは、character additions、new blocks、UAX / UTS changes、UCD files、UAX #38 / UAX #45 / UAX #60 data files、migration implications へのリンクを持つ。正式リリース前は draft warning があるため、変更点の最終確認には beta page と UCD data directory も併用する。

Beta review page は、reviewer 向けに beta UCD、single-block delta charts、all-block charts、emoji charts、auxiliary HTML charts、annex proposed updates、related UTS updates、notable issues をまとめる。実装者が変更点を機械的に確認する場合は、summary description だけでなく beta UCD と delta charts を直接見る必要がある。

### Unicode 18.0 の大枠

Draft release page は、Unicode 18.0 が 13,047 characters を追加し、総文字数が 172,848 characters になると説明している。新 script は Chisoi、Proto-Cuneiform numerals、Jurchen、Seal の 4 つである。新 block は Bengali Supplement、Archaic Cuneiform Numerals、Chisoi、Jurchen、Jurchen Radicals、Musical Symbols Supplement、Miscellaneous Symbols and Arrows Extended、Seal である。

### CJK / Unihan / ideographic scripts の確認点

Beta review page の notable issues は、Unihan properties の review を強調している。主な確認点は、`kIRGDaeJaweon` / `kIRGKangXi` removal、`kJapaneseNewVariant` / `kJapaneseOldVariant` addition、23 properties の delimiter changes、`kGB5` / `kIRG_GSource` syntax changes、U+2B81E / U+2EA07 に関係する disunification、約 1,800 IRG source references changes、`kRSUnicode` / `kTotalStrokes` changes、G / H / K / T / U source horizontal extensions である。

`L2/26-099` は、このうち UTC #187 における CJK & Unihan Working Group の action items をまとめる。`L2/26-105` は UAX #38、`L2/26-112` は UTS #37、`L2/26-134` は `RSIndex.txt` syntax、`L2/26-148` は `kTotalStrokes` values の大規模修正を扱う。

### ISO/IEC 10646 7th edition との同期

`L2/26-102` は、Unicode 18.0 が ISO/IEC 10646 7th edition と同期する必要がある一方、10646 側は 2026-04 時点で committee draft stage にあり、DIS ballot は Unicode 18.0 release 前には完了しない可能性があると説明する。このため、Unicode 18.0 beta に入れる新規内容は、June 2026 の SC2 / WG2 meetings で national body concerns を解決できるように調整する必要がある。

WG2 #73 の `WG2 N5354` は、Small Seal、CJK additions and changes、UAX #60 title / script naming などの一部を ISO/IEC 10646 CD / DIS progression に接続する。したがって Unicode 18.0 の変更点を追うには、UTC release pages だけでなく WG2 #73 recommendations も見る必要がある。

### 実装者が見るべき data

実装影響は UCD と synchronized UTS の data files に現れる。draft release page は UCD 18.0.0 directory、Unihan.zip、USourceData.txt / USourceGlyphs.pdf / USourceRSChart.pdf、JurchenSources.txt、SealSources.txt、NushuSources.txt、TangutSources.txt、StandardizedVariants.txt、security data、emoji data などを list of components として示している。

## 関連文書

- [L2/26-099](../documents/utc-l2-26-099.md) - CJK & Unihan Working Group Recommendations for UTC #187。
- [L2/26-102](../documents/utc-l2-26-102.md) - Release Management Group Report to UTC #187。
- [UTC Meeting #187](../meetings/utc/utc-meeting-187.md) - Unicode 18.0 beta review authorization と working group reports。
- [UTC Meeting #188](../meetings/utc/utc-meeting-188.md) - Unicode 18.0 content finalize 予定の tracking page。
- [CJK Strokes Variation Sequences](cjk-strokes-variation-sequences.md)
- [UAX #60 Data for Large East Asian Scripts](uax60-large-east-asian-scripts.md)
- `L2/26-105` - Proposed Update UAX #38。
- `L2/26-112` - Proposed Update UTS #37。
- `WG2 N5354` - WG2 #73 recommendations。
- `IRG N2935` - IRG Meeting #67 agenda。Unicode 18.0 Beta review 反映済みの CJK source data status を含む。

## 関連トピック

- [Unihan Database Maintenance](unihan-database-maintenance.md)
- [Small Seal Script](small-seal-script.md)
- [UAX #45 U-Source Ideographs](uax45-u-source-ideographs.md)
- [IRG Source Data and Representative Glyphs](irg-source-data-and-representative-glyphs.md)
- [CJK Horizontal Extensions](cjk-horizontal-extensions.md)

## 出典

- Unicode 18.0.0 draft release page - <https://www.unicode.org/versions/Unicode18.0.0/>
- Unicode 18.0.0 beta review page - <https://www.unicode.org/versions/beta-18.0.0.html>
- `utc-l2-26-099` - <https://www.unicode.org/L2/L2026/26099-cjk-unihan-wg-utc187.pdf>
- `utc-l2-26-102` - <https://www.unicode.org/L2/L2026/26102-rmg-report-utc187.pdf>
- `utc-l2-26-092` - <https://www.unicode.org/L2/L2026/26092.htm>
- `utc-l2-26-093` - <https://www.unicode.org/L2/L2026/26093.htm>
- `utc-l2-26-105` - <https://www.unicode.org/L2/L2026/26105-uax38-40-update-pri534.pdf>
- `utc-l2-26-112` - <https://www.unicode.org/L2/L2026/26112-uts37-15-update-pri541.pdf>
- `wg2-n5354` - <https://www.unicode.org/wg2/docs/n5354-Mtg73-Paris-Recs-rev5.pdf>
- `irg-n2935` - <https://www.unicode.org/irg/docs/n2935-ScheduleAgenda.html>
