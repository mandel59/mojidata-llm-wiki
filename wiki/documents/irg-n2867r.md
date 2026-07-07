---
type: Source Document
title: "Multi-Syllabic Characters and Abbreviation Characters"
description: "Witty Wen が Han-only multi-syllabic abbreviation characters と script-hybrid characters の分類境界を整理した文書。"
resource: https://www.unicode.org/irg/docs/n2867r-MultiSyllabicCharacters.pdf
entry_id: irg-n2867r
doc_number: IRG N2867R
document_type: proposal
aliases: [Multi-Syllabic Characters and Abbreviation Characters]
registry: irg
date: "2025-10-15"
source: Witty Wen
documents: [irg-n2866r2, irg-n2885r, irg-n2828, irg-n2826]
topics: [cjk-multi-syllabic-and-abbreviation-characters, cjk-hybrid-characters]
people: [witty-wen, china, irg]
events: [irg-m65-24-cjk-hybrid-characters]
tags: [document, irg, abbreviation, multi-syllabic, cjk-hybrid]
timestamp: 2026-07-08T00:00:00+09:00
---

# IRG N2867R

## 要約

`IRG N2867R` は、Witty Wen による multi-syllabic characters / abbreviation characters の individual contribution である。機能として abbreviation であっても、components がすべて Han である characters と、Latin / Kana / Hangul / Bopomofo など非 Han elements を含む script-hybrid characters を区別すべきだと主張する。

文書は、兛、粁、糎、U+2EDEE のような Han-only multi-syllabic characters は CJKUI review の範囲で扱える一方、`⿸广K` のような Latin letter を意図する form は script-hybrid として別 block 側に分類すべきとする。

## 提案内容

| 区分 | 内容 |
| --- | --- |
| terminology | abbreviation characters は広い機能 category、script-hybrid characters は非 Han script elements を含む structural category、multi-syllabic characters は multi-syllabic expression を 1 graph に圧縮する category と整理する。 |
| Han-only rule | すべての components が Han radicals / components なら、multi-syllabic abbreviation character として通常の IRG / CJKUI process で扱えるとする。 |
| non-Han components | Latin、Kana、Hangul、Zhuyin などに由来する component を含む場合は script-hybrid character として扱う。 |
| source priority | Han-based sources、特に China、Hong Kong SAR、Macao SAR、TCA による evidence を優先すべきとする。 |
| Goryaku-gana | 合略仮名は condensed readings として abbreviation characters だが、CJKUI ではなく independent block が適切とする。 |

## 後続決定

[IRG N2828](irg-n2828.md) は、`IRG N2867R` を CJK Hybrid Characters 関連文書群に含めて review し、Han-Hangul hybrid exceptions を除く hybrid characters を normal CJKUI とは別 block に置くことを提案した。

[IRG N2826](irg-n2826.md) の M65.24 は、CJK hybrid characters の encoding は WG2、oversight は IRG とする consensus を記録した。ただし、Han-only abbreviation characters の independent policy までは決定していない。

## 論点

### function と structure の分離

文書の中心は、abbreviation という機能だけで CJKUI inclusion / exclusion を決めないことである。Han-only の multi-syllabic graph は CJKUI process に残し、非 Han script identity を component として持つ graph は hybrid block に送る、という分類が提案される。

### legacy encoded cases

`IRG N2867R` は、all-Katakana / all-hiragana shaped cases や U+323BF のような legacy cases を oversight として扱う。これは既存 code point の移動を決めたものではなく、今後の GB 18030 mapping、property design、source policy の検討材料である。

## 関連文書

- [IRG N2866R2](irg-n2866r2.md) - Script-Hybrid Characters and GB 18030。
- [IRG N2885R](irg-n2885r.md) - comments on `IRG N2866R`。
- [IRG N2828](irg-n2828.md) - IRG \#65 editorial report。
- [IRG N2826](irg-n2826.md) - IRG Meeting \#65 recommendations。

## 関連トピック

- [CJK Multi-Syllabic and Abbreviation Characters](../topics/cjk-multi-syllabic-and-abbreviation-characters.md)
- [CJK Hybrid Characters](../topics/cjk-hybrid-characters.md)

## 出典

- `irg-n2867r` - <https://www.unicode.org/irg/docs/n2867r-MultiSyllabicCharacters.pdf>
