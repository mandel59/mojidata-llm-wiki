---
type: Topic
title: Arabic Mark Rendering
description: "UAX #53 / AMTRA による Arabic combining marks の rendering order と property data の論点。"
slug: arabic-mark-rendering
bodies: [UTC]
documents: [utc-l2-26-095, utc-l2-26-096, utc-l2-26-106]
topics: [unicode-properties-and-algorithms]
status: draft-uax
tags: [arabic, rendering, combining-marks, uax53, amtra]
timestamp: 2026-07-09T00:00:00+09:00
---

# Arabic Mark Rendering

## 概要

Arabic Mark Rendering は、Arabic combining marks を含む text を、canonical equivalence を保ったまま利用者の期待する mark stacking order で表示するための論点である。

中心文書は [L2/26-106](../documents/utc-l2-26-106.md) の UAX \#53 Revision 12 proposed update で、Arabic Mark Transient Reordering Algorithm (AMTRA)、Modifier Combining Marks (MCM)、CGJ override、dotted circle insertion の扱いを説明する。

この topic は文字追加ではなく、rendering engine、UCD property、normalization、editing behavior の責任分担を見る入口である。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2026-04-03 | UTC | [L2/26-095](../documents/utc-l2-26-095.md) | Michelle Perham が PRI \#539 を public review issue 一覧に含めた。 |
| 2026-04-03 | UTC | [L2/26-106](../documents/utc-l2-26-106.md) | Roozbeh Pournader、Bob Hallissy、Lorna Evans が UAX \#53 Revision 12 proposed update を提出し、AMTRA を Arabic mark rendering の推奨解として整理した。 |
| 2026-04-16 | UTC | [L2/26-096](../documents/utc-l2-26-096.md) | PAG が UTC \#187 向けに Arabic marks の property updates と broader properties / algorithms review を扱った。 |

## 主な論点

### AMTRA は stored text を変更しない

AMTRA は rendering pipeline 内の transient reordering であり、normalization form でも text interchange の変換規則でもない。NFD 相当の ordering を出発点にしつつ、shadda や MCM を base に近づけることで、canonically equivalent な sequences の表示を揃える。

### MCM と将来の property stability

MCM set は、Arabic marks の中でも base を直接修飾する marks を rendering 上区別する。既存文字を後から MCM に加えると既存 data の rendering が変わるため、将来の Arabic combining mark encoding では MCM / ccc / Diacritic property の設計を同時に考える必要がある。

### CGJ と orthography-specific override

default display order が特定 orthography と合わない場合は、CGJ を mark sequence に挟んで AMTRA の reordering を抑制する。これは higher-level markup ではなく plain text 内で例外順序を指定する仕組みであり、normalization と rendering の境界にある。

### dotted circle は validation ではない

Arabic script では、Quranic marks や minority orthographies の有効な組み合わせが rendering engine には invalid に見える場合がある。UAX \#53 は dotted circle insertion を rendering engine の低層 validation に置きすぎることに注意を促す。

## 関連文書

- [L2/26-106](../documents/utc-l2-26-106.md) - UAX \#53 Revision 12 proposed update。
- [L2/26-096](../documents/utc-l2-26-096.md) - UTC \#187 PAG report。
- [L2/26-095](../documents/utc-l2-26-095.md) - PRI \#539 を含む Public Review Issues 一覧。

## 関連トピック

- [Unicode Properties and Algorithms](unicode-properties-and-algorithms.md)
- [Text Model and Core Specification](../families/text-model-and-core-specification.md)

## 出典

- `utc-l2-26-106` - <https://www.unicode.org/L2/L2026/26106-uax53-12-update-pri539.pdf>
- `utc-l2-26-096` - <https://www.unicode.org/L2/L2026/26096-pag-report-utc187.pdf>
- `utc-l2-26-095` - <https://www.unicode.org/L2/L2026/26095-public-review-issues.html>
