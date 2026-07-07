---
type: Topic
title: Kana
description: "仮名の追加符号化、歴史的仮名、変体仮名、小書き仮名、合略仮名、Unihan kJapanese readings を追跡する topic。"
slug: kana
bodies: [UTC, WG2]
documents: [utc-l2-08-358, utc-l2-17-091, utc-l2-22-181, utc-l2-24-150, utc-l2-24-279, utc-l2-25-035, utc-l2-25-036, utc-l2-25-042, utc-l2-25-060, utc-l2-25-151r, utc-l2-25-213]
status: active
tags: [kana, hiragana, katakana, hentaigana, unihan]
timestamp: 2026-07-07T00:00:00+09:00
---

# Kana

## 概要

Kana は、Hiragana / Katakana / Hentaigana / Small Kana Extension / Kana Extended-A などに関わる仮名の標準化議論を束ねる topic である。近年の論点は、歴史的資料を写すための合略仮名（合字的な kana ligatures）、小書き仮名、明治期の alternate Katakana、Unihan `kJapanese` readings の仮名表記に分かれる。

この topic では、仮名文字・仮名由来文字・仮名を使う表記体系に関わる Unicode / ISO/IEC 10646 上の論点を扱う。日本語史資料に限らず、Ryukyuan languages の superscript Katakana や Taiwanese Kana なども kana usage として関連するが、個別の大きな proposal は別 topic に分ける余地がある。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 1999-07-15 | UTC | `L2/99-238` | JCS Committee が JIS X 0213 系の非漢字追加として、linguistic signs、dentist signs、enclosed numbers、publishing signs、Katakana などを UTC に提出。 |
| 1999-09-13 | WG2 | `WG2 N2092` | Japan NB が kana / punctuation を含む 48 characters の追加を WG2 に提出。 |
| 2008-01-14 | UTC / WG2 | `L2/07-421` / `WG2 N3388` | Nozomu Katō が YE に関する 2 kana characters の符号化を提案。 |
| 2008-02-28 | UTC / WG2 | `L2/08-117` / `WG2 N3394` | UTC / L2 が Japan NB に review を求め、個別符号化か obsolete kana / hentaigana の大きな枠組みで扱うかを論点化。 |
| 2008-10-14 | UTC / WG2 | `L2/08-358` / `WG2 N3528` | Japan NB が HIRAGANA LETTER YE は支持し、KATAKANA LETTER ORIGINAL E は時点では反対と回答。YE と hentaigana を混同しないことを求めた。 |
| 2015-12-15 | UTC | `L2/15-343` | Japan NB が Hentaigana revised proposal を提出。phonetic value と mother ideograph に基づく命名・統合の整理を示す。 |
| 2016-07-15 | UTC | `L2/16-188` | Japan NB が Hentaigana revised repertoire を提出。後の Kana Supplement / Kana Extended-A の変体仮名符号化に接続する。 |
| 2017-04-07 | UTC / WG2 | `L2/17-091` / `WG2 N4826` | Japan NB が Small Kana Characters に関する contribution を提出。PDAM 1.2 の 9 small kana だけを選ぶ根拠が不明で、より広い repertoire または modifier model を検討すべきと主張。 |
| 2019-11-21 | UTC | `L2/19-381` | Missing Kana の符号化提案。 |
| 2019-11-22 | UTC | `L2/19-382` | Late Middle Japanese transcription 用 kana character の提案。 |
| 2022-08-23 | UTC | `L2/22-181` | Ken Lunde が provisional Unihan property `kJapanese` を提案。Moji Jōhō Kiban に基づき、readings を hiragana / katakana で表す property とする。 |
| 2023-04-25 | UTC | `L2/23-112` | Gen Kojitani が missing kana ligatures を広く提案。合略仮名を複数 kana の単なる連綿と区別する criteria を提示。 |
| 2023-05-31 | UTC | `L2/23-127` | Eiso Chan が明治期資料に現れる alternate Katakana NE / WI を紹介。 |
| 2024-06-21 | UTC | `L2/24-150` | [L2/24-150](../documents/utc-l2-24-150.md) が `L2/23-112` を reduced set として改訂し、3 kana ligatures を提案。 |
| 2024-12-31 | UTC | `L2/24-279` | [L2/24-279](../documents/utc-l2-24-279.md) が KATAKANA DIGRAPH YORI を追加提案。 |
| 2025-01-13 | UTC | `L2/25-035` | [L2/25-035](../documents/utc-l2-25-035.md) が small kana と Bopomofo small letters の Vertical Orientation value 変更を要請。 |
| 2025-01-15 | UTC | `L2/25-036` | [L2/25-036](../documents/utc-l2-25-036.md) が KATAKANA LETTER SMALL ARCHAIC YE を提案。昭和期の Micronesian / Marshallese transliteration 資料を根拠とする。 |
| 2025-01-16 / 2025-02-24 | UTC | `L2/25-042`, `L2/25-060` | [L2/25-042](../documents/utc-l2-25-042.md) と [L2/25-060](../documents/utc-l2-25-060.md) が KATAKANA LETTER SMALL NE を提案し、広告・看板・表紙資料の attestations を追加。 |
| 2025-05-23 | UTC | `L2/25-151R` | [L2/25-151R](../documents/utc-l2-25-151r.md) が KATAKANA LETTER ALTERNATE NE / WI を提案。明治期活字・教科書資料を根拠とし、current Katakana / Hentaigana との統合不可を主張。 |
| 2025-08-19 | UTC | `L2/25-213` | [L2/25-213](../documents/utc-l2-25-213.md) が Unihan `kJapanese` に含まれる Katakana kun'yomi を調査し、property value / definition の修正を提案。 |

