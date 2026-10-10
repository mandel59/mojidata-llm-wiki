---
type: Event
title: "IVD 2026-08-03 Moji_Joho registration"
description: "IVD Registrar が PRI #546 の review を経て Moji_Joho collection に 8 IVS を追加登録し、IVD 2026-08-03 を公開した出来事。"
slug: ivd-2026-08-03-moji-joho-registration
date: "2026-08-03"
bodies: [UTC]
documents: [pri-546, wg2-n5221]
topics: [jmj-horizontal-extension-review-path, cjk-horizontal-extensions, unihan-data-format-and-property-syntax, unihan-database-maintenance]
people: [japan, ken-lunde]
status: registered
tags: [event, ivd, moji-joho, variation-sequences, jmj]
timestamp: 2026-10-10T00:00:00+09:00
---

# IVD 2026-08-03 Moji_Joho registration

## 概要

IVD Registrar は、2026-07-31 に終了した [PRI \#546](../documents/pri-546.md) の review を経て、2026-08-03 版の Ideographic Variation Database (IVD) を公開した。Moji_Joho collection に 5 base characters に対する 8 IVS を追加登録し、同 collection の登録件数は 11,384 から 11,392 になった。8 件のうち 1 件は Hanyo-Denshi と共有し、7 件は新しい base / VS pair である。

これは IVD の登録完了であり、UTC 会合による文字符号化の採択を表す event ではない。正式な割当は同日版の `IVD_Sequences.txt` で確認できる。

## 背景

Japan の [WG2 N5221](../documents/wg2-n5221.md) による JMJ horizontal extension が Unicode 16.0 / ISO/IEC 10646:2020/Amd.2:2025 に取り込まれる過程で、Moji Jōhō Kiban database の 46 glyphs の対応 code points が更新された。その follow-up として ITSCJ / IPSJ が追加登録を申請し、Shuichi Tashiro が representative を務めた。PRI の提案内容と review instructions は [PRI \#546](../documents/pri-546.md) にまとめる。

## 結果

### 登録された IVS

2025-07-14 版と 2026-08-03 版の `IVD_Sequences.txt` を比較すると、次の 8 行が追加され、削除行はない。提案時に未割当だった VS も正式データでは確定している。

| Base / VS | Collection identifier | Sequence identifier |
| --- | --- | --- |
| `7CA4 E0103` | Moji_Joho | `MJ058288` |
| `805A E0102` | Moji_Joho | `MJ020851` |
| `805A E0104` | Moji_Joho | `MJ058367` |
| `20509 E0103` | Moji_Joho | `MJ057273` |
| `23AA3 E0100` | Moji_Joho | `MJ038918` |
| `23AA3 E0101` | Moji_Joho | `MJ057925` |
| `26BE7 E0100` | Moji_Joho | `MJ046446` |
| `26BE7 E0101` | Moji_Joho | `MJ046463` |

`805A E0102` は Hanyo-Denshi の `JA7060` と共有する。IVD の collection 数は 6 のままで、新規 collection の登録ではない。

### 使用非推奨の既登録 sequences

Moji_Joho の公式 collection page は、登録者が非規範的に deprecated とする 9 件を使用しないよう案内している。対象は `535A E010A` / `535A E010B`、`617A E0103`、`238A7 E0100` / `238A7 E0101`、`24138 E0100` / `24138 E0101`、`27369 E0100` / `27369 E0101` である。これらは 2026-08-03 版の `IVD_Sequences.txt` に残っており、登録抹消や規範的な無効化とは区別する。

### Collection URL

`IVD_Collections.txt` では Adobe-Japan1 の URL が `https://github.com/adobe-type-tools/Adobe-Japan1/` から `https://www.unicode.org/ivd/adobe-japan1/` に、Moji_Joho の URL が `https://moji.or.jp/mojikiban/` から `https://www.unicode.org/ivd/moji_joho/` に更新された。collection identifier と sequence identifier pattern は前版から変わっていない。

## 影響範囲

[JMJ Horizontal Extension Review Path](../topics/jmj-horizontal-extension-review-path.md) から見ると、既存文字の source reference addition が IVD collection maintenance に波及した節目である。[Unihan Data Format and Property Syntax](../topics/unihan-data-format-and-property-syntax.md) からは、UTS \#37 の registration process と正式な IVD data files を結び付ける実例として読む。Unicode 18.0 の文字 repertoire 更新や WG2 の J-source glyph revert とは別の状態変更である。

## 関連ページ

- [PRI \#546](../documents/pri-546.md) - 追加登録の提案と review。
- [JMJ Horizontal Extension Review Path](../topics/jmj-horizontal-extension-review-path.md)
- [CJK Horizontal Extensions](../topics/cjk-horizontal-extensions.md)
- [Unihan Data Format and Property Syntax](../topics/unihan-data-format-and-property-syntax.md)
- [Unihan Database Maintenance](../topics/unihan-database-maintenance.md)
- [Japan](../people/japan.md)
- [Ken Lunde](../people/ken-lunde.md)

## 出典

- `pri-546` - <https://www.unicode.org/ivd/pri/pri546/>。review closing date: 2026-07-31。archive の追記が 2026-08-03 版への登録を明記する。
- IVD version history / collection counts - <https://www.unicode.org/ivd/>
- IVD 2026-08-03 data - <https://www.unicode.org/ivd/data/2026-08-03/IVD_Sequences.txt>、<https://www.unicode.org/ivd/data/2026-08-03/IVD_Collections.txt>、<https://www.unicode.org/ivd/data/2026-08-03/IVD_Stats.txt>
- 比較対象の IVD 2025-07-14 data - <https://www.unicode.org/ivd/data/2025-07-14/IVD_Sequences.txt>、<https://www.unicode.org/ivd/data/2025-07-14/IVD_Collections.txt>
- Moji_Joho collection details / non-normative deprecation - <https://www.unicode.org/ivd/moji_joho/>
- `wg2-n5221` - <https://www.unicode.org/wg2/docs/n5221-JNB_contribution_2304.pdf>
