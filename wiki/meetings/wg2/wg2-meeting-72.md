---
type: Meeting
title: "WG2 Meeting #72"
description: "2025-06 WG2 Meeting #72 の ISO/IEC 10646 7th edition CD.2 progression、code charts、Small Seal、J-source / CJK recommendations。"
slug: wg2-meeting-72
body: WG2
bodies: [WG2]
meeting: 72
date: "2025-06-23/27"
location: Niigata, Japan
documents: [wg2-n5300r9, wg2-n5301, wg2-n5304, wg2-n5315, wg2-n5339, irg-n2721, wg2-n5284, wg2-n5221, wg2-n5296, wg2-n5306, wg2-n5311, wg2-n5317r3, wg2-n5318r, wg2-n5341]
topics: [iso-10646-edition-and-code-charts, small-seal-script, jmj-horizontal-extension-review-path, j-source, cjk-horizontal-extensions, unihan-database-maintenance, script-encoding-pipeline]
tags: [meeting, wg2, iso-10646, code-charts, small-seal, j-source, cjk]
timestamp: 2026-07-08T00:00:00+09:00
---

# WG2 Meeting \#72

## 概要

WG2 Meeting \#72 は 2025-06-23/27 に Niigata, Japan で開催された。中心は ISO/IEC 10646 7th edition CD.2 comments の disposition、次の CD text へ入れる CJK / script 変更、code charts の扱い、Small Seal future edition candidate、J-source glyph correction である。

この meeting の一次入口は revised agenda [WG2 N5300R9](../../documents/wg2-n5300r9.md)、minutes / action items [WG2 N5301](../../documents/wg2-n5301.md)、recommendations [WG2 N5304](../../documents/wg2-n5304.md) である。CD.2 disposition は [WG2 N5339](../../documents/wg2-n5339.md)、code charts 論点は [WG2 N5315](../../documents/wg2-n5315.md) を読む。

## 主要議題

- [ISO/IEC 10646 Edition and Code Charts](../../topics/iso-10646-edition-and-code-charts.md) - CD.2 disposition、CD.3 progression、code charts の external / electronic attachment 化。
- [Small Seal Script](../../topics/small-seal-script.md) - 11,339 characters を future edition candidate として扱う M72.13。
- [J-source and JMJ Source Issues](../../topics/j-source.md) - `WG2 N5296` に基づく J-source glyph changes の revert。
- [JMJ Horizontal Extension Review Path](../../topics/jmj-horizontal-extension-review-path.md) - Japan IRG active participation request と large JMJ horizontal extension の review path。
- [CJK Horizontal Extensions](../../topics/cjk-horizontal-extensions.md) / [Unihan Database Maintenance](../../topics/unihan-database-maintenance.md) - T-source / G-source / Taiwan source additions and changes。
- [Script Encoding Pipeline](../../topics/script-encoding-pipeline.md) - Khitan Small Script additions、Jurchen naming、Tai Xaau、future additions。

## 決定事項

| Recommendation | 主語 | 内容 | 関連 |
| --- | --- | --- | --- |
| M72.01 | WG2 | [WG2 N5339](../../documents/wg2-n5339.md) の CD.2 disposition を SC2 が受け入れるよう勧告した。Sidetic removal、name / alias changes、CJK additions などを含む。 | [ISO/IEC 10646 Edition and Code Charts](../../topics/iso-10646-edition-and-code-charts.md) |
| M72.02 | WG2 | T-source disunifications、G-source urgent ideographs、Taiwan additions など、CJK additions and changes を次の CD に入れるよう勧告した。 | [CJK Horizontal Extensions](../../topics/cjk-horizontal-extensions.md) |
| M72.04 | WG2 | Clauses 24-27 の source descriptions を UAX \#38 / UAX \#60 への normative references に置き換える方向を勧告した。 | [Unihan Database Maintenance](../../topics/unihan-database-maintenance.md) |
| M72.07 | WG2 | `WG2 N5296` に記載された J-source glyph changes を Project Editor が revert するよう勧告した。 | [WG2 M72.07 J-source glyph revert recommendation](../../events/wg2-m72-07-j-source-glyph-revert.md) |
| M72.10 | WG2 | Project Editor が ITTF と、UCS code charts を core text から electronic attachment / linked content へ移す可能性を検討するよう勧告した。 | [WG2 N5315](../../documents/wg2-n5315.md) |
| M72.11 | WG2 | M72.01-M72.10 と final disposition [WG2 N5339](../../documents/wg2-n5339.md) を含む CD.3 text を SC2 consultation へ送るよう勧告した。 | [ISO/IEC 10646 Edition and Code Charts](../../topics/iso-10646-edition-and-code-charts.md) |
| M72.13 | WG2 | Small Seal 11,339 characters を `38000..3AC4A`、block range `38000..3AC4F` の future edition candidate として Project Editor に検討させるよう勧告した。 | [WG2 M72.13 Small Seal future edition candidate](../../events/wg2-m72-13-small-seal-future-candidate.md) |
| M72.15 | WG2 | Dai Xaau proposal の progress を note し、authors に継続作業を促した。 | [Script Encoding Pipeline](../../topics/script-encoding-pipeline.md) |

## 後続確認

- [WG2 N5363R](../../documents/wg2-n5363r.md) - M72.10 の follow-up として、external code charts の normative reference 案を提示。
- [WG2 Meeting \#73](wg2-meeting-73.md) - CD.4 disposition、DIS progression、Amendment 1 project subdivision。
- [WG2 N5344](../../documents/wg2-n5344.md) / [WG2 N5369](../../documents/wg2-n5369.md) - Small Seal は WG2 \#72 時点の future candidate から、WG2 \#73 の CD.4 disposition / DIS progression に移る。
- [IRG N2721](../../documents/irg-n2721.md) / `WG2 N5284` - Japan active IRG participation request。
- [WG2 M72.07 J-source glyph revert recommendation](../../events/wg2-m72-07-j-source-glyph-revert.md)
- [WG2 M72.13 Small Seal future edition candidate](../../events/wg2-m72-13-small-seal-future-candidate.md)

## 出典

- `wg2-n5300r9` - <https://www.unicode.org/wg2/docs/n5300R9-Meeting72Agenda.pdf>
- `wg2-n5301` - <https://www.unicode.org/wg2/docs/n5301-M72minutes-JP-2025-rev5.pdf>
- `wg2-n5304` - <https://www.unicode.org/wg2/docs/n5304-Mtg72-Niigata-Recs-rev5-final.pdf>
- `wg2-n5315` - <https://www.unicode.org/wg2/docs/n5315-Considerations-CodeCharts.pdf>
- `wg2-n5339` - <https://www.unicode.org/wg2/docs/n5339-CD7th-2-DOC.pdf>
