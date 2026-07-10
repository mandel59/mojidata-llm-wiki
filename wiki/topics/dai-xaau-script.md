---
type: Topic
title: "Dai Xaau Script"
description: "Dai Xaau / Tai Xaau script の UCS encoding proposal と Tai Viet からの disunification 論点。"
slug: dai-xaau-script
aliases: ["Tai Xaau Script", "Jinping Dai writing system", "Jinping Dai script"]
bodies: [WG2]
documents: [wg2-n5310r, wg2-n5340, wg2-n5304, wg2-n5368, wg2-n5354]
topics: [script-encoding-pipeline]
people: [china, wg2]
meetings: [wg2-meeting-72, wg2-meeting-73]
status: proposed
tags: [script, proposal, dai-xaau, tai-xaau, tai-viet, wg2]
timestamp: 2026-07-09T00:00:00+09:00
---

# Dai Xaau Script

## 概要

Dai Xaau / Tai Xaau Script は、Yunnan Province の Jinping Dai community が Jinping dialect of Dai language を記録するために使う abugida script を、UCS / Unicode に独立 script として符号化する proposal chain である。

中心文書は [WG2 N5310R](../documents/wg2-n5310r.md) で、76 characters を proposed repertoire とし、Tai Viet からの disunification を主張する。WG2 \#72 は proposal の progress を note し、authors に継続作業を促した。後続の [WG2 N5368](../documents/wg2-n5368.md) は、Dai Xaau と Dai Viet の差、追加 characters、numerical abbreviations を補足した。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2025-06-16 | WG2 | [WG2 N5310R](../documents/wg2-n5310r.md) | China NB が、76 Tai Xaau characters を UCS に追加する revised proposal を提出し、Tai Viet からの disunification を主張した。 |
| 2025-06-26 | WG2 | [WG2 N5340](../documents/wg2-n5340.md) | Dao Jie / Qi Ziyuan が、WG2 \#72 で Tai Xaau proposal の背景、community recognition、教育・使用例を presentation として示した。 |
| 2025-06-27 | WG2 | [WG2 N5304](../documents/wg2-n5304.md) | WG2 \#72 M72.15 が Dai Xaau proposal の progress を note し、proposal authors に継続作業を促した。 |
| 2026-06-18 | WG2 | [WG2 N5368](../documents/wg2-n5368.md) | China が [WG2 N5310R](../documents/wg2-n5310r.md) の補足として、Dai Xaau / White Dai と Dai Viet / Black Tai の差異、追加文字、numerical abbreviations を説明した。 |

## 主な論点

### Tai Viet からの disunification

`WG2 N5310R` は、Tai Xaau と Tai Viet の一部に似た glyph / sound があることを認めつつ、font style、glyph shape、user identity の差を根拠に、Tai Xaau を Tai Viet の localization ではなく独立 script として扱うべきだとする。特に、既存 Tai Viet code chart glyph や font shapes が Tai Xaau community で認識されない場合があり、common font style が存在しないことを問題にする。

`WG2 N5368` はこの論点を補強し、China の Jin Ping Dai Xaau script (White Dai) と Vietnam の Dai Viet script (Black Tai) は form、sound、meaning に大きな差があると述べる。

### encoding model と visual order

Tai Xaau は pre-base vowel letters を持つため、logical order と visual order の選択が問題になる。`WG2 N5310R` は、Tai Xaau には subjoined consonants がなく、all consonants が base characters として振る舞うことから、visual order を提案する。tone marks や vowel marks の placement variation は、同一 syllable の equivalent sequence として扱う必要がある。

### repertoire の変化

`WG2 N5310R` は 76 characters の complete proposal として提出されたが、`WG2 N5368` は 76 Dai Xaau characters に加え、現代生活上の需要から 10 numerical abbreviations を加える方向を示す。したがって、repertoire は WG2 \#72 時点で確定しておらず、補足資料と後続 review を追う必要がある。

## 関連文書

- [WG2 N5310R](../documents/wg2-n5310r.md)
- [WG2 N5340](../documents/wg2-n5340.md)
- [WG2 N5304](../documents/wg2-n5304.md)
- [WG2 N5368](../documents/wg2-n5368.md)
- [WG2 N5354](../documents/wg2-n5354.md)

## 関連トピック

- [Script Encoding Pipeline](script-encoding-pipeline.md)
- [Script and Notation Proposals](../families/script-and-notation-proposals.md)

## 出典

- `wg2-n5310r` - <https://www.unicode.org/wg2/docs/n5310R-ProposaltoEncodeTaiXaauScript.pdf>
- `wg2-n5340` - <https://www.unicode.org/wg2/docs/n5340-Presentation-ProposalTaiXaauScript.pdf>
- `wg2-n5304` - <https://www.unicode.org/wg2/docs/n5304-Mtg72-Niigata-Recs-rev5-final.pdf>
- `wg2-n5368` - <https://www.unicode.org/wg2/docs/n5368-SupplementaryMaterialsDaiXaauScript.pdf>
