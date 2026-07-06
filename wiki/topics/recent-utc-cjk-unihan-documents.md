---
type: Topic
title: Recent UTC CJK and Unihan Documents
description: 2026 年の UTC current documents に見える CJK / Unihan / ideographic 系文書の流れ。
slug: recent-utc-cjk-unihan-documents
kind: topic
bodies: [UTC, IRG, WG2]
documents: [utc-l2-26-099, utc-l2-26-105, utc-l2-26-112, utc-l2-26-127, utc-l2-26-133, utc-l2-26-134, utc-l2-26-136, utc-l2-26-147, utc-l2-26-148]
status: active
tags: [utc, cjk, unihan, ideographic, source-data]
timestamp: 2026-07-07T00:00:00+09:00
---

# Recent UTC CJK and Unihan Documents

## 概要

2026 年の UTC current documents では、CJK / Unihan / ideographic 系の議論が大きく 3 系統に分かれている。第一は UTC #187 に向けた CJK & Unihan Working Group recommendations `L2/26-099` で、Unicode 18.0 を target にした Unihan data、UAX #38、UAX #45、UAX #60、IVD / source data の更新を束ねている。第二は technical report / data file の更新で、UAX #38 `L2/26-105`、UTS #37 `L2/26-112`、RSIndex.txt syntax `L2/26-134`、`kTotalStrokes` 大規模修正 `L2/26-148` が該当する。第三は新しい ideographic punctuation や U-source の proposal で、double ideographic full stop `L2/26-133`、WHITE IDEOGRAPHIC COMMA `L2/26-136`、U-source horizontal extension `L2/26-147` がある。

この topic は、UTC documents を入口に、[IRG Source Data and Representative Glyphs](irg-source-data-and-representative-glyphs.md)、[CJK Horizontal Extensions](cjk-horizontal-extensions.md)、[IRG Indexing Rules](irg-indexing-rules.md)、[Small Seal Script](small-seal-script.md) などの既存 topic へつなぐための整理である。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2026-04-03 | UTC | `L2/26-105` | Proposed Update UAX #38 Revision 40。Unicode 18.0.0 向けに Unihan database の説明を更新し、`kIRGDaeJaweon` / `kIRGKangXi` removal、U+2B81E 追加などを modifications に含める。 |
| 2026-04-03 | UTC | `L2/26-112` | Proposed Update UTS #37 Revision 15。Ideographic Variation Database の組織と IVS 登録手順を Unicode 18.0 時点の proposed update として更新する。 |
| 2026-04-11 | UTC | `L2/26-099` | CJK & Unihan Working Group が UTC #187 向け recommendations を提出。PRI #520 / #534 / #541 などの feedback、Unihan database、UAX #45、source representative glyphs をまとめて処理する。 |
| 2026-05-01 | UTC | `L2/26-127` | Properties and Algorithms WG が CJK confusables data の判断に CJK WG review を求める。EquivalentUnifiedIdeograph、`kSpoofingVariant`、`kZVariant` などから候補 pairs を作る。 |
| 2026-05-21 | UTC | `L2/26-134` | Ken Lunde が `RSIndex.txt` の syntax enhancement を提案。simplified radical の区切りを `|` / `||` / `|||` で明示する案。 |
| 2026-06-08 | UTC / WG2 | `L2/26-133` | Eiso Chan が Cantonese Yueju Opera / Yuequ Show の performance scripts で使う DOUBLE IDEOGRAPHIC FULL STOP と 2 つの standardized variants を提案。 |
| 2026-06-09 | UTC | `L2/26-136` | Gen Kojitani が日本語史資料・翻訳・学術編集で使われる WHITE IDEOGRAPHIC COMMA を提案。U+3001、U+FE46、semicolon とは区別すべきとする。 |
| 2026-07-05 | UTC / IRG | `L2/26-147` / `IRG N2961` | UTC が 40 CJK Unified Ideographs に `kIRG_USource` values と U-source representative glyphs を追加する horizontal extension を IRG へ提出。 |
| 2026-07-05 | UTC | `L2/26-148` | Ken Lunde が 458 ideographs の `kTotalStrokes` property values 変更を提案。IRG N2951 の FS & SC conventions と ORT metadata checking に合わせる準備と位置づける。 |

## 主な論点

### UTC #187 recommendations が hub になっている

`L2/26-099` は、2026-04-03 の CJK & Unihan Working Group meeting に基づく UTC #187 向け recommendations である。単一の proposal ではなく、public feedback、PRI feedback、document review をまとめ、Unicode Version 18.0 target の consensus / action item を並べる hub 文書になっている。

特に `L2/26-099` は、U+2B158 / U+2B25D の `kRSUnicode` / `kTotalStrokes`、Draft UAX #60 の `kSEAL_Rad` / `kSEAL_THXSrc` syntax、PRI #534 に基づく UAX #38 / Unihan data changes、UAX #45 USourceData.txt 追加、V-source representative glyph change、`kJapaneseNewVariant` / `kJapaneseOldVariant` の追加などを扱う。これは UTC 側で CJK / Unihan data maintenance が、IRG source data、Small Seal、U-source、security confusables、variation data と交差していることを示す。

### UAX #38 / UTS #37 / RSIndex の機械可読データ整備

`L2/26-105` は UAX #38 Revision 40 の proposed update で、Unihan database の構造、property、radical-stroke index、history を Unicode 18.0.0 向けに更新する。modifications では、UTC #185 の consensus / action item に基づく provisional properties removal と、U+2B81E の追加が明示されている。

