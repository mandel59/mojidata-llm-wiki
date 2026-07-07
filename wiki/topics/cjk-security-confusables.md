---
type: Topic
title: CJK Security Confusables
description: "UTS #39 security data、Unihan kSpoofingVariant / kZVariant、Han identifier policy における CJK confusables。"
slug: cjk-security-confusables
kind: topic
bodies: [UTC, IRG]
documents: [irg-n2206, utc-l2-19-282, utc-l2-19-328, utc-l2-22-133, utc-l2-25-031, utc-l2-26-082, utc-l2-26-086, utc-l2-26-099, utc-l2-26-127]
status: active
tags: [cjk, security, confusables, uts39]
timestamp: 2026-07-07T00:00:00+09:00
---

# CJK Security Confusables

## 概要

CJK Security Confusables は、UTS #39 security data の `confusables.txt` と、CJK glyph / source data の専門判断が交差する topic である。Properties and Algorithms Working Group は confusables data の保守を担うが、CJK ideographs、CJK radicals、Katakana との類似などは CJK Working Group の専門 review を必要とする。CJK ideographs では、視覚的類似性、source separation、semantic distinction、variant property が重なるため、単純な glyph comparison だけでは confusable pair を決めにくい。Katakana 側では、[Kana](kana.md) で扱う alternate Katakana NE / WI のように、子（U+5B50）/ 井（U+4E95）との視覚的類似を proposal 自身が明示する例もある。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2017-06-15 | IRG / UTC | `IRG N2206` | Henry Chan が easily confused ideographs に informative note と cross reference を付ける提案を提出した。UTS #39 data ではなく、意味を区別すべき似た ideographs の annotation proposal である。 |
| 2019-07-18 | UTC | `L2/19-282` | John H. Jenkins が Unihan `kSpoofingVariant` field の初期 data として 48 ideograph pairs を提案した。 |
| 2019-10-03 | UTC | `L2/19-328` | William T. Nelson が `L2/19-282` の data と review process に問題を指摘し、UTC action item `160-A15` の hold を勧告した。 |
| 2022-07-06 | UTC | `L2/22-133` | Ryusei Yamaguchi が `kSpoofingVariant` / `kZVariant` の追加候補を提出した。 |
| 2025-01-14 | UTC | `L2/25-031` | Asmus Freytag が default identifiers 向け common-use Han subset を提出し、subset 外 CJK Unified Ideographs を `Identifier_Type=Uncommon_Use` とすることを提案した。 |
| 2026-03-18 | UTC | `L2/26-082` | PAWG から CJK WG に CJK confusables の review request が提出された。 |
| 2026-03-27 | UTC | `L2/26-086` | David Corbett suggestions 由来の mid-priority confusables data listing が提出された。CJK 専用 review ではないが、Katakana、CJK Compatibility、fullwidth / halfwidth forms などを含む。 |
| 2026-04-11 | UTC | `L2/26-099` | CJK & Unihan Working Group は U+3A36 / U+6440 を除き、新しい CJK confusable pairs を UTS #39 に追加する action item を置いた。 |
| 2026-05-04 | UTC | `L2/26-127` | PAWG が `EquivalentUnifiedIdeograph.txt`、`kSpoofingVariant`、`kZVariant`、platform glyph comparison に基づく CJK confusables data の second review request を提出した。 |

## 主な論点

### CJK WG review の必要性

`L2/26-082` と `L2/26-127` は、候補 pairs を `confusables.txt` に追加できるかどうかの判断を CJK Working Group に求める review request である。PAWG は UTS #39 data maintenance の担当だが、CJK radicals / ideographs の視覚的類似、既存の字形差、source separation、variant property の意味づけは CJK 専門 review に委ねられている。

`L2/26-127` は、候補 pairs を `EquivalentUnifiedIdeograph.txt`、`kSpoofingVariant`、`kZVariant`、Windows / Android glyph comparison などから作る。CJK ideograph の security data は、glyph shape だけでなく、CJK source data と既存 variant relationships を踏まえる必要がある。

