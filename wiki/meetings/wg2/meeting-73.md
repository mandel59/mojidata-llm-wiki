---
type: Meeting
title: "WG2 Meeting #73"
description: "2026-06 WG2 Meeting #73 の Small Seal Script と ISO/IEC 10646 7th edition DIS 進行。"
slug: wg2-meeting-73
kind: meeting
body: WG2
meeting: 73
date: "2026-06-22/26"
location: Paris, France
documents: [wg2-n5350, wg2-n5354, wg2-n5355, wg2-n5369, utc-l2-26-099, utc-l2-26-102]
tags: [meeting, wg2, small-seal, cjk, unihan]
timestamp: 2026-07-06T21:31:45+09:00
---

# WG2 Meeting #73

## 概要

WG2 meeting #73 は 2026-06-22/26 に Paris で開催された。Small Seal は agenda 上で `N5344R2` と `N5348` が扱われ、recommendations では ISO/IEC 10646 7th edition CD.4 disposition `N5369` の significant changes に Small Seal の name、radical、modern CJK、glyph 修正が含まれた。

## 主要議題

- [Small Seal Script](../../topics/small-seal-script.md)
- CD4 disposition for ISO/IEC 10646 7th edition
- Code charts の linked content 化
- First amendment project subdivision
- IRG source / CJK additions
- [Unihan Database Maintenance](../../topics/unihan-database-maintenance.md) - `L2/26-099` は agenda 9.3.1 に載り、Recommendation M73.02 の CJK additions and changes に反映された。
- [Unicode 18.0 Change Sources](../../topics/unicode-18-change-sources.md) - `L2/26-102` が示す 18.0 / ISO/IEC 10646 7th edition synchronization risk の後続として、WG2 #73 recommendations が CD / DIS progression に接続する。

## 決定事項

Recommendation M73.01 は、[WG2 M73.01 Small Seal CD4 disposition](../../events/wg2-m73-01-small-seal-cd4-disposition.md) として整理する。

Recommendation M73.02 は、[`L2/26-099`](../../documents/utc-l2-26-099.md) Section 01、04、07、11、13、19、20、32 などを参照し、representative glyph changes、property value changes、CJK Strokes standardized variation sequences を CD の CJK additions and changes として扱った。

Recommendation M73.04 は、M73.01 から M73.03 の変更と final disposition を含めて 7th edition DIS text を準備し、SC2 secretariat へ balloting 用に回付することを勧告した。target は DIS 2026-10-01、IS 2027-06-01。

## 後続確認

- `WG2 N5369` disposition of comments on 10646 Ed.7 CD.4
- `WG2 N5355` の `zhèngzhuàn`（正篆）/ `chóngwén`（重文）clarification が Small Seal `kSEAL_MCJK` data にどう反映されるか。
- `L2/26-099` の selected CJK / Unihan changes が DIS text と Unicode Version 18.0 data にどう反映されるか。
- DIS 2026-10-01 target
- ISO/IEC 10646 7th edition IS 2027-06-01 target

## 関連出来事

- [WG2 M73.01 Small Seal CD4 disposition](../../events/wg2-m73-01-small-seal-cd4-disposition.md)

## 出典

- `wg2-n5350` - <https://www.unicode.org/wg2/docs/n5350R8-Meeting73Agenda.pdf>
- `wg2-n5354` - <https://www.unicode.org/wg2/docs/n5354-Mtg73-Paris-Recs-rev5.pdf>
- `wg2-n5355` - <https://www.unicode.org/wg2/docs/n5355-SealNormalizedForm.pdf>
- `wg2-n5369` - <https://www.unicode.org/wg2/docs/n5369-CD7th-4-DOC.pdf>
- `utc-l2-26-099` - <https://www.unicode.org/L2/L2026/26099-cjk-unihan-wg-utc187.pdf>
- `utc-l2-26-102` - <https://www.unicode.org/L2/L2026/26102-rmg-report-utc187.pdf>
