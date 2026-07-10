---
type: Topic
title: UCV and NUCV Lists
description: "IRG の UCV / NUCV lists による component variation と unification / disunification 境界の整理。"
slug: ucv-nucv-lists
bodies: [IRG]
documents: [irg-n2702, irg-n2765, irg-n2909, irg-n2910, irg-n2931, irg-n2935]
topics: [irg-indexing-rules, cjkv-components, unihan-database-maintenance]
people: [irg]
status: active
tags: [irg, ucv, nucv, unification, components]
timestamp: 2026-07-08T00:00:00+09:00
---

# UCV and NUCV Lists

## 概要

UCV / NUCV lists は、CJK Unified Ideographs の review で、component variation を unifiable と見るか、source separation / disunification と見るかを判断するための IRG reference data である。FS / SC や radical assignment が検索・索引 data の運用に近いのに対し、UCV / NUCV は unification policy と candidate review の境界に直接関わる。

[IRG Indexing Rules](irg-indexing-rules.md) は引き続き FS / SC guidelines と radical assignment rules の umbrella として残し、このページでは `IRG N2931` の UCV / NUCV data と Meeting \#66 / \#67 での review schedule を追う。

## 経緯

| 年月日 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2024-10-24 | IRG | [IRG N2702](../documents/irg-n2702.md) | M63.03 / M63.04 が UCV / NUCV examples を確認・更新し、次版 list の review schedule を置いた。 |
| 2025-03-21 | IRG | [IRG N2765](../documents/irg-n2765.md) | M64.02 / M64.03 が UCV / NUCV examples を確認・更新し、Meeting \#65 に向けた review schedule を置いた。 |
| 2026-03-19 | IRG | [IRG N2909](../documents/irg-n2909.md) | M66.04 が updated UCV / NUCV examples を provisionally accept し、editor に [IRG N2931](../documents/irg-n2931.md) preparation を求めた。 |
| 2026-03-31 | IRG | [IRG N2931](../documents/irg-n2931.md) | IWDS Editor が `UCS Ideograph Unifiable Component Variations Summary List (UCV)` と `Non-Unifiable Component Variations Summary List (NUCV)` をまとめた。 |
| 2026-07-05 | IRG | [IRG N2935](../documents/irg-n2935.md) | Meeting \#67 agenda が [IRG N2931](../documents/irg-n2931.md) review を \#66 follow-up に置き、comments due を 2026-07-24 とした。 |

## 主な論点

### unifiable component variation

[IRG N2931](../documents/irg-n2931.md) の UCV list は、stroke / dot の向き、接触、交差、折れ、突出、rooftop modification、extra / reduced stroke などの差を categories a-j に整理する。これは、候補 glyph に見える差が encoded character separation を必要とする差なのか、component variation として同一視できる差なのかを review するための参照表である。

UCV entry は、個別 code point の disposition そのものではなく、似た構成差を持つ既存文字群を例示する data として読む必要がある。WS2024 や horizontal extension の review で、source glyph の差が unification boundary を越えるかどうかを説明する根拠になり得る。

### non-unifiable component variation

NUCV list は、同じく component variation を扱うが、source code separations、disunified ideographs、compatibility ideographs、review system references などを通じて、unification してはいけない、または既に分離された境界を示す。`IRG N2931` では page 186 以降に NUCV list が置かれ、Annex S source separation examples や WS2024 / WS2021 review system references も含まれる。

このため NUCV は、単なる glyph example list ではなく、future working set の candidate を分離すべきか、既存 code points と統合すべきかを判断する negative reference として機能する。

### CJKV Components との接点

[CJKV Components](cjkv-components.md) は components を encoded characters として扱う提案であり、component shape の差をどこまで character として符号化するかが問題になる。UCV / NUCV は、component-like shapes の variation を通常の ideograph unification policy の中で扱う場合の参照であり、CJKV Components の repertoire review と重なる。

### Unihan data との接点

UCV / NUCV の判断は、最終的には encoded character の source references、representative glyphs、`kRSUnicode`、radical / stroke data などと整合する必要がある。[Unihan Database Maintenance](unihan-database-maintenance.md) 側では、UCV / NUCV を直接 property として持つのではなく、review 結果が glyph data や source data、radical / stroke properties に反映される点を追う。

## 関連文書

- [IRG N2931](../documents/irg-n2931.md) - UCV & NUCV lists。
- [IRG N2702](../documents/irg-n2702.md) - Meeting \#63 M63.03 / M63.04。
- [IRG N2765](../documents/irg-n2765.md) - Meeting \#64 M64.02 / M64.03。
- [IRG N2909](../documents/irg-n2909.md) - Meeting \#66 M66.04。
- [IRG N2935](../documents/irg-n2935.md) - Meeting \#67 agenda follow-up。

## 関連トピック

- [IRG Indexing Rules](irg-indexing-rules.md)
- [CJKV Components](cjkv-components.md)
- [Unihan Database Maintenance](unihan-database-maintenance.md)
- [IRG Working Set 2024](irg-working-set-2024.md)

## 出典

- `irg-n2702` - <https://www.unicode.org/irg/docs/n2702-Recommendations.pdf>
- `irg-n2765` - <https://www.unicode.org/irg/docs/n2765-Recommendations.pdf>
- `irg-n2909` - <https://www.unicode.org/irg/docs/n2909-Recommendations.pdf>
- `irg-n2931` - <https://www.unicode.org/irg/docs/n2931-Complete.pdf>
- `irg-n2935` - <https://www.unicode.org/irg/docs/n2935-ScheduleAgenda.html>
