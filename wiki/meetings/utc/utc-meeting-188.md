---
type: Meeting
title: "UTC Meeting #188"
description: "2026-07-28/30 の UTC Meeting #188。Unicode 18.0 release authorization、Unicode 19.0 pipeline、property / CJK decisions。"
slug: utc-meeting-188
body: UTC
bodies: [UTC]
meeting: 188
date: "2026-07-28/30"
location: Redmond, Washington, United States / virtual
documents: [utc-l2-26-150, utc-l2-26-151, utc-l2-26-152, utc-l2-26-153, utc-l2-26-154, utc-l2-26-155, utc-l2-26-156r, utc-l2-26-157, utc-l2-26-158, utc-l2-26-159, utc-l2-26-160r, utc-l2-26-161, utc-l2-26-133r, utc-l2-26-134, utc-l2-26-136, utc-l2-26-141, utc-l2-26-142, utc-l2-26-143, utc-l2-26-144, utc-l2-26-148, pri-548]
topics: [unicode-18-change-sources, cjk-security-confusables, east-asian-quotation-marks, script-encoding-pipeline, leke-script, kore-sebeli-script, chinese-folk-music-notation, indic-script-notation-and-rendering, ideographic-punctuation-proposals, unihan-data-format-and-property-syntax, unicode-properties-and-algorithms, plain-text-composition-and-overstriking, leibnizian-and-historic-mathematical-symbols, maya-hieroglyph-encoding, uax45-u-source-ideographs]
events: [utc-188-unicode-18-release-authorization]
status: completed
tags: [meeting, utc, unicode-18, unicode-19, release, cjk]
timestamp: 2026-07-09T00:00:00+09:00
---

# UTC Meeting \#188

## 概要

UTC Meeting \#188 は 2026-07-28/30 に Microsoft Redmond と online の hybrid meeting として開催された。Agenda `L2/26-150` と [minutes L2/26-151](../../documents/utc-l2-26-151.md) は、Unicode 18.0 finalization、Unicode 19.0 pipeline、working group recommendations を記録する。

会合は48件の consensus と132件の action item を置いた。中心的な節目は、188-C47 による Unicode 18.0 と同期 UTS の release authorization である。

## 主要議題

- [Unicode 18.0 Change Sources](../../topics/unicode-18-change-sources.md) - Chisoi postponement、Small Seal names、property / algorithm / data changes、release authorization。
- [Unicode Properties and Algorithms](../../topics/unicode-properties-and-algorithms.md) - `L2/26-154` の variation selectors、joining、bidi、line break、segmentation、collation、security recommendations。
- [Script Encoding Pipeline](../../topics/script-encoding-pipeline.md) - `L2/26-158` に基づく provisional assignments と保留案件。
- [Unihan Database Maintenance](../../topics/unihan-database-maintenance.md) - `L2/26-157` に基づく property / glyph / source changes。
- [CJKV Components](../../topics/cjkv-components.md) / [kIRG_SGSource](../../topics/kirg-sgsource.md) - Unicode 19.0 target の new blocks / source property。
- [Ideographic Punctuation Proposals](../../topics/ideographic-punctuation-proposals.md) - U+16FE5 / U+16FE6 と standardized variation sequences。

## 決定事項

| Consensus | 決定 |
| --- | --- |
| 188-C2 / C3 | Chisoi を Unicode 18.0 から延期し、Small Seal algorithmic names を変更。 |
| 188-C4〜C18 | Kannada、Tulu-Tigalari、Newa、Brahmi、Arabic、Latin、Leibnizian、musical symbol の provisional assignments / VS。 |
| 188-C19〜C34 | Unicode 18.0 の property、algorithm、security、UAX \#60 title changes。 |
| 188-C35〜C46 | Unihan / CJK changes、U+16FE5 / U+16FE6、Components-A/B、`kIRG_SGSource`、Unikemet changes。 |
| 188-C47 / C48 | Unicode 18.0 と同期 UTS の release、および UTS \#51 Version 18.0 を承認。 |

Codical Maya / Maya Extended-A は `L2/26-158` の reference list には含まれるが、minutes に採択 consensus はない。

## 後続確認

- [L2/26-215 / IRG N2944](../../documents/utc-l2-26-215.md) は Unicode 18.0 が 2026-09-16 に release されたことを確認する。
- [PRI \#555](../../documents/pri-555.md)〜[PRI \#560](../../documents/pri-560.md) は UTC \#189 に向けた後続 review。
- Unicode 19.0 target の provisional assignments は UTC \#189 以降の repertoire decision と alpha review で追う。

## 出典

- `utc-l2-26-150` - <https://www.unicode.org/L2/L2026/26150.htm>
- `utc-l2-26-151` - <https://www.unicode.org/L2/L2026/26151.htm>
- `utc-l2-26-154` - <https://www.unicode.org/L2/L2026/26154-utc188-properties-recs.pdf>
- `utc-l2-26-157` - <https://www.unicode.org/L2/L2026/26157-cjk-unihan-wg-utc188.pdf>
- `utc-l2-26-158` - <https://www.unicode.org/L2/L2026/26158-sew-report-utc188.pdf>
- `utc-l2-26-160r` - <https://www.unicode.org/L2/L2026/26160r-rmg-report-utc188.pdf>
- `utc-l2-26-215` - <https://www.unicode.org/L2/L2026/26215-irgn2944-activity-rept.pdf>
