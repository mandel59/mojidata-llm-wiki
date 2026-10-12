---
type: Event
title: Unicode 13.0 kZVariant data overhaul
description: "Unicode 13.0 の正式 Unihan data で旧 kZVariant の大幅削除と再構成が反映された出来事。"
slug: unicode-13-kzvariant-data-overhaul
date: "2020-03-10"
bodies: [UTC]
documents: [utc-l2-19-015, utc-l2-19-186, utc-l2-19-281, utc-l2-19-328]
topics: [kzvariant, unihan-database-maintenance, cjk-security-confusables]
people: [john-h-jenkins, utc]
status: published
tags: [event, unicode-13, unihan, kzvariant, data-removal]
timestamp: 2026-10-13T00:00:00+09:00
---

# Unicode 13.0 kZVariant data overhaul

## 概要

2020-03-10 公開の Unicode 13.0 では、Unihan の `kZVariant` データが大幅に削除・再構成された。Unicode 12.0.0 と13.0.0の正式 `Unihan_Variants.txt` を比較すると、方向付き関係は2,562件から144件となる。提案された一覧や committee action の数ではなく、リリースされたデータの変更を表す event である。

## 背景

[L2/19-015](../documents/utc-l2-19-015.md) が旧データの全面置換を提案し、[L2/19-186](../documents/utc-l2-19-186.md) が旧データの生成上の問題と再構成方針を説明した。[L2/19-281](../documents/utc-l2-19-281.md) は文書のいう「93 pairs」の初期候補を提出したが、[L2/19-328](../documents/utc-l2-19-328.md) はその review にも問題があると指摘する。

## 結果

### 正式データの比較

| 集計対象 | Unicode 12.0.0 | Unicode 13.0.0 |
| --- | ---: | ---: |
| `kZVariant` 行（property を持つ code point） | 2,559 | 123 |
| 方向付き関係（A→B） | 2,562 | 144 |
| 方向を無視して重複排除した組（A/B） | 1,653 | 72 |

方向付き関係の差集合では、削除2,503件、追加85件、共通59件である。集計は両版の `Unihan.zip` 内の `Unihan_Variants.txt` を使い、`kZVariant` 行の space-separated value を分割し、`<` 以降の出典注記を除いた code point 同士で比較する。A→B と B→A は別件とし、組数では両方向をまとめる。旧データには片方向しかない関係もあるため、方向付き件数を単純に2で割らない。

[UAX \#44 Revision 26 の Unicode 13.0 変更履歴](https://www.unicode.org/reports/tr44/tr44-26.html#Unicode_13.0.0) は `kZVariant` の「2,438 entries」削除を記録する。この記載は上の正式データ差分の集計とは一致しない。公式記載として保持し、削除された pair 数や行数への換算には使わない。

### 削除された関係の例

| Unicode 12.0 にある関係 | Unicode 13.0 の確認結果 |
| --- | --- |
| `U+7DD2 緒 ↔ U+7DD6 緖` | 両方向の `kZVariant` が削除され、両 code point に `kSpoofingVariant` 行もない。 |
| `U+8B21 謡 → U+8B20 謠` | `kZVariant` が削除され、両 code point に `kSpoofingVariant` 行もない。12.0 の逆方向は元からない。 |
| `U+4E04 丄 ↔ U+4E0A 上` | 両方向の `kZVariant` が削除され、両 code point に `kSpoofingVariant` 行もない。 |

これらは版間差分で確認できる例であり、各 pair の削除理由を個別に示す決定記録ではない。データからの削除は、文字自体の削除や異体字関係一般の否定を意味しない。

## 影響範囲

- [kZVariant](../topics/kzvariant.md)：旧版から引き継ぐ variant mapping は使用版を明示する。provisional data の欠落を「異体字ではない」という判定には使わない。
- [Unihan Database Maintenance](../topics/unihan-database-maintenance.md)：提案の全体方針、個々のデータ採否、正式リリース結果を別々に追う。
- [CJK Security Confusables](../topics/cjk-security-confusables.md)：`kZVariant` からの削除を `kSpoofingVariant` への自動移行とみなさない。

## 関連ページ

- [kZVariant](../topics/kzvariant.md)
- [L2/19-015](../documents/utc-l2-19-015.md)
- [L2/19-186](../documents/utc-l2-19-186.md)
- [L2/19-281](../documents/utc-l2-19-281.md)
- [L2/19-328](../documents/utc-l2-19-328.md)

## 出典

- `utc-l2-19-015` — <https://www.unicode.org/L2/L2019/19015-overhaul-unihan.pdf>
- `utc-l2-19-186` — <https://www.unicode.org/L2/L2019/19186-unihan-ad-hoc-rept.pdf>
- `utc-l2-19-281` — <https://www.unicode.org/L2/L2019/19281-prop-kzvariant.pdf>
- `utc-l2-19-328` — <https://www.unicode.org/L2/L2019/19328-nelson-spoofing.pdf>
- Unicode 13.0.0 公開日2020-03-10。<https://www.unicode.org/versions/Unicode13.0.0/>
- UAX \#44 Revision 26、Unicode 13.0.0 change history。<https://www.unicode.org/reports/tr44/tr44-26.html#Unicode_13.0.0>
- Unicode 12.0.0 正式 Unihan data。<https://www.unicode.org/Public/12.0.0/ucd/Unihan.zip>
- Unicode 13.0.0 正式 Unihan data。<https://www.unicode.org/Public/13.0.0/ucd/Unihan.zip>
