---
type: Topic
title: CJKV Components
description: CJK Unified Ideographs Components-A/B の標準化提案と IRG / WG2 での議論を追跡する。
slug: cjkv-components
kind: topic
bodies: [IRG, WG2, SC2]
documents: [irg-n2702, irg-n2733r, irg-n2765, irg-n2799, irg-n2826, irg-n2852, irg-n2878r3, irg-n2890, irg-n2895, irg-n2909, irg-n2917, irg-n2935, wg2-n5358]
status: accepted-for-future-version
tags: [cjk, components, irg, ideographic]
timestamp: 2026-07-06T21:58:00+09:00
---

# CJKV Components

## 概要

CJKV Components は、CJK ideographs を構成要素として扱う characters を UCS / Unicode に符号化する議論である。最終 proposal の `IRG N2878R3` は、`CJK Unified Ideographs Components-A` に 119 characters、`CJK Unified Ideographs Components-B` に 375 characters、合計 494 characters を置く。

議論は、IDS を実際の字形レベルで簡潔に記述したい要求、教育・辞書・検索で使われる部件リスト、各 member body の component data をどう統合するかから始まった。`IRG N2733R` は China の GF 3001-1997 / GF 0014-2009 を土台に 131 components を提案し、`IRG N2799` は HKSAR、TCA、Vietnam、Jianzi Musical Notation 由来の追加 data を含む CJKV 全体の整理へ拡張した。

2026-07-05 更新の `IRG N2935` 時点では、IRG Convenor が `IRG N2878R3` に Proposal Summary Form を付けて WG2 #73 へ提出し、`WG2 N5358` として扱われた。WG2 は two new blocks の受け入れを勧告し、SC2 は 2026-06-26 に ISO/IEC 10646 Seventh Edition Amendment 1 として accept した。Unicode Version 19.0 (2027) target とされる。

## 経緯

| 日付・時期 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2004-2005 | IRG | `IRG N1081`, `IRG N1133` | China / TCA から ideographic components の初期提案が出ている。現行 proposal の直接の text ではないが、component encoding の先行例として catalog に残る。 |
| 2021-07 | UTC | `L2/21-134` | IDS 用の ideograph component collection が UTC 側にも提出される。後の `IRG N2733R` が参照する前史の一つ。 |
| 2024-10 | IRG | `IRG N2733R` | China が GF 3001-1997 / GF 0014-2009 を支える 131 CJK components の preliminary proposal を提出。 |
| 2024-10 | IRG | `IRG N2702` | IRG #63 Recommendation M63.17 が、CJK components block の符号化は useful かつ long overdue とし、TCA / HKSAR に追加 data の検討・参加を促す。 |
| 2025-03 | IRG | `IRG N2799` | China が multi-source の CJKV components proposal へ拡張。HKSAR、TCA、Vietnam、Jianzi Musical Notation、public IDS database 由来の data を加える。 |
| 2025-03 | IRG | `IRG N2765` | IRG #64 Recommendation M64.19 が `IRG N2799` の継続開発を encourage し、TCA の CMEX CJK Components Review Tool を review/comment の場として紹介する。 |
| 2025-05 | IRG | `IRG N2852` | Night Koo が traditional printing orthography に基づく 4 components の追加を `IRG N2799` へ提案する。 |
| 2025-10-10以前 | IRG | `IRG N2878` | `IRG N2799` の後続版で、表題は `Updated proposal to encode CJK Unified Ideographs Components`。現行 catalog では単独 entry としては出てこないが、2025-10-10 付けの `IRG N2890` が `IRG N2878` への feedback として提出されているため、この時点までに review 対象になっていたことが確認できる。 |
| 2025-10-10 | IRG | `IRG N2890` | Wang Xieyang が `IRG N2878` に対し 5 components の追加と Jianzi Musical Notation components の representative glyph style 修正を提案する。 |
| 2025-10 | IRG | `IRG N2878R`, `IRG N2826` | IRG #65 Recommendation M65.23 が `IRG N2878R` を review。Jianzi Musical Notation Components 121 characters と CJK Unified Ideographs Components 367 characters の two-block 構成、source references、property data、non-G glyph の finalization を求める。 |
| 2025-12-19期限 | IRG | `IRG N2878R2`, `IRG N2826` | M65.23 の Action Item が、authors に final attribute data と final representative glyphs を含む `R2` version を 2025-12-19 までに IRG へ提出するよう求める。 |
| 2026-03-02 | IRG | `IRG N2917` | Henry Chan が `IRG N2878R2` に対して、variant を component として符号化すべきでない点、HCP source reference、radical data などを feedback する。 |
| 2026-03-11 / 2026-03-20 | IRG / WG2 | `IRG N2878R3` / `WG2 N5358` | `IRG N2878R3` 本文の日付は 2026-03-11、IRG register 上の日付は 2026-03-20。Final proposal として Components-A 119 characters、Components-B 375 characters、合計 494 characters を提示する。`WG2 N5358` は同じ提案の WG2 registry entry。 |
| 2026-03-19 | IRG | `IRG N2909` | IRG #66 Recommendation M66.17 が `IRG N2878R3` を WG2 へ forward することを勧告し、将来の components 追加方法の検討を authors に求める。 |
| 2026-07-05 | IRG | `IRG N2935` | Meeting #67 agenda が WG2 / SC2 acceptance、Unicode 19.0 target、WS2024 から withdraw すべき 11 ideographs を current status として記録する。 |

