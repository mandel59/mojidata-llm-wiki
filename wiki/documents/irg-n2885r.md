---
type: Source Document
title: "Some comments RE: IRG N2866R, Script-Hybrid Characters and GB 18030"
description: "Kim Kyongsok が IRG N2866R に対し、IRG scope、P&P、legacy mapping、terminology、候補数見積もりを質問した feedback。"
resource: https://www.unicode.org/irg/docs/n2885r-IRGN2866RFeedback.pdf
entry_id: irg-n2885r
doc_number: IRG N2885R
document_type: feedback
aliases: [IRG N2885, "comments RE: IRG N2866R"]
registry: irg
date: "2025-10-11"
source: KIM, Kyongsok
documents: [irg-n2866r2, irg-n2792, irg-n2867r, irg-n2828, irg-n2826]
topics: [cjk-hybrid-characters, cjk-multi-syllabic-and-abbreviation-characters]
people: [kim-kyongsok, witty-wen, irg]
events: [irg-m65-24-cjk-hybrid-characters]
tags: [document, irg, cjk-hybrid, feedback, rok]
timestamp: 2026-07-08T00:00:00+09:00
---

# IRG N2885R

## 要約

`IRG N2885R` は、Kim Kyongsok が Witty Wen の `IRG N2866R` に対して提出した comments である。CJK Hybrid Characters を IRG が扱うとしても、IRG P&P をどう変えるのか、legacy encoded cases の mapping とは何を意味するのか、terminology をどう固定するのかを質問している。

文書は `IRG N2792` を参照し、member body ごとに候補数を見積もるべきだと再度述べる。Korea の新規候補はほぼ 0 とされ、全体候補数が少ないなら複雑な制度変更は不要かもしれないという観点を示す。

## フィードバック内容

| 論点 | 内容 |
| --- | --- |
| IRG scope | IRG は CJK-related issues の expertise を持つが、CJK Hybrid Characters を IRG 外で扱う可能性も評価できるとする。 |
| IRG P&P | CJKUI blocks 以外の CJK Hybrid Characters を IRG が扱うなら、IRG P&P を修正する必要があるのかを質問する。 |
| legacy mapping | already-encoded legacy cases について China may decide mapping とする場合、その mapping が何から何への mapping なのか説明を求める。 |
| terminology | script-hybrid は ideographs ではなく characters として扱うという理解でよいか、"script-hybrid Han Ideographs" という用語を避けるべきかを確認する。 |
| candidate count | `IRG N2792` と同様、各 member body が候補数を見積もるべきとし、Korea の候補はほぼ 0 とする。 |

## 後続決定

`IRG N2866R` は後に [IRG N2866R2](irg-n2866r2.md) として更新され、CJK Hybrid Characters block の独立案を再提示した。

[IRG N2828](irg-n2828.md) と [IRG N2826](irg-n2826.md) は、IRG Meeting \#65 での CJK Hybrid Characters consensus に接続する。

## 論点

### policy before repertoire

`IRG N2885R` は、特定の character list より先に、IRG scope、P&P、terminology、legacy mapping を明確にする必要を示す feedback である。この観点は [CJK Hybrid Characters](../topics/cjk-hybrid-characters.md) の umbrella policy に残す。

### 候補数による process choice

候補数が少ないなら、重い process や block design を急がず、member body feedback と IRG consensus を先に作るという選択肢がある。これは [CJK Multi-Syllabic and Abbreviation Characters](../topics/cjk-multi-syllabic-and-abbreviation-characters.md) の source prioritization 論点にも接続する。

## 関連文書

- [IRG N2792](irg-n2792.md) - KR position paper。
- [IRG N2866R2](irg-n2866r2.md) - Script-Hybrid Characters and GB 18030。
- [IRG N2867R](irg-n2867r.md) - Multi-Syllabic Characters and Abbreviation Characters。
- [IRG N2828](irg-n2828.md) - IRG \#65 editorial report。
- [IRG N2826](irg-n2826.md) - IRG Meeting \#65 recommendations。

## 関連トピック

- [CJK Hybrid Characters](../topics/cjk-hybrid-characters.md)
- [CJK Multi-Syllabic and Abbreviation Characters](../topics/cjk-multi-syllabic-and-abbreviation-characters.md)

## 出典

- `irg-n2885r` - <https://www.unicode.org/irg/docs/n2885r-IRGN2866RFeedback.pdf>
- `irg-n2792` - <https://www.unicode.org/irg/docs/n2792-ScriptHybridPosition.pdf>
