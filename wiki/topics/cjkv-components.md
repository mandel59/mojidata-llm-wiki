---
title: CJKV Components
slug: cjkv-components
kind: topic
bodies: [IRG, WG2]
documents: [irg-n2878r3, irg-n2909, irg-n2935]
status: accepted-for-future-version
tags: [cjk, components, irg, ideographic]
---

# CJKV Components

## 概要

CJKV Components は、CJK ideographs を構成する components を符号化する提案である。`IRG N2878R3` は、`CJK Unified Ideographs Components-A` と `CJK Unified Ideographs Components-B` の 2 blocks を提案し、Components-A に 119 characters、Components-B に 375 characters、合計 494 characters を置く。

IRG Meeting #67 agenda では、IRG #66 からの follow-up として扱われる。`IRG N2935` は、WG2 が two new blocks を accept することを recommend し、SC2 が ISO/IEC 10646 Seventh Edition Amendment 1 として accept したと記録している。target は Unicode Version 19.0 (2027) とされる。

## 経緯

| 年月 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2024-2025 | IRG | `IRG N2733R`, `IRG N2799`, `IRG N2878` | CJKV components encoding proposal が更新される。 |
| 2026-03 | IRG | `IRG N2878R3` | Final proposal として Components-A 119 characters、Components-B 375 characters を提案。 |
| 2026-03 | IRG | `IRG N2909` | IRG #66 Recommendation M66.17 が `IRG N2878R3` を WG2 へ forward することを勧告。 |
| 2026-07 | IRG | `IRG N2935` | Meeting #67 agenda が WG2 / SC2 acceptance と Unicode 19.0 target を current status として記録。 |

## 主な論点

### component と fragment の区別

`IRG N2878R3` は、CJK components と、input method 由来の CJK fragments を区別している。Wubi、Cangjie、Zhengma などの keyboard mapping に現れる object は、統計的・人為的な decomposing の結果であり、component としての rationale を持たない場合があるため、長期的には input method 起源の fragments を受け入れない方針が示されている。

### WS2024 との重複

`IRG N2878R3` と `IRG N2935` は、Components-B に含まれる 11 ideographs が [IRG Working Set 2024](irg-working-set-2024.md) にも含まれていると整理している。Meeting #67 agenda では、これらは WS2024 から withdraw すべきものとして列挙されている。

### 将来の追加方法

IRG #66 Recommendation M66.17 は、`IRG N2878R3` の authors に対して、個別 IRG experts が将来の CJK Unified Ideographs Components blocks へ components を追加提案できる方法を検討するよう求めている。Components は一回限りの encoding ではなく、今後の governance が必要な領域である。

## 関連文書

- [IRG Meeting #67](../meetings/irg/meeting-67.md)
- [IRG Working Set 2024](irg-working-set-2024.md)

## 関連トピック

- [Han Ideographic Scripts](../families/han-ideographic-scripts.md)

## 関連人物・組織

- [China](../people/china.md)
- [TCA](../people/tca.md)
- [Kushim Jiang](../people/kushim-jiang.md)
- [IRG](../people/irg.md)
- [WG2](../people/wg2.md)

## 出典

- `irg-n2878r3` - <https://www.unicode.org/irg/docs/n2878r3-CJKComponents.pdf>
- `irg-n2909` - <https://www.unicode.org/irg/docs/n2909-Recommendations.pdf>
- `irg-n2935` - <https://www.unicode.org/irg/docs/n2935-ScheduleAgenda.html>
