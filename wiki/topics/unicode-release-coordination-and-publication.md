---
type: Topic
title: Unicode Release Coordination and Publication
description: "UTC #187 で扱われた Unicode 18.0 の release、charts、editorial、liaison coordination。"
slug: unicode-release-coordination-and-publication
bodies: [UTC]
documents: [utc-l2-25-230r, utc-l2-26-008r, utc-l2-26-092, utc-l2-26-093, utc-l2-26-095, utc-l2-26-097, utc-l2-26-101, utc-l2-26-102, pri-547, pri-548, utc-l2-26-104, utc-l2-26-126]
topics: [unicode-18-change-sources, iso-10646-edition-and-code-charts, unicode-properties-and-algorithms, emoji-repertoire-proposals]
meetings: [utc-meeting-187, utc-meeting-188]
status: active
tags: [unicode-18, release, charts, editorial, publication, liaison]
timestamp: 2026-07-08T00:00:00+09:00
---

# Unicode Release Coordination and Publication

## 概要

Unicode release coordination は、文字や property の採択だけでなく、core specification、charts、NamesList、UCD / Unihan data、beta review page、implementation liaison を同じ release schedule に乗せる作業である。UTC \#187 では Unicode 18.0 beta review authorization を中心に、RMG、Editorial WG、Charts WG、ICU4X / TC39 liaison reports がこの論点を構成した。

