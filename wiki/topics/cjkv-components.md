---
type: Topic
title: CJKV Components
description: CJK Unified Ideographs Components-A/B の標準化提案と IRG / WG2 での議論を追跡する。
slug: cjkv-components
bodies: [IRG, WG2, SC2]
documents: [irg-n2702, irg-n2733r, irg-n2765, irg-n2799, irg-n2826, irg-n2852, irg-n2878, irg-n2878r, irg-n2878r2, irg-n2878r3, irg-n2890, irg-n2895, irg-n2909, irg-n2917, irg-n2935, wg2-n5358]
topics: [ucv-nucv-lists]
status: accepted-for-future-version
tags: [cjk, components, irg, ideographic]
timestamp: 2026-07-06T21:58:00+09:00
---

# CJKV Components

## 概要

CJKV Components は、CJK ideographs を構成要素として扱う characters を UCS / Unicode に符号化する議論である。最終 proposal の `IRG N2878R3` は、`CJK Unified Ideographs Components-A` に 119 characters、`CJK Unified Ideographs Components-B` に 375 characters、合計 494 characters を置く。

議論は、IDS を実際の字形レベルで簡潔に記述したい要求、教育・辞書・検索で使われる部件リスト、各 member body の component data をどう統合するかから始まった。`IRG N2733R` は China の GF 3001-1997 / GF 0014-2009 を土台に 131 components を提案し、`IRG N2799` は HKSAR、TCA、Vietnam、Jianzi Musical Notation 由来の追加 data を含む CJKV 全体の整理へ拡張した。

2026-07-05 更新の `IRG N2935` 時点では、IRG Convenor が `IRG N2878R3` に Proposal Summary Form を付けて WG2 \#73 へ提出し、`WG2 N5358` として扱われた。WG2 は two new blocks の受け入れを勧告し、SC2 は 2026-06-26 に ISO/IEC 10646 Seventh Edition Amendment 1 として accept した。Unicode Version 19.0 (2027) target とされる。

## 経緯

| 日付・時期 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2004-2005 | IRG | `IRG N1081`, `IRG N1133` | China / TCA から ideographic components の初期提案が出ている。現行 proposal の直接の text ではないが、component encoding の先行例として catalog に残る。 |
| 2021-07 | UTC | `L2/21-134` | IDS 用の ideograph component collection が UTC 側にも提出される。後の `IRG N2733R` が参照する前史の一つ。 |
| 2024-10 | IRG | `IRG N2733R` | China が GF 3001-1997 / GF 0014-2009 を支える 131 CJK components の preliminary proposal を提出。 |
| 2024-10 | IRG | `IRG N2702` | IRG \#63 Recommendation M63.17 が、CJK components block の符号化は useful かつ long overdue とし、TCA / HKSAR に追加 data の検討・参加を促す。 |
| 2025-03 | IRG | `IRG N2799` | China が multi-source の CJKV components proposal へ拡張。HKSAR、TCA、Vietnam、Jianzi Musical Notation、public IDS database 由来の data を加える。 |
| 2025-03 | IRG | `IRG N2765` | IRG \#64 Recommendation M64.19 が `IRG N2799` の継続開発を encourage し、TCA の CMEX CJK Components Review Tool を review/comment の場として紹介する。 |
| 2025-05 | IRG | `IRG N2852` | Night Koo が traditional printing orthography に基づく 4 components の追加を `IRG N2799` へ提案する。 |
| 2025-10-10 | IRG | `IRG N2878`, `IRG N2890` | Wang Xieyang が `IRG N2878` への feedback として、5 components の追加と Jianzi Musical Notation components の representative glyph style 修正を提案する。`IRG N2878` は `IRG N2799` の後続版で、catalog entry `irg-n2878` は `IRG N2878R3` の revision lineage と `IRG N2890` を provenance とする derived entry である。 |
| 2025-10-12 | IRG | `IRG N2878R` | `IRG N2878R` 本文の日付。CJK Unified Ideographs Components と Jianzi Musical Notation Components の two-block 構成を提案し、121 + 367 characters を置く。catalog entry `irg-n2878r` はこの本文 URL と IRG \#65 / \#66 documents を provenance とする derived entry である。 |
| 2025-10-16 | IRG | `IRG N2826` | IRG \#65 Recommendation M65.23 が `IRG N2878R` を review し、source references、property data、non-G glyph の finalization を求める。Action Item では authors に final attribute data と final representative glyphs を含む `R2` version の提出を求めた。 |
| 2026-03-02 | IRG | `IRG N2917` | Henry Chan が `IRG N2878R2` に対して、variant を component として符号化すべきでない点、HCP source reference、radical data などを feedback する。catalog entry `irg-n2878r2` は `IRG N2826` の Action Item と `IRG N2917` の feedback target を provenance とする derived entry である。 |
| 2026-03-11 / 2026-03-20 | IRG / WG2 | `IRG N2878R3` / `WG2 N5358` | [IRG N2878R3 CJKV Components final proposal](../events/irg-n2878r3-cjkv-components-final-proposal.md)。 |
| 2026-03-19 | IRG | `IRG N2909` | [IRG M66.17 CJKV Components forward to WG2](../events/irg-m66-17-cjkv-components-forward-to-wg2.md)。 |
| 2026-07-05 | IRG | `IRG N2935` | Meeting \#67 agenda が WG2 / SC2 acceptance、Unicode 19.0 target、WS2024 から withdraw すべき 11 ideographs を current status として記録する。 |