`L2/26-112` は UTS #37 Revision 15 の proposed update で、Ideographic Variation Database の registration procedure と IVS の扱いを整理する。IVD は glyphic subset を plain text で区別する仕組みであり、J-source / JMJ-source、CJK representative glyph、variation sequence の議論と接続する。

`L2/26-134` は、Unicode 16.0 から含まれる `RSIndex.txt` について、traditional radical、Chinese simplified radical、non-Chinese simplified radical、second non-Chinese simplified radical の区切りを `|` で明示する提案である。これは [IRG Indexing Rules](irg-indexing-rules.md) の radical / stroke count 整理と同じ実装面の問題である。

### U-source と IRG pipeline の接続

`L2/26-147` / `IRG N2961` は、UTC が 40 CJK Unified Ideographs を horizontal extension し、`kIRG_USource` values と U-source representative glyphs を追加する提案である。対象は URO、Extension A、Extension B、Extensions F through J にまたがる。source-specific notes は UCV number や ad hoc unification への参照を含み、UTC の U-source data が IRG の review / unification rules と密接に接続している。

`L2/26-099` でも UAX #45 / U-source documents がまとめて扱われ、`USourceData.txt` と `USourceGlyphs.pdf` の追加が action item になっている。したがって、UTC の recent documents は単に UTC 内の data maintenance ではなく、IRG Working Set や horizontal extension proposal の前段として読む必要がある。

### ideographic punctuation の新規 proposal

`L2/26-133` は DOUBLE IDEOGRAPHIC FULL STOP を U+16FE6 として Ideographic Symbols and Punctuation block に置く案で、corner-justified form と centered form の standardized variants も提案している。用途は Cantonese Yueju Opera / Yuequ Show の performance scripts / librettos における upper / lower sentence marking であり、U+3002 IDEOGRAPHIC FULL STOP 2 文字の代用では plain text semantics を保てないとする。

`L2/26-136` は WHITE IDEOGRAPHIC COMMA を U+16FE5 として提案する。これは日本語の shiroten / shiro-goma ten に対応する inline punctuation で、U+3001 IDEOGRAPHIC COMMA、U+FE46 WHITE SESAME DOT、U+003B / U+FF1B semicolon とは機能が異なると整理している。known usage は主に明治期日本語資料と後年の scholarly / literary editions であり、検索、引用、校訂、デジタルアーカイブで plain-text representation が必要とされる。

### CJK confusables は security data と CJK 専門判断の境界

`L2/26-127` は、Properties and Algorithms Working Group が CJK confusables の候補 pairs について CJK Working Group の review を求める文書である。候補は `EquivalentUnifiedIdeograph.txt`、`kSpoofingVariant`、`kZVariant` などから作られ、Windows / Android glyph comparison も使われている。これは UTS #39 security data を保守するには CJK glyph / source data の専門判断が必要であることを示す。

## 現状

2026-07-05 の current register 時点では、UTC の CJK / Unihan 関連文書は Unicode 18.0 target の data maintenance と、IRG / WG2 へ渡す ideographic proposal の両方を含んでいる。直近で追うべき点は、`L2/26-099` の action items が Unicode 18.0 data にどう反映されるか、`L2/26-147` が IRG の U-source horizontal extension としてどう扱われるか、`L2/26-133` / `L2/26-136` の ideographic punctuation proposals が UTC / WG2 でどのように disposition されるかである。

## 関連文書

- `L2/26-099` - CJK & Unihan Working Group Recommendations for UTC #187。
- `L2/26-105` - Proposed Update UAX #38 Unicode Han Database。
- `L2/26-112` - Proposed Update UTS #37 Unicode Ideographic Variation Database。
- `L2/26-127` - second request for review of CJK confusables。
- `L2/26-133` - double ideographic full stop proposal。
- `L2/26-134` - RSIndex.txt syntax enhancement。
- `L2/26-136` - WHITE IDEOGRAPHIC COMMA proposal。
- `L2/26-147` / `IRG N2961` - U-source horizontal extension。
- `L2/26-148` - `kTotalStrokes` changes for 458 ideographs。

## 関連トピック

- [CJK Horizontal Extensions](cjk-horizontal-extensions.md)
- [IRG Source Data and Representative Glyphs](irg-source-data-and-representative-glyphs.md)
- [IRG Indexing Rules](irg-indexing-rules.md)
- [Small Seal Script](small-seal-script.md)

## 関連人物・組織

- [UTC](../people/utc.md)
- [IRG](../people/irg.md)
- [WG2](../people/wg2.md)
- [Eiso Chan](../people/eiso-chan.md)
- [Ken Lunde](../people/ken-lunde.md)

## 出典

- `utc-l2-26-099` - <https://www.unicode.org/L2/L2026/26099-cjk-unihan-wg-utc187.pdf>
- `utc-l2-26-105` - <https://www.unicode.org/L2/L2026/26105-uax38-40-update-pri534.pdf>
- `utc-l2-26-112` - <https://www.unicode.org/L2/L2026/26112-uts37-15-update-pri541.pdf>
- `utc-l2-26-127` - <https://www.unicode.org/L2/L2026/26127-2nd-cjk-confusables.pdf>
- `utc-l2-26-133` - <https://www.unicode.org/L2/L2026/26133-dbl-ideo-fs.pdf>
- `utc-l2-26-134` - <https://www.unicode.org/L2/L2026/26134-rsindex-syntax-change.pdf>
- `utc-l2-26-136` - <https://www.unicode.org/L2/L2026/26136-white-ideographic-comma.pdf>
- `utc-l2-26-147` - <https://www.unicode.org/L2/L2026/26147-irgn2961-unicodehorizontalextension.pdf>
- `utc-l2-26-148` - <https://www.unicode.org/L2/L2026/26148-ktotalstrokes-changes.pdf>
