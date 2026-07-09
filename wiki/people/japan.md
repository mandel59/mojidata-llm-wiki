---
type: Member Body
title: Japan
description: Japan NB / J-source / 日本関係 ideograph proposals / WG2 関連 activity に関わる IRG / WG2 member body。
slug: japan
bodies: [UTC, IRG, WG2]
documents: [irg-n2367, wg2-n5221, irg-n2721, wg2-n5284, irg-n2722, wg2-n5296, wg2-n5301, wg2-n5304, wg2-n5311, utc-l2-25-053, utc-l2-25-221, utc-l2-25-274, utc-l2-26-044, irg-n2859, irg-n2870, irg-n2934r, pri-546]
topics: [jmj-horizontal-extension-review-path, j-source, irg-source-data-and-representative-glyphs, cjk-horizontal-extensions, unihan-data-format-and-property-syntax, japanese-place-name-ideographs, japanese-historical-ideographs, kana]
events: [utc-187-uax45-futurews-additions, wg2-m72-07-j-source-glyph-revert, irg-n2859-j-source-disposition-request, irg-n2870-japan-feedback-on-j-source-disposition]
tags: [member-body, source, japan, j-source, uax45]
timestamp: 2026-07-06T23:08:00+09:00
---

# Japan

## 概要

Japan は、IRG / WG2 に参加する member body であり、`kIRG_JSource` / `J-source` に関する source owner として CJK source data の確認・回答を担う。UTC 側では、日本の地名・登記資料・古典籍に関係する ideograph proposal や、仮名・Unihan `kJapanese` の data maintenance も Japan 関連 activity として追跡できる。

最近の公開文書では、WG2 への大規模 JMJ horizontal extension、Japan NB の IRG active participation への復帰要請、J-source representative glyph / source reference の disposition、WG2 Meeting \#72 の新潟開催、IRG Meeting \#67 の東京開催に加えて、UAX \#45 へ日本地名 ideographs を追加する UTC documents がまとまって確認できる。

## 最近の活動

