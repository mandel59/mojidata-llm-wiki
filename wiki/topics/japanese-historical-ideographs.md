---
type: Topic
title: "Japanese Historical Ideographs"
description: "日本の古典籍・近世近代資料に現れる未符号化漢字を UTC / CJK 標準化の対象として扱う論点。"
slug: japanese-historical-ideographs
aliases: ["Japanese ancient book ideographs", "Japanese historical book ideographs"]
bodies: [UTC]
documents: [utc-l2-25-274, utc-l2-26-093]
topics: [japanese-place-name-ideographs, uax45-u-source-ideographs]
people: [japan]
status: active
tags: [japan, historical, ideographs, books, cjk]
timestamp: 2026-07-07T22:20:00+09:00
---

# Japanese Historical Ideographs

## 概要

Japanese Historical Ideographs は、日本の古典籍・近世近代資料に現れる未符号化漢字を、UTC / CJK 標準化の候補として扱う topic である。地名・登記資料に基づく [Japanese Place-Name Ideographs](japanese-place-name-ideographs.md) と異なり、ここでは歴史資料・版本・研究分野での安定した使用を evidence とする。

現時点の中心文書は `L2/25-274` である。同文書は、江戸後期の日本の学者 Ikuta Kunihide（生田国秀）による `古学二千文` などに現れる IDS `⿰犭華` の 1 ideograph を提案し、`kJapanese` reading と複数資料での glyph stability を示す。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2025-12-19 | UTC | [L2/25-274](../documents/utc-l2-25-274.md) | Lin Anning が、日本古典籍で使われる IDS `⿰犭華` の 1 ideograph 追加を提案した。 |

## 主な論点

### 地名文字とは異なる evidence

`L2/25-274` の evidence は、土地登記や行政地名ではなく、`古学二千文` の版本、明治期資料、国立公文書館資料に基づく。文書は、同一 glyph が複数資料に現れることから、研究分野で扱う価値のある安定した字形と位置づける。

### `kJapanese` と歴史資料の読み

提案文字は IDS `⿰犭華`、`kJapanese` reading `クワハ` として提示される。これは現代行政用文字ではなく、江戸後期・明治期の資料読解で必要になる歴史的な Japanese reading data として扱う必要がある。

### UAX \#45 topic との関係

`L2/25-274` の registry subject は UAX \#45 additions ではないが、未符号化 CJK ideograph を evidence、IDS、reading、stroke data とともに UTC へ提出する点で UAX \#45 / FutureWS 系の提案と近い。今後、同種の日本古典籍由来文字が増える場合は、UAX \#45 records へ入るものと、直接符号化提案として扱われるものを分けて追跡する必要がある。

### 後続 review の確認状況

現行 catalog と UTC \#187 minutes の範囲では、`L2/25-274` を受け入れた consensus / action item は確認していない。UTC \#187 で処理された UAX \#45 FutureWS additions は 2026 年提出の文書群に限られており、この historical ideograph proposal は pending proposal として扱う。

## 関連文書

- [L2/25-274](../documents/utc-l2-25-274.md)
- `L2/26-093` - UTC \#187 meeting minutes。

## 関連トピック

- [Japanese Place-Name Ideographs](japanese-place-name-ideographs.md)
- [UAX \#45 / U-Source Ideographs](uax45-u-source-ideographs.md)
- [Unihan Database Maintenance](unihan-database-maintenance.md)

## 出典

- `utc-l2-25-274` - <https://www.unicode.org/L2/L2025/25274-japanese-ideograph-addition.pdf>
- `utc-l2-26-093` - <https://www.unicode.org/L2/L2026/26093.htm>
