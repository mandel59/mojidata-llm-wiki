---
type: Topic
title: IRG Working Set 2024
description: IRG Working Set 2024 Version 5.0 review と production schedule に関する論点。
slug: irg-working-set-2024
bodies: [IRG]
documents: [irg-n2909, irg-n2932, irg-n2933, irg-n2935]
status: active
tags: [irg, working-set, cjk, ws2024]
timestamp: 2026-07-06T21:31:45+09:00
---

# IRG Working Set 2024

## 概要

IRG Working Set 2024 は、IRG が review している CJK Unified Ideographs の現行 working set である。IRG Meeting #67 では Version 5.0 が中心議題になっており、`IRG N2935` の schedule では火曜と水曜の大部分がこの review に割り当てられている。

`IRG N2932` は Version 5.0 の chart / list で、各候補の source、attributes、discussion record を含む。`IRG N2933` は Version 5.0 consolidated comments として agenda に載っているが、`IRG N2909` の schedule では 2026-08-14 release 予定であり、2026-07-06 の作業時点では文書実体を確認できなかった。

## 経緯

| 年月 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2026-03 | IRG | `IRG N2909` | IRG #66 Recommendation M66.07 が WS2024 Version 5.0 の生成 schedule を定めた。 |
| 2026-05 | IRG | `IRG N2932` | ORT Manager が WS2024 Version 5.0 を ORT と文書として release する schedule。catalog date は 2026-05-31。 |
| 2026-07 | IRG | `IRG N2935` | Meeting #67 agenda で Version 5.0 review が主要議題として設定された。 |
| 2026-08 | IRG | `IRG N2933` | consolidated comments の release 予定。agenda には載るが、文書実体は未確認。 |
| 2026-10 | IRG | Meeting #67 | submitter responses は 2026-10-09 までに ORT へ入力し、会合で review する予定。 |

## 主な論点

### Version 5.0 review schedule

`IRG N2909` の M66.07 は、2026-05-01 に data fixing、2026-05-29 に Version 5.0 release、2026-07-17 に ORT comments、2026-08-14 に consolidated comments、2026-10-09 に submitter responses という schedule を置いた。Meeting #67 は、この cycle の会合 review にあたる。

### agenda が明示する要注意項目

`IRG N2935` は、Version 5.0 の中で特に注意が必要なものとして、ROK の確認が必要な `GCCPP-00019`、new evidence により unification / withdrawal を戻せる可能性がある `UTC-03362`、disposition が不明な `SAT-09585` を挙げている。

### representative glyph updates

Version 5.0 では、ORT の discussion record に基づき、G-source、K-source、SAT-source、T-source、U-source、UK-source、V-source の representative glyph 更新が agenda に列挙されている。これは [IRG Source Data and Representative Glyphs](irg-source-data-and-representative-glyphs.md) と重なる。

### CJKV Components との重複

Meeting #67 agenda は、`CJK Unified Ideographs Components-B` に入る 11 ideographs が WS2024 にも含まれており、WS2024 から withdraw すべきだとしている。この点は [CJKV Components](cjkv-components.md) と直接接続する。

## 関連文書

- [IRG Meeting #67](../meetings/irg/irg-meeting-67.md)
- [IRG Source Data and Representative Glyphs](irg-source-data-and-representative-glyphs.md)
- [CJK Horizontal Extensions](cjk-horizontal-extensions.md)
- [CJKV Components](cjkv-components.md)
- [CJK Hybrid Characters](cjk-hybrid-characters.md)

## 関連トピック

- [Han Ideographic Scripts](../families/han-ideographic-scripts.md)

## 出典

- `irg-n2909` - <https://www.unicode.org/irg/docs/n2909-Recommendations.pdf>
- `irg-n2932` - <https://www.unicode.org/irg/docs/n2932-WS2024v5.pdf>
- `irg-n2933` - <https://www.unicode.org/irg/docs/n2933-WS2024v5ConsolidatedComments.pdf>
- `irg-n2935` - <https://www.unicode.org/irg/docs/n2935-ScheduleAgenda.html>
