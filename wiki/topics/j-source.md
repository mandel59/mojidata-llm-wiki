---
type: Topic
title: J-source and JMJ Source Issues
description: J-source / JMJ-source horizontal extension、representative glyph、kIRG_JSource disposition の最近の議論。
slug: j-source
bodies: [WG2, IRG, UTC]
documents: [wg2-n5221, irg-n2721, wg2-n5284, irg-n2722, wg2-n5296, wg2-n5301, wg2-n5304, irg-n2859, irg-n2870]
status: active
tags: [cjk, source-data, j-source, jmj, unihan]
timestamp: 2026-07-06T23:26:00+09:00
---

# J-source and JMJ Source Issues

## 概要

J-source は、ISO/IEC 10646 / Unicode の CJK Unified Ideographs における Japan source reference 群である。最近の議論では、MOJI-JOHO-KIBAN IDEOGRAPHS-2018 に基づく JMJ references を J-column へ大量に horizontal extension すること、JMJ-source の representative glyph / code point 対応をどう扱うか、`kIRG_JSource` property value と関連 Unihan properties を変更するか、既に published encoded characters を disunify してよいかが問題になっている。

直近の流れは、Japan NB の `WG2 N5221` から始まり、`IRG N2722` と `WG2 N5296` で issue が顕在化し、WG2 \#72 の `M72.07` と IRG Convenor の `IRG N2859`、Japan NB の `IRG N2870` へ続く。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2023-04-24 | WG2 | `WG2 N5221` | Japan NB が MOJI-JOHO-KIBAN IDEOGRAPHS-2018 に関係する JMJ references を ISO/IEC 10646 の J-column へ追加する horizontal extension request を提出。registry subject は 36,422 horizontal extensions。 |
| 2024-09-17 | WG2 / IRG | `WG2 N5284` / `IRG N2721` | IRG Convenor が Japan に IRG active member body への復帰を要請。`WG2 N5221` の大規模 horizontal extension は WG2 より IRG review に向く、と位置づける。 |
| 2024-09-18 | IRG | `IRG N2722` | Yi Bai と Eiso Chan が `WG2 N5221` 後の JMJ horizontal extension について、IDS / glyph shape から複数の issue を指摘。JMJ-016916 / 016917、JMJ-043941、JMJ-046312 / 046313、JMJ-055359 / 055360 などを挙げる。 |
| 2025-02-18 | WG2 | `WG2 N5296` | CheonHyeong Sim が JMJ-source related glyph issues を提出。code chart generation の font selection により、JK-source / J-source glyphs が HeiseiMincho / MS Mincho から IPAmjMincho へ変わって見える問題を指摘し、Japan NB と WG2 に検討を求める。 |
| 2025-06-23/27 | WG2 | `WG2 N5301`, `WG2 N5304` | [WG2 M72.07 J-source glyph revert recommendation](../events/wg2-m72-07-j-source-glyph-revert.md)。WG2 側で chart glyph stability の問題として処理された。 |
| 2025-08-13 | IRG | [IRG N2859](../documents/irg-n2859.md) | [IRG N2859 J-source disposition request](../events/irg-n2859-j-source-disposition-request.md)。IRG 側で source reference / Unihan data maintenance を含む disposition 案に進んだ。 |
| 2025-09-25 | IRG | [IRG N2870](../documents/irg-n2870.md) | [IRG N2870 Japan feedback on J-source disposition](../events/irg-n2870-japan-feedback-on-j-source-disposition.md)。Japan NB が符号化済み文字の current status 維持を求めた。 |

## 主な論点

### JMJ horizontal extension の規模と review path

`WG2 N5221` は、MOJI-JOHO-KIBAN IDEOGRAPHS-2018 の JMJ references を J-source column に追加する大規模 horizontal extension request である。本文では、ISO/IEC 10646 ed.5 で一部の JMJ IDs は J-source にあるが、その他は J-column に出ていないため、空欄の J-source column へ references を追加することを求めている。

`WG2 N5284` / `IRG N2721` は、このような 36,000 件超の horizontal extension を WG2 に直接提出するより、CJK review に適した IRG に出すべきだと指摘し、Japan の IRG active participation を求める根拠にしている。

### JMJ reference と code point / glyph の対応

`IRG N2722` は、`WG2 N5221` 後に追加された JMJ horizontal extensions の中で、glyph shape と code point 対応に問題がある例を挙げる。たとえば、JMJ-016916 / JMJ-016917 と U+72CA / U+3094D、JMJ-046312 / JMJ-046313 と U+26B20 / U+26B07 のように、IVD として扱われていた JMJ references が別 code point と同形に見えるケースがある。