## 主な論点

### YE と hentaigana の境界

`L2/07-421` / `WG2 N3388` は、historical Japanese の /e/ と /ye/ の区別を扱うために HIRAGANA LETTER YE と KATAKANA LETTER ORIGINAL E を提案した。UTC / L2 は `L2/08-117` で Japan NB review を求め、Japan NB は `L2/08-358` で HIRAGANA LETTER YE には賛成したが、KATAKANA LETTER ORIGINAL E にはさらなる調査が必要だとして反対した。

重要なのは、Japan NB が YE の追加を hentaigana 一般の符号化とは別問題として扱うよう求めた点である。江（U+6C5F）由来の字形は hentaigana とも重なるため、歴史的音価 /ye/ を表す文字なのか、既存 hiragana え の異体字なのかを区別する必要があった。

### 変体仮名の repertoire と統合基準

Japan NB の `L2/15-343` と `L2/16-188` は、Hentaigana を phonetic value と mother ideograph で整理する。たとえば 江、衣、盈、縁、要などを母字とする E 系 hentaigana は同じ現代仮名「え」に対応し得るが、字形・母字・文献用途は異なる。

この系譜は、単に未符号化 kana を増やす話ではなく、歴史資料を plain text でどこまで再現するか、glyph variation と encoded character の境界をどう決めるかという問題である。

### 小書き仮名の model

`L2/17-091` は Small Kana Characters に対する Japan NB の慎重な立場を示す。Japan NB は、近代日本語資料の調査で PDAM に含まれない多数の small kana usage が見つかること、9 文字だけを選ぶ根拠が不明であること、全 kana に対応する小書き字を符号化するのか modifier 的な方式を考えるのかを検討すべきことを述べた。

2025 年の `L2/25-036` と `L2/25-042` / `L2/25-060` はこの問題の続きにある。前者は KATAKANA LETTER SMALL ARCHAIC YE、後者は現代的・表示的な small NE の usage を根拠にするため、同じ Small Kana Extension でも「歴史的 transcription」と「現代の書体・広告表現」の証拠評価が異なる。

### 合略仮名と vertical-only implication

`L2/23-112` と `L2/24-150` は、合略仮名を複数 kana の sequence ではなく、単一文字として扱う条件を整理する。`L2/24-150` は、手書き縦書き資料の連綿と、活字資料で単一文字として印刷された合略仮名を区別し、reduced set として 3 文字を提案した。

`L2/24-279` は、その流れから漏れた KATAKANA DIGRAPH YORI を再提案する文書である。CJK & Unihan WG が hiragana ligatures には vertical-only implication への懸念を持ちつつ、katakana ligatures にはより前向きだった、という整理を根拠にしている。

### alternate Katakana NE / WI

`L2/23-127` と `L2/25-151R` は、明治期活字・教科書資料に現れる current Katakana とは別字形の NE / WI を扱う。提案は KATAKANA LETTER ALTERNATE NE と KATAKANA LETTER ALTERNATE WI を Kana Extended-A に置くことを求め、子（U+5B50）由来の NE、井（U+4E95）由来の WI と説明する。

