---
type: Topic
title: Ideographic Variation Database
description: "IVD の collection、IVS 登録履歴、UTS #37、public review と登録後の正式データを追う入口。"
slug: ideographic-variation-database
aliases: [IVD, Ideographic Variation Database, "UTS #37"]
bodies: [UTC, WG2, IRG]
documents: [pri-98, pri-108, pri-167, pri-183, pri-187, pri-259, pri-326, pri-349, pri-351, pri-354, pri-418, pri-456, pri-521, pri-546, utc-l2-26-112, utc-l2-26-215, utc-l2-26-070r, irg-n2767, wg2-n5221, irg-n2722, wg2-n5089]
topics: [jmj-horizontal-extension-review-path, cjk-horizontal-extensions, unihan-data-format-and-property-syntax, unihan-database-maintenance, ucv-nucv-lists, cjk-strokes-variation-sequences, small-seal-script]
people: [ken-lunde, japan, eiso-chan]
events: [ivd-2025-07-14-caaph-registration, ivd-2026-08-03-moji-joho-registration]
status: active
tags: [ivd, uts37, cjk, variation-sequences, registration]
timestamp: 2026-10-11T00:00:00+09:00
---

# Ideographic Variation Database

## 概要

Ideographic Variation Database (IVD) は、漢字と variation selector の組合せで字形の範囲を指定する Ideographic Variation Sequence (IVS) の登録データベースである。Unicode Consortium が registration authority、IVD Registrar が登録手続を担当する。collection は利用目的ごとに IVS と glyph identifiers を束ねる。

2026-10-11 確認時点の最新版は **IVD 2026-08-03**、登録済み collection は 6。直近の変更は [Moji_Joho 追加登録](../events/ivd-2026-08-03-moji-joho-registration.md)で追う。手続とデータ形式の仕様は **UTS \#37 Version 7.0 / Revision 16 (2026-04-30)**。仕様の版、IVD データの日付、Unicode の文字 repertoire の版はそれぞれ独立して確認する。

