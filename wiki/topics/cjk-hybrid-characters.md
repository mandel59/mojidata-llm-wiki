---
type: Topic
title: CJK Hybrid Characters
description: "仮名・Bopomofo・Latin・Hangul などを部品に含む Han-like characters を CJKUI に入れるか、別 block とするかの IRG / WG2 policy。"
slug: cjk-hybrid-characters
bodies: [IRG, WG2, UTC]
documents: [irg-n2792, irg-n2826, irg-n2828, irg-n2866r2, irg-n2867r, irg-n2885r, irg-n2893]
topics: [cjk-multi-syllabic-and-abbreviation-characters, kana, cjkv-components, irg-working-set-2024, unihan-database-maintenance]
events: [irg-m65-24-cjk-hybrid-characters]
status: active
tags: [cjk, hybrid, kana, bopomofo, hangul, latin, irg]
timestamp: 2026-07-08T00:00:00+09:00
---

# CJK Hybrid Characters

## 概要

CJK Hybrid Characters は、Han-like な字形や CJK text での使用を持つが、Latin、Hiragana、Katakana、Bopomofo、Hangul、記号などの非 Han / 非 CJKUI 的要素を部品に含む文字をどう符号化するかという論点である。

中心問題は、これらを通常の CJK Unified Ideographs extension block に入れると、CJKUI の前提である radical / stroke、source reference、unification、IDS、Unihan property の規則をどこまで拡張する必要があるかである。IRG Meeting \#65 の [IRG M65.24 CJK Hybrid Characters](../events/irg-m65-24-cjk-hybrid-characters.md) は、原則として CJKUI extension とは別 block に置く方向を示した。

multi-syllabic / abbreviation characters は機能面では隣接するが、components がすべて Han なら script-hybrid とは別に扱う必要がある。この subclass-specific 議論は [CJK Multi-Syllabic and Abbreviation Characters](cjk-multi-syllabic-and-abbreviation-characters.md) に分ける。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2025-02-28 | IRG | [IRG N2792](../documents/irg-n2792.md) | ROK が script-hybrid Han ideographs の position paper を提出し、IRG scope、member body ごとの候補数、historical usage に基づく CJKUI inclusion の可能性を論じた。 |
| 2025-10-11 | IRG | [IRG N2885R](../documents/irg-n2885r.md) | Kim Kyongsok が `IRG N2866R` にコメントし、CJK Hybrid Characters を IRG が扱う場合の P&P、terminology、legacy mapping、候補数見積もりを質問した。 |
| 2025-10-15 | IRG | [IRG N2866R2](../documents/irg-n2866r2.md) | Witty Wen が、script-hybrid characters を独立した CJK Hybrid Characters block に置く案を提示した。 |
| 2025-10-15 | IRG | [IRG N2867R](../documents/irg-n2867r.md) | Witty Wen が Multi-Syllabic Characters and Abbreviation Characters を提出し、Han-only abbreviation characters と script-hybrid characters の境界を整理した。 |
| 2025-10-15 | IRG | [IRG N2893](../documents/irg-n2893.md) | China が CJK Hybrid Characters の名称、block policy、Han-Kana / Han-Bopomofo / Han-Latin exclusion、Han-Hangul exception を提示した。 |
| 2025-10-16 | IRG | [IRG N2828](../documents/irg-n2828.md) | CJK Editorial Group report が、Han-Hangul hybrid 例外を除き、CJK Hybrid Characters を normal CJKUI とは別 plane / 別 block に置くことを提案した。 |
| 2025-10-16 | IRG | [IRG N2826](../documents/irg-n2826.md) | [IRG M65.24](../events/irg-m65-24-cjk-hybrid-characters.md)。IRG が CJK hybrid characters の encoding を WG2 に委ねつつ IRG oversight を残し、CJKUI extension か別 block かを IRG が判断する consensus を記録した。 |

## 主な論点

### 仮名や Bopomofo を含む Han-like characters

[IRG N2826](../documents/irg-n2826.md) の M65.24 は、CJK hybrid character の定義として、Latin、Hiragana、Katakana、Bopomofo を部品として含む Han-like characters を明示する。重要なのは、これらの部品が Han components のように見える形で現れていても、CJK hybrid character として扱い得るとした点である。

このため、「仮名などを構成要素に持つ漢字」は、単純に CJKUI として扱うのではなく、CJK Hybrid Characters として独立に評価する対象になる。[IRG N2866R2](../documents/irg-n2866r2.md) は、withdrawn / unencoded の Han-Katakana `⿸广マ`、Han-Latin `⿸广K`、すでに CJKUI に入っている Han-Hiragana U+2D92A、Han-Bopomofo U+20B9A、all-Katakana U+2BCCD、all-hiragana U+2CF00 などを例示する。

### 別 block 原則

M65.24 は、CJK hybrid characters は CJK Unified Ideographs extension blocks とは別 block に符号化すべきと整理した。具体的には Plane 2 / Plane 3 の CJKUI extension block には置かない、と述べている。

理由は、CJKUI の既存 process が Han ideographs を前提としており、非 Han scripts / symbols を部品として含む場合に radical assignment、stroke count、source references、readings、unification rules がそのまま適用できないためである。[IRG N2866R2](../documents/irg-n2866r2.md) も、急いで ordinary ideographs として扱うより、独立 block に置くことで guidelines を整備する時間を確保できると述べる。

