---
type: Topic
title: "UAX #45 U-Source Ideographs"
description: "UAX #45 の U-source ideographs、USourceData.txt、FutureWS records の保守論点。"
slug: uax45-u-source-ideographs
kind: topic
bodies: [UTC, IRG, WG2]
documents: [utc-l2-26-043, utc-l2-26-044, utc-l2-26-057, utc-l2-26-064, utc-l2-26-071, utc-l2-26-072, utc-l2-26-080, utc-l2-26-083, utc-l2-26-085, utc-l2-26-099, utc-l2-26-147]
status: active
tags: [uax45, u-source, futurews, cjk, source-data]
timestamp: 2026-07-07T00:00:00+09:00
---

# UAX #45 U-Source Ideographs

## 概要

UAX #45 U-Source Ideographs は、UTC が管理する urgently needed ideographs / U-source ideographs の data と、それらを将来の IRG working set submission へ渡す流れを扱う topic である。中心となる data は `USourceData.txt` と `USourceGlyphs.pdf` で、各 record には UTC source id、status、radical / stroke data、IDS、関連 Unihan properties が含まれる。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2026-01/03 | UTC | `L2/26-043`, `044`, `057`, `064`, `071`, `072`, `080`, `083`, `085` | UAX #45 へ 30 ideographs を追加する個別 proposal が提出された。 |
| 2026-04-11 | UTC | `L2/26-099` | CJK & Unihan Working Group が 30 records を UTC-03660 から UTC-03689 として `FutureWS` status で受け入れるよう勧告した。 |
| 2026-07-05 | UTC / IRG | `L2/26-147` / `IRG N2961` | 既存 encoded ideographs への U-source horizontal extension が提出された。 |

## 主な論点

### FutureWS records

`L2/26-099` Sections 23-31 は、9 documents から 30 U-source records を受け入れ、`USourceData.txt` と `USourceGlyphs.pdf` に追加する action item を置いた。これらは `FutureWS` status とされ、UTC の次期 IRG working set submission に含める候補として位置づけられる。

### UAX #45 additions と horizontal extension の違い

UAX #45 additions は、未符号化 ideograph を UTC source data として蓄積し、将来の working set へ渡す前段である。一方、`L2/26-147` / `IRG N2961` の U-source horizontal extension は、既に encoded された CJK Unified Ideographs に `kIRG_USource` values と U-source representative glyphs を追加する作業である。

### Unicode 19.0 までの intake pause

`L2/26-099` Section 40 は、Unicode Version 18.0 で UAX #45 additions が 200 ideographs を超えるため、Unicode Version 19.0 までは CJK & Unihan Working Group が新たな UAX #45 additions を検討しないと整理した。これは UAX #45 を単なる backlog ではなく、IRG submission pipeline の容量管理対象として扱っていることを示す。

## 関連文書

- [L2/26-099](../documents/utc-l2-26-099.md)
- `L2/26-043`, `044`, `057`, `064`, `071`, `072`, `080`, `083`, `085` - UAX #45 additions。
- `L2/26-147` / `IRG N2961` - U-source horizontal extension。

## 関連トピック

- [CJK Horizontal Extensions](cjk-horizontal-extensions.md)
- [IRG Working Set 2024](irg-working-set-2024.md)
- [Unihan Database Maintenance](unihan-database-maintenance.md)

## 出典

- `utc-l2-26-043` - <https://www.unicode.org/L2/L2026/26043-uax45-addition.pdf>
- `utc-l2-26-044` - <https://www.unicode.org/L2/L2026/26044-uax45-japanese-place-names.pdf>
- `utc-l2-26-057` - <https://www.unicode.org/L2/L2026/26057-additions-uax45.pdf>
- `utc-l2-26-064` - <https://www.unicode.org/L2/L2026/26064-ideograph-proposal.pdf>
- `utc-l2-26-071` - <https://www.unicode.org/L2/L2026/26071-3-ideographs.pdf>
- `utc-l2-26-072` - <https://www.unicode.org/L2/L2026/26072-uax45-hosogyo-samuhara.pdf>
- `utc-l2-26-080` - <https://www.unicode.org/L2/L2026/26080-1-addition-uax45.pdf>
- `utc-l2-26-083` - <https://www.unicode.org/L2/L2026/26083-5-ideographs.pdf>
- `utc-l2-26-085` - <https://www.unicode.org/L2/L2026/26085-uax45-abbr.pdf>
- `utc-l2-26-099` - <https://www.unicode.org/L2/L2026/26099-cjk-unihan-wg-utc187.pdf>
- `utc-l2-26-147` - <https://www.unicode.org/L2/L2026/26147-irgn2961-unicodehorizontalextension.pdf>
