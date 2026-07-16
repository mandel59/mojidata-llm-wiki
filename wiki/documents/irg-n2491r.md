---
type: Source Document
title: "IRG Disunified Ideographs from IRG #45 to IRG #56"
description: "IRG Meetings 45-56 の source remapping / disunification cases を旧 code point、decision、status、根拠文書で集約した初期一覧。"
resource: https://www.unicode.org/irg/docs/n2491r-Disunified.pdf
entry_id: irg-n2491r
doc_number: IRG N2491R
document_type: report
registry: irg
date: "2021-10-08"
source: IRG Chief Editor
documents: [irg-n2106, irg-n2218, irg-n2265, irg-n2329, irg-n2365, irg-n2463, irg-n2892]
topics: [irg-disunified-ideographs, irg-source-data-and-representative-glyphs]
people: [china, irg]
meetings: [irg-meeting-56]
tags: [document, irg, report, disunification, source-remapping]
timestamp: 2026-07-16T00:00:00+09:00
---

# IRG N2491R

## 要約

`IRG N2491R` は、IRG Meeting \#45 以降の editorial reports から Meeting \#56 までの source remapping / disunification cases を集約した初期一覧である。各行に source、historical code point、decision code point、文書時点の status、reference、移動元に残す source reference を置く。

Meeting \#45-\#52 の多くは `done` とされ、Meeting \#56 の T6-487C、T4-2A44、T5-2160 は approved、KP0-E5A9 は DPRK confirmation 待ちとして記録される。2021-10-08 revision では、TCA feedback により Meeting \#52 / \#56 の7 source references が追加された。

## 報告内容

### status と decision の区別

表の `Decision` は新しい対応先 code point、`Current Status` はその処理段階を表す。Meeting \#56 の U+317B2 / U+31C34 は draft で変更可能と注記されており、後続版で確定した code point と同一視してはならない。

### historical code point の source preservation

T-source や H-source を別 code point へ移す case では、移動元に `TU-...`、`TB-...`、`HU-...` といった historical / internal source reference を残す。たとえば T4-2135 を U+4DB9 へ移した後の U+2F878 は `TU-2F878`、H-8FA8 を U+270F0 へ移した後の U+2F9B2 は `HU-2F9B2` で記録する。

### 会合別の蓄積

| Meeting | 主な内容 |
| --- | --- |
| \#45 | K3-2A46 を U+3E02 から U+9FEA へ disunify。 |
| \#48-\#50 | T / H source glyphs の mapping correction と別 code point への移動。 |
| \#51-\#52 | compatibility ideographs や T-source glyphs の分離、新 code point、historical source reference の追加。 |
| \#56 | T6-487C、T4-2A44、T5-2160 などの approved cases と、DPRK confirmation 待ちの KP0-E5A9。 |

## 後続決定

[IRG N2892](irg-n2892.md) は対象を Meeting \#65 まで拡張し、`IRG N2491R` の approved / draft cases について後続の code point と status を更新した。さらに Meeting \#66 は official [IRG Disunified Ideographs](https://www.unicode.org/irg/disunified.html) web page を旧一覧の replacement として accept している。

したがって `IRG N2491R` は 2021-10-08 時点の decision trail として使い、現在の status は後続版と official web page で確認する。

## 論点

### source remapping と disunification

文書 title page は `List of source-remapping cases` とし、表には glyph correction、source exchange、compatibility ideograph からの分離、new encoding を一緒に載せる。すべてを「新文字の追加」として読むのではなく、source reference と code point identity の変化を分ける必要がある。

### dated snapshot の値

`approved` は Unicode / ISO/IEC 10646 への最終反映を必ずしも意味しない。特に draft code point は後続文書で変更され得るため、この文書の値を current assignment として再利用しない。

## 関連文書

- [IRG N2892](irg-n2892.md) - Meeting \#65 まで拡張された後続一覧。

## 関連トピック

- [IRG Disunified Ideographs](../topics/irg-disunified-ideographs.md)
- [IRG Source Data and Representative Glyphs](../topics/irg-source-data-and-representative-glyphs.md)

## 出典

- `irg-n2491r` - <https://www.unicode.org/irg/docs/n2491r-Disunified.pdf>
- IRG, [IRG Disunified Ideographs](https://www.unicode.org/irg/disunified.html)