この提案は Hentaigana とも関係するが、Katakana repertoire の歴史的字種として扱う点が特徴である。`L2/25-151R` は、これらを current Katakana NE / WI や Hentaigana と統合できないと主張し、同時に 子 / 井 との confusable pair として扱う必要にも触れている。

### Unihan kJapanese と kana readings

`L2/22-181` は `kJapanese` を Moji Jōhō Kiban 由来の Japanese readings property として提案し、hiragana は概ね kun'yomi（訓読み）、katakana は概ね on'yomi（音読み）と説明した。`L2/25-213` は、この説明には例外があり、Katakana で表記された kun'yomi が存在すると指摘する。

この論点は kana character encoding ではなく Unihan data maintenance だが、仮名表記を機械可読データに落とす際の基準に関わる。[Unihan Database Maintenance](unihan-database-maintenance.md) と併せて追跡する。

## 関連文書

- [L2/24-150](../documents/utc-l2-24-150.md) - missing three Kana-Ligatures。
- [L2/24-279](../documents/utc-l2-24-279.md) - KATAKANA DIGRAPH YORI。
- [L2/25-035](../documents/utc-l2-25-035.md) - small kana / Bopomofo small letters の Vertical Orientation。
- [L2/25-036](../documents/utc-l2-25-036.md) - KATAKANA LETTER SMALL ARCHAIC YE。
- [L2/25-042](../documents/utc-l2-25-042.md) / [L2/25-060](../documents/utc-l2-25-060.md) - KATAKANA LETTER SMALL NE。
- [L2/25-151R](../documents/utc-l2-25-151r.md) - KATAKANA LETTER ALTERNATE NE / WI。
- [L2/25-213](../documents/utc-l2-25-213.md) - Katakana kun'yomi in Unihan `kJapanese`。

## 関連トピック

- [CJK Hybrid Characters](cjk-hybrid-characters.md)
- [Unihan Database Maintenance](unihan-database-maintenance.md)
- [CJK Security Confusables](cjk-security-confusables.md)

## 出典

- `utc-l2-07-421` - <https://www.unicode.org/L2/L2007/07421-e-ye.pdf>
- `utc-l2-08-117` - <https://www.unicode.org/L2/L2008/08117-kana-letter.pdf>
- `utc-l2-08-358` - <https://www.unicode.org/L2/L2008/08358-n3528.pdf>
- `utc-l2-15-343` - <https://www.unicode.org/L2/L2015/15343-hentaigana-revised.pdf>
- `utc-l2-16-188` - <https://www.unicode.org/L2/L2016/16188-rev-hentaigana-rep.pdf>
- `utc-l2-17-091` - <https://www.unicode.org/L2/L2017/17091-sc2-n4523-small-kana.pdf>
- `utc-l2-22-181` - <https://www.unicode.org/L2/L2022/22181-unihan-kjapanese.pdf>
- `utc-l2-23-112` - <https://www.unicode.org/L2/L2023/23112-missing-kana-ligatures.pdf>
- `utc-l2-23-127` - <https://www.unicode.org/L2/L2023/23127-katakana.pdf>
- `utc-l2-24-150` - <https://www.unicode.org/L2/L2024/24150-three-kana-ligatures.pdf>
- `utc-l2-24-279` - <https://www.unicode.org/L2/L2024/24279-proposal-to-encode-kana-ligature.pdf>
- `utc-l2-25-035` - <https://www.unicode.org/L2/L2025/25035-vo-small-kana-and-bopomofo.pdf>
- `utc-l2-25-036` - <https://www.unicode.org/L2/L2025/25036-encode-one-small-kana.pdf>
- `utc-l2-25-042` - <https://www.unicode.org/L2/L2025/25042-katakana-letter-small-ne.pdf>
- `utc-l2-25-060` - <https://www.unicode.org/L2/L2025/25060-katakana-letter-small-ne.pdf>
- `utc-l2-25-151r` - <https://www.unicode.org/L2/L2025/25151r-katakana-ne-wi.pdf>
- `utc-l2-25-213` - <https://www.unicode.org/L2/L2025/25213-katakana_kun-yomi.pdf>