### kSpoofingVariant / kZVariant との関係

`L2/19-282` は `kSpoofingVariant` の初期 data proposal、`L2/19-328` はその data と review process への問題提起、`L2/22-133` は `kSpoofingVariant` / `kZVariant` の追加候補である。2026 年の `L2/26-127` は、これらの Unihan variant properties を CJK confusable pair 候補の生成根拠として使っている。

この流れから、CJK security confusables は UTS #39 `confusables.txt` だけでなく、Unihan property maintenance と review discipline に依存する。特に `L2/19-328` は、CJK security-related data では author 以外の expert review、public review の時間、text-based data availability が必要だと指摘した。

### identifier policy との関係

`L2/25-031` は confusable pair ではなく、default identifiers に入る Han character subset を制限する提案である。CJK の security work には、特定 pair を `confusables.txt` に入れる作業と、identifier に common-use として許容する CJK Unified Ideographs の範囲を決める作業の両方がある。

### annotation proposal との関係

`IRG N2206` は、UTS #39 security data ではなく、easily confused ideographs へ informative note と cross reference を付ける提案である。意味を区別すべき似た ideographs を利用者に示すという点で、CJK confusables と隣接するが、data target は `confusables.txt` ではなく CJK ideograph annotation である。

### broader confusables data との切り分け

`L2/26-086` は CJK 専用 review request ではなく、PAWG 向けの mid-priority confusables data listing である。ただし Katakana、Enclosed CJK Letters and Months、CJK Compatibility、Small Form Variants、Halfwidth and Fullwidth Forms などを含むため、CJK 圏の文字・記号が UTS #39 security data に現れる周辺資料として追跡する。

### one-stroke difference の扱い

`L2/26-099` Section 33 は、`L2/26-082` の候補のうち U+3A36 / U+6440 pair を除外した。理由は、U+9CE5 鳥と U+70CF 烏が一画差でも区別されるように、この pair も distinct と判断されたためである。

## 関連文書

- [IRG N2206](../documents/irg-n2206.md)
- [L2/19-282](../documents/utc-l2-19-282.md)
- [L2/19-328](../documents/utc-l2-19-328.md)
- [L2/22-133](../documents/utc-l2-22-133.md)
- [L2/25-031](../documents/utc-l2-25-031.md)
- [L2/26-082](../documents/utc-l2-26-082.md)
- [L2/26-086](../documents/utc-l2-26-086.md)
- [L2/26-099](../documents/utc-l2-26-099.md)
- [L2/26-127](../documents/utc-l2-26-127.md)

## 関連トピック

- [Unihan Database Maintenance](unihan-database-maintenance.md)
- [IRG Source Data and Representative Glyphs](irg-source-data-and-representative-glyphs.md)
- [Kana](kana.md)

## 出典

- `irg-n2206` - <https://www.unicode.org/irg/docs/n2206-EasilyConfusedIdeographs.pdf>
- `utc-l2-19-282` - <https://www.unicode.org/L2/L2019/19282-prop-kspoofing-var.pdf>
- `utc-l2-19-328` - <https://www.unicode.org/L2/L2019/19328-nelson-spoofing.pdf>
- `utc-l2-22-133` - <https://www.unicode.org/L2/L2022/22133-kspoofing-kzvariant-cand.pdf>
- `utc-l2-25-031` - <https://www.unicode.org/L2/L2025/25031-common-use-han-subset.html>
- `utc-l2-26-082` - <https://www.unicode.org/L2/L2026/26082-review-cjk-confusables.pdf>
- `utc-l2-26-086` - <https://www.unicode.org/L2/L2026/26086-mid-priority-confusables-data.pdf>
- `utc-l2-26-099` - <https://www.unicode.org/L2/L2026/26099-cjk-unihan-wg-utc187.pdf>
- `utc-l2-26-127` - <https://www.unicode.org/L2/L2026/26127-2nd-cjk-confusables.pdf>
