---
type: Topic
title: "Japanese Place-Name Ideographs"
description: "日本の地名・登記資料に現れる未符号化漢字を UAX #45 / FutureWS record として扱う UTC proposals。"
slug: japanese-place-name-ideographs
aliases: ["Japanese place-name ideographs", "Japanese place name ideographs", "Japanese place names in UAX #45"]
bodies: [UTC]
documents: [utc-l2-25-053, utc-l2-25-221, utc-l2-26-044, utc-l2-26-099]
topics: [uax45-u-source-ideographs]
people: [japan]
events: [utc-187-uax45-futurews-additions]
status: active
tags: [japan, uax45, place-names, ideographs, futurews]
timestamp: 2026-07-07T22:20:00+09:00
---

# Japanese Place-Name Ideographs

## 概要

Japanese Place-Name Ideographs は、日本の地名・小字名・橋名・登記資料に現れる未符号化漢字を、UTC の UAX \#45 / U-Source Ideographs に追加する一連の提案である。提案文書は、対象文字をすぐに CJK Unified Ideographs に符号化するのではなく、`USourceData.txt` の `FutureWS` record として蓄積し、将来の IRG working set submission へ渡す入口を作る。

この topic の中心は、Tsukada Masaki による `L2/25-053`、`L2/25-221`、`L2/26-044` である。いずれも IDS、radical / stroke data、`kJapanese` reading、UTCHan.ttf 用 representative glyph file を添え、日本国内の公的・準公的資料を evidence とする。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2025-01-30 | UTC | [L2/25-053](../documents/utc-l2-25-053.md) | 兵庫県淡路市の地名に使われる IDS `⿰向鳥` の 1 ideograph を UAX \#45 へ追加する提案。 |
| 2025-10-07 | UTC | [L2/25-221](../documents/utc-l2-25-221.md) | 愛媛県大洲市、大分県竹田市、長崎県五島市の地名・橋名に使われる 3 ideographs を UAX \#45 へ追加する提案。 |
| 2026-01-14 | UTC | [L2/26-044](../documents/utc-l2-26-044.md) | 山形県東根市の複数地名に使われる IDS `⿰山入` の 1 ideograph を UAX \#45 へ追加する提案。 |
| 2026-04-11 | UTC | [L2/26-099](../documents/utc-l2-26-099.md) | [UTC \#187 UAX \#45 FutureWS additions](../events/utc-187-uax45-futurews-additions.md) として、CJK & Unihan Working Group が `L2/26-044` を含む 2026 年の UAX \#45 additions を `FutureWS` status で受け入れるよう勧告した。 |

## 主な論点

### 登記・地名資料を evidence とする UAX \#45 additions

`L2/25-053` と `L2/26-044` は、法務局・登記情報提供サービス由来の公図、旧土地台帳、登記簿・地積測量図を evidence に含める。`L2/25-221` も、古い公図や旧土地台帳に加えて、自治体資料、県公報、国立国会図書館デジタルコレクションの地域資料を根拠にする。

このため、提案の焦点は一般語彙の頻度ではなく、行政・土地権利・地名記録で実在する文字を Unicode / ISO の pipeline にどう渡すかにある。

### 2025 年提案の後続状態

現行 catalog と UTC \#187 minutes の範囲では、`L2/25-053` と `L2/25-221` を受け入れた consensus / action item は確認していない。2026 年 4 月の [UTC \#187 UAX \#45 FutureWS additions](../events/utc-187-uax45-futurews-additions.md) は同じ topic の [L2/26-044](../documents/utc-l2-26-044.md) を `UTC-03661` として受理したが、2025 年提出の 1+3 ideographs はその decision set に含まれない。

そのため、この topic では `L2/25-053` と `L2/25-221` を「submitted / pending」として扱い、採択済みの UAX \#45 record とは分けて読む。

### Hanyo-Denshi で拾われなかった地名文字

`L2/25-053` は、Hanyo-Denshi project（汎用電子情報交換環境整備プログラム）が行政システムで使われる文字を整理した一方、Touki System（登記システム）上のすべての文字を網羅していなかったと説明する。この文脈では、UAX \#45 は日本国内システムに残る地名文字を後から標準化 pipeline へ載せる補助的な入口になっている。

### `kJapanese` reading と IDS による識別

各提案は、未符号化文字そのものを符号位置で参照できないため、IDS と `kJapanese` reading を組み合わせて record を識別する。代表例として、`L2/26-044` は IDS `⿰山入` と readings `はさま` / `はざま`、`L2/25-221` は `⿱投石` / `なげ`、`⿱米𥹫` / `ひとぎ`、`⿰魚久` / `ひさ` を示す。

## 関連文書

- [L2/25-053](../documents/utc-l2-25-053.md)
- [L2/25-221](../documents/utc-l2-25-221.md)
- [L2/26-044](../documents/utc-l2-26-044.md)
- [L2/26-099](../documents/utc-l2-26-099.md)

## 関連出来事

- [UTC \#187 UAX \#45 FutureWS additions](../events/utc-187-uax45-futurews-additions.md)

## 関連トピック

- [UAX \#45 / U-Source Ideographs](uax45-u-source-ideographs.md)
- [Japanese Historical Ideographs](japanese-historical-ideographs.md)
- [Unihan Database Maintenance](unihan-database-maintenance.md)

## 出典

- `utc-l2-25-053` - <https://www.unicode.org/L2/L2025/25053-uax45-japanese-place-name.pdf>
- `utc-l2-25-221` - <https://www.unicode.org/L2/L2025/25221-3ideographs-for-Japanese-place-names.pdf>
- `utc-l2-26-044` - <https://www.unicode.org/L2/L2026/26044-uax45-japanese-place-names.pdf>
- `utc-l2-26-093` - <https://www.unicode.org/L2/L2026/26093.htm>
- `utc-l2-26-099` - <https://www.unicode.org/L2/L2026/26099-cjk-unihan-wg-utc187.pdf>
