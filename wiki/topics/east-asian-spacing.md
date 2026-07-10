---
type: Topic
title: East Asian Spacing
description: "UTR #59 draft が提案する East Asian scripts と Latin / digits などの間の自動 visible spacing algorithm と property data。"
slug: east-asian-spacing
aliases: ["UTR #59", "East_Asian_Spacing"]
bodies: [UTC]
documents: [utc-l2-25-100, utc-l2-26-092, utc-l2-26-096, pri-545, pri-551]
topics: [unicode-properties-and-algorithms, east-asian-quotation-marks]
meetings: [utc-meeting-187]
status: draft-utr
tags: [east-asian, typography, spacing, algorithm, utr59]
timestamp: 2026-07-08T00:00:00+09:00
---

# East Asian Spacing

## 概要

East Asian Spacing は、East Asian scripts と Latin letters / digits などが混在する text で、読みやすさのために薄い visible spacing を自動付与する algorithm と property data の提案である。[L2/25-100](../documents/utc-l2-25-100.md) が Proposed Draft UTR \#59 として登録された。

この topic は、punctuation や quotation marks の code point 追加ではなく、UCD property、language context、layout behavior を使って spacing を調整する text algorithm の論点として扱う。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2025-04-04 | UTC | [L2/25-100](../documents/utc-l2-25-100.md) | Koji Ishii が UTR \#59 draft と `East_Asian_Spacing` property / algorithm を public review document として提出した。 |
| 2026-04-17 | UTC | [L2/26-092](../documents/utc-l2-26-092.md) | UTC \#187 agenda が UTR \#59 を Properties & Algorithms public review issues の一つとして置いた。 |
| 2026-04-16 | UTC | [L2/26-096](../documents/utc-l2-26-096.md) | PAG report が UTC \#187 の properties / algorithms review として UTR \#59 周辺の確認入口になった。 |
| 2026-07-07 | UTC | [PRI \#545](../documents/pri-545.md), [PRI \#551](../documents/pri-551.md) | UAX \#11 East_Asian_Width と UAX \#14 Line Breaking の Unicode 18.0 public review が close し、East Asian layout 周辺 property / algorithm の finalization が UTC \#188 に接続した。 |

## 主な論点

### visible spacing と semantic space

UTR \#59 draft は、East Asian typography で見られる薄い spacing を、可読性のための visible spacing として扱う。`U+0020 SPACE` は semantic boundary を表すため、この目的で本文に挿入することは推奨されない。実装は可能なら text layout process の glyph spacing / kerning に近い調整として扱う。

### `East_Asian_Spacing` property

Property values は `W`、`N`、`O`、`C` である。Algorithm は grapheme cluster ごとに先頭 code point の値を取得し、`C` を language context で解決してから、`W` / `N` の隣接箇所に visible spacing を入れる。

### language context と punctuation

`C` は Chinese context では `N`、それ以外または不明な context では `O` として解決される。括弧や percent sign などの punctuation / symbols は、word boundary を目立たせる spacing practice と、文字どうしの接近を避ける readability practice の両方に関わるため、property data だけで完結しない。

### vertical text と East Asian quotation

Vertical text では upright に表示される `N` characters を spacing 対象から外す。East Asian quotation marks や punctuation の地域差と重なる部分はあるが、quotation mark の文字追加・core spec guidance は [East Asian Quotation Marks](east-asian-quotation-marks.md) に分ける。

### East_Asian_Width / line breaking との境界

[PRI \#545](../documents/pri-545.md) の UAX \#11 は `East_Asian_Width` property、[PRI \#551](../documents/pri-551.md) の UAX \#14 は line breaking algorithm を扱う。どちらも East Asian layout の input になるが、UTR \#59 の `East_Asian_Spacing` property とは別の specification layer である。

## 関連文書

- [L2/25-100](../documents/utc-l2-25-100.md) - Proposed Draft UTR \#59, East Asian Spacing。
- [L2/26-092](../documents/utc-l2-26-092.md) - UTC \#187 Agenda。
- [L2/26-096](../documents/utc-l2-26-096.md) - UTC \#187 PAG report。
- [PRI \#545](../documents/pri-545.md) - UAX \#11 East Asian Width Revision 45 public review。
- [PRI \#551](../documents/pri-551.md) - UAX \#14 Unicode Line Breaking Algorithm Revision 56 public review。

## 関連トピック

- [Unicode Properties and Algorithms](unicode-properties-and-algorithms.md)
- [East Asian Quotation Marks](east-asian-quotation-marks.md)

## 出典

- `utc-l2-25-100` - <https://www.unicode.org/L2/L2025/25100-utr59-1-draft-pri510.pdf>
- `utc-l2-26-092` - <https://www.unicode.org/L2/L2026/26092.htm>
- `utc-l2-26-096` - <https://www.unicode.org/L2/L2026/26096-pag-report-utc187.pdf>
- `pri-545` - <https://www.unicode.org/review/pri545/>
- `pri-551` - <https://www.unicode.org/review/pri551/>
