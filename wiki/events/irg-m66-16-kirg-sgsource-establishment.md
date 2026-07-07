---
type: Event
title: IRG M66.16 kIRG_SGSource establishment
description: "IRG #66 Recommendation M66.16 が kIRG_SGSource の establishment と GS prefix の SG source への移行を勧告した出来事。"
slug: irg-m66-16-kirg-sgsource-establishment
date: "2026-03-19"
bodies: [IRG]
documents: [irg-n2909, irg-n2926]
topics: [kirg-sgsource, irg-source-data-and-representative-glyphs]
people: [irg, wg2, eiso-chan]
meetings: [irg-meeting-66]
status: adopted
tags: [event, unihan, source-data, singapore]
timestamp: 2026-07-06T23:50:00+09:00
---

# IRG M66.16 kIRG_SGSource establishment

## 概要

IRG Meeting \#66 Recommendation M66.16 は、new normative `kIRG_SGSource` property を establish し、既存の `GS` prefix を `SG` source へ移すことを勧告した出来事である。根拠文書は [IRG N2926](../documents/irg-n2926.md) である。

## 背景

[IRG N2926](../documents/irg-n2926.md) は、Singapore characters が `kIRG_GSource` の中に `GS` prefix として置かれていることを問題にした。Singapore が IRG encoding work に参加していない状態で、GS-source glyph issues を誰が処理するかが曖昧になるため、Singapore 専用 source property として `kIRG_SGSource` を設ける案が出された。

## 結果

M66.16 は `kIRG_SGSource` の establishment と `GS` prefix の `SG` source への移行を勧告し、IRG Convenor が WG2 \#73 へ提出する follow-up につながった。Meeting \#67 agenda `IRG N2935` は、WG2 と SC2 が受け入れ、Unicode Version 19.0 target としている current status を記録する。

## 影響範囲

この event は、Singapore characters を G-source から分離する source data governance の変更として扱う。個別 glyph issue である U+48B4 / GS-2151 の扱いは、source data and representative glyphs topic とあわせて追跡する。

## 関連ページ

- [kIRG_SGSource](../topics/kirg-sgsource.md)
- [IRG Source Data and Representative Glyphs](../topics/irg-source-data-and-representative-glyphs.md)
- [IRG Meeting \#66](../meetings/irg/irg-meeting-66.md)
- [IRG](../people/irg.md)
- [WG2](../people/wg2.md)
- [Eiso Chan](../people/eiso-chan.md)

## 出典

- `irg-n2909` - <https://www.unicode.org/irg/docs/n2909-Recommendations.pdf>
- `irg-n2926` - <https://www.unicode.org/irg/docs/n2926-SGSource.pdf>
- `irg-n2935` - <https://www.unicode.org/irg/docs/n2935-ScheduleAgenda.html>
