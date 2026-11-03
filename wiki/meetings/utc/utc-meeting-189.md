---
type: Meeting
title: "UTC Meeting #189"
description: "2026-10-26〜28、Nancy / onlineのUTC #189資料。改訂WG reports・SEI報告・PRI終了を束ね、未公開minutesの採択確認と分ける。"
slug: utc-meeting-189
body: UTC
bodies: [UTC]
meeting: 189
date: 2026-10-26/28
location: Nancy, France / online
documents: [utc-l2-26-231, utc-l2-26-232, utc-l2-26-233, utc-l2-26-234, utc-l2-26-235, utc-l2-26-236, utc-l2-26-237, utc-l2-26-238, utc-l2-26-239, utc-l2-26-240, utc-l2-26-241, utc-l2-26-260, utc-l2-26-261, utc-l2-26-262, utc-l2-26-263, utc-l2-26-237r, utc-l2-26-241r, utc-l2-26-242, utc-l2-26-226, pri-523, pri-555, pri-556, pri-561]
topics: [unicode-release-coordination-and-publication, script-encoding-pipeline, unicode-properties-and-algorithms, unihan-database-maintenance, emoji-repertoire-proposals, irg-working-process-and-liaison]
events: [sew-189-script-provisional-assignment-recommendations, esr-189-four-characters-directional-zwj-recommendations, utc-189-pri-523-555-556-review-closures]
status: awaiting-minutes
tags: [meeting, utc, unicode-19]
timestamp: "2026-11-03T00:00:00+09:00"
---

# UTC Meeting \#189

## 概要

UTC \#189の会期は2026-10-26〜28、Nancy, Franceとonline。公開agendaと、10月27日に改訂されたWG reports、SEI liaison reportを入口にする。2026-11-03のcatalogでもminutesは未公開であり、以下のWG勧告はUTCの採択結果とは分ける。

[Agenda L2/26-231](../../documents/utc-l2-26-231.md) と各 Working Group report を入口に、Unicode 19.0 の repertoire・property・release plan、ISO/IEC 10646 の進行を追う。

## 主要議題

- [Script Encoding Pipeline](../../topics/script-encoding-pipeline.md): [SEW report](../../documents/utc-l2-26-239.md)、[新script の勧告 event](../../events/sew-189-script-provisional-assignment-recommendations.md)、[community 支援案](../../documents/utc-l2-26-219.md)。
- [Unihan](../../topics/unihan-database-maintenance.md): [CJK & Unihan 勧告](../../documents/utc-l2-26-238.md) が IRG \#67 の勧告と PRI feedback を Unicode 19.0 の変更案へ接続する。
- [Properties and Algorithms](../../topics/unicode-properties-and-algorithms.md): [PAG 勧告](../../documents/utc-l2-26-235.md)、finite automata、UTS \#61、UTR \#25、segmentation / security。
- [Emoji](../../topics/emoji-repertoire-proposals.md): [改訂ESR勧告 event](../../events/esr-189-four-characters-directional-zwj-recommendations.md) と20.0の受付予定。
- [Release coordination](../../topics/unicode-release-coordination-and-publication.md): [RMG report](../../documents/utc-l2-26-241.md)、[Editorial](../../documents/utc-l2-26-236.md)、[Charts](../../documents/utc-l2-26-240.md) の19.0計画。
- [ISO/IEC 10646](../../topics/iso-10646-edition-and-code-charts.md): [CDAM 1](../../documents/utc-l2-26-262.md) と [MA ToR consultation 結果](../../documents/utc-l2-26-263.md)。
- [SEQ report](../../documents/utc-l2-26-260.md): orthographic sequence の validation と normalization の設計。
- [SEI liaison report](../../documents/utc-l2-26-242.md): proposal支援・research・font・community活動。

## 決定事項

WG reports の Consensus / Action Item 文案や SEW-189 番号は、UTC の numbered decisions とは異なる。

<!-- editorial:
2026-11-03のcatalogでもL2/26-232 minutesはunposted。公開URLを再確認し、WG勧告から採択・変更・保留になった箇所を照合する。
Unicode 19.0 scopeと日程、script provisional assignments、CJK / property changes、emoji4文字とdirectional ZWJ sequenceの採否を追う。
PRI #523 / #555 / #556のreview終了は確認済み。UTS #61の正式Status、finite automataの正式data公開、各feedbackのUTC dispositionは個別に確認する。
-->

## 後続確認

- [Recently Closed Action Items](../../documents/utc-l2-26-233.md) は前会合等の作業完了記録として参照する。
- [review終了 event](../../events/utc-189-pri-523-555-556-review-closures.md) は受付終了をまとめる。次の一般feedbackは [PRI \#561](../../documents/pri-561.md)。

## 出典

- `utc-l2-26-231` - <https://www.unicode.org/L2/L2026/26231.htm>（registry date: 2026-10-23）
- `utc-l2-26-235` - <https://www.unicode.org/L2/L2026/26235-utc189-properties-recs.pdf>（registry date: 2026-10-20）
- `utc-l2-26-237r` - <https://www.unicode.org/L2/L2026/26237r-esr-report-utc-189.pdf>（registry date: 2026-10-27）
- `utc-l2-26-238` - <https://www.unicode.org/L2/L2026/26238-cjk-unihan-wg-utc189.pdf>（registry date: 2026-10-19）
- `utc-l2-26-239` - <https://www.unicode.org/L2/L2026/26239-sew-report-utc189.pdf>（registry date: 2026-10-24）
- `utc-l2-26-241r` - <https://www.unicode.org/L2/L2026/26241r-rmg-report-utc189.pdf>（registry date: 2026-10-27）
- `utc-l2-26-263` - <https://www.unicode.org/L2/L2026/26263-isoiec-jtc1-sc2-n5073-summary-consultation.zip>（registry date: 2026-10-16）
- `utc-l2-26-242` - <https://www.unicode.org/L2/L2026/26242-sei-report-october2026.pdf>（registry date: 2026-10-26）
- `pri-523` - <https://www.unicode.org/review/pri523/>
- `pri-555` - <https://www.unicode.org/review/pri555/>
- `pri-556` - <https://www.unicode.org/review/pri556/>
- `pri-561` - <https://www.unicode.org/review/pri561/>
- `utc-l2-26-232` - <https://www.unicode.org/L2/L-curdoc.htm>（2026-11-03時点でminutesはunposted）