まず [IVD 公式ページ](https://www.unicode.org/ivd/) の release history / review 状態を確認し、対象 PRI の archive、日付付き正式データ、collection page の順で読む。以下の登録履歴は公式 IVD history に基づく。

## 経緯

| 登録日 / 仕様公開日 | 担当 | 文書・出典 | できごと |
| --- | --- | --- | --- |
| 2007-12-14 | IVD Registrar | PRI \#98 / \#108; [IVD history](https://www.unicode.org/ivd/) | Adobe-Japan1 の初回登録。 |
| 2010-11-14 | IVD Registrar | PRI \#167; [IVD history](https://www.unicode.org/ivd/) | Hanyo-Denshi の初回登録。 |
| 2012-03-02 | IVD Registrar | PRI \#183 / \#187; [IVD history](https://www.unicode.org/ivd/) | Adobe-Japan1 と Hanyo-Denshi への追加登録。 |
| 2014-05-16 | IVD Registrar | [PRI \#259](../documents/pri-259.md) | Moji_Joho の初回登録。 |
| 2016-08-15 | IVD Registrar | PRI \#326; [IVD history](https://www.unicode.org/ivd/) | MSARG の初回登録。 |
| 2017-12-12 | IVD Registrar | PRI \#349 / \#351; [PRI \#354](../documents/pri-354.md) | Adobe-Japan1 / Moji_Joho 追加登録と KRName 初回登録。 |
| 2020-11-06 | IVD Registrar | [PRI \#418](../documents/pri-418.md) | MSARG 追加登録。review comments により一部代表字形を調整。 |
| 2022-09-13 | IVD Registrar | [PRI \#456](../documents/pri-456.md) | Adobe-Japan1-7 の Extension H ideograph に対応する追加登録。 |
| 2025-07-14 | IVD Registrar | [CAAPH 登録 event](../events/ivd-2025-07-14-caaph-registration.md); [PRI \#521](../documents/pri-521.md) | CAAPH 初回登録。 |
| 2026-04-30 | Unicode Consortium | [UTS \#37 Revision 16](https://www.unicode.org/reports/tr37/tr37-16.html); [L2/26-112](../documents/utc-l2-26-112.md) | proposed Revision 15 に続く仕様公開。collection URL を registrar が確立・維持する扱いへ更新。 |
| 2026-08-03 | IVD Registrar | [Moji_Joho 登録 event](../events/ivd-2026-08-03-moji-joho-registration.md); [PRI \#546](../documents/pri-546.md) | 第10版 IVD。Moji_Joho の追加登録と collection URL 更新。 |
| 2026-09-17 | UTC / IRG | [L2/26-215 / IRG N2944](../documents/utc-l2-26-215.md) | US/Unicode activity report が 8 月の公開を報告。会合決定ではなく登録済みデータの報告。 |

## 主な論点

### 登録済み collections

以下は IVD 2026-08-03 の collection 別登録件数。複数 collection が同じ base / VS pair を共有できるため、合計は distinct IVS 数ではない。

| Collection | 初回登録 | 最新登録更新 | 登録件数 | 関連 PRI |
| --- | --- | --- | ---: | --- |
| Adobe-Japan1 | 2007-12-14 | 2022-09-13 | 14,684 | PRI \#98 / \#108 / \#183 / \#349; [PRI \#456](../documents/pri-456.md) |
| Hanyo-Denshi | 2010-11-14 | 2012-03-02 | 13,045 | PRI \#167 / \#187 |
| Moji_Joho | 2014-05-16 | 2026-08-03 | 11,392 | [PRI \#259](../documents/pri-259.md), [PRI \#354](../documents/pri-354.md), [PRI \#546](../documents/pri-546.md) |
| MSARG | 2016-08-15 | 2020-11-06 | 154 | PRI \#326; [PRI \#418](../documents/pri-418.md) |
| KRName | 2017-12-12 | 2017-12-12 | 36 | PRI \#351 |
| CAAPH | 2025-07-14 | 2025-07-14 | 198 | [PRI \#521](../documents/pri-521.md) |

### 仕様改訂と正式データ

UTS \#37 は IVS の適格性、登録手続、データ形式を規定する。base character は `Ideographic` property を持ち、canonical / compatibility decomposition を持たない文字で、VS は U+E0100〜U+E01EF を使う。登録した IVS と glyphic subset の対応は恒久的で、別の subset へ再割当しない。

`IVD_Collections.txt` は collection identifier・identifier pattern・説明 URL、`IVD_Sequences.txt` は base / VS pair・collection・sequence identifier を記録する。`IVD_Stats.txt` は collection 別件数などを確認する補助資料として使う。仕様改訂は [L2/26-112](../documents/utc-l2-26-112.md) と正式な Revision 16 を併読する。

### Public review と登録完了

collection と sequence の登録には、それぞれ少なくとも 90 日の public review がある。同時申請もできる。review closing date は登録日ではなく、PRI page の冒頭に当初の「review 中」という文言が残っていても、archive の登録完了追記と IVD release history を確認する。

IVD 公式ページでは 2026-10-11 確認時点に審査中の submission はない。[PRI \#546](../documents/pri-546.md) は Resolved Issues に掲載され、archive も登録完了を記録する。具体的な割当は [2026-08-03 event](../events/ivd-2026-08-03-moji-joho-registration.md) を参照する。登録完了の一次根拠は PRI archive と日付付き正式データである。

### 字形共有、mapping correction、使用非推奨

collection 間で同じ glyphic subset の sequence を共有することは推奨されるが、必須ではなく登録者間の合意に基づく。Hanyo-Denshi と Moji_Joho の共有は [PRI \#259](../documents/pri-259.md) と [PRI \#354](../documents/pri-354.md) に実例がある。

JMJ の source mapping correction が IVD に波及した経緯は [JMJ Horizontal Extension Review Path](jmj-horizontal-extension-review-path.md)、具体的な割当と非規範的な使用非推奨は [2026-08-03 event](../events/ivd-2026-08-03-moji-joho-registration.md) を読む。使用非推奨と、正式データからの削除・登録抹消を同一視しない。

### 他の variation mechanisms との境界

IVD の IVS、`StandardizedVariants.txt` の standardized variation sequences、emoji variation sequences は別の登録・データ経路を持つ。[L2/26-070R](../documents/utc-l2-26-070r.md) は variation selector conformance を横断して扱う提案であり、IVD への新規登録結果ではない。[CJK Strokes Variation Sequences](cjk-strokes-variation-sequences.md) も IVD collection とは分ける。

[WG2 N5089](../documents/wg2-n5089.md) の informal meeting report が記録する IVS の検討は、字形と独立文字の区別を考える関連論点である。Small Seal の IVD collection 登録が成立した根拠としては扱わない。

### 継続して確認する資料

更新確認では、IVD 公式ページの新 release / submission と、PRI archive の登録結果を照合し、前版との `IVD_Collections.txt` / `IVD_Sequences.txt` 差分を読む。collection page の代表字形・注意事項も確認する。activity report に登録完了が載った場合は、対応する PRI、event、topic まで接続する。

UTS \#37 は proposed update と確定版を分け、登録申請は review 期間と実際の登録日を分けて追う。IRG の endorsement や source-data correction は背景資料として読み、Registrar の登録完了と混同しない。

## 関連文書

- [PRI \#259](../documents/pri-259.md)、[PRI \#354](../documents/pri-354.md)、[PRI \#546](../documents/pri-546.md) - Moji_Joho の初回登録と追加登録。
- [PRI \#418](../documents/pri-418.md) - MSARG と MSCS-2020。
- [PRI \#456](../documents/pri-456.md) - Adobe-Japan1-7 / Extension H。
- [PRI \#521](../documents/pri-521.md)、[IRG N2767](../documents/irg-n2767.md) - CAAPH の登録申請と IRG editorial report。
- [L2/26-112](../documents/utc-l2-26-112.md) - UTS \#37 Revision 15 proposed update (PRI \#541)。
- [L2/26-215 / IRG N2944](../documents/utc-l2-26-215.md) - IVD 2026-08-03 公開後の activity report。
- [WG2 N5221](../documents/wg2-n5221.md)、[IRG N2722](../documents/irg-n2722.md) - JMJ horizontal extension と source / glyph 対応。
- [L2/26-070R](../documents/utc-l2-26-070r.md) - variation selector conformance の横断提案。
- [WG2 N5089](../documents/wg2-n5089.md) - Small Seal informal meeting report の IVS 検討。

## 関連トピック

- [JMJ Horizontal Extension Review Path](jmj-horizontal-extension-review-path.md)
- [CJK Horizontal Extensions](cjk-horizontal-extensions.md)
- [Unihan Data Format and Property Syntax](unihan-data-format-and-property-syntax.md)
- [Unihan Database Maintenance](unihan-database-maintenance.md)
- [UCV and NUCV Lists](ucv-nucv-lists.md)
- [CJK Strokes Variation Sequences](cjk-strokes-variation-sequences.md)
- [Small Seal Script](small-seal-script.md)
- [Han Ideographic Scripts](../families/han-ideographic-scripts.md)

## 出典

- PRI Resolved Issues - <https://www.unicode.org/review/resolved.html> (2026-10-11 確認)。
- IVD 登録履歴・collections・review 状態 - <https://www.unicode.org/ivd/> (2026-10-11 確認)。
- UTS \#37 Version 7.0 / Revision 16, 2026-04-30 - <https://www.unicode.org/reports/tr37/tr37-16.html>。
- IVD 2026-08-03 - <https://www.unicode.org/ivd/data/2026-08-03/IVD_Collections.txt>、<https://www.unicode.org/ivd/data/2026-08-03/IVD_Sequences.txt>、<https://www.unicode.org/ivd/data/2026-08-03/IVD_Stats.txt>。
- `pri-259` - <https://www.unicode.org/ivd/pri/pri259/>
- `pri-354` - <https://www.unicode.org/ivd/pri/pri354/>
- `pri-418` - <https://www.unicode.org/ivd/pri/pri418/>
- `pri-456` - <https://www.unicode.org/ivd/pri/pri456/>
- `pri-521` - <https://www.unicode.org/ivd/pri/pri521/>
- `pri-546` - <https://www.unicode.org/ivd/pri/pri546/>
- `utc-l2-26-112` - <https://www.unicode.org/L2/L2026/26112-uts37-15-update-pri541.pdf>
- `utc-l2-26-215` - <https://www.unicode.org/L2/L2026/26215-irgn2944-activity-rept.pdf>
- `irg-n2767` - <https://www.unicode.org/irg/docs/n2767-MiscEditorialReport.pdf>
- `wg2-n5221` - <https://www.unicode.org/wg2/docs/n5221-JNB_contribution_2304.pdf>
- `irg-n2722` - <https://www.unicode.org/irg/docs/n2722-JSourceIssues.pdf>
- `utc-l2-26-070r` - <https://www.unicode.org/L2/L2026/26070r-multiple-variation-selectors-non-conformant.pdf>
- `wg2-n5089` - <https://unicode.org/wg2/docs/n5089_Shuowen%20Seal%20Informal%20Meeting%20Report.pdf>
- `pri-98` - <https://www.unicode.org/review/resolved-pri.html#pri-98>
- `pri-108` - <https://www.unicode.org/review/resolved-pri-100.html#pri-108>
- `pri-167` - <https://www.unicode.org/review/resolved-pri-100.html#pri-167>
- `pri-183` - <https://www.unicode.org/ivd/pri/pri183/>
- `pri-187` - <https://www.unicode.org/ivd/pri/pri187/>
- `pri-326` - <https://www.unicode.org/ivd/pri/pri326/>
- `pri-349` - <https://www.unicode.org/ivd/pri/pri349/>
- `pri-351` - <https://www.unicode.org/ivd/pri/pri351/>
