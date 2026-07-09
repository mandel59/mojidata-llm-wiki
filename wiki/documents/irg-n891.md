---
type: Source Document
title: "Extension C1 Submission from China"
description: "China が IRG に提出した CJK Extension C1 候補一覧。G-source evidence history の古い参照点になる。"
resource: https://www.unicode.org/irg/docs/n0891-China-ExtensionC1-sub.pdf
entry_id: irg-n891
doc_number: IRG N891
document_type: data
registry: irg
date: "2002-04-18"
source: China
documents: [irg-n1519, irg-n2955]
topics: [g-source-glyph-and-reference-issues, irg-source-data-and-representative-glyphs]
people: [china, irg]
tags: [document, irg, g-source, extension-c, evidence, data]
timestamp: 2026-07-09T00:00:00+09:00
---

# IRG N891

## 要約

`IRG N891` は、China が 2002 年に提出した CJK Extension C1 candidate list である。Kangxi radical / stroke、first sequence、source identifier、128x128 font glyph を並べる一覧型の submission で、個別文字の後続判断では original submission record として参照される。

PDF text extraction では glyph 部分の確認に限界があるが、`zjw00932` は radical 宀、13 strokes の entry として現れ、後続の U+2CCA3 / `GZFY-00932` 論点で source history の一部として扱われる。

## データ内容

| 項目 | 内容 |
| --- | --- |
| repertoire | China 由来の Extension C1 candidate list。 |
| listed fields | Kangxi radical / stroke、Firstseq、Source、128x128 Font。 |
| source identifiers | `zjw`、`CYY`、`BK` などの source identifiers が並ぶ。 |
| later relevance | [IRG N2955](irg-n2955.md) が、U+2CCA3 / `GZFY-00932` issue の source history を説明する際に `IRG N891` を参照している。 |

## 後続決定

この文書自体は submission data であり、accept / reject の会議決定は記録していない。U+2CCA3 / `GZFY-00932` の後続論点は [IRG N2954](irg-n2954.md) と [IRG N2955](irg-n2955.md) に集約されている。

## 論点

### original submission と後続 evidence の分離

`IRG N891` は、後年の chart glyph や Unihan source reference の正誤を直接判断する文書ではない。役割は、China が Extension C1 phase でどの source identifier と glyph data を提出していたかをたどるための original submission record である。

## 関連文書

- [IRG N1519](irg-n1519.md) - China CJK_D candidate evidence package。
- [IRG N2955](irg-n2955.md) - U+2CCA3 / `GZFY-00932` issue への feedback。
- [G-source Glyph and Source Reference Issues](../topics/g-source-glyph-and-reference-issues.md)

## 出典

- `irg-n891` - <https://www.unicode.org/irg/docs/n0891-China-ExtensionC1-sub.pdf>
