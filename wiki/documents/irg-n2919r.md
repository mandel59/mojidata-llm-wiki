---
type: Source Document
title: "Proposal on modifying 3 G-source representative glyphs and changing 10 G-source references"
description: "Wang Xieyang が 3 G-source representative glyphs と 10 G-source references の変更を提案し、GCW-source を rare place / personal name characters 用の future source として説明した文書。"
resource: https://www.unicode.org/irg/docs/n2919r-GSourceChanges.pdf
entry_id: irg-n2919r
doc_number: IRG N2919R
document_type: proposal
registry: irg
date: "2026-03-09"
source: WANG, Xieyang
documents: [irg-n2909, irg-n2911, irg-n2923r, irg-n2930]
topics: [g-source-glyph-and-reference-issues, irg-source-data-and-representative-glyphs, cjk-horizontal-extensions]
people: [china, irg]
meetings: [irg-meeting-66, irg-meeting-67]
tags: [document, irg, g-source, representative-glyphs, source-reference, proposal]
timestamp: 2026-07-08T00:00:00+09:00
---

# IRG N2919R

## 要約

`IRG N2919R` は、3 G-source representative glyphs の修正と、10 G-source references の変更を提案する文書である。提案者は Wang Xieyang / Center for Toponym Research of SISU で、rare characters used in Chinese official place names and personal names を扱う将来 database と同じ source reference として `GCW` source を説明している。

glyph 修正対象は U+250A9、U+25805、U+26C25 である。source reference 変更対象は U+23B48、U+23FE8、U+241C5、U+25618、U+256AE、U+29596、U+29AF5、U+29AFB、U+2B962、U+2C28D の 10 characters で、`GU` / `GDM` references から `GCW` references への変更を提案する。

## 提案内容

### Representative glyphs

| Code point | Pronunciation | Suggested reference | 要点 |
| --- | --- | --- | --- |
| U+250A9 | gǔ | `GCW-80000` | current G-source glyph は《康熙字典》《汉语大字典》由来の error form とし、actual usage に合わせる。 |
| U+25805 | huàn | `GHZR-52793.09` | current glyph は《康熙字典》由来で modern Chinese convention と合わないため、《汉语大字典》に基づく glyph を提案する。 |
| U+26C25 | bāng | `GCW-80001` | current evidence には具体的 meaning がなく、WS2017 で重複 encoding された U+31U68 との関係も踏まえ、U+26C25 側の glyph / reference を変更する。 |

### Source references

文書は 10 characters について、existing `GU` / `GDM` references を `GCW-80002` から `GCW-80011` へ変更する案を示す。根拠として、紅楼夢、地理情報関連の庫外字登记表、同音姓氏表、中华姓氏源流大辞典、人名用生僻字注音字典などの evidence images を挙げる。

## 後続決定

[IRG N2911](irg-n2911.md) は、IRG Meeting \#66 editorial group が U+250A9 と U+25805 の G-source glyph revisions を in principle に受け入れた一方、U+26C25 は further investigation が必要で、China が Meeting \#67 に feedback を提出するとした。

同じ report は、`IRG N2919R` と [IRG N2923R](irg-n2923r.md) に含まれる 342 G-source reference changes は further discussion が必要であり、この meeting では action しなかったと記録している。したがって、この文書の全提案が accepted になったわけではない。

## 論点

### `GCW` source の位置づけ

文書は `GCW` source を、IRG WS2024 で新たに導入された source であり、Center for Toponym Research of SISU が将来 publish する free database と連動するものとして説明する。既存 encoded characters の source references を新 source へ移すには、source の安定性と IRG / China NB の確認が必要である。

### glyph correction と source reference change の混在

`IRG N2919R` は representative glyph correction と source reference correction を同時に扱う。Meeting \#66 の結果は、glyph の一部は in principle accepted、reference changes は pending という分離された状態であり、wiki でも同一文書内の提案を一括で採否判定しない。

## 関連文書

- [IRG N2911](irg-n2911.md) - Meeting \#66 editorial report。
- [IRG N2909](irg-n2909.md) - Meeting \#66 recommendations。
- [IRG N2923R](irg-n2923r.md) - 329 G-source reference changes and 9 horizontal extensions。
- [IRG N2930](irg-n2930.md) - accepted 3 G-source reference changes。
- [G-source Glyph and Source Reference Issues](../topics/g-source-glyph-and-reference-issues.md)

## 出典

- `irg-n2919r` - <https://www.unicode.org/irg/docs/n2919r-GSourceChanges.pdf>