## 主な論点

### component と ideograph の境界

`IRG N2878R3` は、CJK components と CJK ideographs の間に明確な境界がないことを明示する。textual behavior、East Asian width、vertical orientation などの観点では通常の CJK ideographs と差がないため、proposal は components を「component usage によって group された CJK ideographs」として扱う。

この整理により、components は symbols や別 script ではなく、CJK Unified Ideographs の一種として扱われる。`IRG N2917` は variant forms を components として入れるべきではないと指摘したが、`IRG N2878R3` は過去会合の consensus として、対象 characters は CJKUI behavior と整合し、component collection のために提案されていると回答している。

### component と input method fragment の区別

`IRG N2878R3` は、Wubi、Cangjie、Zhengma などの keyboard mapping に現れる objects を CJK components ではなく fragments として扱う。input method 由来の decomposition は統計的結果や人為的介入に基づくことがあり、rationale を含まないためである。

このため、working group は input methods 由来の proposal を reject し、長期的にも受け入れない方針を示している。将来 batch の候補になり得るものも、rational decomposition または visual decomposition として説明できることが前提になる。

### repertoire の source と review process

`IRG N2799` は、GF 3001-1997 / GF 0014-2009、HKSAR の component tables、TCA-CNS 11643-2、Vietnam 提供 data、public IDS database、Jianzi Musical Notation などを暫定 source として整理した。IRG #64 では、TCA が CMEX CJK Components Review Tool を demo し、IRG experts が comments や new components を追加できる review environment として扱われた。

`IRG N2878R3` では、GCP / HCP / TCP などの source reference が整えられ、HCP source は Henry Chan の feedback を受けて Hong Kong の Song Style (Print Style) component table へ修正された。TCA については、Component ORT と horizontal extension に伴う TCP-source numbering の再整理が記録されている。

### feedback の採否

`IRG N2852` は traditional printing orthography を理由に 4 components を追加提案した。`IRG N2890` は 5 components の追加と Jianzi Musical Notation components の glyph style 修正を提案した。`IRG N2878R3` は individual contributions を review したうえで、関係が rational decomposition / visual decomposition として十分でない、または GB 18030 implementation level 2 の範囲外であるとして、first batch には採用しない整理を置いている。ただし second or subsequent batches への再提出可能性は残している。

`IRG N2917` の feedback は部分的に採用された。`IRG N2878R3` は HCP-00033 と HCP-00400 の removal、secondary radical の追加、HCP source reference paragraph の修正に同意した。一方、U+2FAEF を normal CJK Unified Ideograph として分離するべきという主張については、component collection としての扱いを維持している。

### `IRG N2878` の位置づけ

`IRG N2878` は、`IRG N2799` から final proposal `IRG N2878R3` へ至る途中の updated proposal である。`IRG N2878R3` の executive summary は、`IRG N2878` を `Updated proposal to encode CJK Unified Ideographs Components` として revision history に挙げている。また 2025-10-10 付けの `IRG N2890` は表題上 `IRG N2878` への feedback であり、5 components の追加と Jianzi Musical Notation components の representative glyph style を論じている。

ただし、2026-07-06 時点の local catalog / IRG current document register では、公開 entry として確認できるのは `IRG N2878R3` であり、`IRG N2878` / `IRG N2878R` / `IRG N2878R2` は standalone document page としては catalog 化されていない。このため、この wiki では `IRG N2878` を独立 document page ではなく、revision lineage として topic 内で扱い、日付は `IRG N2890`、`IRG N2826`、`IRG N2878R3` などの周辺文書で確認できる範囲に限定して記述する。

### WS2024 との重複