## 主な論点

### component と ideograph の境界

`IRG N2878R3` は、CJK components と CJK ideographs の間に明確な境界がないことを明示する。textual behavior、East Asian width、vertical orientation などの観点では通常の CJK ideographs と差がないため、proposal は components を「component usage によって group された CJK ideographs」として扱う。

この整理により、components は symbols や別 script ではなく、CJK Unified Ideographs の一種として扱われる。`IRG N2917` は variant forms を components として入れるべきではないと指摘したが、`IRG N2878R3` は過去会合の consensus として、対象 characters は CJKUI behavior と整合し、component collection のために提案されていると回答している。

### component と input method fragment の区別

`IRG N2878R3` は、Wubi、Cangjie、Zhengma などの keyboard mapping に現れる objects を CJK components ではなく fragments として扱う。input method 由来の decomposition は統計的結果や人為的介入に基づくことがあり、rationale を含まないためである。

このため、working group は input methods 由来の proposal を reject し、長期的にも受け入れない方針を示している。将来 batch の候補になり得るものも、rational decomposition または visual decomposition として説明できることが前提になる。

### repertoire の source と review process

`IRG N2799` は、GF 3001-1997 / GF 0014-2009、HKSAR の component tables、TCA-CNS 11643-2、Vietnam 提供 data、public IDS database、Jianzi Musical Notation などを暫定 source として整理した。IRG \#64 では、TCA が CMEX CJK Components Review Tool を demo し、IRG experts が comments や new components を追加できる review environment として扱われた。

`IRG N2878R3` では、GCP / HCP / TCP などの source reference が整えられ、HCP source は Henry Chan の feedback を受けて Hong Kong の Song Style (Print Style) component table へ修正された。TCA については、Component ORT と horizontal extension に伴う TCP-source numbering の再整理が記録されている。

### feedback の採否

`IRG N2852` は traditional printing orthography を理由に 4 components を追加提案した。`IRG N2890` は 5 components の追加と Jianzi Musical Notation components の glyph style 修正を提案した。`IRG N2878R3` は individual contributions を review したうえで、関係が rational decomposition / visual decomposition として十分でない、または GB 18030 implementation level 2 の範囲外であるとして、first batch には採用しない整理を置いている。ただし second or subsequent batches への再提出可能性は残している。

`IRG N2917` の feedback は部分的に採用された。`IRG N2878R3` は HCP-00033 と HCP-00400 の removal、secondary radical の追加、HCP source reference paragraph の修正に同意した。一方、U+2FAEF を normal CJK Unified Ideograph として分離するべきという主張については、component collection としての扱いを維持している。

### `IRG N2878` の位置づけ

`IRG N2878` は、`IRG N2799` から final proposal `IRG N2878R3` へ至る途中の updated proposal である。catalog entry `irg-n2878` は、`IRG N2878R3` の executive summary が `IRG N2878` を `Updated proposal to encode CJK Unified Ideographs Components` として revision history に挙げていることと、2025-10-10 付けの `IRG N2890` が表題上 `IRG N2878` への feedback であることを provenance とする。

`IRG N2878R` は本文ヘッダの日付が 2025-10-12 で、IRG \#65 Recommendation M65.23 でも review 対象として扱われる。catalog entry `irg-n2878r` は本文 URL、IRG \#66 agenda item 4.19、M65.23 を provenance とし、本文日付を catalog の `date` として持つ derived entry である。`IRG N2878R2` は M65.23 の Action Item が要求した次版で、`IRG N2917` が feedback target として明示しているため、catalog entry `irg-n2878r2` はこの 2 件を provenance とする。

ただし、2026-07-06 時点の IRG current document register で公開 row として確認できるのは `IRG N2878R3` であり、`IRG N2878` / `IRG N2878R` / `IRG N2878R2` は Document Register 由来の entry ではない。このため、catalog では `status: referenced` と `provenance` を持つ derived entry として区別し、この wiki でも独立 document page ではなく revision lineage として topic 内で扱う。日付は `IRG N2890`、`IRG N2826`、`IRG N2917`、`IRG N2878R3` などの周辺文書で確認できる範囲に限定して記述する。

### WS2024 との重複

`IRG N2878R3` と `IRG N2935` は、Components-B に含まれる 11 ideographs が [IRG Working Set 2024](irg-working-set-2024.md) にも含まれていると整理している。`IRG N2935` は、これらは WS2024 から withdraw すべきものとして U+2FABF、U+2FADC、U+2FB13、U+2FB18、U+2FB69、U+2FB79、U+2FBC9、U+2FBED、U+2FC04、U+2FC0E、U+2FC0F を列挙する。

この重複整理は、components が CJK ideographs と同じように振る舞う一方で、source data と block policy 上は WS2024 とは別の proposal pipeline に載ることを示している。