| 日付 | 文書 | できごと | 読み取り |
| --- | --- | --- | --- |
| 2019-05-10 | [IRG N2367](../documents/irg-n2367.md) | Japan NB が IRG Meeting \#52 activity report で、human resource 不足により future IRG Working Set review には参加せず、SC2 balloting phase で CJK Unified Ideograph extension proposals を review し続けると報告した。 | 後続の IRG active participation 復帰要請の前提。Japan は source owner として重要な role を持つ一方、IRG Working Set review workload が課題になっていた。 |
| 2023-04-24 | [WG2 N5221](../documents/wg2-n5221.md) | Japan NB が、MOJI-JOHO-KIBAN IDEOGRAPHS-2018 に関係する 36,422 characters について、ISO/IEC 10646 の J-column へ JMJ references を追加する horizontal extension を WG2 に提出。 | 近年の WG2 における Japan NB の最大の直接提出。後続文書では、IRG Convenor がこの規模の horizontal extension は IRG で review する方が適切だったと指摘する。 |
| 2024-09-17 | [IRG N2721](../documents/irg-n2721.md) / `WG2 N5284` | IRG Convenor が Japan に IRG active member body への復帰を要請。2019 年に Japan が human resource 不足を理由に IRG Working Set review へ参加しない方針を示した経緯を引用しつつ、balloting phase での comment や large horizontal extension の提出実績を踏まえ、IRG 内で早期に review へ参加する意義を述べる。 | Japan NB の近年の位置づけを示す入口文書。Japan は inactive とされていたが、IRG からは Han ideograph 標準化の expertise を持つ member body として復帰を求められている。 |
| 2024-09-18 | [IRG N2722](../documents/irg-n2722.md) | Yi Bai と Eiso Chan が、Unicode 16.0 で追加された JMJ horizontal extensions について source reference / glyph correspondence issues を指摘。 | Japan NB の提出ではないが、JMJ source owner として後続 disposition で回答が必要になる入口文書。 |
| 2025-02-18 | `WG2 N5296` | CheonHyeong Sim が、JMJ-source / J-source glyph issues を WG2 と Japan NB に提示。Unicode / ISO code chart 生成時の font change により、JK-source characters in CJK Extension C や compatibility block の一部 J-source glyphs が HeiseiMincho / MS Mincho から IPAmjMincho へ変わった問題を指摘する。 | Japan NB の提出ではないが、WG2 が Japan / J-source owner の明確な position を必要とした文書。J-source 管理の実務上の複雑さが表面化している。 |
| 2025-06-23/27 | [WG2 N5301](../documents/wg2-n5301.md), [WG2 N5304](../documents/wg2-n5304.md) | WG2 Meeting \#72 が Niigata, Japan で hybrid 開催。[WG2 M72.07 J-source glyph revert recommendation](../events/wg2-m72-07-j-source-glyph-revert.md) も採択された。 | WG2 側で J-source glyph issue が実際に処理された会合。minutes では Japan の IRG 復帰についても議論され、human resources / workload が課題とされた。 |
| 2025-01-30/2026-01-14 | `L2/25-053`, `L2/25-221`, `L2/26-044` | Tsukada Masaki が、日本の地名・登記資料に現れる 5 ideographs を UAX \#45 へ追加する proposals を UTC に提出。 | Japan NB 文書ではないが、日本の登記・地名資料を根拠に UTC source data / FutureWS pipeline へ文字を載せる recent activity。 |
| 2025-12-19 | `L2/25-274` | Lin Anning が、日本古典籍 `古学二千文` などに現れる IDS `⿰犭華` の 1 ideograph 追加を提案。 | 日本古典籍由来の未符号化 ideograph を扱う UTC document。地名文字とは異なる historical evidence の系統として追う必要がある。 |
| 2025-08-13 | `IRG N2859` | [IRG N2859 J-source disposition request](../events/irg-n2859-j-source-disposition-request.md)。 | J-source の具体的な保守・変更判断が Japan NB の確認事項として扱われている。 |
| 2025-09-25 | `IRG N2870` | [IRG N2870 Japan feedback on J-source disposition](../events/irg-n2870-japan-feedback-on-j-source-disposition.md)。 | Japan NB の最新の明示的 position。既存符号化済み文字への disunification を避け、現状維持を求める立場が確認できる。 |
| 2026-04-02 | `IRG N2934R` | IRG Meeting \#67 の First Call。会合は 2026-10-12 から 2026-10-16 に東京で hybrid 開催され、SAT Daizōkyō Text Database Committee が host とされる。 | これは Japan NB の文書ではないが、日本国内で IRG 会合が開催される直近の activity として関連する。Japan NB の J-source issues と同じ IRG 文脈で追跡する価値がある。 |
| 2026-07-31 closing | [PRI \#546](../documents/pri-546.md) | IVD Registrar が Moji_Joho collection への 8 IVS 追加登録を public review に出した。registrant は ITSCJ / IPSJ、representative は Shuichi Tashiro。 | `WG2 N5221` 後の Moji Jōhō Kiban code point 対応更新が IVD collection maintenance へ波及した例。 |

## 主な論点

### WG2 での JMJ horizontal extension

[WG2 N5221](../documents/wg2-n5221.md) は、Japan NB が WG2 に提出した J-column horizontal extension request である。対象は MOJI-JOHO-KIBAN IDEOGRAPHS-2018 に関係する JMJ references で、registry subject は 36,422 horizontal extensions としている。本文では、ISO/IEC 10646 の J-source column に出ていない JMJ references を空欄の J-Source column へ追加することを求めている。

この提出は後続の [IRG N2721](../documents/irg-n2721.md) / `WG2 N5284` で重要な根拠として引用された。IRG Convenor は、Japan が WG2 に大規模 horizontal extension を提出したことを挙げ、こうした案件はより頻繁に会合し CJK review に適した IRG へ提出する方がよいと述べ、Japan の IRG active participation を促した。review path の詳細は [JMJ Horizontal Extension Review Path](../topics/jmj-horizontal-extension-review-path.md) に分ける。

[PRI \#546](../documents/pri-546.md) は、この horizontal extension が Unicode 16.0 / ISO/IEC 10646:2020/Amd.2:2025 に取り込まれた後、Moji Jōhō Kiban database の code point 対応更新を理由として Moji_Joho IVD collection の追加登録 review が必要になったことを示す。

### WG2 \#72 と J-source glyph corrections

[WG2 N5296](../documents/wg2-n5296.md) は、JMJ-source related glyph issues を Japan NB と WG2 に検討依頼した文書である。問題の中心は、code chart generation における J-source font selection の変更により、既存の J-source representative glyphs が意図せず変化して見える点にある。

WG2 Meeting \#72 での処理結果は [WG2 M72.07 J-source glyph revert recommendation](../events/wg2-m72-07-j-source-glyph-revert.md) に集約する。この recommendation は、Japan / J-source owner の position が求められた WG2 側の具体的な処理結果である。

### WG2 \#72 Niigata host

WG2 Meeting \#72 は 2025-06-23/27 に Niigata, Japan で開催された。`WG2 N5304` の Appreciation M72.21 は、IPSJ/ITSCJ を JISC から accredited された Japanese National Body として host に感謝し、Masaru Takechi、Shuichi Tashiro、Toki Messe staff の meeting support も記録している。これは文字符号化提案そのものではないが、WG2 運営面での Japan NB の最近の活動として扱える。

### IRG active participation

[IRG N2367](../documents/irg-n2367.md) は、Japan が 2019 年時点で human resource 不足により future IRG Working Set review には参加しない一方、SC2 balloting phase では CJK Unified Ideograph extension proposals の review を続けると報告した文書である。[IRG N2721](../documents/irg-n2721.md) は、この経緯を前提に、IRG への active member body としての復帰を求める。理由として、Extension G / H への ballot comments、WG2 へ提出された大規模 horizontal extension、Han ideograph 標準化における Japan の専門性、post-COVID の virtual / hybrid meeting による参加障壁の低下が挙げられている。

### UTC における日本関係 ideograph proposals

[Japanese Place-Name Ideographs](../topics/japanese-place-name-ideographs.md) は、日本の地名・登記資料に現れる未符号化文字を UAX \#45 / `FutureWS` records として扱う。`L2/25-053`、`L2/25-221`、`L2/26-044` は Japan NB の公式 contribution ではないが、日本国内の登記資料、小字名集、自治体資料、県公報、国立国会図書館デジタルコレクションを evidence とし、UTC source data に日本関係文字を追加する流れを示している。

[Japanese Historical Ideographs](../topics/japanese-historical-ideographs.md) は、日本古典籍に現れる未符号化文字を扱う。`L2/25-274` は `古学二千文` と関連資料に基づく提案で、地名・行政システム由来の文字とは異なる historical evidence の系統を示す。

### J-source disposition

`IRG N2859` と `IRG N2870` の経緯は [IRG N2859 J-source disposition request](../events/irg-n2859-j-source-disposition-request.md) と [IRG N2870 Japan feedback on J-source disposition](../events/irg-n2870-japan-feedback-on-j-source-disposition.md) に集約する。Japan ページでは、J-source 関連の最近の活動が単なる glyph correction ではなく、符号化済み文字の安定性と post-encoding correction の境界に関わる点を重視する。

### 東京開催の IRG \#67

`IRG N2934R` は、IRG Meeting \#67 が 2026-10-12/16 に東京で開催されることを告知する。host は SAT Daizōkyō Text Database Committee であり、Japan NB の position paper ではない。ただし、日本国内での IRG 会合開催は、Japan / Japanese experts / SAT の IRG activity を追跡するうえで関連するイベントである。

## 関連文書

- `WG2 N5221` - Japan NB による JMJ-source 36,422 characters の J-column horizontal extension request。
- [IRG N2367](../documents/irg-n2367.md) - 2019 年時点の Japan Activity Report。
- `IRG N2721` / `WG2 N5284` - Japan に IRG active member body への復帰を求める文書。
- `IRG N2722` - JMJ horizontal extension issue report。
- `WG2 N5296` - JMJ-source related glyph issues; Japan NB / WG2 への検討依頼。
- `WG2 N5301` / `WG2 N5304` - WG2 Meeting \#72 minutes / recommendations; J-source glyph correction と Niigata host。
- `WG2 N5311` - WG2 \#72 social event information, Niigata, Japan。
- `IRG N2859` - J-source disposition recommendations; Japan NB feedback request。
- `IRG N2870` - National Body of Japan による `IRG N2859` への comment。
- `IRG N2934R` - IRG Meeting \#67 First Call, Tōkyō, Japan。
- `PRI #546` - Moji_Joho collection への IVS 追加登録 review。
- `L2/25-053`, `L2/25-221`, `L2/26-044` - 日本地名 ideographs の UAX \#45 additions。
- `L2/25-274` - 日本古典籍由来 ideograph の追加提案。

## 関連出来事

- [WG2 M72.07 J-source glyph revert recommendation](../events/wg2-m72-07-j-source-glyph-revert.md)
- [IRG N2859 J-source disposition request](../events/irg-n2859-j-source-disposition-request.md)
- [IRG N2870 Japan feedback on J-source disposition](../events/irg-n2870-japan-feedback-on-j-source-disposition.md)

## 関連トピック

- [J-source and JMJ Source Issues](../topics/j-source.md)
- [JMJ Horizontal Extension Review Path](../topics/jmj-horizontal-extension-review-path.md)
- [IRG Source Data and Representative Glyphs](../topics/irg-source-data-and-representative-glyphs.md)
- [CJK Horizontal Extensions](../topics/cjk-horizontal-extensions.md)
- [Unihan Data Format and Property Syntax](../topics/unihan-data-format-and-property-syntax.md)
- [Japanese Place-Name Ideographs](../topics/japanese-place-name-ideographs.md)
- [Japanese Historical Ideographs](../topics/japanese-historical-ideographs.md)
- [Kana](../topics/kana.md)
- [SAT](sat.md)

## 出典

- `irg-n2367` - <https://www.unicode.org/irg/docs/n2367-JapanActivityReport.pdf>
- `wg2-n5221` - <https://www.unicode.org/wg2/docs/n5221-JNB_contribution_2304.pdf>
- `irg-n2721` - <https://www.unicode.org/irg/docs/n2721-JapanIRGParticipation.pdf>
- `irg-n2722` - <https://www.unicode.org/irg/docs/n2722-JSourceIssues.pdf>
- `wg2-n5284` - <https://www.unicode.org/wg2/docs/n5284-JPN-IRG-request.pdf>
- `wg2-n5296` - <https://www.unicode.org/wg2/docs/n5296-JMJ-source%20related%20glyph%20issues.pdf>
- `wg2-n5301` - <https://www.unicode.org/wg2/docs/n5301-M72minutes-JP-2025-rev5.pdf>
- `wg2-n5304` - <https://www.unicode.org/wg2/docs/n5304-Mtg72-Niigata-Recs-rev5-final.pdf>
- `wg2-n5311` - <https://www.unicode.org/wg2/docs/n5311-SocialEventInformation-Niigata.pdf>
- `irg-n2859` - <https://www.unicode.org/irg/docs/n2859-JapanRecommendations.pdf>
- `irg-n2870` - <https://www.unicode.org/irg/docs/n2870-IRGN2859Feedback.pdf>
- `irg-n2934r` - <https://www.unicode.org/irg/docs/n2934r-FirstCallIRG67.pdf>
- `pri-546` - <https://www.unicode.org/ivd/pri/pri546/>
- `utc-l2-25-053` - <https://www.unicode.org/L2/L2025/25053-uax45-japanese-place-name.pdf>
- `utc-l2-25-221` - <https://www.unicode.org/L2/L2025/25221-3ideographs-for-Japanese-place-names.pdf>
- `utc-l2-25-274` - <https://www.unicode.org/L2/L2025/25274-japanese-ideograph-addition.pdf>
- `utc-l2-26-044` - <https://www.unicode.org/L2/L2026/26044-uax45-japanese-place-names.pdf>
