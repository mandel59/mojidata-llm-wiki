---
type: Topic
title: JMJ Horizontal Extension Review Path
description: MOJI-JOHO-KIBAN IDEOGRAPHS-2018 の JMJ references を J-column に追加する large horizontal extension と、その review body を WG2 から IRG へ接続する議論。
slug: jmj-horizontal-extension-review-path
bodies: [WG2, IRG]
documents: [wg2-n5221, irg-n2721, wg2-n5284, irg-n2722, wg2-n5301, wg2-n5304, irg-n2859, irg-n2870]
topics: [cjk-horizontal-extensions, j-source, irg-source-data-and-representative-glyphs]
people: [japan, wg2, irg, ken-lunde]
status: active
tags: [cjk, horizontal-extension, jmj, j-source, source-data]
timestamp: 2026-07-08T00:00:00+09:00
---

# JMJ Horizontal Extension Review Path

## 概要

JMJ horizontal extension は、MOJI-JOHO-KIBAN IDEOGRAPHS-2018 に由来する JMJ references を、既存 CJK Unified Ideographs の J-source column へ追加する大規模 source-data addition である。新しい code point を追加する proposal ではなく、既存文字に Japan source references と representative glyph information を追加・調整する作業として扱う。

この chain は、Japan NB が `WG2 N5221` を WG2 に提出したことから始まり、IRG Convenor が `IRG N2721` / `WG2 N5284` で Japan の IRG active participation を求め、`IRG N2722` が追加後の JMJ source / glyph 対応の issue を指摘する流れで読む。後続の J-source glyph revert や source disposition は関連するが、review path そのものとは分けて追う。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2023-04-24 | WG2 | [WG2 N5221](../documents/wg2-n5221.md) | Japan NB が MOJI-JOHO-KIBAN IDEOGRAPHS-2018 の JMJ references を J-column へ追加する horizontal extension request を提出した。registry subject は 36,422 horizontal extensions とする。 |
| 2024-09-17 | IRG / WG2 | [IRG N2721](../documents/irg-n2721.md) / `WG2 N5284` | IRG Convenor が、`WG2 N5221` 規模の horizontal extension は WG2 より IRG review に向くとして、Japan に IRG active member body への復帰を求めた。 |
| 2024-09-18 | IRG | [IRG N2722](../documents/irg-n2722.md) | Yi Bai と Eiso Chan が、Unicode 16.0 で追加された JMJ horizontal extension について、IDS / glyph shape から code point 対応の issue を指摘した。 |
| 2025-06-23/27 | WG2 | [WG2 N5301](../documents/wg2-n5301.md) | WG2 Meeting \#72 minutes が `WG2 N5284` を扱い、Japan は復帰を検討できるが human resources / workload が課題だと記録した。 |
| 2025-06-23/27 | WG2 | [WG2 N5301](../documents/wg2-n5301.md), [WG2 N5304](../documents/wg2-n5304.md) | WG2 は `WG2 N5296` に基づく chart glyph revert を M72.07 として勧告した。これは horizontal extension review path ではなく、追加後の chart glyph stability issue として接続する。 |
| 2025-08-13 | IRG | [IRG N2859](../documents/irg-n2859.md) | IRG Convenor が `IRG N2722` などを受け、J-source source reference / representative glyph disposition 案を Japan NB に照会した。 |
| 2025-09-25 | IRG | [IRG N2870](../documents/irg-n2870.md) | Japan NB が `IRG N2859` に対し、符号化済み文字の current status 維持を求めた。 |

## 主な論点

### J-column への source reference addition

[WG2 N5221](../documents/wg2-n5221.md) は、ISO/IEC 10646 ed.5 の Annex A.5.11 に示される MOJI-JOHO-KIBAN IDEOGRAPHS-2018 について、既に JMJ ID が J-source として載る新規追加文字以外にも、J-column が空欄の文字へ JMJ references を追加することを求めた。関連 chart PDF は 36,000 件超の対象を示す大規模 data package である。

同じ文書には 44 件の「UCS変更予定一覧」も添付され、MJ IDs の対応先 UCS を変更予定として示している。これは horizontal extension の対象件数とは別に、MOJI-JOHO-KIBAN 側の mapping maintenance が review path と絡むことを示す。

### WG2 から IRG review への接続

[IRG N2721](../documents/irg-n2721.md) / `WG2 N5284` は、Japan が WG2 に `WG2 N5221` を提出したことを、Japan が Han ideograph review の能力と必要性を持つ根拠として扱う。IRG Convenor は、IRG の方が WG2 より頻繁に会合し、CJK experts が horizontal extension を review しやすいと説明した。