`IRG N2878R3` と `IRG N2935` は、Components-B に含まれる 11 ideographs が [IRG Working Set 2024](irg-working-set-2024.md) にも含まれていると整理している。`IRG N2935` は、これらは WS2024 から withdraw すべきものとして U+2FABF、U+2FADC、U+2FB13、U+2FB18、U+2FB69、U+2FB79、U+2FBC9、U+2FBED、U+2FC04、U+2FC0E、U+2FC0F を列挙する。

この重複整理は、components が CJK ideographs と同じように振る舞う一方で、source data と block policy 上は WS2024 とは別の proposal pipeline に載ることを示している。

### 将来の追加方法

IRG #66 Recommendation M66.17 は、`IRG N2878R3` の authors に対して、individual IRG experts が将来の CJK Unified Ideographs Components blocks へ components を追加提案できる方法を検討するよう求めている。Components は一回限りの encoding ではなく、review tool、source references、property data、future block policy を含む governance が必要な領域である。

## 現状

2026-07-05 更新の `IRG N2935` 時点では、CJK Unified Ideographs Components-A / B は WG2 #73 で受け入れが勧告され、SC2 が 2026-06-26 に ISO/IEC 10646 Seventh Edition Amendment 1 として accept した。Unicode 側の target は Unicode Version 19.0 (2027)。

未決・後続確認は、WS2024 からの 11 characters withdrawal、Unicode / ISO の actual code chart and property data への反映、future batch の proposal procedure、individual feedback を second or later batches でどう扱うかである。

## 関連文書

- [IRG N2733R](../documents/irg-n2733r.md) - China source の preliminary proposal
- [IRG N2799](../documents/irg-n2799.md) - multi-source CJKV components proposal
- [IRG N2852](../documents/irg-n2852.md) - traditional printing orthography feedback
- [IRG N2878R3](../documents/irg-n2878r3.md) - final proposal
- [IRG N2890](../documents/irg-n2890.md) - individual feedback to add components
- `IRG N2895` - feedback on `IRG N2878R`
- [IRG N2917](../documents/irg-n2917.md) - feedback on IRG N2878R2
- [IRG Meeting #66](../meetings/irg/meeting-66.md)
- [IRG Meeting #67](../meetings/irg/meeting-67.md)
- [IRG Working Set 2024](irg-working-set-2024.md)

## 関連トピック

- [Han Ideographic Scripts](../families/han-ideographic-scripts.md)
- [IRG Source Data and Representative Glyphs](irg-source-data-and-representative-glyphs.md)
- [IRG Indexing Rules](irg-indexing-rules.md)

## 関連人物・組織

- [China](../people/china.md)
- [TCA](../people/tca.md)
- [SAT](../people/sat.md)
- [Vietnam](../people/vietnam.md)
- [Kushim Jiang](../people/kushim-jiang.md)
- [Eiso Chan](../people/eiso-chan.md)
- [Henry Chan](../people/henry-chan.md)
- [IRG](../people/irg.md)
- [WG2](../people/wg2.md)

## 出典

- `irg-n2702` - <https://www.unicode.org/irg/docs/n2702-Recommendations.pdf>
- `irg-n2733r` - <https://www.unicode.org/irg/docs/n2733r-CJKComponents4IDS.pdf>
- `irg-n2765` - <https://www.unicode.org/irg/docs/n2765-Recommendations.pdf>
- `irg-n2799` - <https://www.unicode.org/irg/docs/n2799-CJKComponents4IDS.pdf>
- `irg-n2826` - <https://www.unicode.org/irg/docs/n2826-Recommendations.pdf>
- `irg-n2852` - <https://www.unicode.org/irg/docs/n2852-IRGN2799Feedback.pdf>
- `irg-n2878r3` - <https://www.unicode.org/irg/docs/n2878r3-CJKComponents.pdf>
- `irg-n2890` - <https://www.unicode.org/irg/docs/n2890-IRGN2878Feedback.pdf>
- `irg-n2895` - <https://www.unicode.org/irg/docs/n2895-IRGN2878RFeedback.pdf>
- `irg-n2909` - <https://www.unicode.org/irg/docs/n2909-Recommendations.pdf>
- `irg-n2917` - <https://www.unicode.org/irg/docs/n2917-IRGN2878R2Feedback.pdf>
- `irg-n2935` - <https://www.unicode.org/irg/docs/n2935-ScheduleAgenda.html>
- `wg2-n5358` - <https://www.unicode.org/wg2/docs/n5358-irgn2878r3-CJKComponents.pdf>
