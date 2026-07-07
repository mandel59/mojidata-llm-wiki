---
type: Source Document
title: "Proposed Horizontal Extension to ISO/IEC 10646"
description: "UAX #45 にあるが U-source identifiers を欠く encoded ideographs へ U-source references を付ける 2019 horizontal extension proposal。"
resource: https://www.unicode.org/irg/docs/n2369r-UnicodeHorizontalExtension.pdf
entry_id: irg-n2369r
doc_number: IRG N2369R
document_type: proposal
aliases: [WG2 N5085, Proposed Horizontal U Source Extension]
registry: irg
date: "2019-05-09"
source: UTC
topics: [uax45-u-source-ideographs, cjk-horizontal-extensions, irg-source-data-and-representative-glyphs]
people: [john-h-jenkins, utc, irg, wg2]
documents: [utc-l2-26-147]
tags: [document, u-source, horizontal-extension, kirg-usource]
timestamp: 2026-07-08T00:00:00+09:00
---

# IRG N2369R

## 要約

`IRG N2369R` / `WG2 N5085` は、ISO/IEC 10646 で既に encoded されている約 150 unified ideographs に対し、U-source identifiers を horizontal extension として追加する proposal である。対象 characters は UAX \#45 に存在するが U-source identifiers を欠いており、UTC が tracking しやすくし、users の混乱を減らすために source identifiers を付けると説明する。

## 提案内容

文書は、URO、Extensions A-F などの blocks にまたがる encoded ideographs について、block、IRG U-source、UAX \#45 glyph、UCS glyph、code point の表を提示する。これは新規符号化 proposal ではなく、既存 code points に source data を追加する horizontal extension である。

## 後続決定

現行 catalog と既存 cache では、`IRG N2369R` そのものの採否を示す meeting decision はまだ確認していない。一方で、同じ型の後続提案として 2026 年の [L2/26-147](utc-l2-26-147.md) / `IRG N2961` があり、既符号化文字へ `kIRG_USource` values と U-source representative glyphs を追加する horizontal extension は継続している。

したがって、このページでは `IRG N2369R` を「採択済み event 不明」ではなく、2019 年時点の horizontal extension proposal として扱い、確定した後続処理は `L2/26-147` など個別の後続文書・meeting で追う。

## 論点

`IRG N2369R` は、UAX \#45 と `kIRG_USource` の関係を明確にする文書である。UAX \#45 に record がある candidate が、別 source や earlier process で encoded された場合、後から `kIRG_USource` / representative glyph を追加して UTC 側の tracking と ISO/IEC 10646 source requirements を整合させることがある。

## 出典

- `irg-n2369r` - <https://www.unicode.org/irg/docs/n2369r-UnicodeHorizontalExtension.pdf>
- `wg2-n5085` - <https://unicode.org/wg2/docs/n5085-IRGN2369RProposedHorizontalExtension.pdf>
- `utc-l2-26-147` - <https://www.unicode.org/L2/L2026/26147-irgn2961-unicodehorizontalextension.pdf>
