---
type: Topic
title: Script Encoding Pipeline
description: "UTC #187 SEW report を入口にした script proposal の provisional assignment、保留、安定性論点。"
slug: script-encoding-pipeline
bodies: [UTC, WG2]
documents: [utc-l2-26-092, utc-l2-26-093, utc-l2-26-100, utc-l2-26-040r2, utc-l2-26-065, utc-l2-26-079, utc-l2-26-089, utc-l2-26-117, utc-l2-26-118, utc-l2-26-119, utc-l2-26-120, utc-l2-26-129, utc-l2-26-131, utc-l2-26-132, utc-l2-26-137, utc-l2-25-131, wg2-n5354, wg2-n5361r, wg2-n5362, wg2-n5365, wg2-n5368]
topics: [unicode-18-change-sources, unicode-properties-and-algorithms, indic-script-notation-and-rendering, maya-hieroglyph-encoding, shaaldaa-script, iso-10646-edition-and-code-charts]
meetings: [utc-meeting-187, utc-meeting-188, wg2-meeting-72, wg2-meeting-73]
status: active
tags: [script, proposal, encoding, utc, unicode-18, stability]
timestamp: 2026-07-08T00:00:00+09:00
---

# Script Encoding Pipeline

## 概要

Script Encoding Pipeline は、script / character proposals が UTC で provisional assignment、保留、再提案、property / glyph correction に分かれて進む過程を追う topic である。UTC \#187 では [L2/26-100](../documents/utc-l2-26-100.md) Script Encoding WG report が主要文書で、Unicode 18.0 に向けた Latin、Arabic、currency / alchemical symbols、Shaaldaa、Cossic などの処理を束ねる。

この topic は特定 script の解説ではなく、SEW report と WG2 recommendations を decision hub として、どの proposal がどの条件で先へ進むかを読むための入口である。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2025-04-14 | UTC | [L2/25-131](../documents/utc-l2-25-131.md) | Historic alchemical symbols proposal が提出された。 |
| 2026-02-09 | UTC | [L2/26-065](../documents/utc-l2-26-065.md) | LATIN SMALL LETTER ZH proposal が提出された。 |
| 2026-03-09 | UTC | [L2/26-079](../documents/utc-l2-26-079.md) | Romance dialectological atlas additions proposal が提出された。 |
| 2026-04-13 | UTC | [L2/26-040R2](../documents/utc-l2-26-040r2.md) | Oreen Yousuf / Daniel Yacob が Shaaldaa revised proposal を提出した。 |
| 2026-04-13 | UTC | [L2/26-089](../documents/utc-l2-26-089.md), [L2/26-117](../documents/utc-l2-26-117.md), [L2/26-118](../documents/utc-l2-26-118.md), [L2/26-119](../documents/utc-l2-26-119.md) | Belarusian Ruble sign、Catholic Albanian edhe、modifier capital Y、Arabic Waw with Ring proposal が登録された。 |
| 2026-04-17 | UTC | [L2/26-100](../documents/utc-l2-26-100.md) | SEW が UTC \#187 に script proposal recommendations を提出した。 |
| 2026-04-21/23 | UTC | [L2/26-093](../documents/utc-l2-26-093.md) | UTC \#187 minutes が SEW report を Unicode 18.0 beta review の処理対象にした。 |
| 2026-05-14 | UTC | [L2/26-129](../documents/utc-l2-26-129.md), [L2/26-131](../documents/utc-l2-26-131.md), [L2/26-132](../documents/utc-l2-26-132.md) | UTC \#188 候補として Leke、Kannada Samavedic svara markers、KORE SEBELI が登録された。 |
| 2026-06-09 | UTC | [L2/26-137](../documents/utc-l2-26-137.md) | LTR joining scripts に対する Joining_Type property の解釈問題が提出された。 |
| 2026-06-26 | WG2 | [WG2 N5354](../documents/wg2-n5354.md) | WG2 \#73 が Amendment 1 project、first amendment additions、Sirmauri / Leke / Proto-Cuneiform / Mwangwego / Shaaldaa などの script additions、Maya review request を勧告した。 |

## 主な論点

