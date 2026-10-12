---
type: Topic
title: kZVariant
description: "Unihan の Z-variant property、Unicode 12.0→13.0 のデータ見直しと大量削除、spoofing variants との境界。"
slug: kzvariant
aliases: [Z-variants, Unihan kZVariant]
bodies: [UTC]
documents: [utc-l2-15-266, utc-l2-19-015, utc-l2-19-008, utc-l2-19-186, utc-l2-19-122, utc-l2-19-281, utc-l2-19-282, utc-l2-19-270, utc-l2-19-328, utc-l2-22-133, utc-l2-26-127]
topics: [unihan-database-maintenance, unihan-data-format-and-property-syntax, cjk-security-confusables, ucv-nucv-lists]
people: [john-h-jenkins, utc]
meetings: [utc-meeting-158, utc-meeting-159, utc-meeting-160]
events: [unicode-13-kzvariant-data-overhaul]
status: active
tags: [cjk, unihan, variants, kzvariant, unicode-13]
timestamp: 2026-10-13T00:00:00+09:00
---

# kZVariant

## 概要

`kZVariant` は Unihan の provisional property で、Z-variants を記録する。Unicode 13.0 の UAX \#38 は、同じ abstract shape と semantics を持つ文字が、誤りや source separation によって複数回符号化された関係と説明する。一般的な異体字すべてや、意味を問わない視覚的類似を網羅する property ではない。

Unicode 12.0→13.0 の大量削除を調べる入口は、見直し提案 [L2/19-015](../documents/utc-l2-19-015.md)、理由を説明する [L2/19-186](../documents/utc-l2-19-186.md)、初期データ提案 [L2/19-281](../documents/utc-l2-19-281.md) である。確定データの件数と削除例は [Unicode 13.0 の見直し event](../events/unicode-13-kzvariant-data-overhaul.md) を参照。

## 経緯

| 日付 | Body | 文書・一次出典 | できごと |
| --- | --- | --- | --- |
| 2015-10-29 | UTC | [L2/15-266](../documents/utc-l2-15-266.md) | 旧データの全面置換と定義の明確化を提案。本文日付は10月26日。 |
| 2019-01-07 | UTC | [L2/19-015](../documents/utc-l2-19-015.md) | Unicode 13.0 向けに旧提案を改訂し、関係分類・locale・出典を持つ syntax も提案。 |
| 2019-01-15 | UTC \#158 | [L2/19-008、158-A58](https://www.unicode.org/L2/L2019/19008.htm#158-A58) | John Jenkins に Unihan mail list での議論と第2四半期 UTC への報告を指示。 |
| 2019-04-29 | UTC | [L2/19-186](../documents/utc-l2-19-186.md) | 旧データの生成上の問題、Z-variants と spoofing variants の境界、データ再構成を報告。 |
| 2019-05-01 | UTC \#159 | [L2/19-122、159-C11](https://www.unicode.org/L2/L2019/19122.htm#159-C11) | 新 field の UAX \#38 proposed update と public review を進める。個々の `kZVariant` pair の採択とは別。 |
| 2019-07-18 | UTC | [L2/19-281](../documents/utc-l2-19-281.md) | 文書が「93 pairs」と呼ぶ初期データで既存内容を置換する提案。 |
| 2019-10-03 | UTC | [L2/19-328](../documents/utc-l2-19-328.md) | `kSpoofingVariant` データの review に異議を述べ、note で `kZVariant` 提案にも同じ問題があると指摘。 |
| 2020-03-10 | UTC / Unicode release | [Unicode 13.0 の見直し](../events/unicode-13-kzvariant-data-overhaul.md) | 正式データの変更、集計方法、削除例は canonical event を参照。 |
| 2022-07-06 | UTC | [L2/22-133](../documents/utc-l2-22-133.md) | 追加候補を提出。全面見直し後にも未収録の関係を指摘する。 |
| 2026-05-04 | UTC | [L2/26-127](../documents/utc-l2-26-127.md) | `kZVariant` を CJK confusable pair 候補生成の根拠の一つに使う。 |

## 主な論点

### 旧データを取り除いた理由：再構成方針と個別採否

[L2/19-186](../documents/utc-l2-19-186.md) は、CCCII の構造の誤解に基づく機械生成と校正の欠如を旧データの品質問題として挙げる。これがほぼ全面的な再構成を求めた根拠である。ただし、各削除 pair の理由を一件ずつ説明する文書ではない。個別関係の有無は使用する版の正式データで確認する。

### 定義と syntax：旧提案を確定仕様にしない

