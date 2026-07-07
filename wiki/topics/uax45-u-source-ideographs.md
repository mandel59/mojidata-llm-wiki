---
type: Topic
title: "UAX #45 / U-Source Ideographs"
description: "UAX #45 の U-source database、USourceData.txt、kIRG_USource、FutureWS records、horizontal extension の保守論点。"
slug: uax45-u-source-ideographs
aliases: [U-Source, U-source, USourceData, kIRG_USource]
bodies: [UTC, IRG, WG2]
documents: [utc-l2-07-159, utc-l2-07-160, utc-l2-08-284, irg-n1534, irg-n1535, utc-l2-11-439, irg-n2369r, irg-n2439, irg-n2511, utc-l2-22-185, utc-l2-25-053, utc-l2-25-199, utc-l2-25-221, utc-l2-26-043, utc-l2-26-044, utc-l2-26-057, utc-l2-26-064, utc-l2-26-071, utc-l2-26-072, utc-l2-26-080, utc-l2-26-083, utc-l2-26-085, utc-l2-26-099, utc-l2-26-147]
topics: [unihan-database-maintenance, cjk-horizontal-extensions, irg-source-data-and-representative-glyphs, irg-indexing-rules, japanese-place-name-ideographs, japanese-historical-ideographs]
people: [utc, irg, wg2, john-h-jenkins, richard-cook, ken-lunde, uk]
events: [utc-187-uax45-futurews-additions]
status: active
tags: [uax45, u-source, futurews, cjk, source-data, horizontal-extension]
timestamp: 2026-07-08T00:00:00+09:00
---

# UAX \#45 / U-Source Ideographs

## 概要

UAX \#45 / U-Source Ideographs は、UTC が受け取った CJK ideograph candidates と、それらに付く `UTC` / `UCI` / `UK` source identifiers、status、representative glyph、source evidence を公開・保守する仕組みである。IRG / WG2 から見ると、U-source は member body source の一つであり、encoded CJK Unified Ideographs では `kIRG_USource` property や code chart glyph に現れる。

UAX \#45 の中心 data は `USourceData.txt`、`USourceGlyphs.pdf`、`USourceRSChart.pdf` である。`USourceData.txt` は identifier、status、Unicode code point、radical / stroke data、IDS、source field、comments などを持ち、提案段階の ideograph と、既符号化文字へ source reference を後付けする horizontal extension の両方を扱う。

この topic は、既存の UAX \#45 / FutureWS additions に加えて、U-source database を public/versioned reference にする初期提案、Extension D evidence、`AJ1` source reference、2019/2026 horizontal extension、U-source glyph issue を統合して読む入口である。

## 経緯

