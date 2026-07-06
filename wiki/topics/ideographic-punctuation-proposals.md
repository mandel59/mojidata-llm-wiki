---
type: Topic
title: Ideographic Punctuation Proposals
description: Ideographic Symbols and Punctuation block 周辺の句読点追加提案。
slug: ideographic-punctuation-proposals
kind: topic
bodies: [UTC, WG2]
documents: [utc-l2-26-133, utc-l2-26-136]
status: active
tags: [punctuation, ideographic, cjk]
timestamp: 2026-07-07T00:00:00+09:00
---

# Ideographic Punctuation Proposals

## 概要

Ideographic Punctuation Proposals は、CJK / ideographic text で使われる句読点・記号の追加提案を扱う topic である。既存の U+3001 IDEOGRAPHIC COMMA、U+3002 IDEOGRAPHIC FULL STOP、U+FE46 WHITE SESAME DOT、semicolon などで代用できるか、plain text semantics と glyph variation をどう分けるかが主な論点になる。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2026-06-08 | UTC / WG2 | `L2/26-133` | DOUBLE IDEOGRAPHIC FULL STOP と 2 つの standardized variants を提案。 |
| 2026-06-09 | UTC | `L2/26-136` | WHITE IDEOGRAPHIC COMMA を提案。 |

## 主な論点

### double ideographic full stop

`L2/26-133` は DOUBLE IDEOGRAPHIC FULL STOP を U+16FE6 として Ideographic Symbols and Punctuation block に置く案で、corner-justified form と centered form の standardized variants も提案した。用途は Cantonese Yueju Opera / Yuequ Show の performance scripts / librettos における upper / lower sentence marking であり、U+3002 IDEOGRAPHIC FULL STOP 2 文字の代用では plain text semantics を保てないとする。

### white ideographic comma

`L2/26-136` は WHITE IDEOGRAPHIC COMMA を U+16FE5 として提案する。これは日本語の shiroten / shiro-goma ten に対応する inline punctuation で、U+3001、U+FE46、semicolon とは機能が異なると整理している。known usage は主に明治期日本語資料と後年の scholarly / literary editions であり、検索、引用、校訂、デジタルアーカイブで plain-text representation が必要とされる。

## 関連文書

- `L2/26-133` - double ideographic full stop proposal。
- `L2/26-136` - WHITE IDEOGRAPHIC COMMA proposal。

## 関連トピック

- [Han Ideographic Scripts](../families/han-ideographic-scripts.md)

## 出典

- `utc-l2-26-133` - <https://www.unicode.org/L2/L2026/26133-dbl-ideo-fs.pdf>
- `utc-l2-26-136` - <https://www.unicode.org/L2/L2026/26136-white-ideographic-comma.pdf>
