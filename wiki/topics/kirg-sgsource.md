---
type: Topic
title: kIRG_SGSource
description: Singapore characters を kIRG_GSource から分離する normative IRG source property 提案。
slug: kirg-sgsource
bodies: [IRG, WG2, UTC]
documents: [irg-n2909, irg-n2926, irg-n2935, wg2-n5354, wg2-n5359]
status: accepted-for-future-version
tags: [unihan, source-data, singapore, irg]
timestamp: 2026-07-06T21:31:45+09:00
---

# kIRG_SGSource

## 概要

`kIRG_SGSource` は、Singapore characters を `kIRG_GSource` から分離して扱うために提案された新しい normative IRG source property である。現在の `GS` source prefix は G-source の中に置かれているが、Singapore が IRG encoding work に参加していない状態で、GS-source glyph issues を誰が処理するかが問題になっていた。

[IRG N2926](../documents/irg-n2926.md) は、`SG-[0-9A-F]{4}` という syntax を持つ `kIRG_SGSource` を設け、既存の `GS` prefix を `SG` prefix に移すことを提案した。

## 経緯

| 年月 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2026-02 | IRG | [IRG N2926](../documents/irg-n2926.md) | Eiso Chan が new normative `kIRG_SGSource` property を提案。 |
| 2026-03 | IRG | [IRG N2909](../documents/irg-n2909.md) | [IRG M66.16 kIRG_SGSource establishment](../events/irg-m66-16-kirg-sgsource-establishment.md)。 |
| 2026-05 | IRG / WG2 | [IRG N2935](../documents/irg-n2935.md) | agenda は、IRG Convenor が [IRG N2926](../documents/irg-n2926.md) を WG2 \#73 へ提出したと記録。 |
| 2026-06-26 | WG2 | [WG2 N5354](../documents/wg2-n5354.md) | WG2 \#73 M73.15 が `kIRG_SGSource` を Amendment 1 target として追加するよう勧告した。 |
| 2026-06 | WG2 / SC2 | [IRG N2935](../documents/irg-n2935.md) | agenda は、WG2 が追加を recommend し、SC2 が ISO/IEC 10646 Seventh Edition Amendment 1 として accept したと記録。 |
| 2027 target | Unicode | [IRG N2935](../documents/irg-n2935.md) | agenda は Unicode Version 19.0 target としている。 |

## 主な論点

### GS-source の扱い

[IRG N2926](../documents/irg-n2926.md) は、既存 code charts / UAX \#38 にある `GS Singapore Characters` を、G-source ではなく Singapore 専用 source として扱うべきだとする。これにより、`kIRG_GSource` の syntax / description から `GS` prefix を外し、current GS-prefixed references は `SG` prefix に移る。

### U+48B4 の扱い

[IRG N2926](../documents/irg-n2926.md) は、U+48B4 の GS-2151 glyph issue を例に、GS-source glyph をそのまま維持すべきか、別の G-source reference へ変更すべきかを挙げている。提案では、original GS-2151 glyph を new SG-2151 glyph として U+9097 へ移し、U+48B4 の G-source reference は China が同意すれば `GKX-1268.18` に変える案が示されている。

### target version

Meeting \#67 agenda の current status では、WG2 と SC2 の acceptance を経て、`kIRG_SGSource` は Unicode Version 19.0 (2027) target とされている。IRG \#66 での establishment は [IRG M66.16 kIRG_SGSource establishment](../events/irg-m66-16-kirg-sgsource-establishment.md) に集約する。

## 関連文書

- [IRG Meeting \#67](../meetings/irg/irg-meeting-67.md)
- [IRG N2926](../documents/irg-n2926.md)
- [WG2 N5354](../documents/wg2-n5354.md)
- [IRG Source Data and Representative Glyphs](irg-source-data-and-representative-glyphs.md)

## 関連出来事

- [IRG M66.16 kIRG_SGSource establishment](../events/irg-m66-16-kirg-sgsource-establishment.md)

## 関連トピック

- [Han Ideographic Scripts](../families/han-ideographic-scripts.md)

## 関連人物・組織

- [Eiso Chan](../people/eiso-chan.md)
- [IRG](../people/irg.md)
- [WG2](../people/wg2.md)

## 出典

- `irg-n2909` - <https://www.unicode.org/irg/docs/n2909-Recommendations.pdf>
- `irg-n2926` - <https://www.unicode.org/irg/docs/n2926-SGSource.pdf>
- `irg-n2935` - <https://www.unicode.org/irg/docs/n2935-ScheduleAgenda.html>
- `wg2-n5354` - <https://www.unicode.org/wg2/docs/n5354-Mtg73-Paris-Recs-rev5.pdf>
