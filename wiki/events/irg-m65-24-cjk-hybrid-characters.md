---
type: Event
title: "IRG M65.24 CJK Hybrid Characters"
description: "IRG #65 Recommendation M65.24 が CJK hybrid characters を WG2 に委ねつつ IRG oversight で CJKUI / 別 block を判断する方針を記録した出来事。"
slug: irg-m65-24-cjk-hybrid-characters
date: "2025-10-16"
bodies: [IRG, WG2]
documents: [irg-n2792, irg-n2826, irg-n2828, irg-n2866r2, irg-n2867r, irg-n2885r, irg-n2893]
topics: [cjk-hybrid-characters, cjk-multi-syllabic-and-abbreviation-characters, kana]
status: active
tags: [event, recommendation, irg, hybrid, cjkui]
timestamp: 2026-07-07T00:00:00+09:00
---

# IRG M65.24 CJK Hybrid Characters

## 概要

IRG Meeting \#65 Recommendation M65.24 は、CJK hybrid characters の encoding policy を整理した recommendation である。対象は、Latin、Hiragana、Katakana、Bopomofo などを部品として含む Han-like characters を含む。

IRG は、well-attested Korean ideographs with Hangul-based phonetic components を例外とし、CJK hybrid characters は CJK Unified Ideographs extension blocks ではなく別 block に符号化すべきとした。encoding は WG2 に委ねるが、IRG が oversight を持ち、個別 character が CJKUI extension block に入るか CJK Hybrid Characters block に入るかを判断する。

## 背景

IRG \#65 では、CJK Unified Ideographs に非 Han script components を持つ Han-like characters を入れるか、別 block として扱うかが問題になった。関連文書には、script-hybrid characters を独立 block に置く案、GB 18030 側の扱いに関する feedback、multi-syllabic / abbreviation characters との分類境界が含まれる。

## 結果

| 項目 | 内容 |
| --- | --- |
| 分担 | Encoding は WG2、oversight は IRG。 |
| 判断 | IRG が CJKUI extension block か CJK Hybrid Characters block かを判断する。 |
| 原則 | Latin / Hiragana / Katakana / Bopomofo などを部品に含む Han-like characters は CJKUI extension とは別 block。 |
| 例外 | Hangul に基づく phonetic components を含む well-attested Korean ideographs。 |
| 後続 | Unihan properties を付ける場合、source references、radical、stroke count、readings などの規則を IRG review で議論する。 |

## 影響範囲

この event は、[CJK Hybrid Characters](../topics/cjk-hybrid-characters.md) の block policy を整理する中心的な decision point である。仮名を component に持つ Han-like characters については、通常の CJKUI extension ではなく hybrid block 側で検討する方向を示すため、[Kana](../topics/kana.md) と CJKUI boundary の議論にも関係する。

Han-only の multi-syllabic / abbreviation characters との境界は [CJK Multi-Syllabic and Abbreviation Characters](../topics/cjk-multi-syllabic-and-abbreviation-characters.md) に分ける。M65.24 は hybrid block policy の consensus であり、Han-only abbreviation characters の独立 encoding policy までは決めていない。

## 関連ページ

- [IRG N2792](../documents/irg-n2792.md)
- [IRG N2826](../documents/irg-n2826.md)
- [IRG N2828](../documents/irg-n2828.md)
- [IRG N2866R2](../documents/irg-n2866r2.md)
- [IRG N2867R](../documents/irg-n2867r.md)
- [IRG N2885R](../documents/irg-n2885r.md)
- [IRG N2893](../documents/irg-n2893.md)
- [CJK Hybrid Characters](../topics/cjk-hybrid-characters.md)
- [CJK Multi-Syllabic and Abbreviation Characters](../topics/cjk-multi-syllabic-and-abbreviation-characters.md)
- [Kana](../topics/kana.md)

## 出典

- `irg-n2792` - <https://www.unicode.org/irg/docs/n2792-ScriptHybridPosition.pdf>
- `irg-n2826` - <https://www.unicode.org/irg/docs/n2826-Recommendations.pdf>
- `irg-n2828` - <https://www.unicode.org/irg/docs/n2828-MiscEditorialReport.pdf>
- `irg-n2866r2` - <https://www.unicode.org/irg/docs/n2866r2-ScriptHybridFeedback.pdf>
- `irg-n2867r` - <https://www.unicode.org/irg/docs/n2867r-MultiSyllabicCharacters.pdf>
- `irg-n2885r` - <https://www.unicode.org/irg/docs/n2885r-IRGN2866RFeedback.pdf>
- `irg-n2893` - <https://www.unicode.org/irg/docs/n2893-CJKHybridCharacters.pdf>
