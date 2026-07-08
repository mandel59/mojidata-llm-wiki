---
type: Topic
title: ISO/IEC 10646 Edition and Code Charts
description: "WG2 / SC2 における ISO/IEC 10646 7th edition、DIS progression、code charts 外部参照、Amendment 1 project の整理。"
slug: iso-10646-edition-and-code-charts
bodies: [WG2, SC2, UTC]
documents: [wg2-n5300r9, wg2-n5304, wg2-n5315, wg2-n5339, wg2-n5350r8, wg2-n5354, wg2-n5361r, wg2-n5362, wg2-n5363r, wg2-n5369, utc-l2-26-102]
topics: [unicode-release-coordination-and-publication, unicode-18-change-sources, script-encoding-pipeline, unihan-database-maintenance]
meetings: [wg2-meeting-72, wg2-meeting-73, utc-meeting-187]
status: active
tags: [iso-10646, code-charts, dis, amendment, wg2, sc2]
timestamp: 2026-07-08T00:00:00+09:00
---

# ISO/IEC 10646 Edition and Code Charts

## 概要

ISO/IEC 10646 Edition and Code Charts は、WG2 / SC2 が ISO/IEC 10646 の edition text、ballot disposition、code charts、future amendment repertoire をどう進めるかを追う topic である。Unicode release との同期は [Unicode 18.0 Change Sources](unicode-18-change-sources.md) で追い、この topic では ISO/IEC 10646 7th edition と Amendment 1 の ballot / publication artifact を中心に扱う。

WG2 \#72 では CD.2 disposition と code charts の外部化検討が採択され、WG2 \#73 では CD.4 disposition、DIS progression、外部 code charts の normative reference、7th edition Amendment 1 project subdivision が採択された。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2025-05-26 | WG2 | [WG2 N5315](../documents/wg2-n5315.md) | ISO/IEC 10646 と Unicode Standard の code charts を共通資源化し、10646 text 本体を軽くする方向を提案した。 |
| 2025-06-23/27 | WG2 | [WG2 N5300R9](../documents/wg2-n5300r9.md) | WG2 \#72 agenda が 7th edition CD.2 disposition、code charts、Small Seal、CJK additions を主要議題に置いた。 |
| 2025-06-25 | WG2 | [WG2 N5339](../documents/wg2-n5339.md) | ISO/IEC 10646 7th edition CD.2 comments の disposition がまとめられた。 |
| 2025-06-27 | WG2 | [WG2 N5304](../documents/wg2-n5304.md) | WG2 \#72 recommendations が CD.2 disposition、code charts 検討、CD.3 progression を採択した。 |
| 2026-06-21 | WG2 | [WG2 N5350R8](../documents/wg2-n5350r8.md) | WG2 \#73 agenda が CD.4 disposition、external code charts、Amendment 1 project subdivision を adoption item にした。 |
| 2026-06-24 | WG2 | [WG2 N5369](../documents/wg2-n5369.md) | ISO/IEC 10646 7th edition CD.4 comments の disposition がまとめられた。 |
| 2026-06-25 | WG2 | [WG2 N5363R](../documents/wg2-n5363r.md) | 10646 code charts を Unicode Consortium が生成する外部 chart resource として normative reference する案が具体化された。 |
| 2026-06-26 | WG2 | [WG2 N5354](../documents/wg2-n5354.md) | WG2 \#73 recommendations が DIS progression、external code charts、Amendment 1 project subdivision、first amendment additions を採択した。 |
| 2026-06-29 | WG2 / UTC | [WG2 N5361R](../documents/wg2-n5361r.md) | Unicode 18.0 後の future repertoire として、Amendment 1 候補を含む provisionally assigned code points が整理された。 |

## 主な論点

### 7th edition CD から DIS への進行

[WG2 N5304](../documents/wg2-n5304.md) の M72.11 は、CD.2 disposition [WG2 N5339](../documents/wg2-n5339.md) と M72.01-M72.10 の変更を含む CD.3 text を SC2 consultation へ進める勧告である。次の [WG2 N5354](../documents/wg2-n5354.md) の M73.04 は、CD.4 disposition [WG2 N5369](../documents/wg2-n5369.md) と M73.01-M73.03 の変更を含む DIS text を balloting に回す勧告で、target は DIS 2026-10-01、IS 2027-06-01 とされた。

