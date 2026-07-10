---
type: Source Document
title: "G-Source references updates for 1,538 characters"
description: "China が9種類のG-sourceに属する1,538 charactersのreference values、4 source prefixesの書誌記述、および3 source reference syntaxesの更新を提案した文書。"
resource: https://www.unicode.org/irg/docs/n2864r-GSourceChanges.pdf
entry_id: irg-n2864r
doc_number: IRG N2864R
document_type: proposal
registry: irg
date: "2025-09-28"
source: China
documents: [irg-n2689, irg-n2835r, irg-n2837, irg-n2838, irg-n2840, irg-n2863, irg-n2868, irg-n2874, irg-n2923r]
topics: [g-source-glyph-and-reference-issues, irg-source-data-and-representative-glyphs]
people: [china, irg]
meetings: [irg-meeting-65]
tags: [document, irg, g-source, source-reference, unihan, proposal]
timestamp: 2026-07-10T00:00:00+09:00
---

# IRG N2864R

## 要約

`IRG N2864R` は、China が G-source references for 1,538 characters の更新を IRG と WG2 に提案した文書である。対象は G3 19、G5 15、GCH 624、GCY 192、GE 1、GHC 601、GHZ 1、GU 3、GXC 82 characters で、複数の先行feedbackを照合して publishing source に対応するreferenceへ整理する。

文書は個々の値だけでなく、GCH / GCY / GHC / GXC source prefixesの書誌記述と、GCH / GCY / GHC reference syntaxの更新も求める。1,538件の完全なproposed valuesは別添appendixに置かれ、本文は根拠、例外処理、schema変更を説明する。

## 提案内容

| 分類 | 変更範囲 | 提案の要点 |
| --- | ---: | --- |
| 大規模reference更新 | GCH 624、GHC 601、GCY 192、GXC 82 | `IRG N2835R`、`IRG N2837`、`IRG N2838`等のevidenceを照合し、publishing sourceに即した値へ更新する。 |
| その他のG-source | G3 19、G5 15、GE 1、GHZ 1 | `IRG N2840`、`IRG N2863`等で指摘された個別reference issueを取り込む。 |
| GU-source置換 | 3 | U+FA11、U+FA18、U+2528Cを、根拠資料が特定されたGCA / GWY referencesへ移す。 |
| source description | GCH、GCY、GHC、GXC | 辞書名だけの曖昧な説明を、edition、publisher、刊行年、ISBN等を含む書誌記述へ改め、ISO/IEC 10646 Section 24.2とUAX \#38にも同期する。 |
| syntax | GCH、GCY、GHC | code point型の暫定referenceから、辞書上の位置を表す `dddd.dd` または7-digit形式へ戻す。 |
| 例外 | 62 requests | 先行文書の要求をそのまま採用せず、別のpublishing sourceとreferenceを提示する。 |

## 後続決定

本文は `Status: Member's submission`、`Actions required: To be considered by IRG and WG2` として提出されたproposalであり、それ自体は採択記録ではない。U+246C9とU+249E9のglyph updatesは `IRG N2874` で別途扱うとして、reference updateとglyph changeを分離している。

[IRG N2923R](irg-n2923r.md) は本提案を先行する大規模G-source reviewの一つとして参照しつつ、別の329 reference updatesと9 horizontal extension candidatesを扱う。したがって両文書の件数を単純に合算したり、`IRG N2923R`を本提案の採択結果と解釈したりはできない。

## 論点

### 値の更新とdata modelの更新

提案は1,538 charactersのdata patchに留まらない。source prefix descriptionとreference syntaxも同時に変更するため、IRG source data、ISO/IEC 10646、UAX \#38の記述を整合させる必要がある。一方、本文が詳細に列挙するのは先行要求と異なる62件などに限られ、全件の監査には別添appendixと各evidence文書が必要である。

### 根拠資料とglyph issueの境界

referenceは辞書・刊本中の位置を識別するものであり、同じcharacterにより適切なpublishing sourceが確認された場合はsource prefix自体の置換も提案される。ただしreferenceの修正はrepresentative glyphの正しさを自動的に保証しないため、glyph updatesは別文書へ切り出されている。

## 関連文書

- [IRG N2923R](irg-n2923r.md) - 後続の329 G-source reference updatesと9 horizontal extension candidates。
- `IRG N2835R` / `IRG N2838` - GCH / GCY / GHC requestsと相違点。
- `IRG N2837` - 82 GXC-source charactersの更新要求。
- `IRG N2868` - source descriptionsとGXC syntaxへのfeedback。
- [G-source Glyph and Source Reference Issues](../topics/g-source-glyph-and-reference-issues.md)
- [IRG Source Data and Representative Glyphs](../topics/irg-source-data-and-representative-glyphs.md)

## 出典

- `irg-n2864r` - <https://www.unicode.org/irg/docs/n2864r-GSourceChanges.pdf>
