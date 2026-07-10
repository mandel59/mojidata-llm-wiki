---
type: Topic
title: Leibnizian and Historic Mathematical Symbols
description: "Leibnizian ambiguous signs と historic mathematical sources 用 symbols / combining marks / letterlike symbols。"
slug: leibnizian-and-historic-mathematical-symbols
bodies: [UTC, WG2]
documents: [pri-533, utc-l2-25-131, utc-l2-26-140, utc-l2-26-141, utc-l2-26-142, utc-l2-26-143, utc-l2-26-149, wg2-n5354, wg2-n5361r, wg2-n5364]
topics: [mathematical-text-support, unicode-18-change-sources, script-encoding-pipeline]
status: proposed
tags: [math, leibniz, symbols, variation-sequences, unicode-18]
timestamp: 2026-07-08T00:00:00+09:00
---

# Leibnizian and Historic Mathematical Symbols

## 概要

Leibnizian and Historic Mathematical Symbols は、Leibniz manuscripts と historical mathematical sources の正確な digital / facsimile editions を支える symbol encoding を扱う topic である。UTC \#188 候補文書では、miscellaneous mathematical symbols、combining overlays、letterlike symbols、Leibnizian ambiguous signs、Unicode 18.0 delta chart feedback が一群として提出されている。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2025-04-14 | UTC | [L2/25-131](../documents/utc-l2-25-131.md) | Historic scientific characters proposal の分割として、7 historic alchemical symbols が提案された。 |
| 2026-05-26 | UTC / WG2 | [L2/26-140](../documents/utc-l2-26-140.md) | Historic mathematical sources 用 miscellaneous symbols 10 文字の 4th revision が提出された。 |
| 2026-05-26 | UTC / WG2 | [L2/26-141](../documents/utc-l2-26-141.md) | Slashed digits 用 combining overlays 2 文字が提案された。 |
| 2026-05-26 | UTC / WG2 | [L2/26-142](../documents/utc-l2-26-142.md) | Historic sources 用 letterlike symbols 6 文字が提案された。 |
| 2026-05-26 | UTC / WG2 | [L2/26-143](../documents/utc-l2-26-143.md) | Leibnizian ambiguous signs 59 signs / 5 VS の 4th revision が提出された。 |
| 2026-06-26 | WG2 | [WG2 N5354](../documents/wg2-n5354.md) | WG2 \#73 M73.06 が combining overlays、letterlike / Leibnizian symbols を first amendment additions として扱った。 |
| 2026-07-05 | UTC | [L2/26-149](../documents/utc-l2-26-149.md) | Leibnizian VS names と Unicode 18.0 delta charts への corrections / recommendations が提出された。 |
| 2026-07-07 | PRI | [PRI \#533](../documents/pri-533.md) | UTR \#25 Revision 16 public review の closing date。数学文字 support 全体の HTML migration / data update 前段として、この topic の個別 proposal 群とは別 layer に置く。 |

## 主な論点

### proposal split

この文書群は一つの巨大 proposal ではなく、alchemical symbols、miscellaneous symbols、combining marks、letterlike symbols、Leibnizian ambiguous signs、delta review feedback に分割されている。個々の characters の eligibility と、Leibnizian / historic scientific symbols 全体の block / naming / VS model を分けて読む必要がある。

### variation sequences と descriptive names

[L2/26-143](../documents/utc-l2-26-143.md) は 5 characters を variation sequences として提案し、[L2/26-149](../documents/utc-l2-26-149.md) はその descriptive names の wording options を提示する。文字名・VS description は data / charts に残るため、review の中心になる。

### historical editing の plain text boundary

これらの proposals は、facsimile editions や manuscript research で glyph-level distinction を保持するための encoding を求める。単なる font style、markup、editorial annotation で済むか、plain text character として必要かが共通論点である。

### UTR \#25 との関係

[Mathematical Text Support](mathematical-text-support.md) は UTR \#25 を入口に、現代的な mathematical repertoire、Math property、math data files、plain-text math と markup の境界を扱う。この topic は、その中でも historic sources / Leibnizian signs の個別 proposal chain に焦点を置く。

## 関連文書

- [PRI \#533](../documents/pri-533.md) - UTR \#25 Revision 16 public review。
- [L2/26-140](../documents/utc-l2-26-140.md) - miscellaneous mathematical symbols。
- [L2/25-131](../documents/utc-l2-25-131.md) - historic alchemical symbols。
- [L2/26-141](../documents/utc-l2-26-141.md) - two combining marks。
- [L2/26-142](../documents/utc-l2-26-142.md) - letterlike symbols。
- [L2/26-143](../documents/utc-l2-26-143.md) - Leibnizian ambiguous signs。
- [L2/26-149](../documents/utc-l2-26-149.md) - Leibniz Unicode Characters Project feedback。
- [WG2 N5354](../documents/wg2-n5354.md) - WG2 \#73 recommendations。
- [WG2 N5361R](../documents/wg2-n5361r.md) - provisionally assigned future repertoire。

## 関連トピック

- [Mathematical Text Support](mathematical-text-support.md)
- [Unicode 18.0 Change Sources](unicode-18-change-sources.md)
- [Script Encoding Pipeline](script-encoding-pipeline.md)

## 出典

- `pri-533` - <https://www.unicode.org/review/pri533/>
- `utc-l2-25-131` - <https://www.unicode.org/L2/L2025/25131-alchemical-symbols.pdf>
- `utc-l2-26-140` - <https://www.unicode.org/L2/L2026/26140-miscellaneous-symbols.pdf>
- `utc-l2-26-141` - <https://www.unicode.org/L2/L2026/26141-two-combining-marks.pdf>
- `utc-l2-26-142` - <https://www.unicode.org/L2/L2026/26142-letterlike-symbols.pdf>
- `utc-l2-26-143` - <https://www.unicode.org/L2/L2026/26143-leibnizian-ambiguous-signs.pdf>
- `utc-l2-26-149` - <https://www.unicode.org/L2/L2026/26149-leibniz.pdf>
- `wg2-n5354` - <https://www.unicode.org/wg2/docs/n5354-Mtg73-Paris-Recs-rev5.pdf>
