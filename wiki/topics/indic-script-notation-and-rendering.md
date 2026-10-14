---
type: Topic
title: Indic Script Notation and Rendering
description: "Indic scripts における Vedic notation、combining marks、rendering guidance。"
slug: indic-script-notation-and-rendering
bodies: [UTC]
documents: ["utc-l2-26-062", "pri-552", "utc-l2-26-113", "utc-l2-26-114", "utc-l2-26-131", "utc-l2-26-138", "utc-l2-26-181r", "utc-l2-26-221", "utc-l2-26-222", "utc-l2-26-248", "utc-l2-26-249", "utc-l2-26-250", "utc-l2-26-251", "utc-l2-26-252", "utc-l2-26-253", "utc-l2-26-254", "utc-l2-26-255", "utc-l2-26-256"]
topics: [script-encoding-pipeline, unicode-properties-and-algorithms]
status: active
tags: [indic, vedic, kannada, rendering, combining-marks]
timestamp: 2026-07-08T00:00:00+09:00
---

# Indic Script Notation and Rendering

## 概要

Indic Script Notation and Rendering は、Indic scripts における Vedic / Sanskrit notation、combining marks、valid sequences、font / shaping behavior を扱う topic である。UTC \#188 候補文書では、[L2/26-113](../documents/utc-l2-26-113.md) と [L2/26-114](../documents/utc-l2-26-114.md) が language-specific vowel marks を提案し、[L2/26-131](../documents/utc-l2-26-131.md) が Kannada 用 Samavedic svara markers の追加を提案し、[L2/26-138](../documents/utc-l2-26-138.md) が consecutive anusvaras の rendering issue を FYI として報告する。