| 日付         | Body      | 文書                                                                                     | できごと                                                                                                                                   |
| ---------- | --------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| 2007-05-10 | UTC       | [L2/07-159](../documents/utc-l2-07-159.md), [L2/07-160](../documents/utc-l2-07-160.md) | U-source database を public / versioned UTR として公開し、Extension C の U-source attribution correction を追えるようにする提案が出た。                        |
| 2008-08-04 | UTC       | [L2/08-284](../documents/utc-l2-08-284.md)                                             | Draft UTR \#45 が、U-source identifier、status field、source field、glyph / data files を定義した。                                                |
| 2008-11-12 | IRG       | [IRG N1534](../documents/irg-n1534.md), [IRG N1535](../documents/irg-n1535.md)         | UTC Extension D proposal の source descriptions と sample evidence が IRG に提出された。                                                         |
| 2011-11-11 | UTC / IRG | [L2/11-439](../documents/utc-l2-11-439.md) / `IRG N1825R`                              | Adobe-Japan1-6 由来の 27 ideographs について、`kIRG_USource` の source reference を `UTC-...` から `AJ1-...` へ明確化する提案が出た。                          |
| 2019-05    | IRG / WG2 | [IRG N2369R](../documents/irg-n2369r.md) / `WG2 N5085`                                 | UAX \#45 に存在するが U-source identifier を欠く約 150 encoded ideographs に horizontal extension で source identifiers を付ける提案が出た。                  |
| 2020-08/09 | UTC / IRG | [IRG N2439](../documents/irg-n2439.md) / `L2/20-204`                                   | UTC-02993 と UTC-03009 を Urgently Needed Characters として提出し、現行 UAX \#45 data ではそれぞれ U+9FFF / U+9FFE の encoded records として追跡できる。                 |
| 2021-08-24 | IRG       | [IRG N2511](../documents/irg-n2511.md)                                                 | U+30759 / UTC-01250 の representative glyph が evidence と合わない可能性を指摘し、glyph update または別符号化を提案した。                                          |
| 2022-08-15 | UTC       | [L2/22-185](../documents/utc-l2-22-185.md)                                             | `N`, `V`, `W`, `X` の一文字 status を `FutureWS`, `Variant`, `Rejected`, `NoAction` に置き換える提案が出た。                                            |
| 2025-07-17 | UTC       | [L2/25-199](../documents/utc-l2-25-199.md)                                             | UAX \#45 Revision 31 proposed update が、`ExtJ` と `WS-2024` status、first residual stroke value `6`、Unicode 17.0 additions を反映した。          |
| 2026-04-11 | UTC       | [L2/26-099](../documents/utc-l2-26-099.md)                                             | UTC \#187 向けに 30 UAX \#45 additions を `FutureWS` records として受け入れるよう勧告された。                                                                |
| 2026-07-05 | UTC / IRG | [L2/26-147](../documents/utc-l2-26-147.md) / `IRG N2961`                               | 40 encoded CJK Unified Ideographs へ `kIRG_USource` values と U-source representative glyphs を追加する U-source horizontal extension が提出された。 |

## 抽出したコンセプト

| コンセプト | 意味 | 主な根拠 |
| --- | --- | --- |
| U-source database | UTC に持ち込まれた CJK ideograph candidates と、後から UTC が source reference を引き受けた encoded ideographs の公開 database。 | `L2/07-159`, `L2/08-284`, `L2/25-199` |
| U-source identifier | `UTC-00001` のような stable identifier。現在は `UTC`、obsolete な `UCI`、UK 経由 submission の `UK` prefix が UAX \#45 で説明される。 | `L2/08-284`, `L2/25-199` |
| status field | ideograph の状態を示す field。初期の `C/D/E/U/V/W/X` から、`Ext*`, `FutureWS`, `WS-2024`, `Variant`, `Rejected`, `NoAction` などへ拡張された。 | `L2/08-284`, `L2/22-185`, `L2/25-199` |
| source field | source tag と source-specific index を保持する field。URI、Unihan `k*` sources、UTC document references、dictionary references などを扱う。 | `L2/08-284`, `L2/25-199` |
| representative glyph | U-source record の代表 glyph。IRG の unification work に使う modern style glyph として扱われるが、evidence と乖離すると後続 issue になる。 | `L2/08-284`, `IRG N2511`, `L2/26-147` |
| source evidence | IRG submission で追跡可能性を示す根拠。UAX \#45 source field は候補整理の入口であり、常に current IRG evidence requirement を満たすとは限らない。 | `IRG N1534`, `IRG N1535`, `L2/10-198`, `L2/25-199` |
| FutureWS | UTC が将来の IRG working set submission へ回す候補 status。2026 年の `L2/26-099` では 30 records がこの status で受け入れられた。 | `L2/22-185`, `L2/26-099` |
| `kIRG_USource` | encoded CJK Unified Ideographs に付く U-source reference。source reference の明確化や horizontal extension の対象になる。 | `L2/11-439`, `IRG N2369R`, `L2/26-147` |
| horizontal extension | 新しい code point ではなく、既符号化文字へ source reference と representative glyph を追加する作業。 | `IRG N2369R`, `L2/26-147` |

## 主な論点

### Public / versioned reference としての UAX \#45

[L2/07-159](../documents/utc-l2-07-159.md) は、U-source characters が UTC 内部や過去の L2 documents に埋もれると、WG2 review や U-source attribution correction で参照できないことを問題にした。UAX \#45 はこの問題への答えとして、U-source database 全体を public / versioned reference にし、Unicode Standard や ISO/IEC 10646 から追える source にするために作られた。

