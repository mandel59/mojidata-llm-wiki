---
type: Topic
title: Plain-Text Composition and Overstriking
description: "COMPOSE character、overstriking、format controls と Unicode text model の境界。"
slug: plain-text-composition-and-overstriking
bodies: [UTC, WG2]
documents: [utc-l2-26-130, utc-l2-26-139]
topics: [unicode-properties-and-algorithms]
status: proposed
tags: [text-model, compose, overstriking, format-control, security]
timestamp: 2026-07-08T00:00:00+09:00
---

# Plain-Text Composition and Overstriking

## 概要

Plain-Text Composition and Overstriking は、Unicode plain text がどこまで glyph composition / format controls を持つべきかを扱う topic である。UTC \#188 候補文書では [L2/26-139](../documents/utc-l2-26-139.md) が general-purpose COMPOSE character を提案し、[L2/26-130](../documents/utc-l2-26-130.md) が music notation の BEGIN / END FREE REPEAT controls を提案している。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2026-05-14 | UTC / WG2 | [L2/26-130](../documents/utc-l2-26-130.md) | Chinese folk music notation 用の visible symbol と free repeat format controls が提案された。 |
| 2026-06-09 | UTC | [L2/26-139](../documents/utc-l2-26-139.md) | General-purpose COMPOSE character が提案された。 |

## 主な論点

### overstriking は plain text か

[L2/26-139](../documents/utc-l2-26-139.md) は typewriter overstriking や APL practice を根拠に、COMPOSE を plain-text transformation として扱う。一方、任意の glyph composition は confusability、search、normalization、grapheme cluster、font shaping に広く影響する。

### domain-specific controls

[L2/26-130](../documents/utc-l2-26-130.md) は music notation の free repeat を domain-specific format controls として提案する。既存 Musical Symbols controls との整合がある一方、controls の追加は rendering instruction と encoded semantics の境界を明確にする必要がある。

## 関連文書

- [L2/26-139](../documents/utc-l2-26-139.md) - COMPOSE proposal。
- [L2/26-130](../documents/utc-l2-26-130.md) - Chinese folk music format controls。

## 関連トピック

- [Unicode Properties and Algorithms](unicode-properties-and-algorithms.md)
- [Chinese Folk Music Notation](chinese-folk-music-notation.md)

## 出典

- `utc-l2-26-139` - <https://www.unicode.org/L2/L2026/26139-compose.pdf>
- `utc-l2-26-130` - <https://www.unicode.org/L2/L2026/26130-chinese-folk-music.pdf>