### CJK Hybrid Characters との境界

`IRG N2826` の M65.24 は、Latin、Hiragana、Katakana、Bopomofo などを部品に含む Han-like characters を [CJK Hybrid Characters](cjk-hybrid-characters.md) として扱い、原則として CJKUI extension とは別 block に置く方針を記録した。これは CJKV Components とは別の論点である。CJKV Components は CJKUI behavior と整合する component collection として進んだが、script-hybrid characters は radical / stroke / source reference / Unihan property の規則を別途設計する必要がある。

### 将来の追加方法

IRG \#66 Recommendation M66.17 による WG2 forwarding は [IRG M66.17 CJKV Components forward to WG2](../events/irg-m66-17-cjkv-components-forward-to-wg2.md) に集約する。同 recommendation は `IRG N2878R3` の authors に対して、individual IRG experts が将来の CJK Unified Ideographs Components blocks へ components を追加提案できる方法を検討するよう求めている。Components は一回限りの encoding ではなく、review tool、source references、property data、future block policy を含む governance が必要な領域である。

### UCV / NUCV との接点

[UCV and NUCV Lists](ucv-nucv-lists.md) は、component variation を unifiable と見るか、source separation / disunification と見るかを示す IRG reference data である。CJKV Components は components を encoded characters として扱うため、component shape の差が ordinary ideograph unification の範囲内か、component repertoire として別に持つべきかを判断する際に UCV / NUCV と接続する。

## 現状

2026-07-05 更新の `IRG N2935` 時点では、CJK Unified Ideographs Components-A / B は WG2 \#73 で受け入れが勧告され、SC2 が 2026-06-26 に ISO/IEC 10646 Seventh Edition Amendment 1 として accept した。Unicode 側の target は Unicode Version 19.0 (2027)。

未決・後続確認は、WS2024 からの 11 characters withdrawal、Unicode / ISO の actual code chart and property data への反映、future batch の proposal procedure、individual feedback を second or later batches でどう扱うかである。

## 関連文書

- [IRG N2733R](../documents/irg-n2733r.md) - China source の preliminary proposal
- [IRG N2799](../documents/irg-n2799.md) - multi-source CJKV components proposal
- [IRG N2852](../documents/irg-n2852.md) - traditional printing orthography feedback
- `IRG N2878` - catalog entry `irg-n2878`; `IRG N2890` と `IRG N2878R3` から復元した referenced revision
- `IRG N2878R` - catalog entry `irg-n2878r`; `IRG N2826` と IRG \#66 agenda から復元した referenced revision
- `IRG N2878R2` - catalog entry `irg-n2878r2`; `IRG N2826` と `IRG N2917` から復元した referenced revision
- [IRG N2878R3](../documents/irg-n2878r3.md) - final proposal
- [IRG N2890](../documents/irg-n2890.md) - individual feedback to add components
- `IRG N2895` - feedback on `IRG N2878R`
- [IRG N2917](../documents/irg-n2917.md) - feedback on IRG N2878R2
- [IRG Meeting \#66](../meetings/irg/irg-meeting-66.md)
- [IRG Meeting \#67](../meetings/irg/irg-meeting-67.md)
- [IRG Working Set 2024](irg-working-set-2024.md)

## 関連出来事

- [IRG N2878R3 CJKV Components final proposal](../events/irg-n2878r3-cjkv-components-final-proposal.md)
- [IRG M66.17 CJKV Components forward to WG2](../events/irg-m66-17-cjkv-components-forward-to-wg2.md)

## 関連トピック

- [Han Ideographic Scripts](../families/han-ideographic-scripts.md)
- [IRG Source Data and Representative Glyphs](irg-source-data-and-representative-glyphs.md)
- [IRG Indexing Rules](irg-indexing-rules.md)
- [UCV and NUCV Lists](ucv-nucv-lists.md)
- [CJK Hybrid Characters](cjk-hybrid-characters.md)

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
- `irg-n2878` - referenced entry derived from `irg-n2878r3` and `irg-n2890`
- `irg-n2878r` - <https://www.unicode.org/irg/docs/n2878r-CJKComponents4IDS.pdf>
- `irg-n2878r2` - referenced entry derived from `irg-n2826` and `irg-n2917`
- `irg-n2878r3` - <https://www.unicode.org/irg/docs/n2878r3-CJKComponents.pdf>
- `irg-n2890` - <https://www.unicode.org/irg/docs/n2890-IRGN2878Feedback.pdf>
- `irg-n2895` - <https://www.unicode.org/irg/docs/n2895-IRGN2878RFeedback.pdf>
- `irg-n2909` - <https://www.unicode.org/irg/docs/n2909-Recommendations.pdf>
- `irg-n2917` - <https://www.unicode.org/irg/docs/n2917-IRGN2878R2Feedback.pdf>
- `irg-n2935` - <https://www.unicode.org/irg/docs/n2935-ScheduleAgenda.html>
- `wg2-n5358` - <https://www.unicode.org/wg2/docs/n5358-irgn2878r3-CJKComponents.pdf>