[WG2 N5301](../documents/wg2-n5301.md) の Section 8.2 はこの request を WG2 Meeting \#72 で議論した記録である。Japan representative は復帰を検討できるが human resources / workload が課題だと述べ、他の experts は Maintenance Agency model や IRG review の効率化を踏まえて active participation を促している。

### 追加後に見つかった JMJ source issues

[IRG N2722](../documents/irg-n2722.md) は、Unicode 16.0 で追加された JMJ horizontal extensions を IDS で確認し、複数の source reference / glyph correspondence issues を挙げた。主な例は、JMJ-016916 / 016917 と U+72CA / U+3094D、JMJ-046312 / 046313 と U+26B20 / U+26B07、JMJ-043941 と U+25CBB / U+7BF9、JMJ-055359 / 055360 である。

これらの issue は、horizontal extension が単なる property addition ではなく、IVD、representative glyph、既存 code point との同形性、source owner の correction policy に接続することを示す。

### 後続の correction topics との境界

[WG2 N5296](../documents/wg2-n5296.md) と WG2 M72.07 は、JMJ-source horizontal extension 後の code chart font selection によって既存 J-source / JK-source glyphs が変わって見える問題を扱う。これは JMJ review path の後続影響だが、中心は chart glyph stability である。

[IRG N2859](../documents/irg-n2859.md) と [IRG N2870](../documents/irg-n2870.md) は、`IRG N2722` などを受けた source reference / Unihan data disposition である。review path から派生した correction 議論として [J-source and JMJ Source Issues](j-source.md) で追う。

## 現状

`WG2 N5221` の提出により、JMJ references の大規模 J-column horizontal extension は WG2 / IRG の両方で可視化された。`IRG N2721` / `WG2 N5284` と `WG2 N5301` は、今後の同種 review は IRG active participation と IRG review workflow に接続する必要があることを示す。

一方、追加済み JMJ data の具体的 correction は、`IRG N2722` から `IRG N2859` / `IRG N2870` へ進み、符号化済み文字の安定性と source-data correction の調整問題として残っている。

## 関連文書

- [WG2 N5221](../documents/wg2-n5221.md) - Japan NB の JMJ horizontal extension request。
- [IRG N2721](../documents/irg-n2721.md) / `WG2 N5284` - Japan の IRG active participation request。
- [IRG N2722](../documents/irg-n2722.md) - JMJ horizontal extension issue report。
- [WG2 N5301](../documents/wg2-n5301.md) - WG2 Meeting \#72 minutes; Section 8.2 と Section 11。
- [WG2 N5304](../documents/wg2-n5304.md) - WG2 Meeting \#72 recommendations; M72.07。
- [IRG N2859](../documents/irg-n2859.md) - J-source disposition recommendations。
- [IRG N2870](../documents/irg-n2870.md) - Japan NB feedback on `IRG N2859`。

## 関連トピック

- [CJK Horizontal Extensions](cjk-horizontal-extensions.md)
- [J-source and JMJ Source Issues](j-source.md)
- [IRG Source Data and Representative Glyphs](irg-source-data-and-representative-glyphs.md)

## 関連人物・組織

- [Japan](../people/japan.md)
- [WG2](../people/wg2.md)
- [IRG](../people/irg.md)
- [Ken Lunde](../people/ken-lunde.md)

## 出典

- `wg2-n5221` - <https://www.unicode.org/wg2/docs/n5221-JNB_contribution_2304.pdf>
- `irg-n2721` - <https://www.unicode.org/irg/docs/n2721-JapanIRGParticipation.pdf>
- `wg2-n5284` - <https://www.unicode.org/wg2/docs/n5284-JPN-IRG-request.pdf>
- `irg-n2722` - <https://www.unicode.org/irg/docs/n2722-JSourceIssues.pdf>
- `wg2-n5301` - <https://www.unicode.org/wg2/docs/n5301-M72minutes-JP-2025-rev5.pdf>
- `wg2-n5304` - <https://www.unicode.org/wg2/docs/n5304-Mtg72-Niigata-Recs-rev5-final.pdf>
- `irg-n2859` - <https://www.unicode.org/irg/docs/n2859-JapanRecommendations.pdf>
- `irg-n2870` - <https://www.unicode.org/irg/docs/n2870-IRGN2859Feedback.pdf>
