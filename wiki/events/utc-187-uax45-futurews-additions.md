---
type: Event
title: "UTC #187 UAX #45 FutureWS additions"
description: "CJK & Unihan Working Group が UTC #187 向け recommendations で UAX #45 additions を FutureWS records として受け入れるよう勧告した出来事。"
slug: utc-187-uax45-futurews-additions
date: "2026-04-11"
bodies: [UTC]
documents: [utc-l2-26-044, utc-l2-26-099]
topics: [uax45-u-source-ideographs, japanese-place-name-ideographs]
people: [japan]
meetings: [utc-meeting-187]
status: adopted
tags: [event, utc, uax45, futurews, ideographs]
timestamp: 2026-07-07T22:45:00+09:00
---

# UTC #187 UAX #45 FutureWS additions

## 概要

`L2/26-099` は、UTC #187 向けの CJK & Unihan Working Group recommendations として、2026 年に提出された UAX #45 additions を `USourceData.txt` / `USourceGlyphs.pdf` の `FutureWS` records として受け入れるよう勧告した。

この event は、個別 proposal が提案した文字そのものではなく、UTC CJK & Unihan Working Group が UAX #45 additions を data update / future IRG working set pipeline へ接続した decision point を表す。

## 背景

UAX #45 additions は、未符号化 ideographs を UTC source records として保持し、将来の IRG working set submission に渡すための入口である。`L2/26-044` は、日本の山形県東根市の地名に使われる IDS `⿰山入` の 1 ideograph を UAX #45 に追加する提案であり、この recommendation bundle に含まれる日本関係 proposal の一例である。

## 結果

`L2/26-099` は、対象 records を `FutureWS` status で UAX #45 data に追加する action item を置いた。これにより、個別 proposal の内容は UTC source data の更新対象になり、将来の CJK working set submission へ進む候補として扱われる。

## 影響範囲

[Japanese Place-Name Ideographs](../topics/japanese-place-name-ideographs.md) では、`L2/26-044` の提案内容とこの event を分けて扱う。proposal page は対象文字・evidence・proposed record を説明し、採択・data update 側の概要はこの event に集約する。

## 関連ページ

- [L2/26-044](../documents/utc-l2-26-044.md)
- [L2/26-099](../documents/utc-l2-26-099.md)
- [UAX #45 U-Source Ideographs](../topics/uax45-u-source-ideographs.md)
- [Japanese Place-Name Ideographs](../topics/japanese-place-name-ideographs.md)
- [UTC Meeting #187](../meetings/utc/utc-meeting-187.md)

## 出典

- `utc-l2-26-044` - <https://www.unicode.org/L2/L2026/26044-uax45-japanese-place-names.pdf>
- `utc-l2-26-099` - <https://www.unicode.org/L2/L2026/26099-cjk-unihan-wg-utc187.pdf>
