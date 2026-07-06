---
type: Member Body
title: Japan
description: 最近の Japan NB / J-source / WG2 関連 activity を追跡する member body ページ。
slug: japan
kind: member-body
bodies: [IRG, WG2]
documents: [wg2-n5221, irg-n2721, wg2-n5284, wg2-n5296, wg2-n5301, wg2-n5304, wg2-n5311, irg-n2859, irg-n2870, irg-n2934r]
topics: [j-source, irg-source-data-and-representative-glyphs, cjk-horizontal-extensions]
tags: [member-body, source, japan, j-source]
timestamp: 2026-07-06T23:08:00+09:00
---

# Japan

## 概要

Japan は、この wiki では IRG / WG2 の member body、および `kIRG_JSource` / `J-source` の source owner として扱う。最近の公開文書では、WG2 への大規模 JMJ horizontal extension、Japan NB の IRG active participation への復帰要請、J-source representative glyph / source reference の disposition、WG2 Meeting #72 の新潟開催、IRG Meeting #67 の東京開催がまとまって確認できる。

## 最近の活動

| 日付 | 文書 | できごと | 読み取り |
| --- | --- | --- | --- |
| 2023-04-24 | `WG2 N5221` | Japan NB が、MOJI-JOHO-KIBAN IDEOGRAPHS-2018 に関係する 36,422 characters について、ISO/IEC 10646 の J-column へ JMJ references を追加する horizontal extension を WG2 に提出。 | 近年の WG2 における Japan NB の最大の直接提出。後続文書では、IRG Convenor がこの規模の horizontal extension は IRG で review する方が適切だったと指摘する。 |
| 2024-09-17 | `IRG N2721` / `WG2 N5284` | IRG Convenor が Japan に IRG active member body への復帰を要請。2019 年に Japan が human resource 不足を理由に IRG Working Set review へ参加しない方針を示した経緯を引用しつつ、balloting phase での comment や large horizontal extension の提出実績を踏まえ、IRG 内で早期に review へ参加する意義を述べる。 | Japan NB の近年の位置づけを示す入口文書。Japan は inactive とされていたが、IRG からは Han ideograph 標準化の expertise を持つ member body として復帰を求められている。 |
| 2025-02-18 | `WG2 N5296` | CheonHyeong Sim が、JMJ-source / J-source glyph issues を WG2 と Japan NB に提示。Unicode / ISO code chart 生成時の font change により、JK-source characters in CJK Extension C や compatibility block の一部 J-source glyphs が HeiseiMincho / MS Mincho から IPAmjMincho へ変わった問題を指摘する。 | Japan NB の提出ではないが、WG2 が Japan / J-source owner の明確な position を必要とした文書。J-source 管理の実務上の複雑さが表面化している。 |
| 2025-06-23/27 | `WG2 N5301`, `WG2 N5304` | WG2 Meeting #72 が Niigata, Japan で hybrid 開催。[WG2 M72.07 J-source glyph revert recommendation](../events/wg2-m72-07-j-source-glyph-revert.md) も採択された。 | WG2 側で J-source glyph issue が実際に処理された会合。minutes では Japan の IRG 復帰についても議論され、human resources / workload が課題とされた。 |
| 2025-08-13 | `IRG N2859` | [IRG N2859 J-source disposition request](../events/irg-n2859-j-source-disposition-request.md)。 | J-source の具体的な保守・変更判断が Japan NB の確認事項として扱われている。 |
| 2025-09-25 | `IRG N2870` | [IRG N2870 Japan feedback on J-source disposition](../events/irg-n2870-japan-feedback-on-j-source-disposition.md)。 | Japan NB の最新の明示的 position。既存符号化済み文字への disunification を避け、現状維持を求める立場が確認できる。 |
| 2026-04-02 | `IRG N2934R` | IRG Meeting #67 の First Call。会合は 2026-10-12 から 2026-10-16 に東京で hybrid 開催され、SAT Daizōkyō Text Database Committee が host とされる。 | これは Japan NB の文書ではないが、日本国内で IRG 会合が開催される直近の activity として関連する。Japan NB の J-source issues と同じ IRG 文脈で追跡する価値がある。 |

## 主な論点

### WG2 での JMJ horizontal extension

`WG2 N5221` は、Japan NB が WG2 に提出した J-column horizontal extension request である。対象は MOJI-JOHO-KIBAN IDEOGRAPHS-2018 に関係する JMJ references で、registry subject は 36,422 horizontal extensions としている。本文では、ISO/IEC 10646 の J-source column に出ていない JMJ references を空欄の J-Source column へ追加することを求めている。

この提出は後続の `WG2 N5284` で重要な根拠として引用された。IRG Convenor は、Japan が WG2 に大規模 horizontal extension を提出したことを挙げ、こうした案件はより頻繁に会合し CJK review に適した IRG へ提出する方がよいと述べ、Japan の IRG active participation を促した。

### WG2 #72 と J-source glyph corrections

