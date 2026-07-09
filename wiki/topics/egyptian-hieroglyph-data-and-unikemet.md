---
type: Topic
title: Egyptian Hieroglyph Data and Unikemet
description: "UAX #57 / Unikemet.txt による Egyptian hieroglyphs の catalog、source、function、Core data の論点。"
slug: egyptian-hieroglyph-data-and-unikemet
bodies: [UTC]
documents: [utc-l2-26-095, utc-l2-26-096, utc-l2-26-107]
topics: [unicode-properties-and-algorithms]
status: draft-uax
tags: [egyptian-hieroglyphs, unikemet, uax57, data-files]
timestamp: 2026-07-09T00:00:00+09:00
---

# Egyptian Hieroglyph Data and Unikemet

## 概要

Egyptian Hieroglyph Data and Unikemet は、Egyptian hieroglyphs の character identity、source references、catalog indexes、function、Core set、mirroring / rotation、alternate sequences を UCD data として扱う論点である。

中心文書は [L2/26-107](../documents/utc-l2-26-107.md) の UAX \#57 Revision 6 proposed update で、`Unikemet.txt` の file format と properties を説明する。

この topic は Egyptian hieroglyph character additions そのものではなく、既符号化文字と Extended-A の algorithmic names を実装・検索・学術参照で扱えるようにする data layer を追う。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2026-04-03 | UTC | [L2/26-095](../documents/utc-l2-26-095.md) | Michelle Perham が PRI \#538 を public review issue 一覧に含めた。 |
| 2026-04-03 | UTC | [L2/26-107](../documents/utc-l2-26-107.md) | Michel Suignard が UAX \#57 Revision 6 proposed update を提出し、Unikemet database と `Unikemet.txt` properties を整理した。 |
| 2026-04-16 | UTC | [L2/26-096](../documents/utc-l2-26-096.md) | PAG が `kEH_FVal` delimiter を `U+007C` に統一する recommendation を記録した。 |

## 主な論点

### algorithmic names を補う identity data

Egyptian Hieroglyphs Extended-A の algorithmic names は code point を示すだけで、sign の形状、source、function を伝えない。Unikemet の `kEH_Cat`、`kEH_UniK`、`kEH_Desc`、source properties は、sign identity を復元する data layer になる。

### source properties と provisional properties

`kEH_HG`、`kEH_JSesh`、`kEH_IFAO` などの source properties は normative parts として扱われる。一方、`kEH_Func`、`kEH_FVal`、`kEH_Core` のような properties は expert review と今後の evidence によって変わり得るため、実装で使うときは stability の違いを意識する必要がある。

### function value syntax

`kEH_FVal` は transliterated text を含み、複数値の区切りに `/` や `|` が関係する。UTC \#187 PAG report は delimiter を `U+007C` に統一する recommendation を出しており、これは data file validation と downstream tooling に直接関わる。

### Core set と font support

`kEH_Core` は、Egyptologists が evidence を確認した Core set を示し、widely used fonts が優先的に実装すべき set の目安になる。Legacy / None の区別は、既符号化文字の互換性と、complex layout scenarios で preferred sequence を使うべきかの判断にも関係する。

## 関連文書

- [L2/26-107](../documents/utc-l2-26-107.md) - UAX \#57 Revision 6 proposed update。
- [L2/26-096](../documents/utc-l2-26-096.md) - `kEH_FVal` delimiter recommendation を含む UTC \#187 PAG report。
- [L2/26-095](../documents/utc-l2-26-095.md) - PRI \#538 を含む Public Review Issues 一覧。

## 関連トピック

- [Unicode Properties and Algorithms](unicode-properties-and-algorithms.md)
- [Text Model and Core Specification](../families/text-model-and-core-specification.md)

## 出典

- `utc-l2-26-107` - <https://www.unicode.org/L2/L2026/26107-uax57-6-update-pri538.pdf>
- `utc-l2-26-096` - <https://www.unicode.org/L2/L2026/26096-pag-report-utc187.pdf>
- `utc-l2-26-095` - <https://www.unicode.org/L2/L2026/26095-public-review-issues.html>