### Code charts の外部参照化

[WG2 N5315](../documents/wg2-n5315.md) は、10646 text 本体に大量の code charts を埋め込む代わりに、Unicode と共通の chart resource を使う方向を提案した。WG2 \#72 の M72.10 は ITTF と実現可能性を検討する勧告であり、[WG2 N5363R](../documents/wg2-n5363r.md) はこれを、Unicode Consortium が生成する edition-specific charts を normative reference する具体案へ進めた。WG2 \#73 の M73.03 は、この変更を 7th edition DIS に入れることを勧告した。

### Amendment 1 の starting repertoire

[WG2 N5362](../documents/wg2-n5362.md) は、ISO/IEC 10646 7th edition の新しい amendment project を始める proposal である。[WG2 N5361R](../documents/wg2-n5361r.md) は starting repertoire の data source で、Sirmauri、Leke、Proto-Cuneiform、Mwangwego、Shaaldaa、CJK Unified Ideographs Components-A/B などを含む。ただし WG2 \#73 recommendations は、Mwangwego の扱いを含め、ballot text に入れる前の調整余地を残している。

### Unicode release coordination との境界

[L2/26-102](../documents/utc-l2-26-102.md) は Unicode 18.0 の beta / release schedule と ISO/IEC 10646 7th edition synchronization risk を扱う。一方、この topic の WG2 文書群は、ISO/IEC 10646 側の edition text、DIS ballot、Amendment 1 project を扱う。両者は同期するが、UTC の release authorization と WG2 / SC2 の ballot decision は body と時点を分けて読む必要がある。

## 関連文書

- [WG2 N5300R9](../documents/wg2-n5300r9.md) - WG2 \#72 revised agenda。
- [WG2 N5304](../documents/wg2-n5304.md) - WG2 \#72 recommendations。
- [WG2 N5315](../documents/wg2-n5315.md) - ISO/IEC 10646 code charts consideration。
- [WG2 N5339](../documents/wg2-n5339.md) - CD.2 disposition。
- [WG2 N5350R8](../documents/wg2-n5350r8.md) - WG2 \#73 revised agenda。
- [WG2 N5354](../documents/wg2-n5354.md) - WG2 \#73 recommendations。
- [WG2 N5361R](../documents/wg2-n5361r.md) - provisionally assigned code points after Unicode 18.0。
- [WG2 N5362](../documents/wg2-n5362.md) - Amendment 1 project proposal。
- [WG2 N5363R](../documents/wg2-n5363r.md) - external code charts proposal。
- [WG2 N5369](../documents/wg2-n5369.md) - CD.4 disposition。

## 関連トピック

- [Unicode Release Coordination and Publication](unicode-release-coordination-and-publication.md)
- [Unicode 18.0 Change Sources](unicode-18-change-sources.md)
- [Script Encoding Pipeline](script-encoding-pipeline.md)
- [Unihan Database Maintenance](unihan-database-maintenance.md)

## 出典

- `wg2-n5304` - <https://www.unicode.org/wg2/docs/n5304-Mtg72-Niigata-Recs-rev5-final.pdf>
- `wg2-n5315` - <https://www.unicode.org/wg2/docs/n5315-Considerations-CodeCharts.pdf>
- `wg2-n5339` - <https://www.unicode.org/wg2/docs/n5339-CD7th-2-DOC.pdf>
- `wg2-n5354` - <https://www.unicode.org/wg2/docs/n5354-Mtg73-Paris-Recs-rev5.pdf>
- `wg2-n5361r` - <https://www.unicode.org/wg2/docs/n5361R-ProvisionnallyAssigned.pdf>
- `wg2-n5362` - <https://www.unicode.org/wg2/docs/n5362-proposal_to_start_new_amendment_of_10646.pdf>
- `wg2-n5363r` - <https://www.unicode.org/wg2/docs/n5363R-codechart.pdf>
- `wg2-n5369` - <https://www.unicode.org/wg2/docs/n5369-CD7th-4-DOC.pdf>
