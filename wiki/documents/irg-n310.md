---
type: "Source Document"
title: "Ideographic Components and Composition Scheme"
description: "1996-02-05 の Ideographic Components and Composition Scheme 討議文書。"
resource: "https://www.unicode.org/irg/docs/n0310-IdeographicComposition.pdf"
entry_id: "irg-n310"
doc_number: "IRG N310"
document_type: "proposal"
aliases: ["WG2 N1348"]
registry: "irg"
date: "1996-02-05"
source: "ZHANG, Zhoucai at al."
topics: ["early-irg-history", "cjkv-components"]
documents: ["irg-n200", "irg-n259", "irg-n313", "irg-n315", "irg-n365", "irg-n392"]
meetings: ["irg-meeting-6"]
events: []
people: ["irg", "zhang-zhoucai"]
tags: ["document", "irg", "history"]
---

# IRG N310

## 要約

1996-02-05 の Ideographic Components and Composition Scheme 討議文書。
符号化されていない使用頻度の低い漢字を、components と再帰的 composition functions で表す構想を説明する。
検索、教育、OCR、入力方式への用途と、PU / UTF-16 / UCS-4 との併用を挙げる。
囲み関数の分け方、Resemble、Combined Ideographic Sequence の定義には継続検討を残す。

## 提案内容

- p.2: component、radical、composition scheme を定義し、LTR / ATB / AMB / LMR / OTI の関数を説明する。
- p.3: Outside-to-Inside を1関数にするか、囲み方で細分するかを検討する。似ているが同一ではないことを示す RSM の採否も further study とする。
- p.3–4: prefix notation の再帰的な Combined Ideographic Sequence（CIS）構文例を示すが、定義は確定していないとする。
- p.4: Korea / Vietnam / TCA の feasibility studies を報告し、既存文字・Vertical Extension と重複しない未符号化 components を特定する方針を示す。

## 後続決定

[N315](irg-n315.md)項目2–5 が選択条件と構造記号の扱いを決議する。後続は [N313](irg-n313.md)、[N365](irg-n365.md)、[WG2 の明確化要求](../events/wg2-31-ideographic-description-refinement.md)へ。

## 論点

CIS はこの提案の用語であり、現在の IDS の仕様・等価性・表示動作をこの構文だけから確定しない。

## 出典

- `irg-n310` - <https://www.unicode.org/irg/docs/n0310-IdeographicComposition.pdf>（registry date: 1996-02-05）
