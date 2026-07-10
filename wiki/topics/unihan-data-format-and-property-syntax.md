---
type: Topic
title: Unihan Data Format and Property Syntax
description: "Unicode 18.0 cycle の UAX #38 / UTS #37 / RSIndex.txt / kTotalStrokes など、Unihan 周辺 data format と property syntax の更新論点。"
slug: unihan-data-format-and-property-syntax
bodies: [UTC, IRG, WG2]
documents: [utc-l2-26-099, utc-l2-26-102, utc-l2-26-105, utc-l2-26-112, pri-546, pri-549, utc-l2-26-134, utc-l2-26-148, irg-n2951, wg2-n5354]
topics: [unihan-database-maintenance, unicode-18-change-sources, irg-indexing-rules, ucv-nucv-lists, jmj-horizontal-extension-review-path]
people: [ken-lunde, utc, irg, wg2]
status: active
tags: [unihan, data-format, property-syntax, uax38, uts37, unicode-18]
timestamp: 2026-07-08T00:00:00+09:00
---

# Unihan Data Format and Property Syntax

## 概要

Unihan Data Format and Property Syntax は、Unihan database 本体や related data files を機械的に読むための形式、property syntax、radical / stroke data の記録形式を扱う topic である。[Unihan Database Maintenance](unihan-database-maintenance.md) が property 追加・値修正・release tracking を含む umbrella であるのに対し、このページでは UAX \#38、UTS \#37、`RSIndex.txt`、`kTotalStrokes` のような data format / syntax 層に焦点を置く。

