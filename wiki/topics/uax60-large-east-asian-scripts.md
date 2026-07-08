---
type: Topic
title: "UAX #60 Data for Large East Asian Scripts"
description: "UAX #60 の title / data model と Small Seal など large East Asian scripts 向け data の保守。"
slug: uax60-large-east-asian-scripts
bodies: [UTC]
documents: [utc-l2-26-099, utc-l2-26-102]
topics: [unicode-18-change-sources, small-seal-script]
status: active
tags: [uax60, east-asian-scripts, data-files, small-seal, unicode-18]
timestamp: 2026-07-07T21:45:00+09:00
---

# UAX \#60 Data for Large East Asian Scripts

## 概要

UAX \#60 Data for Large East Asian Scripts は、Unicode の large East Asian scripts 向け補助 data を扱う technical annex である。この wiki では、Unicode 18.0 周辺で UAX \#60 が `Data for Non Han Ideographic Scripts` から `Data for Large East Asian Scripts` へ title 変更され、Small Seal data の syntax / description update と接続する点を追う。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2026-04-11 | UTC | `L2/26-099` | CJK & Unihan Working Group recommendations が PRI \#520 / Draft UAX \#60 feedback として、`kSEAL_Rad` delimiter、`kSEAL_THXSrc` syntax、description 文字列の修正を action item 化した。 |
| 2026-04-15 | UTC | `L2/26-102` | RMG report が Unicode 18.0 beta に入れる調整として、UAX \#60 title を `Data for Non Han Ideographic Scripts` から `Data for Large East Asian Scripts` に変える action を記録した。 |

## 主な論点

### Small Seal data との接続

UAX \#60 は Small Seal Script そのものの encoding proposal ではないが、Small Seal に付随する data property の仕様面に関係する。`L2/26-099` では、`kSEAL_Rad` と `kSEAL_THXSrc` の syntax / description correction が PRI feedback の処理として扱われた。

### Unicode 18.0 release 管理との関係

`L2/26-102` は UAX \#60 title change を Unicode 18.0 beta deliverables の調整項目として記録している。したがって UAX \#60 は、Small Seal proposal、Unicode 18.0 beta data、draft annex update の接点にある。

## 関連文書

- [L2/26-099](../documents/utc-l2-26-099.md) - CJK & Unihan Working Group recommendations。
- [L2/26-102](../documents/utc-l2-26-102.md) - Release Management Group report to UTC \#187。

## 関連トピック

- [Han Ideographic Scripts](../families/han-ideographic-scripts.md)
- [Unicode 18.0 Change Sources](unicode-18-change-sources.md)
- [Small Seal Script](small-seal-script.md)

## 出典

- `utc-l2-26-099` - <https://www.unicode.org/L2/L2026/26099-cjk-unihan-wg-utc187.pdf>
- `utc-l2-26-102` - <https://www.unicode.org/L2/L2026/26102-rmg-report-utc187.pdf>