### Provisional assignment に進む proposal

[L2/26-100](../documents/utc-l2-26-100.md) は、[LATIN SMALL LETTER ZH](../documents/utc-l2-26-065.md)、[MODIFIER LETTER CAPITAL Y](../documents/utc-l2-26-118.md)、[Romance dialectology symbols](../documents/utc-l2-26-079.md)、[Catholic Albanian letter edhe](../documents/utc-l2-26-117.md)、[Belarusian Ruble sign](../documents/utc-l2-26-089.md)、[Alchemical Symbol Retort-2](../documents/utc-l2-25-131.md) などを先へ進める。これらは個別 proposal の evidence と、SEW report の recommendation を合わせて確認する。

### Glyph correction と confusables

[L2/26-119](../documents/utc-l2-26-119.md) / [L2/26-120](../documents/utc-l2-26-120.md) の Arabic Letter Waw With Ring では、U+06C4 の glyph correction だけでなく U+06C4 / U+1EE85 の confusables と cross-reference update が扱われた。glyph change は chart issue に見えるが、security data や cross-reference に連鎖する場合がある。

### Encoding model が未決の script

Ndiko Jonam / Luo Lakeside、N'ti、N'Ko Bambara、Brahmi virama minimization などは、joining model、positional forms、productive mechanism、stability の未解決点がある。SEW は、文字集合の必要性だけでなく text model が既存 Unicode behavior と整合するかを見ている。

### Stability と backwards compatibility

Mongolian standardized variants の扱いは、既存 standardized variation sequences を削除せず、後方互換性を保つ revised proposal を求める方向である。Script pipeline では、新規 encoding と同じくらい既存 encoded text の安定性が重視される。

### UTC \#188 候補の新規 script / notation proposals

UTC \#187 後には、[L2/26-129](../documents/utc-l2-26-129.md) Leke、[L2/26-132](../documents/utc-l2-26-132.md) KORE SEBELI、[L2/26-131](../documents/utc-l2-26-131.md) Kannada Samavedic svara markers が登録された。これらは次回 UTC meeting の agenda が未公開なため決定済みではないが、script / notation pipeline の候補として追跡する。

### WG2 \#73 と Amendment 1

[WG2 N5354](../documents/wg2-n5354.md) は、[WG2 N5362](../documents/wg2-n5362.md) / [WG2 N5361R](../documents/wg2-n5361r.md) をもとに ISO/IEC 10646 7th edition Amendment 1 project を始めるよう勧告した。SEI liaison report [WG2 N5365](../documents/wg2-n5365.md) は、WG2 submissions と Unicode SEW submissions の pipeline を俯瞰する入口である。

### Joining_Type for LTR scripts

[L2/26-137](../documents/utc-l2-26-137.md) は、N'ti や Ndiko Jonam のような joining left-to-right scripts を前提に、Joining_Type `L` / `R` の semantics を整理する必要を示す。これは個別 script proposal ではなく、future script encoding の property model を先に決める論点である。

## 関連文書

- [L2/26-100](../documents/utc-l2-26-100.md) - SEW recommendations for UTC \#187。
- [L2/26-092](../documents/utc-l2-26-092.md) - UTC \#187 Agenda。
- [L2/26-093](../documents/utc-l2-26-093.md) - UTC \#187 Meeting Minutes。
- [L2/26-040R2](../documents/utc-l2-26-040r2.md) - Shaaldaa revised proposal。
- [L2/26-065](../documents/utc-l2-26-065.md) - LATIN SMALL LETTER ZH proposal。
- [L2/26-079](../documents/utc-l2-26-079.md) - Romance dialectological atlas additions。
- [L2/26-089](../documents/utc-l2-26-089.md) - Belarusian Ruble sign proposal。
- [L2/26-117](../documents/utc-l2-26-117.md) - Catholic Albanian letter edhe proposal。
- [L2/26-118](../documents/utc-l2-26-118.md) - modifier capital Y proposal。
- [L2/26-119](../documents/utc-l2-26-119.md), [L2/26-120](../documents/utc-l2-26-120.md) - Arabic Waw with Ring glyph correction。
- [L2/26-129](../documents/utc-l2-26-129.md) - Leke script proposal。
- [L2/26-131](../documents/utc-l2-26-131.md) - Samavedic svara markers in Kannada。
- [L2/26-132](../documents/utc-l2-26-132.md) - KORE SEBELI script proposal。
- [L2/26-137](../documents/utc-l2-26-137.md) - Joining_Type for left-to-right scripts。
- [L2/25-131](../documents/utc-l2-25-131.md) - historic alchemical symbols proposal。
- [WG2 N5354](../documents/wg2-n5354.md) - WG2 \#73 recommendations。
- [WG2 N5361R](../documents/wg2-n5361r.md) - provisionally assigned future repertoire。
- [WG2 N5362](../documents/wg2-n5362.md) - ISO/IEC 10646 7th edition Amendment 1 project proposal。
- [WG2 N5365](../documents/wg2-n5365.md) - SEI liaison contribution。
- [WG2 N5368](../documents/wg2-n5368.md) - Dai Xaau supplementary materials。