[L2/08-284](../documents/utc-l2-08-284.md) では、U-source identifier、status field、source field、glyph / data files が定義された。2025 年の [L2/25-199](../documents/utc-l2-25-199.md) では、UAX \#45 が Unicode Standard Annex として、`USourceData.txt`、`USourceGlyphs.pdf`、`USourceRSChart.pdf` の 3 data files と、`UTC` / `UCI` / `UK` prefixes、長い status values を説明する形に発展している。

### Source evidence と IRG submission

[IRG N1534](../documents/irg-n1534.md) と [IRG N1535](../documents/irg-n1535.md) は、UTC Extension D submission で U-source entries の source evidence を IRG に説明する文書である。UAX \#45 の source field は database 上の出典を表すが、IRG submission では第三者が追跡できる bibliographic evidence、glyph evidence、属性 data が別途必要になる。

この違いは UAX \#45 自体にも残っている。[L2/25-199](../documents/utc-l2-25-199.md) は、UAX \#45 に listed された sources が必ず current IRG evidence requirement を満たすとは限らないと説明する。したがって U-source record は「将来符号化される保証」ではなく、UTC が候補・根拠・処理状態を管理する public record と読む必要がある。

### `kIRG_USource` と source reference の精密化

[L2/11-439](../documents/utc-l2-11-439.md) / `IRG N1825R` は、Adobe-Japan1-6 由来の 27 encoded ideographs が `kIRG_USource` に `UTC-...` として入っている状態を、より正確な `AJ1-...` source reference に置き換える提案である。ここでは representative glyph は変えず、source reference を明確化することが主眼になっている。

現行 UAX \#45 data では Adobe-Japan1 values が source field に残る一方、UAX \#38 の `kIRG_USource` は引き続き UAX \#45 の `UTC-00000` 型 index を参照する property として説明される。そのため `L2/11-439` は、AJ1 evidence の反映と `kIRG_USource` prefix 変更を分けて読む必要がある。

2019 年の [IRG N2369R](../documents/irg-n2369r.md) / `WG2 N5085` と、2026 年の [L2/26-147](../documents/utc-l2-26-147.md) / `IRG N2961` は、encoded ideographs に U-source reference を後付けする horizontal extension である。これは UAX \#45 additions とは逆向きで、未符号化候補を増やすのではなく、既に符号化された文字に `kIRG_USource` values と U-source representative glyphs を追加する。

### FutureWS records と intake capacity

