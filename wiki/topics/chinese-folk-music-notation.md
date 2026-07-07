---
type: Topic
title: Chinese Folk Music Notation
description: "Chinese folk music / Xiqu / Quyi notation の musical symbols と format controls。"
slug: chinese-folk-music-notation
bodies: [UTC, WG2]
documents: [utc-l2-26-130]
topics: [plain-text-composition-and-overstriking]
status: proposed
tags: [music, notation, xiqu, quyi, format-control]
timestamp: 2026-07-08T00:00:00+09:00
---

# Chinese Folk Music Notation

## 概要

Chinese Folk Music Notation は、Chinese folk music、Chinese Xiqu Opera、Chinese Quyi Show で使われる musical symbols / format controls を扱う topic である。UTC \#188 候補文書 [L2/26-130](../documents/utc-l2-26-130.md) は、1 visible musical symbol と 2 free-repeat format controls を Musical Symbols Supplement block に追加することを提案した。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2026-05-14 | UTC / WG2 | [L2/26-130](../documents/utc-l2-26-130.md) | Eiso Chan が Chinese folk music 用 breath mark と free repeat controls を提案した。 |
| 2026-07-30 | UTC | [UTC Meeting \#188](../meetings/utc/utc-meeting-188.md) | UTC \#188 の agenda / minutes は未掲載だが、UTC \#187 後の候補文書として追跡する。 |

## 主な論点

### musical symbol と format controls

[L2/26-130](../documents/utc-l2-26-130.md) は U+1D282 MUSICAL SYMBOL DOWN ARROWHEAD-SHAPED BREATH MARK を visible symbol とし、U+1D283 / U+1D284 を BEGIN / END FREE REPEAT controls とする。Musical Symbols Supplement は既に format controls を持つため、既存 model と同じ層に入れられるかが review point になる。

### East Asian music notation と plain text

提案は Chinese folk music / Xiqu / Quyi の notation を plain text で保持する必要を主張する。free repeat は layout / rendering の指示にも見えるため、format control と markup の境界を確認する必要がある。

## 関連文書

- [L2/26-130](../documents/utc-l2-26-130.md) - Chinese folk music musical symbol / format controls proposal。

## 関連トピック

- [Plain-Text Composition and Overstriking](plain-text-composition-and-overstriking.md)

## 出典

- `utc-l2-26-130` - <https://www.unicode.org/L2/L2026/26130-chinese-folk-music.pdf>

