---
type: Event
title: "UAX #60 Unicode 18.0 first published version"
description: "PRI #520 の review と UTC の調整を経た UAX #60 が、Unicode 18.0.0 の初の承認済み公開版 Revision 3 として確定した節目。"
slug: uax60-unicode-18-first-published-version
date: "2026-09-02"
bodies: [Unicode Consortium]
documents: [pri-520, utc-l2-26-108, utc-l2-26-099, utc-l2-26-102, utc-l2-26-151, utc-l2-26-215]
topics: [uax60-large-east-asian-scripts, small-seal-script, unicode-18-change-sources, unicode-properties-and-algorithms]
people: [michel-suignard]
meetings: [utc-meeting-187, utc-meeting-188]
status: published
tags: [event, uax60, unicode-18, ucd, data-files, public-review]
timestamp: 2026-10-11T00:00:00+09:00
---

# UAX \#60 Unicode 18.0 first published version

## 概要

UAX \#60 は、Unicode 18.0.0 の **Data for East Asian Scripts Revision 3** として、初の承認済み公開版になった。editor は Michel Suignard。Jurchen、Nüshu、Small Seal、Tangut のデータを扱い、Han は UAX \#38 で扱う。

この event の日付 2026-09-02 は確定版の header に記された仕様日付であり、実際の配布開始日を推定したものではない。Unicode 18.0 全体の release は [L2/26-215 / IRG N2944](../documents/utc-l2-26-215.md) が 2026-09-16 と報告する。

## 背景

[PRI \#520 / L2/26-108](../documents/utc-l2-26-108.md) は draft と public review の入口で、registry 上の closing date は 2026-07-07。[L2/26-099](../documents/utc-l2-26-099.md) は Seal property syntax / description の修正を、[L2/26-102](../documents/utc-l2-26-102.md) は draft title の調整を記録する。

Resolved Issues は PRI \#520 を解決済みとして掲載する。一方、個別 PRI page は `Status: Open` を残しており、この表示から確定版の公開状態を判断しない。最終結果は Revision 3 の Status / Modifications と versioned data で確認する。

## 結果

確定版の表題は `Data for East Asian Scripts`。draft 段階の `Data for Non Han Ideographic Scripts` / `Data for Large East Asian Scripts` と区別する。正式データは Unicode 18.0.0 の `JurchenSources.txt`、`NushuSources.txt`、`SealSources.txt`、`TangutSources.txt` にある。

Seal の `kSEAL_Rad` は space 区切りで複数の radical 値を許し、`kSEAL_THXSrc` は `TH-(\d{5}|X\d{3}|Y\d{3})` の syntax を持つ。取得した正式な `SealSources.txt` でも両 property の値が確定版の syntax に一致し、複数 radical 値の使用が確認できる。

## 影響範囲

[UAX \#60 topic](../topics/uax60-large-east-asian-scripts.md) からは draft の審査結果と実装用の確定版を結び付ける節目。[Small Seal Script](../topics/small-seal-script.md) では文字 repertoire の符号化と、付随データの仕様確定を分けて追う。draft への提案・action item は過去の記録として残し、実装は versioned specification / data を参照する。

## 関連ページ

- [PRI \#520 / L2/26-108](../documents/utc-l2-26-108.md)
- [UAX \#60 Data for East Asian Scripts](../topics/uax60-large-east-asian-scripts.md)
- [Small Seal Script](../topics/small-seal-script.md)
- [Unicode 18.0 Change Sources](../topics/unicode-18-change-sources.md)
- [Michel Suignard](../people/michel-suignard.md)
- [UTC Meeting \#188](../meetings/utc/utc-meeting-188.md)

## 出典

- UAX \#60 Revision 3, 2026-09-02 - <https://www.unicode.org/reports/tr60/tr60-3.html>。Status と Modifications が初の承認済み公開版であることを示す。
- `pri-520` - <https://www.unicode.org/review/pri520/>。closing date: 2026-07-07。
- PRI Resolved Issues - <https://www.unicode.org/review/resolved.html> (2026-10-11 確認)。
- Unicode 18.0.0 data - <https://www.unicode.org/Public/18.0.0/ucd/JurchenSources.txt>、<https://www.unicode.org/Public/18.0.0/ucd/NushuSources.txt>、<https://www.unicode.org/Public/18.0.0/ucd/SealSources.txt>、<https://www.unicode.org/Public/18.0.0/ucd/TangutSources.txt>。
- `utc-l2-26-108` - <https://www.unicode.org/L2/L2026/26108-uax60-2-draft-pri520.pdf>
- `utc-l2-26-099` - <https://www.unicode.org/L2/L2026/26099-cjk-unihan-wg-utc187.pdf>
- `utc-l2-26-102` - <https://www.unicode.org/L2/L2026/26102-rmg-report-utc187.pdf>
- `utc-l2-26-151` - <https://www.unicode.org/L2/L2026/26151.htm>
- `utc-l2-26-215` - <https://www.unicode.org/L2/L2026/26215-irgn2944-activity-rept.pdf>
