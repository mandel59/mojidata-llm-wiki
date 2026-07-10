---
type: Topic
title: Mathematical Text Support
description: "UTR #25 を入口に、Unicode の数学文字 repertoire、Math property、math data files、plain-text math と markup の境界を扱う topic。"
slug: mathematical-text-support
aliases: ["UTR #25", "Unicode Support for Mathematics", "MathClass"]
bodies: [UTC]
documents: [pri-533, utc-l2-25-267, utc-l2-26-140, utc-l2-26-141, utc-l2-26-142, utc-l2-26-143, utc-l2-26-149]
topics: [unicode-properties-and-algorithms, leibnizian-and-historic-mathematical-symbols, plain-text-composition-and-overstriking, unicode-set-notation]
meetings: [utc-meeting-188]
status: active
tags: [math, mathematical-text, utr25, properties, data-files, text-model]
timestamp: 2026-07-10T00:00:00+09:00
---

# Mathematical Text Support

## 概要

Mathematical Text Support は、Unicode の数学文字 repertoire、mathematical alphanumeric symbols、`Math` property、math data files、plain-text math と MathML / TeX / UnicodeMath などの markup / notation systems の境界を扱う topic である。

[PRI \#533](../documents/pri-533.md) は UTR \#25 Unicode Support for Mathematics Revision 16 draft の public review であり、2026-07-10 時点では status が Open のままである。今回の draft は主に HTML migration と structural cleanup を扱うが、Unicode 9 から Unicode 17 までの characters / properties / examples / tables を取り込む後続 content update の前段でもある。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2025-10-24 | UTC | [L2/25-267](../documents/utc-l2-25-267.md) | Barbara Beeton らが UTR \#25 Revision 16 proposed update を登録した。 |
| 2026-05-26 | UTC / WG2 | [L2/26-140](../documents/utc-l2-26-140.md), [L2/26-141](../documents/utc-l2-26-141.md), [L2/26-142](../documents/utc-l2-26-142.md), [L2/26-143](../documents/utc-l2-26-143.md) | historic mathematical sources / Leibnizian signs 用の symbols、combining marks、letterlike symbols、variation sequences が UTC \#188 / WG2 Amendment 1 候補として提出された。 |
| 2026-07-05 | UTC | [L2/26-149](../documents/utc-l2-26-149.md) | Leibnizian VS names と Unicode 18.0 delta charts への feedback が提出された。 |
| 2026-07-07 | PRI | [PRI \#533](../documents/pri-533.md) | UTR \#25 Revision 16 draft 2 public review の closing date。2026-07-10 時点で PRI page / catalog は Open。 |

## 主な論点

### UTR \#25 の役割

UTR \#25 は Unicode Standard 本体の conformance rule ではなく、数学文字 repertoire と実装上の扱いを説明する informative technical report である。数式で使われる plain text characters、MathML / OpenMath / TeX / UnicodeMath、programming language での use、math data files を横断して扱う。

Revision 16 draft は HTML 化が中心で、content は Unicode 9 support から Unicode 17 support へ更新中の段階である。したがって、現時点では UTR \#25 を「最新数学文字全体の完全な最終整理」としてではなく、更新作業中の review artifact として読む。

### Math property と MathClass data

UTR \#25 は、UCD の `Math` property と、数学文字の primary usage を分類する `MathClass-16.txt` / mapping data `MathClassEx-16.txt` を実装入口として示す。`Math_Class` は UCD property そのものではなく UTR \#25 側の informative data なので、UAX \#44 / UCD property model とは層を分けて読む必要がある。

### plain text と markup

Mathematical alphanumeric symbols は、数式内で font style に見える差が semantic distinction になる場合に plain text character として必要になる。一方で、built-up fractions、large delimiters、layout、annotation は MathML / TeX / UnicodeMath などの higher-level representation と関係する。Unicode character encoding と markup / rendering engine の責任分担が、この topic の中心論点である。

### historic mathematical symbols との境界

[Leibnizian and Historic Mathematical Symbols](leibnizian-and-historic-mathematical-symbols.md) は、historical sources の特殊 symbols / variation sequences を個別 proposal として扱う。この topic は、それらを含むかどうかの採否ではなく、Unicode における数学文字 support 全体、math data、plain-text math の実装方針を扱う。

### security

数学用 alphanumeric symbols は、regular text の styled letters と混同されやすい。UTR \#25 draft は domain names など security sensitive environments での除外に触れており、UTS \#39 / identifier policy と隣接する。

## 関連文書

- [PRI \#533](../documents/pri-533.md) - UTR \#25 Revision 16 public review。
- [L2/25-267](../documents/utc-l2-25-267.md) - UTR \#25 Revision 16 proposed update。
- [L2/26-140](../documents/utc-l2-26-140.md) - miscellaneous mathematical symbols。
- [L2/26-141](../documents/utc-l2-26-141.md) - slashed digits 用 combining marks。
- [L2/26-142](../documents/utc-l2-26-142.md) - historic letterlike symbols。
- [L2/26-143](../documents/utc-l2-26-143.md) - Leibnizian ambiguous signs。
- [L2/26-149](../documents/utc-l2-26-149.md) - Leibniz Unicode Characters Project feedback。

## 関連トピック

- [Unicode Properties and Algorithms](unicode-properties-and-algorithms.md)
- [Leibnizian and Historic Mathematical Symbols](leibnizian-and-historic-mathematical-symbols.md)
- [Plain-Text Composition and Overstriking](plain-text-composition-and-overstriking.md)
- [Unicode Set Notation](unicode-set-notation.md)

## 出典

- `pri-533` - <https://www.unicode.org/review/pri533/>
- UTR \#25 Revision 16 draft 2 - <https://www.unicode.org/reports/tr25/tr25-16d2.html>
- `utc-l2-25-267` - <https://www.unicode.org/L2/L2025/25267-utr25-update-16-pri533.pdf>
