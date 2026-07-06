---
type: Event
title: WG2 M72.07 J-source glyph revert recommendation
description: "WG2 #72 が WG2 N5296 に基づき J-source glyph changes の revert を勧告した出来事。"
slug: wg2-m72-07-j-source-glyph-revert
kind: event
date: "2025-06-27"
bodies: [WG2]
documents: [wg2-n5296, wg2-n5301, wg2-n5304]
topics: [j-source, irg-source-data-and-representative-glyphs]
people: [japan, wg2, michel-suignard]
meetings: [wg2-meeting-72]
status: adopted
tags: [event, j-source, glyph, recommendation]
timestamp: 2026-07-06T23:30:00+09:00
---

# WG2 M72.07 J-source glyph revert recommendation

## 概要

WG2 Meeting #72 は、`WG2 N5296` の JMJ-source related glyph issues を errata / modification として扱い、Recommendation M72.07 で Project Editor に J-source glyph changes の revert を勧告した。対象は Japan NB の JMJ-source horizontal extension そのものではなく、Code Charts 生成時の font selection 変更によって既存 J-source / JK-source representative glyphs の見え方が変わった部分である。

## 背景

`WG2 N5296` は、CJK Extension C の JK-source characters の一部で HeiseiMincho から IPAmjMincho へ、compatibility block の J-source characters の一部で MS Mincho から IPAmjMincho へ chart glyph の見え方が変わったことを指摘した。文書は、この変更が Japan NB の明示的な要求ではなく、J-source font handling を簡略化しようとした Code Charts 生成側の処理に起因すると整理している。

## 結果

`WG2 N5301` の minutes は、Project Editor が `WG2 N5296` の first part に基づく修正に同意したことを記録する。`WG2 N5304` の Recommendation M72.07 は、`WG2 N5296` に記載された J-source glyph changes を revert するよう Project Editor に勧告した。

## 影響範囲

この event は、J-source / JMJ-source 議論のうち chart glyph stability に関する WG2 側の処理結果である。`kIRG_JSource` value や published encoded characters の disunification を扱う IRG 側の disposition とは分けて読む必要がある。

## 関連ページ

- [J-source and JMJ Source Issues](../topics/j-source.md)
- [IRG Source Data and Representative Glyphs](../topics/irg-source-data-and-representative-glyphs.md)
- [WG2 Meeting #72](../meetings/wg2/meeting-72.md)
- [Japan](../people/japan.md)

## 出典

- `wg2-n5296` - <https://www.unicode.org/wg2/docs/n5296-JMJ-source%20related%20glyph%20issues.pdf>
- `wg2-n5301` - <https://www.unicode.org/wg2/docs/n5301-M72minutes-JP-2025-rev5.pdf>
- `wg2-n5304` - <https://www.unicode.org/wg2/docs/n5304-Mtg72-Niigata-Recs-rev5-final.pdf>