Unicode 18.0 cycle では、UAX \#38 Revision 40、UTS \#37 Revision 15、`RSIndex.txt` syntax enhancement、458 ideographs の `kTotalStrokes` 修正が同時期に現れたため、実装者は property の意味だけでなく、data files の field 区切り、identifier syntax、radical / stroke grouping の変更を追う必要がある。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2026-04-03 | UTC | [L2/26-105](../documents/utc-l2-26-105.md) | Proposed Update UAX \#38 Revision 40。Unihan database の organization、property categories、property syntax、history を Unicode 18.0.0 向けに更新する。 |
| 2026-04-03 | UTC | [L2/26-112](../documents/utc-l2-26-112.md) | Proposed Update UTS \#37 Revision 15。IVD data file format、collection URL の管理主体、IVS 登録手順を更新する。 |
| 2026-04-11 | UTC | [L2/26-099](../documents/utc-l2-26-099.md) | CJK & Unihan Working Group が UTC \#187 向けに UAX \#38 / UTS \#37 / Unihan data changes を recommendations に束ねた。 |
| 2026-05-21 | UTC | [L2/26-134](../documents/utc-l2-26-134.md) | `RSIndex.txt` に simplified radical group を示す `|` / `||` / `|||` separator を導入する syntax enhancement を提案。 |
| 2026-07-05 | UTC | [L2/26-148](../documents/utc-l2-26-148.md) | 458 ideographs の `kTotalStrokes` values を IRG FS & SC conventions と ORT metadata checking に合わせる変更を提案。 |
| 2026-07-07 | PRI | [PRI \#549](../documents/pri-549.md) | UAX \#42 Revision 39 public review が close し、UCD XML schema に `kJapaneseNewVariant` / `kJapaneseOldVariant` 追加と `kIRGDaeJaweon` / `kIRGKangXi` 削除が反映された。 |
| 2026-06 | WG2 | [WG2 N5354](../documents/wg2-n5354.md) | WG2 \#73 が `L2/26-099` 由来の CJK additions and changes を ISO/IEC 10646 CD progression に接続した。 |
| 2026-07-31 closing | PRI | [PRI \#546](../documents/pri-546.md) | IVD Registrar が Moji_Joho collection への 8 IVS 追加登録を public review に出した。 |

## 主な論点

### UAX \#38 property syntax

[L2/26-105](../documents/utc-l2-26-105.md) は UAX \#38 の proposed update であり、Unihan database の mechanics、property categories、property syntax、Unihan.zip の構成、property history を Unicode 18.0.0 向けに更新する。`L2/26-099` は PRI \#534 feedback と個別文書の結果を UTC \#187 の action items に変換しており、`kIICore` syntax、`kOtherNumeric` description、`kSpoofingVariant`、`kIRG_GSource`、`kRSUnicode` などを扱う。

UAX \#38 は各 property の意味だけでなく、value delimiter、source reference の prefix、data file の構成を実装者が読む入口になる。Unicode 18.0 の beta data を確認する際は、UAX \#38 draft と `Unihan.zip` の実 data の両方を見る必要がある。

### UAX \#42 XML representation

[PRI \#549](../documents/pri-549.md) は UAX \#42 Revision 39 の public review であり、Unicode 18.0 の Unihan property changes を XML representation に写す。特に `kJapaneseNewVariant` / `kJapaneseOldVariant` の追加と、`kIRGDaeJaweon` / `kIRGKangXi` の削除は、plain text `Unihan.zip` だけでなく `ucdxml` schema を読む tool にも影響する。

UAX \#42 は Unihan の意味論そのものを定義する文書ではないが、data pipeline が XML UCD を使う場合は schema compatibility の一次入口になる。

### UTS \#37 と IVD data files

[L2/26-112](../documents/utc-l2-26-112.md) は UTS \#37 Revision 15 の proposed update である。IVD は `IVD_Collections.txt` と `IVD_Sequences.txt` を中心に、UTF-8 text、semicolon separated fields、comment lines、`# EOF` marker、collection identifier / sequence identifier の syntax を定義する。

Revision 15 の変更点は、collection URL を registrant ではなく registrar が確立・維持する扱いへ整理すること、U+82A6 の glyph examples を web fonts に置き換えること、editor / references を更新することにある。IVS の登録論点は encoded character の boundary と重なるため、[UCV and NUCV Lists](ucv-nucv-lists.md) の unification / disunification 境界とも接続する。

[PRI \#546](../documents/pri-546.md) は、UTS \#37 の registration process が Moji_Joho collection の具体的な update に適用される recent example である。Japan の JMJ horizontal extension 後に Moji Jōhō Kiban database の code point 対応が更新され、5 base characters に対する 8 IVS を `sequences.txt` と representative glyph chart で review する形になっている。

### RSIndex.txt の group separator

[L2/26-134](../documents/utc-l2-26-134.md) は、`RSIndex.txt` の second field に並ぶ code points を、traditional radical、Chinese simplified radical、non-Chinese simplified radical、second non-Chinese simplified radical の groups として機械可読に分ける proposal である。提案は `kRSUnicode` の apostrophe 表記に対応して、`RSIndex.txt` 側では one / two / three `|` separators を挿入する。

この変更は code point repertoire を変えるものではないが、radical-stroke index を生成する tool、差分検出、UI の group labeling に影響する。[IRG Indexing Rules](irg-indexing-rules.md) が扱う radical assignment / stroke count の運用 rule と、UAX \#38 が配布する data files の間をつなぐ変更である。

### kTotalStrokes と IRG review data

[L2/26-148](../documents/utc-l2-26-148.md) は、458 ideographs の informative `kTotalStrokes` values を変更する proposal である。根拠は [IRG N2951](../documents/irg-n2951.md) の Consolidated FS & SC Guidelines と、IRG working set review で ORT が使う `totalstrokes.txt` metadata checking との整合である。

`kTotalStrokes` は informative property だが、検索、indexing、review metadata に影響する。FS / SC conventions と Unihan property value の差が大きい場合、IRG review infrastructure と published Unihan data のどちらを基準にするかを明示して追う必要がある。

### Unicode 18.0 release chain

[Unicode 18.0 Change Sources](unicode-18-change-sources.md) では、UCD、Unihan.zip、UAX / UTS proposed updates、WG2 recommendations、IRG agenda を横断して release 影響を追う。この topic は、そのうち Unihan data format / property syntax に関係する文書を束ねる。正式 release 前の段階では、proposal page だけでなく beta UCD / Unihan.zip と UTC \#188 以降の minutes を確認する必要がある。

## 関連文書

- [L2/26-105](../documents/utc-l2-26-105.md) - Proposed Update UAX \#38。
- [L2/26-112](../documents/utc-l2-26-112.md) - Proposed Update UTS \#37。
- [PRI \#546](../documents/pri-546.md) - Moji_Joho collection への 8 IVS 追加登録 review。
- [PRI \#549](../documents/pri-549.md) - UAX \#42 Unicode Character Database in XML Revision 39 public review。
- [L2/26-099](../documents/utc-l2-26-099.md) - CJK & Unihan Working Group Recommendations for UTC \#187。
- [L2/26-134](../documents/utc-l2-26-134.md) - `RSIndex.txt` syntax enhancement。
- [L2/26-148](../documents/utc-l2-26-148.md) - `kTotalStrokes` changes。
- [IRG N2951](../documents/irg-n2951.md) - Consolidated FS & SC Guidelines。
- [WG2 N5354](../documents/wg2-n5354.md) - WG2 \#73 recommendations。

## 関連トピック

- [Unihan Database Maintenance](unihan-database-maintenance.md)
- [Unicode 18.0 Change Sources](unicode-18-change-sources.md)
- [IRG Indexing Rules](irg-indexing-rules.md)
- [UCV and NUCV Lists](ucv-nucv-lists.md)
- [UAX \#45 / U-Source Ideographs](uax45-u-source-ideographs.md)
- [JMJ Horizontal Extension Review Path](jmj-horizontal-extension-review-path.md)

## 出典

- `utc-l2-26-099` - <https://www.unicode.org/L2/L2026/26099-cjk-unihan-wg-utc187.pdf>
- `utc-l2-26-105` - <https://www.unicode.org/L2/L2026/26105-uax38-40-update-pri534.pdf>
- `utc-l2-26-112` - <https://www.unicode.org/L2/L2026/26112-uts37-15-update-pri541.pdf>
- `pri-546` - <https://www.unicode.org/ivd/pri/pri546/>
- `pri-549` - <https://www.unicode.org/review/pri549/>
- `utc-l2-26-134` - <https://www.unicode.org/L2/L2026/26134-rsindex-syntax-change.pdf>
- `utc-l2-26-148` - <https://www.unicode.org/L2/L2026/26148-ktotalstrokes-changes.pdf>
- `irg-n2951` - <https://www.unicode.org/irg/docs/n2951-FSSC.pdf>
- `wg2-n5354` - <https://www.unicode.org/wg2/docs/n5354-Mtg73-Paris-Recs-rev5.pdf>
