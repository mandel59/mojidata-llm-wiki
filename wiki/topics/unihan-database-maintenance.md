---
type: Topic
title: Unihan Database Maintenance
description: "Unihan database、関連 k* properties、release updates の保守論点。data format / syntax は専用 topic に分割する。"
slug: unihan-database-maintenance
bodies: [UTC, IRG, WG2]
documents: [utc-l2-22-181, utc-l2-25-213, utc-l2-26-068, utc-l2-26-074, utc-l2-26-084, utc-l2-26-099, utc-l2-26-102, utc-l2-26-105, utc-l2-26-112, utc-l2-26-134, utc-l2-26-148, wg2-n5354]
topics: [unihan-data-format-and-property-syntax, ucv-nucv-lists]
status: active
tags: [unihan, uax38, uts37, cjk, properties]
timestamp: 2026-07-07T00:00:00+09:00
---

# Unihan Database Maintenance

## 概要

Unihan Database Maintenance は、CJK Unified Ideographs に付与される `k*` properties、Unihan database の release updates、個別 property value の追加・変更・削除を追う umbrella topic である。代表字形や source reference の変更は、最終的に `kRSUnicode`、`kTotalStrokes`、`kIRG_*Source`、`kMandarin`、variant properties などの Unihan property 更新として反映される。

Data file の field structure、property syntax、IVD file format、`RSIndex.txt` separator、`kTotalStrokes` と IRG review data の接続は [Unihan Data Format and Property Syntax](unihan-data-format-and-property-syntax.md) に分割する。このページでは、property / release maintenance の入口と、関連文書の全体像を保つ。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2022-08-23 | UTC | [L2/22-181](../documents/utc-l2-22-181.md) | Ken Lunde が provisional Unihan property `kJapanese` を提案。Moji Jōhō Kiban に基づき、Japanese readings を hiragana / katakana で記録する。 |
| 2025-08-19 | UTC | [L2/25-213](../documents/utc-l2-25-213.md) | HarJIT が `kJapanese` に含まれる Katakana 表記の kun'yomi を調査し、definition と values の修正を提案。 |
| 2026-04-03 | UTC | [L2/26-105](../documents/utc-l2-26-105.md) | Proposed Update UAX \#38 Revision 40。Unicode 18.0.0 向けに Unihan database の説明、property、history を更新する。 |
| 2026-04-03 | UTC | [L2/26-112](../documents/utc-l2-26-112.md) | Proposed Update UTS \#37 Revision 15。Ideographic Variation Database と IVS 登録手順を更新する。 |
| 2026-04-11 | UTC | `L2/26-099` | CJK & Unihan Working Group が UTC \#187 向けに Unihan database additions / changes / removals、UAX \#38、UTS \#37 関連 action items をまとめた。 |
| 2026-05-21 | UTC | [L2/26-134](../documents/utc-l2-26-134.md) | `RSIndex.txt` syntax enhancement。simplified radical の区切りを `|` / `||` / `|||` で表す案。 |
| 2026-07-05 | UTC | [L2/26-148](../documents/utc-l2-26-148.md) | 458 ideographs の `kTotalStrokes` values を IRG N2951 FS & SC conventions と ORT metadata checking に合わせて変更する proposal。 |

## 主な論点

### UAX \#38 と実データ更新

[L2/26-105](../documents/utc-l2-26-105.md) は UAX \#38 の proposed update であり、`L2/26-099` は PRI \#534 feedback と個別文書を UTC action item に変換する。`L2/26-099` では、`kIICore` syntax、`kOtherNumeric` description、`kSpoofingVariant`、`kIRG_GSource`、`kRSUnicode`、`kTotalStrokes` などが対象になった。Format / syntax の詳細は [Unihan Data Format and Property Syntax](unihan-data-format-and-property-syntax.md) に寄せる。

### 新しい provisional properties

`L2/26-074` と `L2/26-099` Section 21 は、`kJapaneseNewVariant` と `kJapaneseOldVariant` を provisional Unihan database properties として追加する流れを示す。初期 data は 400 ideographs 以上を対象とし、将来の追加には慎重な vetting が必要とされた。

### readings と radical / stroke data

