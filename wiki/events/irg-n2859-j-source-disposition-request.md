---
type: Event
title: IRG N2859 J-source disposition request
description: IRG Convenor が J-source representative glyph / source reference issues の disposition をまとめ、Japan NB に feedback を求めた出来事。
slug: irg-n2859-j-source-disposition-request
date: "2025-08-13"
bodies: [IRG]
documents: [irg-n2859]
topics: [j-source, irg-source-data-and-representative-glyphs]
people: [japan, irg]
status: feedback-requested
tags: [event, j-source, source-data, representative-glyph]
timestamp: 2026-07-06T23:30:00+09:00
---

# IRG N2859 J-source disposition request

## 概要

`IRG N2859` は、IRG Convenor が J-source representative glyph と source reference に関する複数の issue を disposition 案として整理し、Japan NB に feedback を求めた出来事である。対象には `kIRG_JSource` property value、representative glyph、`kJapanese`、`kMojiJoho`、`kMorohashi` への影響が含まれる。

## 背景

この disposition は、`IRG N2676`、`IRG N2722`、`IRG N2780`、`IRG N2846` などで指摘された J-source / JMJ-source issues を受けたものである。WG2 側の M72.07 が chart glyph の revert を扱ったのに対し、`IRG N2859` は source reference と Unihan data maintenance に踏み込んだ整理である。

## 結果

`IRG N2859` は、U+2A50D、U+5CC0、U+72CA、U+26B20 などについて、J-source data の修正案や no action 案を並べた。Japan NB には 2025-09-26 までの feedback が求められた。

## 影響範囲

この event は、J-source の post-encoding correction と符号化済み文字の安定性の境界を扱う。後続の `IRG N2870` で Japan NB は published encoded characters の current status 維持を求めたため、`IRG N2859` は J-source disposition 議論の分岐点として参照する。

## 関連ページ

- [J-source and JMJ Source Issues](../topics/j-source.md)
- [IRG Source Data and Representative Glyphs](../topics/irg-source-data-and-representative-glyphs.md)
- [Japan](../people/japan.md)
- [IRG](../people/irg.md)

## 出典

- `irg-n2859` - <https://www.unicode.org/irg/docs/n2859-JapanRecommendations.pdf>