[L2/26-099](../documents/utc-l2-26-099.md) Sections 23-31 は、9 documents から 30 U-source records を受け入れ、`USourceData.txt` と `USourceGlyphs.pdf` に追加する action item を置いた。この decision point は [UTC \#187 UAX \#45 FutureWS additions](../events/utc-187-uax45-futurews-additions.md) に集約する。

`L2/26-099` Section 40 は、Unicode Version 18.0 で UAX \#45 additions が 200 ideographs を超えるため、Unicode Version 19.0 までは CJK & Unihan Working Group が新たな UAX \#45 additions を検討しないと整理した。UAX \#45 は単なる backlog ではなく、UTC から IRG working set へ渡す pipeline の容量管理対象でもある。

### Glyph issue と unification note

[IRG N2511](../documents/irg-n2511.md) は、U+30759 / UTC-01250 の code chart glyph が historical evidence と合わない可能性を指摘し、glyph update または別符号化を提案した。2026 年の [L2/26-147](../documents/utc-l2-26-147.md) も、40 characters の U-source horizontal extension で UCV number や ad hoc unification を source-specific notes として列挙している。U-source では、source reference だけでなく representative glyph と unification rationale も後続 review の対象になる。

### 日本の地名 ideographs

[Japanese Place-Name Ideographs](japanese-place-name-ideographs.md) は、UAX \#45 additions のうち日本の地名・登記資料に基づく提案を束ねる topic である。`L2/25-053`、`L2/25-221`、`L2/26-044` は、Hanyo-Denshi project で網羅されなかった登記・小字名・橋名の文字を、IDS、`kJapanese` reading、radical / stroke data とともに `FutureWS` record として扱う。

UTC \#187 では `L2/26-044` が受理されたが、現行 catalog / cache の範囲では `L2/25-053` と `L2/25-221` の採択 decision は確認できない。UAX \#45 topic では、同じ地名 evidence 系の proposal でも、decision set に入ったものと pending のものを分けて扱う。

## 関連文書

- [L2/07-159](../documents/utc-l2-07-159.md) - U-source database を public / versioned UTR にする提案。
- [L2/07-160](../documents/utc-l2-07-160.md) - Extension C の U-source correction。
- [L2/08-284](../documents/utc-l2-08-284.md) - Draft UTR \#45: U-Source Ideographs。
- [IRG N1534](../documents/irg-n1534.md), [IRG N1535](../documents/irg-n1535.md) - UTC Extension D source descriptions / evidence。
- [L2/11-439](../documents/utc-l2-11-439.md) / `IRG N1825R` - `AJ1` source for `kIRG_USource`。
- [IRG N2369R](../documents/irg-n2369r.md) / `WG2 N5085` - 2019 U-source horizontal extension。
- [IRG N2439](../documents/irg-n2439.md) / `L2/20-204` - two U-source UNC ideographs。
- [IRG N2511](../documents/irg-n2511.md) - U+30759 / UTC-01250 glyph issue。
- [L2/22-185](../documents/utc-l2-22-185.md) - UAX \#45 status value names。
- [L2/25-199](../documents/utc-l2-25-199.md) - UAX \#45 Revision 31 proposed update。
- [L2/26-099](../documents/utc-l2-26-099.md) - UTC \#187 CJK & Unihan Working Group recommendations。
- [L2/26-147](../documents/utc-l2-26-147.md) / `IRG N2961` - 2026 U-source horizontal extension。

## 関連トピック

- [Unihan Database Maintenance](unihan-database-maintenance.md)
- [CJK Horizontal Extensions](cjk-horizontal-extensions.md)
- [IRG Source Data and Representative Glyphs](irg-source-data-and-representative-glyphs.md)
- [IRG Indexing Rules](irg-indexing-rules.md)
- [IRG Working Set 2024](irg-working-set-2024.md)
- [Japanese Place-Name Ideographs](japanese-place-name-ideographs.md)
- [Japanese Historical Ideographs](japanese-historical-ideographs.md)

## 関連出来事

- [UTC \#187 UAX \#45 FutureWS additions](../events/utc-187-uax45-futurews-additions.md)

## 出典

- `utc-l2-07-159` - <https://www.unicode.org/L2/L2007/07159-u-source-db.pdf>
- `utc-l2-07-160` - <https://www.unicode.org/L2/L2007/07160-u-source-correction.pdf>
- `utc-l2-08-284` - <https://www.unicode.org/L2/L2008/08284-utr45-1.pdf>
- `irg-n1534` - <https://www.unicode.org/irg/docs/n1534-USourceDescriptionsExtensionD.pdf>
- `irg-n1535` - <https://www.unicode.org/irg/docs/n1535-USourceEvidenceExtensionD.pdf>
- `utc-l2-11-439` - <https://www.unicode.org/L2/L2011/11439-irgn1825r.pdf>
- `irg-n2369r` - <https://www.unicode.org/irg/docs/n2369r-UnicodeHorizontalExtension.pdf>
- `irg-n2439` - <https://www.unicode.org/irg/docs/n2439-UNC-UTC.pdf>
- `irg-n2511` - <https://www.unicode.org/irg/docs/n2511-USourceGlyphIssue.pdf>
- `utc-l2-22-185` - <https://www.unicode.org/L2/L2022/22185-uax45-status-values.pdf>
- `utc-l2-25-199` - <https://www.unicode.org/L2/L2025/25199-uax45-31-update-pri522.pdf>
- `utc-l2-26-099` - <https://www.unicode.org/L2/L2026/26099-cjk-unihan-wg-utc187.pdf>
- `utc-l2-26-147` - <https://www.unicode.org/L2/L2026/26147-irgn2961-unicodehorizontalextension.pdf>
- `USourceData.txt` - <https://www.unicode.org/Public/UCD/latest/ucd/USourceData.txt>