[PRI \#552](../documents/pri-552.md) は Indic conjunct 周辺の UAX \#29 GB9c を Unicode 18.0 向けに更新する public review issue であり、encoding proposal ではなく grapheme cluster boundary / `Indic_Conjunct_Break` data の論点として読む。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2026-01-29 | UTC | [L2/26-062](../documents/utc-l2-26-062.md) | Karan Miśra が Indian languages の text rendering / input / search / processing に関する report を提出した。 |
| 2026-04-13 | UTC | [L2/26-113](../documents/utc-l2-26-113.md) | Biswajit Mandal が Kodava 用 Kannada diacritics 4 文字を提案した。 |
| 2026-04-13 | UTC | [L2/26-114](../documents/utc-l2-26-114.md) | Biswajit Mandal が Sunuwar / Wambule 用 Devanagari vowel length mark を提案した。 |
| 2026-05-14 | UTC | [L2/26-131](../documents/utc-l2-26-131.md) | Kannada script 用 Samavedic svara markers 12 文字が提案された。 |
| 2026-06-09 | UTC | [L2/26-138](../documents/utc-l2-26-138.md) | Consecutive anusvaras が valid Sanskrit forms に現れることと rendering support の問題が報告された。 |
| 2026-07-07 | UTC | [PRI \#552](../documents/pri-552.md) | UTC が UAX \#29 Revision 48 public review を close し、GB9c の `InCB=Linker` / `InCB=Extend` / `InCB=Consonant` rule update を Unicode 18.0 finalization へ接続した。 |
| 2026-10-09 | UTC | [L2/26-181R](../documents/utc-l2-26-181r.md), [L2/26-221](../documents/utc-l2-26-221.md), [L2/26-222](../documents/utc-l2-26-222.md) | Jain Nagari の FINAL ANUSVARA / vowel correction mark と Southern Pa’O の combining / tone signs が登録された。 |
| 2026-10-13 | UTC | L2/26-248–L2/26-256 | Devanagari / Malayalam 追加、Kannada / Sinhala 表現、Indic properties の調査報告を登録。 |

## 主な論点

### 2026年10月の新規入力

[L2/26-248](../documents/utc-l2-26-248.md) / [249](../documents/utc-l2-26-249.md) は写本 punctuation、[251](../documents/utc-l2-26-251.md) は Malayalam Vedic anusvara の追加案。[250](../documents/utc-l2-26-250.md) / [253](../documents/utc-l2-26-253.md) は Kannada の独立 mark usage と shaping、[254](../documents/utc-l2-26-254.md) は Sinhala nukta、[252](../documents/utc-l2-26-252.md) は Turkestan Brāhmī の preliminary model を扱う。[255](../documents/utc-l2-26-255.md) / [256](../documents/utc-l2-26-256.md) の property 調査は、新文字提案と分けて読む。

### script-specific Samavedic marks

[L2/26-131](../documents/utc-l2-26-131.md) は、Devanagari / Grantha に符号化済みの Samavedic notation と同種の marks を Kannada block に追加する提案である。script-specific encoding と cross-script notation consistency の両方を確認する必要がある。

### language-specific vowel marks

[L2/26-113](../documents/utc-l2-26-113.md) は Kodava の unrounded vowels を Kannada script で表す 4 combining marks、[L2/26-114](../documents/utc-l2-26-114.md) は Sunuwar / Wambule の vowel length を Devanagari text で表す mark を提案する。どちらも new script ではなく既存 Indic script block への追加であり、orthography-specific evidence、combining / spacing behavior、Indic property assignment が中心論点になる。

### valid sequence と rendering support

[L2/26-138](../documents/utc-l2-26-138.md) は、two consecutive anusvaras が generic invalid sequence ではなく、Sanskrit grammar に基づく valid forms に現れる場合があるとする。encoding action よりも、Core Specification guidance、font shaping、dotted circle behavior の論点である。

[L2/26-062](../documents/utc-l2-26-062.md) は、atomic vowel letters を分解 sequence と同じ glyph にしないこと、invalid repeated / out-of-order dependent marks を dotted circle で見せること、language-specific orthography validation を input / search / NLP preprocessing に使うことを整理する。Indic topic では、encoding proposal だけでなく shaping and validation guidance として読む。

[PRI \#552](../documents/pri-552.md) の GB9c update は、valid Indic conjunct sequences を editing / selection / regex などの text segmentation layer でどう扱うかに関わる。これは glyph shaping の成否を直接決めるものではないが、rendering guidance と同じく Indic text の user-perceived character boundary に影響する。

### 写本記号と orthography-specific marks

[L2/26-181R](../documents/utc-l2-26-181r.md) は行末 anusvara に gap filler 用例も添えて Lo を提案する。[L2/26-221](../documents/utc-l2-26-221.md) は omitted vowel signs の上付き correction mark と、その結合・表示を扱う。音価だけでなく写本上の機能を区別する必要がある。

[L2/26-222](../documents/utc-l2-26-222.md) は Kham Dom Pa’O の medial consonant、vowel sign、tone mark の保存順序と下付き glyph 配置を記述する。提案 property と Northern Pa’O の代替文字を混同せず、collation の未決点を追う。

## 関連文書

- [L2/26-256](../documents/utc-l2-26-256.md) - Roozbeh Pournader が UTC 164-A63 の Devanagari / Vedic shaping properties 調査を報告する。

- [L2/26-255](../documents/utc-l2-26-255.md) - Roozbeh Pournader が UTC 158-A106 の Unicode 12.0 beta feedback 調査を報告する。

- [L2/26-254](../documents/utc-l2-26-254.md) - Sridatta A / Srinidhi A が Sinhala の nukta 使用を提示する preliminary document。

- [L2/26-253](../documents/utc-l2-26-253.md) - Sridatta A / Srinidhi A が Kannada の repha と他の marks の表示順を報告し、SEWG へ feedback を求める。

- [L2/26-252](../documents/utc-l2-26-252.md) - Francesco Catoni が North / South Turkestan Brāhmī を既存 Brahmi block 内で扱う preliminary proposal を提出する。

- [L2/26-251](../documents/utc-l2-26-251.md) - Sridatta A / Srinidhi A が Malayalam の Vedic Double Anusvara 1文字を提案する。

- [L2/26-250](../documents/utc-l2-26-250.md) - Sridatta A / Srinidhi A が U+0CD5 KANNADA LENGTH MARK の独立使用と property を検討する。

- [L2/26-249](../documents/utc-l2-26-249.md) - Biswajit Mandal が DEVANAGARI DOUBLE SEPARATOR 1文字を提案する。

- [L2/26-248](../documents/utc-l2-26-248.md) - Biswajit Mandal が Jain Nagari などの Sanskrit / Prakrit 写本に使う3 signs を提案する。

- [L2/26-222](../documents/utc-l2-26-222.md) - Proposal to encode Myanmar letters for Kham Dom Pa'O。

- [L2/26-221](../documents/utc-l2-26-221.md) - Proposal to encode the Devanagari Correction Mark for Vowel Signs。

- [L2/26-181R](../documents/utc-l2-26-181r.md) - Proposal to encode the Devanagari Sign Final Anusvara in Unicode (revised)。

- [PRI \#552](../documents/pri-552.md) - UAX \#29 Unicode Text Segmentation Revision 48 public review。
- [L2/26-131](../documents/utc-l2-26-131.md) - Samavedic svara markers in Kannada。
- [L2/26-138](../documents/utc-l2-26-138.md) - consecutive anusvaras in Indic scripts。
- [L2/26-062](../documents/utc-l2-26-062.md) - Text Rendering, Input, Search and Processing in Indian Languages。
- [L2/26-113](../documents/utc-l2-26-113.md) - Four Diacritic Marks of Kannada。
- [L2/26-114](../documents/utc-l2-26-114.md) - Devanagari Vowel Length Mark。

## 関連トピック

- [Script Encoding Pipeline](script-encoding-pipeline.md)
- [Unicode Properties and Algorithms](unicode-properties-and-algorithms.md)

## 出典

- `utc-l2-26-131` - <https://www.unicode.org/L2/L2026/26131-samavedic-svara-markers.pdf>
- `pri-552` - <https://www.unicode.org/review/pri552/>
- `utc-l2-26-138` - <https://www.unicode.org/L2/L2026/26138-consecutive-anusvaras.pdf>
- `utc-l2-26-062` - <https://www.unicode.org/L2/L2026/26062-indian-language-feedback.pdf>
- `utc-l2-26-113` - <https://www.unicode.org/L2/L2026/26113-kannada-diacritics.pdf>
- `utc-l2-26-114` - <https://www.unicode.org/L2/L2026/26114-devanagari-vowel-length-mark.pdf>
- `utc-l2-26-181r` - <https://www.unicode.org/L2/L2026/26181r-final-anusvara.pdf>
- `utc-l2-26-221` - <https://www.unicode.org/L2/L2026/26221-devanagari-correction-mark.pdf>
- `utc-l2-26-222` - <https://www.unicode.org/L2/L2026/26222-kham-dom.pdf>
- `utc-l2-26-248` - <https://www.unicode.org/L2/L2026/26248-three-new-characters-devanagari.pdf>
- `utc-l2-26-249` - <https://www.unicode.org/L2/L2026/26249-devanagari-double-separator.pdf>
- `utc-l2-26-250` - <https://www.unicode.org/L2/L2026/26250-kannada-length-mark.pdf>
- `utc-l2-26-251` - <https://www.unicode.org/L2/L2026/26251-vedic-double-anusvara.pdf>
- `utc-l2-26-252` - <https://www.unicode.org/L2/L2026/26252-turkestan-brahmi.pdf>
- `utc-l2-26-253` - <https://www.unicode.org/L2/L2026/26253-repha-in-kannada.pdf>
- `utc-l2-26-254` - <https://www.unicode.org/L2/L2026/26254-nukta-in-sinhala.pdf>
- `utc-l2-26-255` - <https://www.unicode.org/L2/L2026/26255-indic-158-a106.pdf>
- `utc-l2-26-256` - <https://www.unicode.org/L2/L2026/26256-indic-164-a63.pdf>
