---
type: Event
title: "UTC #189向けPRI #523・#555・#556のreview終了"
description: "closing dateが2026-10-05の3 PRIがClosedとなり、UTS #61公開予定とUTC #190 feedback受付への移行が告知された。"
slug: utc-189-pri-523-555-556-review-closures
date: 2026-10-05
bodies: [UTC]
status: closed
documents: [pri-523, pri-555, pri-556, pri-561, utc-l2-26-226]
topics: [unicode-set-notation, unicode-properties-and-algorithms, unicode-release-coordination-and-publication]
meetings: [utc-meeting-189]
tags: [event, pri, review-closed, uts61, feedback]
timestamp: "2026-11-03T00:00:00+09:00"
---

# UTC \#189向けPRI \#523・\#555・\#556のreview終了

## 概要

closing dateを2026-10-05とするPRI \#523・\#555・\#556がreviewを終了し、Resolved Issues archiveに収録された。eventの日付は共通のclosing dateを表し、Resolutionの公開日やUTC決定日を表すものではない。

## 背景

3件はUTS \#61の集合構文、finite automataのデータ公開案、UTC \#189向け一般feedbackをそれぞれ扱っていた。

## 結果

| PRI | 確認できる結果 |
| --- | --- |
| [PRI \#523](../documents/utc-l2-26-111.md) | feedbackを本文へ反映し、UTSを公開する予定とのResolution。現行Revision 2はDraft。 |
| [PRI \#555](../documents/pri-555.md) | Closed。正式採用やデータ公開のResolutionは記載なし。 |
| [PRI \#556](../documents/pri-556.md) | UTC \#189向け受付を終了し、UTC \#190向け受付への移行を告知。 |

PRI \#523の公開予定、PRI \#555の受付終了、PRI \#556のfeedback受付の切替は、いずれも個別のUTC採択結果とは分ける。

## 影響範囲

[Unicode Set Notation](../topics/unicode-set-notation.md) と [Properties and Algorithms](../topics/unicode-properties-and-algorithms.md) では、review終了と最終仕様・正式データの公開を区別する。次の一般feedback入口は [PRI \#561](../documents/pri-561.md) で、closing dateは2026-12-30。

## 関連ページ

- [UTC Meeting \#189](../meetings/utc/utc-meeting-189.md)
- [UTS \#61 snapshot](../documents/utc-l2-26-226.md)

## 出典

- `pri-523` - <https://www.unicode.org/review/pri523/>
- `pri-555` - <https://www.unicode.org/review/pri555/>
- `pri-556` - <https://www.unicode.org/review/pri556/>
- `Resolved Issues` - <https://www.unicode.org/review/resolved.html>
- `UTS #61 Revision 2` - <https://www.unicode.org/reports/tr61/tr61-2.html>