`WG2 N5296` は、JMJ-source related glyph issues を Japan NB と WG2 に検討依頼した文書である。問題の中心は、code chart generation における J-source font selection の変更により、既存の J-source representative glyphs が意図せず変化して見える点にある。

WG2 Meeting #72 での処理結果は [WG2 M72.07 J-source glyph revert recommendation](../events/wg2-m72-07-j-source-glyph-revert.md) に集約する。Japan ページでは、Japan / J-source owner の position が求められた WG2 側の具体的な処理結果として扱う。

### WG2 #72 Niigata host

WG2 Meeting #72 は 2025-06-23/27 に Niigata, Japan で開催された。`WG2 N5304` の Appreciation M72.21 は、IPSJ/ITSCJ を JISC から accredited された Japanese National Body として host に感謝し、Masaru Takechi、Shuichi Tashiro、Toki Messe staff の meeting support も記録している。これは文字符号化提案そのものではないが、WG2 運営面での Japan NB の最近の活動として扱える。

### IRG active participation

`IRG N2721` は、Japan が 2019 年以降 IRG Working Set review から距離を置いていたことを前提に、IRG への active member body としての復帰を求める。理由として、Extension G / H への ballot comments、WG2 へ提出された大規模 horizontal extension、Han ideograph 標準化における Japan の専門性、post-COVID の virtual / hybrid meeting による参加障壁の低下が挙げられている。

### J-source disposition

`IRG N2859` と `IRG N2870` の経緯は [IRG N2859 J-source disposition request](../events/irg-n2859-j-source-disposition-request.md) と [IRG N2870 Japan feedback on J-source disposition](../events/irg-n2870-japan-feedback-on-j-source-disposition.md) に集約する。Japan ページでは、J-source 関連の最近の活動が単なる glyph correction ではなく、符号化済み文字の安定性と post-encoding correction の境界に関わる点を重視する。

### 東京開催の IRG #67

`IRG N2934R` は、IRG Meeting #67 が 2026-10-12/16 に東京で開催されることを告知する。host は SAT Daizōkyō Text Database Committee であり、Japan NB の position paper ではない。ただし、日本国内での IRG 会合開催は、Japan / Japanese experts / SAT の IRG activity を追跡するうえで関連イベントとして扱う。

## 関連文書

- `WG2 N5221` - Japan NB による JMJ-source 36,422 characters の J-column horizontal extension request。
- `IRG N2721` / `WG2 N5284` - Japan に IRG active member body への復帰を求める文書。
- `WG2 N5296` - JMJ-source related glyph issues; Japan NB / WG2 への検討依頼。
- `WG2 N5301` / `WG2 N5304` - WG2 Meeting #72 minutes / recommendations; J-source glyph correction と Niigata host。
- `WG2 N5311` - WG2 #72 social event information, Niigata, Japan。
- `IRG N2859` - J-source disposition recommendations; Japan NB feedback request。
- `IRG N2870` - National Body of Japan による `IRG N2859` への comment。
- `IRG N2934R` - IRG Meeting #67 First Call, Tōkyō, Japan。

## 関連出来事

- [WG2 M72.07 J-source glyph revert recommendation](../events/wg2-m72-07-j-source-glyph-revert.md)
- [IRG N2859 J-source disposition request](../events/irg-n2859-j-source-disposition-request.md)
- [IRG N2870 Japan feedback on J-source disposition](../events/irg-n2870-japan-feedback-on-j-source-disposition.md)

## 関連トピック

- [J-source and JMJ Source Issues](../topics/j-source.md)
- [IRG Source Data and Representative Glyphs](../topics/irg-source-data-and-representative-glyphs.md)
- [CJK Horizontal Extensions](../topics/cjk-horizontal-extensions.md)
- [SAT](sat.md)

## 出典

- `wg2-n5221` - <https://www.unicode.org/wg2/docs/n5221-JNB_contribution_2304.pdf>
- `irg-n2721` - <https://www.unicode.org/irg/docs/n2721-JapanIRGParticipation.pdf>
- `wg2-n5284` - <https://www.unicode.org/wg2/docs/n5284-JPN-IRG-request.pdf>
- `wg2-n5296` - <https://www.unicode.org/wg2/docs/n5296-JMJ-source%20related%20glyph%20issues.pdf>
- `wg2-n5301` - <https://www.unicode.org/wg2/docs/n5301-M72minutes-JP-2025-rev5.pdf>
- `wg2-n5304` - <https://www.unicode.org/wg2/docs/n5304-Mtg72-Niigata-Recs-rev5-final.pdf>
- `wg2-n5311` - <https://www.unicode.org/wg2/docs/n5311-SocialEventInformation-Niigata.pdf>
- `irg-n2859` - <https://www.unicode.org/irg/docs/n2859-JapanRecommendations.pdf>
- `irg-n2870` - <https://www.unicode.org/irg/docs/n2870-IRGN2859Feedback.pdf>
- `irg-n2934r` - <https://www.unicode.org/irg/docs/n2934r-FirstCallIRG67.pdf>
