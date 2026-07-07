---
type: Topic
title: Script Encoding Pipeline
description: "UTC #187 SEW report を入口にした script proposal の provisional assignment、保留、安定性論点。"
slug: script-encoding-pipeline
bodies: [UTC]
documents: [utc-l2-26-092, utc-l2-26-093, utc-l2-26-100, utc-l2-26-040r2, utc-l2-26-065, utc-l2-26-079, utc-l2-26-089, utc-l2-26-117, utc-l2-26-118, utc-l2-26-119, utc-l2-26-120, utc-l2-25-131]
topics: [unicode-18-change-sources, unicode-properties-and-algorithms]
meetings: [utc-meeting-187]
status: active
tags: [script, proposal, encoding, utc, unicode-18, stability]
timestamp: 2026-07-08T00:00:00+09:00
---

# Script Encoding Pipeline

## 概要

Script Encoding Pipeline は、script / character proposals が UTC で provisional assignment、保留、再提案、property / glyph correction に分かれて進む過程を追う topic である。UTC \#187 では [L2/26-100](../documents/utc-l2-26-100.md) Script Encoding WG report が主要文書で、Unicode 18.0 に向けた Latin、Arabic、currency / alchemical symbols、Shaaldaa、Cossic などの処理を束ねる。

この topic は特定 script の解説ではなく、SEW report を decision hub として、どの proposal がどの条件で先へ進むかを読むための入口である。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2025-04-14 | UTC | `L2/25-131` | Historic alchemical symbols proposal が提出された。 |
| 2026-02-09 | UTC | `L2/26-065` | LATIN SMALL LETTER ZH proposal が提出された。 |
| 2026-03-09 | UTC | `L2/26-079` | Romance dialectological atlas additions proposal が提出された。 |
| 2026-04-13 | UTC | `L2/26-089`, `L2/26-117`, `L2/26-118`, `L2/26-119` | Belarusian Ruble sign、Catholic Albanian edhe、modifier capital Y、Arabic Waw with Ring proposal が登録された。 |
| 2026-04-17 | UTC | [L2/26-100](../documents/utc-l2-26-100.md) | SEW が UTC \#187 に script proposal recommendations を提出した。 |
| 2026-04-21/23 | UTC | [L2/26-093](../documents/utc-l2-26-093.md) | UTC \#187 minutes が SEW report を Unicode 18.0 beta review の処理対象にした。 |

## 主な論点

### Provisional assignment に進む proposal

[L2/26-100](../documents/utc-l2-26-100.md) は、LATIN SMALL LETTER ZH、MODIFIER LETTER CAPITAL Y、Romance dialectology symbols、Catholic Albanian letter edhe、Belarusian Ruble sign、Alchemical Symbol Retort-2 などを先へ進める。これらは個別 proposal の evidence と、SEW report の recommendation を合わせて確認する。

### Glyph correction と confusables

Arabic Letter Waw With Ring では、U+06C4 の glyph correction だけでなく U+06C4 / U+1EE85 の confusables と cross-reference update が扱われた。glyph change は chart issue に見えるが、security data や cross-reference に連鎖する場合がある。

### Encoding model が未決の script

Ndiko Jonam / Luo Lakeside、N'ti、N'Ko Bambara、Brahmi virama minimization などは、joining model、positional forms、productive mechanism、stability の未解決点がある。SEW は、文字集合の必要性だけでなく text model が既存 Unicode behavior と整合するかを見ている。

### Stability と backwards compatibility

Mongolian standardized variants の扱いは、既存 standardized variation sequences を削除せず、後方互換性を保つ revised proposal を求める方向である。Script pipeline では、新規 encoding と同じくらい既存 encoded text の安定性が重視される。

## 関連文書

- [L2/26-100](../documents/utc-l2-26-100.md) - SEW recommendations for UTC \#187。
- [L2/26-092](../documents/utc-l2-26-092.md) - UTC \#187 Agenda。
- [L2/26-093](../documents/utc-l2-26-093.md) - UTC \#187 Meeting Minutes。
- `L2/26-040R2` - Shaaldaa revised proposal。
- `L2/26-065` - LATIN SMALL LETTER ZH proposal。
- `L2/26-079` - Romance dialectological atlas additions。
- `L2/26-089` - Belarusian Ruble sign proposal。
- `L2/26-117` - Catholic Albanian letter edhe proposal。
- `L2/26-118` - modifier capital Y proposal。
- `L2/26-119`, `L2/26-120` - Arabic Waw with Ring glyph correction。
- `L2/25-131` - historic alchemical symbols proposal。

## 関連トピック

- [Unicode 18.0 Change Sources](unicode-18-change-sources.md)
- [Unicode Release Coordination and Publication](unicode-release-coordination-and-publication.md)
- [Unicode Properties and Algorithms](unicode-properties-and-algorithms.md)

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
- `utc-l2-25-131` - <https://www.unicode.org/L2/L2025/25131-alchemical-symbols.pdf>