[IRG N2859](../documents/irg-n2859.md) はこれらを disposition 案に落とし込み、U+72CA の `kIRG_JSource` を JMJ-016916 から JMJ-016917 に変え、U+3094D に JMJ-016916 を horizontal extension する案などを示した。一方、U+7BF9 / U+25CBB や JMJ-055359 / JMJ-055360 については no action を勧告している。

### font selection と representative glyph

`WG2 N5296` は、code chart generation における font selection の変更が J-source representative glyph の見え方を変えた問題を扱う。CJK Extension C の JK-source characters と compatibility block の J-source characters で、HeiseiMincho / MS Mincho から IPAmjMincho へ変わった例があり、文書は Japan NB の明確な position を求めている。

WG2 \#72 での処理結果は [WG2 M72.07 J-source glyph revert recommendation](../events/wg2-m72-07-j-source-glyph-revert.md) に集約する。この topic では、JMJ horizontal extension と IRG 側の disposition とは別の chart glyph stability issue として位置づける。

### disunification と published encoded characters

[IRG N2859](../documents/irg-n2859.md) の disposition request と [IRG N2870](../documents/irg-n2870.md) の Japan NB feedback は、それぞれ [IRG N2859 J-source disposition request](../events/irg-n2859-j-source-disposition-request.md) と [IRG N2870 Japan feedback on J-source disposition](../events/irg-n2870-japan-feedback-on-j-source-disposition.md) に集約する。この topic の未決点は「J-source data の整合性を高める変更」と「符号化済み文字の安定性」の衝突である。

## 現状

2025-09-25 の [IRG N2870](../documents/irg-n2870.md) 時点では、Japan NB は [IRG N2859](../documents/irg-n2859.md) の変更案に対し、current status 維持を求める立場を明示した。WG2 側では `WG2 N5296` に対して M72.07 が採択され、J-source glyph changes の revert が勧告済みである。一方、IRG 側の J-source disposition が Unicode 18.0 / ISO/IEC 10646 Seventh Edition の data にどう反映されるかは、Japan NB の回答と IRG / WG2 / UTC 側の後続処理を追う必要がある。

## 関連文書

- `WG2 N5221` - Japan NB の JMJ-source horizontal extension request。
- `IRG N2722` - JMJ horizontal extension issue report。
- `WG2 N5296` - JMJ-source related glyph issues。
- [WG2 Meeting \#72](../meetings/wg2/wg2-meeting-72.md) - M72.07 J-source glyph correction。
- [IRG N2859](../documents/irg-n2859.md) - J-source disposition recommendations。
- [IRG N2870](../documents/irg-n2870.md) - Japan NB comment on `IRG N2859`。

## 関連出来事

- [WG2 M72.07 J-source glyph revert recommendation](../events/wg2-m72-07-j-source-glyph-revert.md)
- [IRG N2859 J-source disposition request](../events/irg-n2859-j-source-disposition-request.md)
- [IRG N2870 Japan feedback on J-source disposition](../events/irg-n2870-japan-feedback-on-j-source-disposition.md)

## 関連トピック

- [IRG Source Data and Representative Glyphs](irg-source-data-and-representative-glyphs.md)
- [CJK Horizontal Extensions](cjk-horizontal-extensions.md)
- [IRG Indexing Rules](irg-indexing-rules.md)

## 関連人物・組織

- [Japan](../people/japan.md)
- [WG2](../people/wg2.md)
- [IRG](../people/irg.md)

## 出典

- `wg2-n5221` - <https://www.unicode.org/wg2/docs/n5221-JNB_contribution_2304.pdf>
- `irg-n2721` - <https://www.unicode.org/irg/docs/n2721-JapanIRGParticipation.pdf>
- `wg2-n5284` - <https://www.unicode.org/wg2/docs/n5284-JPN-IRG-request.pdf>
- `irg-n2722` - <https://www.unicode.org/irg/docs/n2722-JSourceIssues.pdf>
- `wg2-n5296` - <https://www.unicode.org/wg2/docs/n5296-JMJ-source%20related%20glyph%20issues.pdf>
- `wg2-n5301` - <https://www.unicode.org/wg2/docs/n5301-M72minutes-JP-2025-rev5.pdf>
- `wg2-n5304` - <https://www.unicode.org/wg2/docs/n5304-Mtg72-Niigata-Recs-rev5-final.pdf>
- `irg-n2859` - <https://www.unicode.org/irg/docs/n2859-JapanRecommendations.pdf>
- `irg-n2870` - <https://www.unicode.org/irg/docs/n2870-IRGN2859Feedback.pdf>