### Han-Hangul hybrid の例外

M65.24 は、Hangul に基づく phonetic components を含む well-attested Korean ideographs について例外を置く。[IRG N2893](../documents/irg-n2893.md) も、Han-Hangul hybrid characters は font style と usage が Han ideographs と概ね一致し、明確な non-Han ideograph components がないとして、CJKUI に引き続き入れ得ると述べる。

一方で [IRG N2893](../documents/irg-n2893.md) は、Bopomofo、Hiragana、Katakana は Han ideographs に由来する面があっても、独自の application scenarios と font styles を持ち、゜（U+309C）や ㆱ（U+31B1）のように歴史的な Han ideographs に現れない部品も含むため、Han-Bopomofo / Han-Kana hybrid characters は CJKUI に入れるべきでないとする。

### 既に符号化済みの legacy cases

議論は新規提案だけでなく、すでに CJKUI blocks に入った characters の扱いにも関わる。[IRG N2866R2](../documents/irg-n2866r2.md) は U+323BF を例に、intent としては Latin X に由来するが code chart では Han component 㐅 として描かれた case を挙げる。また U+2A708、U+2BCCD、U+2CF00 などの already encoded cases を GB 18030 側でどう扱うかを China に確認すべきと述べる。

この点は、既存 CJKUI からの移動や再分類が直ちに決まったという意味ではない。M65.24 は future encoding path と review responsibility を整理したもので、legacy cases については mapping、property、standard text の扱いが今後の課題として残る。

### IRG と WG2 の分担

M65.24 は、encoding work 自体は WG2 に委ねるが、IRG が oversight を持ち、特定の character を CJKUI extension block に入れるか CJK Hybrid Characters block に入れるかを判断するとする。Unihan database properties を付ける場合も、IRG review process で IRG source references、Kangxi radical、stroke count、readings などの規則を議論できると整理している。

### abbreviation characters との境界

[IRG N2867R](../documents/irg-n2867r.md) は、abbreviation function と script identity を分ける。兛・粁・糎・U+2EDEE のように all components が Han である multi-syllabic abbreviation characters は、script-hybrid ではなく通常の CJKUI review に残せる。一方、Latin / Kana / Hangul / Bopomofo を component として意図する forms は CJK Hybrid Characters 側に送る。

この整理は [CJK Multi-Syllabic and Abbreviation Characters](cjk-multi-syllabic-and-abbreviation-characters.md) に分けて追跡する。

## 現状

2025-10-16 の [IRG N2826](../documents/irg-n2826.md) 時点では、CJK hybrid characters は active な設計課題であり、CJKUI extension とは別 block とする方向が IRG consensus として示された。未決点は、block 名と code space、IRG P&P への反映要否、Unihan property 付与規則、legacy encoded cases の扱い、Han-Hangul hybrid の例外範囲である。

multi-syllabic / abbreviation characters は、subclass-specific な整理として [CJK Multi-Syllabic and Abbreviation Characters](cjk-multi-syllabic-and-abbreviation-characters.md) で追い、CJK Hybrid Characters page では script boundary と block policy を中心に扱う。

## 関連文書

- [IRG N2792](../documents/irg-n2792.md) - KR position on script-hybrid Han ideographs。
- [IRG N2866R2](../documents/irg-n2866r2.md) - Script-Hybrid Characters and GB 18030。
- [IRG N2867R](../documents/irg-n2867r.md) - Multi-Syllabic Characters and Abbreviation Characters。
- [IRG N2885R](../documents/irg-n2885r.md) - comments on `IRG N2866R`。
- [IRG N2893](../documents/irg-n2893.md) - China の CJK Hybrid Characters encoding policy。
- [IRG N2828](../documents/irg-n2828.md) - Editorial Report on Miscellaneous Issues; CJK Hybrid Characters item。
- [IRG N2826](../documents/irg-n2826.md) - IRG Meeting \#65 recommendations; M65.24。

## 関連出来事

- [IRG M65.24 CJK Hybrid Characters](../events/irg-m65-24-cjk-hybrid-characters.md)

## 関連トピック

- [CJK Multi-Syllabic and Abbreviation Characters](cjk-multi-syllabic-and-abbreviation-characters.md)
- [Kana](kana.md)
- [CJKV Components](cjkv-components.md)
- [IRG Working Set 2024](irg-working-set-2024.md)
- [Unihan Database Maintenance](unihan-database-maintenance.md)

## 出典

- `irg-n2792` - <https://www.unicode.org/irg/docs/n2792-ScriptHybridPosition.pdf>
- `irg-n2826` - <https://www.unicode.org/irg/docs/n2826-Recommendations.pdf>
- `irg-n2828` - <https://www.unicode.org/irg/docs/n2828-MiscEditorialReport.pdf>
- `irg-n2866r2` - <https://www.unicode.org/irg/docs/n2866r2-ScriptHybridFeedback.pdf>
- `irg-n2867r` - <https://www.unicode.org/irg/docs/n2867r-MultiSyllabicCharacters.pdf>
- `irg-n2885r` - <https://www.unicode.org/irg/docs/n2885r-IRGN2866RFeedback.pdf>
- `irg-n2893` - <https://www.unicode.org/irg/docs/n2893-CJKHybridCharacters.pdf>
