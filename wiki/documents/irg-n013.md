---
type: "Source Document"
title: "Error report of CJK Unified Ideographs in the 10646 UCS Part 1"
description: "Japan が初版 ISO/IEC 10646-1 の CJK chart の誤りを報告した文書。"
resource: "https://www.unicode.org/irg/docs/n0013-ErrorReport.pdf"
entry_id: "irg-n013"
doc_number: "IRG N013"
document_type: "report"
aliases: ["WG2 N933"]
registry: "irg"
date: "1993-10-04"
source: "Japan"
documents: ["irg-n034", "irg-n2946"]
topics: ["early-irg-history", "irg-source-data-and-representative-glyphs"]
meetings: ["irg-meeting-1"]
events: []
tags: ["document", "irg", "history"]
people: ["japan"]
---

# IRG N013

## 要約

Japan が初版 ISO/IEC 10646-1 の CJK chart の誤りを報告した文書。
source code の誤りと glyph の誤りを分け、後者を wrong shape と wrong quality に分類する。
次の SC 2/WG2 会合へ correction を求める意向を示し、IRG への requested action は Information only とする。
個別の修正が採択・反映されたことまでは示さない。

## 報告内容

- p.2 の Wrong source code は U+8778、U+9BEF、U+9D6F の参照を挙げる。U+9D6F の一例は `0-223B` から `0-723B` への訂正要求である。
- p.3 は S=wrong shape、Q=wrong quality として対照表を載せる。U+8429 は S の例。
- これは1993年版に対する報告である。表の文字を現在も誤っている文字の一覧として扱わない。

## 後続決定

個々の correction の WG2 処理・規格反映はこの資料だけでは確定しない。比較先の [IRG N2946](irg-n2946.md) M67.13–18 は、2026年の source / glyph issue の受入勧告と継続照会を記録する。

## 出典

- `irg-n013` - <https://www.unicode.org/irg/docs/n0013-ErrorReport.pdf>（registry date: 1993-10-04）