`L2/26-084` は 2024 年の UTC action items に基づく 169 characters の `kMandarin` additions / changes を整理した。[L2/26-134](../documents/utc-l2-26-134.md) と [L2/26-148](../documents/utc-l2-26-148.md) は、radical / stroke count 系 data の機械可読性と IRG review data との整合を扱うため、詳細は [Unihan Data Format and Property Syntax](unihan-data-format-and-property-syntax.md) から読む。

[UCV and NUCV Lists](ucv-nucv-lists.md) は Unihan property そのものではないが、unification / disunification boundary の参照表として、representative glyph、source reference、radical / stroke data の判断に影響する。

### `kJapanese` と kana readings

[L2/22-181](../documents/utc-l2-22-181.md) は、Moji Jōhō Kiban 由来の Japanese readings を hiragana / katakana で記録する `kJapanese` property を提案した。[L2/25-213](../documents/utc-l2-25-213.md) は、Katakana 表記が常に on'yomi とは限らず、taxonomic terms や non-Sino-Japanese loanwords などで Katakana 表記の kun'yomi が現れることを指摘する。これは kana character encoding ではなく、Unihan property definition と value corrections の保守問題として扱う。

### CJK Hybrid Characters の property 設計

`IRG N2826` M65.24 は、CJK Hybrid Characters に Unihan database properties を付与する場合、IRG review process で IRG source references、Kangxi radical、stroke count、readings などの規則を議論できると整理した。CJKUI と別 block に置く場合でも、CJK text で使われる文字として検索・分類 data をどう持つかは [CJK Hybrid Characters](cjk-hybrid-characters.md) 側の未決点である。

## 関連文書

- [L2/26-099](../documents/utc-l2-26-099.md)
- [L2/22-181](../documents/utc-l2-22-181.md)
- [L2/25-213](../documents/utc-l2-25-213.md)
- [L2/26-105](../documents/utc-l2-26-105.md) - Proposed Update UAX \#38。
- [L2/26-112](../documents/utc-l2-26-112.md) - Proposed Update UTS \#37。
- [L2/26-134](../documents/utc-l2-26-134.md) - RSIndex.txt syntax enhancement。
- [L2/26-148](../documents/utc-l2-26-148.md) - `kTotalStrokes` changes。

## 関連トピック

- [Unicode 18.0 Change Sources](unicode-18-change-sources.md)
- [Unihan Data Format and Property Syntax](unihan-data-format-and-property-syntax.md)
- [IRG Source Data and Representative Glyphs](irg-source-data-and-representative-glyphs.md)
- [IRG Indexing Rules](irg-indexing-rules.md)
- [UCV and NUCV Lists](ucv-nucv-lists.md)
- [UAX \#45 / U-Source Ideographs](uax45-u-source-ideographs.md)
- [CJK Security Confusables](cjk-security-confusables.md)
- [CJK Hybrid Characters](cjk-hybrid-characters.md)

## 出典

- `utc-l2-22-181` - <https://www.unicode.org/L2/L2022/22181-unihan-kjapanese.pdf>
- `utc-l2-25-213` - <https://www.unicode.org/L2/L2025/25213-katakana_kun-yomi.pdf>
- `utc-l2-26-068` - <https://www.unicode.org/L2/L2026/26068-v-source-character-u2b8a0.pdf>
- `utc-l2-26-074` - <https://www.unicode.org/L2/L2026/26074-two-new-unihan-properties.pdf>
- `utc-l2-26-084` - <https://www.unicode.org/L2/L2026/26084-kMan-feedback.pdf>
- `utc-l2-26-099` - <https://www.unicode.org/L2/L2026/26099-cjk-unihan-wg-utc187.pdf>
- `utc-l2-26-105` - <https://www.unicode.org/L2/L2026/26105-uax38-40-update-pri534.pdf>
- `utc-l2-26-112` - <https://www.unicode.org/L2/L2026/26112-uts37-15-update-pri541.pdf>
- `utc-l2-26-134` - <https://www.unicode.org/L2/L2026/26134-rsindex-syntax-change.pdf>
- `utc-l2-26-148` - <https://www.unicode.org/L2/L2026/26148-ktotalstrokes-changes.pdf>