この topic は [Unicode 18.0 Change Sources](unicode-18-change-sources.md) のうち、publication artifact と release process に関する文書を分けて読むための入口である。個別の CJK / script / property decisions は関連 topic に分ける。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2026-04-03 | UTC | [L2/26-095](../documents/utc-l2-26-095.md) | Michelle Perham が 2025-12-30 から 2026-03-31 まで開いていた Public Review Issues 一覧を登録し、Unicode 18.0 alpha / emoji / UAX / UTS / UTR feedback の入口を束ねた。 |
| 2026-04-09 | UTC | [L2/26-097](../documents/utc-l2-26-097.md) | Editorial WG が Unicode 18.0 core spec text、NamesList、PDF publication policy を報告した。 |
| 2026-04-15 | UTC | [L2/26-102](../documents/utc-l2-26-102.md) | RMG が Unicode 18.0 timeline と beta review authorization を UTC \#187 に勧告した。 |
| 2026-04-19 | UTC | [L2/26-101](../documents/utc-l2-26-101.md) | Charts WG が versioned block charts、PDF permissions、NamesList ownership transfer を報告した。 |
| 2026-04-21/23 | UTC | [L2/26-092](../documents/utc-l2-26-092.md), [L2/26-093](../documents/utc-l2-26-093.md) | UTC \#187 が WG reports を処理し、Unicode 18.0 beta review の開始を authorize した。 |
| 2026-04-22 | UTC | [L2/26-126](../documents/utc-l2-26-126.md) | ICU4X / TC39 liaison が Unicode data consumption と Intl / Temporal proposal 状況を報告した。 |
| 2026-07-07 | UTC | [PRI \#547](../documents/pri-547.md) | UAX \#44 Revision 37 public review が close し、UCD / non-UCD release data directory structure の整理が beta feedback snapshot に入った。 |
| 2026-07-07 | UTC | [PRI \#548](../documents/pri-548.md) | Unicode 18.0.0 Beta public review が close し、substantive feedback は July UTC meeting での検討対象になった。 |
| 2026-07-30 | UTC | [L2/26-102](../documents/utc-l2-26-102.md) | UTC \#188 で Unicode 18.0 content finalize が予定されている。 |

## 主な論点

### Beta review gate

[L2/26-102](../documents/utc-l2-26-102.md) は、UTC \#187 で Unicode 18.0 beta review を authorize し、2026-05-26 に beta review を開始し、2026-07-07 に public review を閉じ、UTC \#188 で content finalize する schedule を示した。したがって UTC \#187 の WG reports は、Unicode 18.0 beta に入れる内容を確定する gate として読む。

[PRI \#548](../documents/pri-548.md) は、この schedule の public review close point を表す。`L2/26-102` が予定と deliverables を示すのに対し、`PRI #548` は beta page、feedback route、closed status、July UTC meeting への substantive feedback deadline を示す入口である。

[L2/26-095](../documents/utc-l2-26-095.md) は、その前段階として 2025-12-30 から 2026-03-31 まで開いていた PRIs と feedback pages の索引を示す。UTR \#59、UAX \#60、UTS \#61、UAX \#57、UAX \#53、UAX \#31、UAX \#38、UTS \#37 などの feedback は、UTC \#187 の PAG / WG reports と合わせて読む必要がある。

### Core spec と editorial text

[L2/26-097](../documents/utc-l2-26-097.md) は Unicode 18.0 core spec の chapter updates と terminology cleanup をまとめる。新 script / block の説明、NamesList fixes、West Asian terminology、chapter heading restructuring は、UCD data ではなく specification text 側の release artifact である。

### Charts と NamesList

[L2/26-101](../documents/utc-l2-26-101.md) は、Unicode 18.0 beta から charts の owner password protection を外し、per-block charts を versioned archive として公開する方向を示した。NamesList ownership を Charts WG に移す点も、今後の annotation / cross-reference 修正を追う上で重要である。

### UCD directory と release data

[PRI \#547](../documents/pri-547.md) は UAX \#44 Revision 37 の public review であり、Section 4.1 Directory Structure の書き直しによって、UCD と release に付随する non-UCD data files の関係を説明する。Unicode 18.0 の beta package では、core data、Unihan.zip、UAX \#45 data、UAX \#60 source files、auxiliary algorithm data などを同時に確認する必要がある。

### Implementation liaison

[L2/26-126](../documents/utc-l2-26-126.md) は、ICU4X が UCD / Unihan data、segmentation、properties をどう取り込むか、TC39 Intl / Temporal proposals がどこまで進んだかを報告する。release artifact の変更が実装 ecosystem にどう接続するかを見るための資料である。

### Emoji data と release artifact

[L2/25-230R](../documents/utc-l2-25-230r.md) / [L2/26-008R](../documents/utc-l2-26-008r.md) は Unicode 18.0 emoji candidates を整理し、[L2/26-104](../documents/utc-l2-26-104.md) は UTS \#51 / emoji data layer を更新する。Emoji additions は code charts だけでなく RGI sets、modifier sequences、CLDR data にも反映される。

## 関連文書

- [L2/26-092](../documents/utc-l2-26-092.md) - UTC \#187 Agenda。
- [L2/26-093](../documents/utc-l2-26-093.md) - UTC \#187 Meeting Minutes。
- [L2/26-095](../documents/utc-l2-26-095.md) - Public Review Issues 一覧。
- [L2/26-097](../documents/utc-l2-26-097.md) - Editorial WG report。
- [L2/26-101](../documents/utc-l2-26-101.md) - Charts WG report。
- [L2/26-102](../documents/utc-l2-26-102.md) - RMG report。
- [PRI \#547](../documents/pri-547.md) - UAX \#44 Unicode Character Database Revision 37 public review。
- [PRI \#548](../documents/pri-548.md) - Unicode 18.0.0 Beta public review。
- [L2/26-126](../documents/utc-l2-26-126.md) - ICU4X / TC39 liaison update。
- [L2/25-230R](../documents/utc-l2-25-230r.md) - UTC \#185 ESR report and Unicode 18.0 emoji short list。
- [L2/26-008R](../documents/utc-l2-26-008r.md) - UTC \#186 ESR report and CRACKING FACE name change。
- [L2/26-104](../documents/utc-l2-26-104.md) - UTS \#51 Revision 30 proposed update。

## 関連トピック

- [Unicode 18.0 Change Sources](unicode-18-change-sources.md)
- [ISO/IEC 10646 Edition and Code Charts](iso-10646-edition-and-code-charts.md)
- [Unicode Properties and Algorithms](unicode-properties-and-algorithms.md)
- [Script Encoding Pipeline](script-encoding-pipeline.md)
- [Emoji Interoperability and Intake](emoji-interoperability-and-intake.md)
- [Emoji Repertoire Proposals](emoji-repertoire-proposals.md)

## 出典

- `utc-l2-26-092` - <https://www.unicode.org/L2/L2026/26092.htm>
- `utc-l2-26-093` - <https://www.unicode.org/L2/L2026/26093.htm>
- `utc-l2-26-095` - <https://www.unicode.org/L2/L2026/26095-public-review-issues.html>
- `utc-l2-26-097` - <https://www.unicode.org/L2/L2026/26097-edc-report-utc187.html>
- `utc-l2-26-101` - <https://www.unicode.org/L2/L2026/26101-charts-wg-rept-utc187.pdf>
- `utc-l2-26-102` - <https://www.unicode.org/L2/L2026/26102-rmg-report-utc187.pdf>
- `pri-547` - <https://www.unicode.org/review/pri547/>
- `pri-548` - <https://www.unicode.org/review/pri548/>
- `utc-l2-26-126` - <https://www.unicode.org/L2/L2026/26126-icu4x-and-tc39-liason-report.pdf>
- `utc-l2-25-230r` - <https://www.unicode.org/L2/L2025/25230r-esr-report-utc185.pdf>
- `utc-l2-26-008r` - <https://www.unicode.org/L2/L2026/26008r-esr-report-utc186.pdf>
- `utc-l2-26-104` - <https://www.unicode.org/L2/L2026/26104-uts51-30-update-pri543.pdf>
