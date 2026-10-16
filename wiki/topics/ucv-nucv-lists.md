---
type: Topic
title: UCV and NUCV Lists
description: "IRG の UCV / NUCV lists による component variation と unification / disunification 境界の整理。"
slug: ucv-nucv-lists
bodies: [IRG]
documents: ["irg-n2702", "irg-n2765", "irg-n2909", "irg-n2910", "irg-n2931", "irg-n2935", "irg-n2978", "irg-n100", "irg-n131", "irg-n2946"]
topics: ["irg-indexing-rules", "irg-disunified-ideographs", "cjkv-components", "unihan-database-maintenance", "ideographic-variation-database", "early-irg-history"]
people: [irg]
status: active
tags: [irg, ucv, nucv, unification, components]
timestamp: 2026-10-10T00:00:00+09:00
events: ["irg-3-unification-annex-forwarding"]
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

### 次回 review 用 URL

[N2946](../documents/irg-n2946.md) M67.03 は N2978 の準備を2026-11-27、expert feedback を2027-01-01、必要な改訂版を01-29、残る feedback を02-19とする。次版の作成予定と公開済み list の切替を区別する。

### 初期 IRG との接続

[N100](../documents/irg-n100.md)の構造・字形差と [第3回 Annex 送付](../events/irg-3-unification-annex-forwarding.md)は、統合判断の対象範囲を読む歴史的な比較点となる。[初期 IRG 議論](early-irg-history.md)では1994年の Annex を現行の UCV / NUCV 一覧と同一視しない。[N2946](../documents/irg-n2946.md) M67.02–03 が2026年の確認・新規例受理と次回 review schedule を記録する。

## 関連文書

- [IRG N2931](../documents/irg-n2931.md) - UCV & NUCV lists。
- [IRG N2702](../documents/irg-n2702.md) - Meeting \#63 M63.03 / M63.04。
- [IRG N2765](../documents/irg-n2765.md) - Meeting \#64 M64.02 / M64.03。
- [IRG N2909](../documents/irg-n2909.md) - Meeting \#66 M66.04。
- [IRG N2935](../documents/irg-n2935.md) - Meeting \#67 agenda follow-up。

## 関連トピック

- [Ideographic Variation Database](ideographic-variation-database.md)
- [IRG Indexing Rules](irg-indexing-rules.md)
- [IRG Disunified Ideographs](irg-disunified-ideographs.md)
- [CJKV Components](cjkv-components.md)
- [Unihan Database Maintenance](unihan-database-maintenance.md)
- [IRG Working Set 2024](irg-working-set-2024.md)

## 出典

- `irg-n2702` - <https://www.unicode.org/irg/docs/n2702-Recommendations.pdf>
- `irg-n2765` - <https://www.unicode.org/irg/docs/n2765-Recommendations.pdf>
- `irg-n2909` - <https://www.unicode.org/irg/docs/n2909-Recommendations.pdf>
- `irg-n2931` - <https://www.unicode.org/irg/docs/n2931-Complete.pdf>
- `irg-n2935` - <https://www.unicode.org/irg/docs/n2935-ScheduleAgenda.html>
- `irg-n2978` - <https://www.unicode.org/irg/docs/n2978-Complete.pdf>
- `irg-n100` - <https://www.unicode.org/irg/docs/n0100-AnnexS.pdf>（registry date: 1994-07-07）
- `irg-n131` - <https://www.unicode.org/irg/docs/n0131-Resolutions.pdf>（registry date: 1994-09-02）
- `irg-n2946` - <https://www.unicode.org/irg/docs/n2946-Recommendations.pdf>（registry date: 2026-10-15）