## 関連トピック

- [Unicode 18.0 Change Sources](unicode-18-change-sources.md)
- [Unicode Release Coordination and Publication](unicode-release-coordination-and-publication.md)
- [Unicode Properties and Algorithms](unicode-properties-and-algorithms.md)
- [Indic Script Notation and Rendering](indic-script-notation-and-rendering.md)
- [Maya Hieroglyph Encoding](maya-hieroglyph-encoding.md)
- [Shaaldaa Script](shaaldaa-script.md)
- [ISO/IEC 10646 Edition and Code Charts](iso-10646-edition-and-code-charts.md)

## 出典

- `utc-l2-26-100` - <https://www.unicode.org/L2/L2026/26100-sew-report-utc187.pdf>
- `utc-l2-26-040r2` - <https://www.unicode.org/L2/L2026/26040r2-shaaldaa-proposal.pdf>
- `utc-l2-26-065` - <https://www.unicode.org/L2/L2026/26065-zh-ligature.pdf>
- `utc-l2-26-079` - <https://www.unicode.org/L2/L2026/26079-dialectological-atlas-additions.pdf>
- `utc-l2-26-089` - <https://www.unicode.org/L2/L2026/26089-belarusian-ruble-sign.pdf>
- `utc-l2-26-117` - <https://www.unicode.org/L2/L2026/26117-catholic-albanian-edhe.pdf>
- `utc-l2-26-118` - <https://www.unicode.org/L2/L2026/26118-modifier-capital-y.pdf>
- `utc-l2-26-119` - <https://www.unicode.org/L2/L2026/26119-arabic-letter-waw-with-ring-within.pdf>
- `utc-l2-26-120` - <https://www.unicode.org/L2/L2026/26120-waw-ring-glyph-change.pdf>
- `utc-l2-26-129` - <https://www.unicode.org/L2/L2026/26129-leke-proposal.pdf>
- `utc-l2-26-131` - <https://www.unicode.org/L2/L2026/26131-samavedic-svara-markers.pdf>
- `utc-l2-26-132` - <https://www.unicode.org/L2/L2026/26132-kore-sebeli-proposal.pdf>
- `utc-l2-26-137` - <https://www.unicode.org/L2/L2026/26137-left-right.pdf>
- `utc-l2-25-131` - <https://www.unicode.org/L2/L2025/25131-alchemical-symbols.pdf>
- `wg2-n5354` - <https://www.unicode.org/wg2/docs/n5354-Mtg73-Paris-Recs-rev5.pdf>
- `wg2-n5361r` - <https://www.unicode.org/wg2/docs/n5361R-ProvisionnallyAssigned.pdf>
- `wg2-n5362` - <https://www.unicode.org/wg2/docs/n5362-proposal_to_start_new_amendment_of_10646.pdf>
- `wg2-n5365` - <https://www.unicode.org/wg2/docs/n5365-SEILiaisonReport-June2026_WG2.pdf>
- `wg2-n5368` - <https://www.unicode.org/wg2/docs/n5368-SupplementaryMaterialsDaiXaauScript.pdf>