[L2/15-266](../documents/utc-l2-15-266.md) / [L2/19-015](../documents/utc-l2-19-015.md) は non-cognate rule による別符号化も定義案に含める。一方、[L2/19-186](../documents/utc-l2-19-186.md) と [Unicode 13.0 の UAX \#38](https://www.unicode.org/reports/tr38/tr38-28.html#kZVariant) は、semantics と abstract shape の同一性を明示する。

`L2/19-015` の関係分類 `[DINSU]` と locale syntax は Unicode 13.0 の確定 syntax に入っていない。確定版は code point と、任意の Unihan field tag による出典注記を使う。data format の横断的な説明は [Unihan Data Format and Property Syntax](unihan-data-format-and-property-syntax.md) を参照。

### 提案の「93 pairs」と確定データ：同一視しない

[L2/19-281](../documents/utc-l2-19-281.md) は preliminary data set の提案であり、最終収録一覧ではない。[L2/19-328](../documents/utc-l2-19-328.md) は review 上の問題を指摘し、UTC \#160 minutes に `L2/19-281` の参照がないことにも触れる。`160-A15` は `L2/19-282` の spoofing field に関する指示であり、`kZVariant` の採択記録として代用しない。確定件数との比較は [release event](../events/unicode-13-kzvariant-data-overhaul.md) に置く。

### kSpoofingVariant との境界：削除は自動移行ではない

Z-variants は同じ semantics と abstract shape を持つ関係、spoofing variants は意味を問わず似た glyph による誤認に関わる関係である。Unicode 13.0 の仕様は `kSpoofingVariant` に Z-variants / compatibility variants 以外の spoofing variants を記録する。削除された関係が他 property に収録されたかは別途確認する必要がある。security data の用途は [CJK Security Confusables](cjk-security-confusables.md) にまとめる。

### 欠落の読み方：provisional data は網羅的ではない

データに関係がないことだけで、異体字ではないと判定しない。[L2/22-133](../documents/utc-l2-22-133.md) は、`緖` / `緒`、`謠` / `謡` を Z-variant 候補として再び挙げるが、候補提出と採択・収録は別である。`kZVariant` の変更は code point の廃止や正規化 mapping の変更でもない。

## 関連文書

- [L2/15-266](../documents/utc-l2-15-266.md) — 2015年の全面置換提案。
- [L2/19-015](../documents/utc-l2-19-015.md) — Unicode 13.0 向け改訂提案。
- [L2/19-186](../documents/utc-l2-19-186.md) — 旧データの問題と field 間の境界を説明する report。
- [L2/19-281](../documents/utc-l2-19-281.md) — 初期置換データの提案。
- [L2/19-282](../documents/utc-l2-19-282.md) — 同時期の `kSpoofingVariant` 初期データ提案。
- [L2/19-328](../documents/utc-l2-19-328.md) — データと review process への異議。
- [L2/22-133](../documents/utc-l2-22-133.md) — 後年の追加候補。
- [L2/26-127](../documents/utc-l2-26-127.md) — CJK confusables review request。
- `L2/19-008` / `L2/19-122` / `L2/19-270` — UTC \#158 / \#159 / \#160 minutes。決定箇所は経緯表と出典を参照。

## 関連トピック

- [Unihan Database Maintenance](unihan-database-maintenance.md)
- [Unihan Data Format and Property Syntax](unihan-data-format-and-property-syntax.md)
- [CJK Security Confusables](cjk-security-confusables.md)
- [UCV and NUCV Lists](ucv-nucv-lists.md)
- [Han Ideographic Scripts](../families/han-ideographic-scripts.md)

## 出典

- `utc-l2-15-266` — <https://www.unicode.org/L2/L2015/15266-kzvariant-overhaul.pdf>
- `utc-l2-19-015` — <https://www.unicode.org/L2/L2019/19015-overhaul-unihan.pdf>
- `utc-l2-19-008` — <https://www.unicode.org/L2/L2019/19008.htm>
- `utc-l2-19-186` — <https://www.unicode.org/L2/L2019/19186-unihan-ad-hoc-rept.pdf>
- `utc-l2-19-122` — <https://www.unicode.org/L2/L2019/19122.htm>
- `utc-l2-19-281` — <https://www.unicode.org/L2/L2019/19281-prop-kzvariant.pdf>
- `utc-l2-19-282` — <https://www.unicode.org/L2/L2019/19282-prop-kspoofing-var.pdf>
- `utc-l2-19-270` — <https://www.unicode.org/L2/L2019/19270.htm>
- `utc-l2-19-328` — <https://www.unicode.org/L2/L2019/19328-nelson-spoofing.pdf>
- `utc-l2-22-133` — <https://www.unicode.org/L2/L2022/22133-kspoofing-kzvariant-cand.pdf>
- `utc-l2-26-127` — <https://www.unicode.org/L2/L2026/26127-2nd-cjk-confusables.pdf>
- UAX \#38 Revision 28、Unicode 13.0 の確定仕様。<https://www.unicode.org/reports/tr38/tr38-28.html#kZVariant>
