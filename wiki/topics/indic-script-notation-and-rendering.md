---
type: Topic
title: Indic Script Notation and Rendering
description: "Indic scripts における Vedic notation、combining marks、rendering guidance。"
slug: indic-script-notation-and-rendering
bodies: [UTC]
documents: [utc-l2-26-131, utc-l2-26-138, utc-l2-26-062]
topics: [script-encoding-pipeline, unicode-properties-and-algorithms]
status: active
tags: [indic, vedic, kannada, rendering, combining-marks]
timestamp: 2026-07-08T00:00:00+09:00
---

# Indic Script Notation and Rendering

## 概要

Indic Script Notation and Rendering は、Indic scripts における Vedic / Sanskrit notation、combining marks、valid sequences、font / shaping behavior を扱う topic である。UTC \#188 候補文書では [L2/26-131](../documents/utc-l2-26-131.md) が Kannada 用 Samavedic svara markers の追加を提案し、[L2/26-138](../documents/utc-l2-26-138.md) が consecutive anusvaras の rendering issue を FYI として報告する。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2026-01-29 | UTC | `L2/26-062` | Indian languages の text rendering / input / search / processing に関する background discussion が登録された。 |
| 2026-05-14 | UTC | [L2/26-131](../documents/utc-l2-26-131.md) | Kannada script 用 Samavedic svara markers 12 文字が提案された。 |
| 2026-06-09 | UTC | [L2/26-138](../documents/utc-l2-26-138.md) | Consecutive anusvaras が valid Sanskrit forms に現れることと rendering support の問題が報告された。 |

## 主な論点

### script-specific Samavedic marks

[L2/26-131](../documents/utc-l2-26-131.md) は、Devanagari / Grantha に符号化済みの Samavedic notation と同種の marks を Kannada block に追加する提案である。script-specific encoding と cross-script notation consistency の両方を確認する必要がある。

### valid sequence と rendering support

[L2/26-138](../documents/utc-l2-26-138.md) は、two consecutive anusvaras が generic invalid sequence ではなく、Sanskrit grammar に基づく valid forms に現れる場合があるとする。encoding action よりも、Core Specification guidance、font shaping、dotted circle behavior の論点である。

## 関連文書

- [L2/26-131](../documents/utc-l2-26-131.md) - Samavedic svara markers in Kannada。
- [L2/26-138](../documents/utc-l2-26-138.md) - consecutive anusvaras in Indic scripts。
- `L2/26-062` - Text Rendering, Input, Search and Processing in Indian Languages。

## 関連トピック

- [Script Encoding Pipeline](script-encoding-pipeline.md)
- [Unicode Properties and Algorithms](unicode-properties-and-algorithms.md)

## 出典

- `utc-l2-26-131` - <https://www.unicode.org/L2/L2026/26131-samavedic-svara-markers.pdf>
- `utc-l2-26-138` - <https://www.unicode.org/L2/L2026/26138-consecutive-anusvaras.pdf>
- `utc-l2-26-062` - <https://www.unicode.org/L2/L2026/26062-indian-language-feedback.pdf>
