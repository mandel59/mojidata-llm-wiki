---
type: Member Body
title: Japan
description: 最近の Japan NB / J-source 関連 activity を追跡する member body ページ。
slug: japan
kind: member-body
bodies: [IRG, WG2]
documents: [irg-n2721, wg2-n5284, irg-n2859, irg-n2870, irg-n2934r]
topics: [irg-source-data-and-representative-glyphs, cjk-horizontal-extensions]
tags: [member-body, source, japan, j-source]
timestamp: 2026-07-06T23:08:00+09:00
---

# Japan

## 概要

Japan は、この wiki では IRG / WG2 の member body、および `kIRG_JSource` / `J-source` の source owner として扱う。最近の公開文書では、Japan NB の IRG active participation への復帰要請、J-source representative glyph / source reference の disposition、IRG Meeting #67 の東京開催がまとまって確認できる。

## 最近の活動

| 日付 | 文書 | できごと | 読み取り |
| --- | --- | --- | --- |
| 2024-09-17 | `IRG N2721` / `WG2 N5284` | IRG Convenor が Japan に IRG active member body への復帰を要請。2019 年に Japan が human resource 不足を理由に IRG Working Set review へ参加しない方針を示した経緯を引用しつつ、balloting phase での comment や large horizontal extension の提出実績を踏まえ、IRG 内で早期に review へ参加する意義を述べる。 | Japan NB の近年の位置づけを示す入口文書。Japan は inactive とされていたが、IRG からは Han ideograph 標準化の expertise を持つ member body として復帰を求められている。 |
| 2025-08-13 | `IRG N2859` | IRG Convenor が、`IRG N2676`、`IRG N2722`、`IRG N2780`、`IRG N2846` などに関係する `kIRG_JSource` property value と J-source representative glyph changes の disposition を勧告し、Japan NB に feedback を求める。 | J-source の具体的な保守・変更判断が Japan NB の確認事項として扱われている。Unicode 18.0 Alpha review と ISO/IEC 10646 Seventh Edition synchronization が背景にある。 |
| 2025-09-25 | `IRG N2870` | National Body of Japan が `IRG N2859` へ回答。published encoded characters には disunification を適用しないという原則を再確認し、U+2A50D、U+5CC0、U+72CA、U+7BF9、U+26B20、U+2F93B、U+21694 の current status を維持すべきと述べる。 | Japan NB の最新の明示的 position。既存符号化済み文字への disunification を避け、現状維持を求める立場が確認できる。 |
| 2026-04-02 | `IRG N2934R` | IRG Meeting #67 の First Call。会合は 2026-10-12 から 2026-10-16 に東京で hybrid 開催され、SAT Daizōkyō Text Database Committee が host とされる。 | これは Japan NB の文書ではないが、日本国内で IRG 会合が開催される直近の activity として関連する。Japan NB の J-source issues と同じ IRG 文脈で追跡する価値がある。 |

## 主な論点

### IRG active participation

`IRG N2721` は、Japan が 2019 年以降 IRG Working Set review から距離を置いていたことを前提に、IRG への active member body としての復帰を求める。理由として、Extension G / H への ballot comments、WG2 へ提出された大規模 horizontal extension、Han ideograph 標準化における Japan の専門性、post-COVID の virtual / hybrid meeting による参加障壁の低下が挙げられている。

### J-source disposition

`IRG N2859` は、複数の J-source glyph / source reference issues について Japan NB の feedback を求める文書である。対象には U+2A50D、U+5CC0、U+72CA、U+7BF9、U+26B20 などが含まれ、`kIRG_JSource`、`kJapanese`、`kMojiJoho`、`kMorohashi` といった Unicode / Unihan data への波及も明示されている。

`IRG N2870` では、Japan NB が「published encoded characters には disunification を適用しない」という原則を示し、`IRG N2859` が検討した複数 code point について current status の維持を求めた。このため、J-source 関連の最近の活動は、単なる glyph correction ではなく、符号化済み文字の安定性と post-encoding correction の境界に関わる。

### 東京開催の IRG #67

`IRG N2934R` は、IRG Meeting #67 が 2026-10-12/16 に東京で開催されることを告知する。host は SAT Daizōkyō Text Database Committee であり、Japan NB の position paper ではない。ただし、日本国内での IRG 会合開催は、Japan / Japanese experts / SAT の IRG activity を追跡するうえで関連イベントとして扱う。

## 関連文書

- `IRG N2721` / `WG2 N5284` - Japan に IRG active member body への復帰を求める文書。
- `IRG N2859` - J-source disposition recommendations; Japan NB feedback request。
- `IRG N2870` - National Body of Japan による `IRG N2859` への comment。
- `IRG N2934R` - IRG Meeting #67 First Call, Tōkyō, Japan。

## 関連トピック

- [IRG Source Data and Representative Glyphs](../topics/irg-source-data-and-representative-glyphs.md)
- [CJK Horizontal Extensions](../topics/cjk-horizontal-extensions.md)
- [SAT](sat.md)

## 出典

- `irg-n2721` - <https://www.unicode.org/irg/docs/n2721-JapanIRGParticipation.pdf>
- `wg2-n5284` - <https://www.unicode.org/wg2/docs/n5284-JPN-IRG-request.pdf>
- `irg-n2859` - <https://www.unicode.org/irg/docs/n2859-JapanRecommendations.pdf>
- `irg-n2870` - <https://www.unicode.org/irg/docs/n2870-IRGN2859Feedback.pdf>
- `irg-n2934r` - <https://www.unicode.org/irg/docs/n2934r-FirstCallIRG67.pdf>
