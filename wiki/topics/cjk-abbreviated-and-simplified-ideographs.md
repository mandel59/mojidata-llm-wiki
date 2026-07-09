---
type: Topic
title: CJK Abbreviated and Simplified Ideographs
description: "UAX #45 additions として扱われた CJK abbreviated / simplified ideograph forms の proposal chain。"
slug: cjk-abbreviated-and-simplified-ideographs
bodies: [UTC]
documents: [utc-l2-26-057, utc-l2-26-064, utc-l2-26-071, utc-l2-26-083, utc-l2-26-085, utc-l2-26-099]
topics: [uax45-u-source-ideographs, cjk-multi-syllabic-and-abbreviation-characters, japanese-historical-ideographs]
events: [utc-187-uax45-futurews-additions]
status: active
tags: [cjk, abbreviation, simplified-forms, uax45, futurews]
timestamp: 2026-07-09T00:00:00+09:00
---

# CJK Abbreviated and Simplified Ideographs

## 概要

CJK abbreviated and simplified ideographs は、正式な現代 standard simplification に限らず、近現代の略字、俗簡字、Ryakuji、repeated component shorthand、unit / term abbreviation などとして実用された Han-only forms を、UAX \#45 `FutureWS` records として扱う論点である。

この topic は、script-hybrid かどうかを論じる [CJK Multi-Syllabic and Abbreviation Characters](cjk-multi-syllabic-and-abbreviation-characters.md) とは別に、UAX \#45 additions として提出された abbreviated / simplified ideograph forms の evidence と intake を追う。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2026-01-19 | UTC | [L2/26-057](../documents/utc-l2-26-057.md) | 8 ideographs のうち、炎 / 品 abbreviated forms などが UAX \#45 additions として提案された。 |
| 2026-02-05 | UTC | [L2/26-064](../documents/utc-l2-26-064.md) | 译 / 訳 / 譯 variant 系の non-standard simplified form 1 字が提案された。 |
| 2026-02-25 | UTC | [L2/26-071](../documents/utc-l2-26-071.md) | 涨 / 張 / 临 系の common simplified forms 3 字が提案された。 |
| 2026-03-24 | UTC | [L2/26-083](../documents/utc-l2-26-083.md) | 蠱、談、綴、等、衆に関係する simplified / abbreviated forms 5 字が提案された。 |
| 2026-03-27 | UTC | [L2/26-085](../documents/utc-l2-26-085.md) | 風、姦、磊、鑷、發 の abbreviated variants 5 字が提案された。 |
| 2026-04-11 | UTC | [L2/26-099](../documents/utc-l2-26-099.md) | CJK & Unihan Working Group が 2026 年 UAX \#45 additions を `FutureWS` records として受け入れるよう勧告した。 |

## 主な論点

### Han-only abbreviated forms と script-hybrid の境界

この topic の対象は、components が Han script domain に留まる abbreviated / simplified ideographs である。Latin、Kana、Hangul など非 Han component を含む script-hybrid characters とは分けて読む必要がある。

### evidence の地域横断性

2026 年の UAX \#45 additions では、中国の character reform / 俗簡字資料、日本の Ryakuji / 近代資料、米軍の日本語資料、ソ連の辞書、方块瑶字研究などが evidence として使われる。略字・簡体字形は地域・時代ごとに形が揺れるため、proposal は normalized glyph と variant evidence の関係を明示する必要がある。

### UAX \#45 record と将来 IRG review

これらの proposal は、ただちに CJK Unified Ideographs に符号化する最終決定ではなく、UTC source records として UAX \#45 に置き、将来の IRG working set submission へ渡す候補を整理する段階である。

## 関連文書

- [L2/26-057](../documents/utc-l2-26-057.md)
- [L2/26-064](../documents/utc-l2-26-064.md)
- [L2/26-071](../documents/utc-l2-26-071.md)
- [L2/26-083](../documents/utc-l2-26-083.md)
- [L2/26-085](../documents/utc-l2-26-085.md)
- [L2/26-099](../documents/utc-l2-26-099.md)

## 関連トピック

- [UAX \#45 / U-Source Ideographs](uax45-u-source-ideographs.md)
- [CJK Multi-Syllabic and Abbreviation Characters](cjk-multi-syllabic-and-abbreviation-characters.md)
- [Japanese Historical Ideographs](japanese-historical-ideographs.md)

## 出典

- `utc-l2-26-057` - <https://www.unicode.org/L2/L2026/26057-additions-uax45.pdf>
- `utc-l2-26-064` - <https://www.unicode.org/L2/L2026/26064-ideograph-proposal.pdf>
- `utc-l2-26-071` - <https://www.unicode.org/L2/L2026/26071-3-ideographs.pdf>
- `utc-l2-26-083` - <https://www.unicode.org/L2/L2026/26083-5-ideographs.pdf>
- `utc-l2-26-085` - <https://www.unicode.org/L2/L2026/26085-uax45-abbr.pdf>
- `utc-l2-26-099` - <https://www.unicode.org/L2/L2026/26099-cjk-unihan-wg-utc187.pdf>
