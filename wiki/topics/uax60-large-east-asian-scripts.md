---
type: Topic
title: "UAX #60 Data for Large East Asian Scripts"
description: "UAX #60 の title / data model と Small Seal など large East Asian scripts 向け data の保守。"
slug: uax60-large-east-asian-scripts
bodies: [UTC, WG2]
documents: [utc-l2-26-095, utc-l2-26-099, utc-l2-26-102, utc-l2-26-108, pri-549, wg2-n5209, wg2-n5344r2]
topics: [unicode-18-change-sources, unicode-properties-and-algorithms, small-seal-script]
status: active
tags: [uax60, east-asian-scripts, data-files, small-seal, unicode-18]
timestamp: 2026-07-07T21:45:00+09:00
---

# UAX \#60 Data for Large East Asian Scripts

## 概要

UAX \#60 Data for Large East Asian Scripts は、Unicode の large East Asian scripts 向け補助 data を扱う technical annex である。[L2/26-108](../documents/utc-l2-26-108.md) は、Unicode 18.0.0 向け draft として Jurchen、Nüshu、Seal、Tangut の source / radical-stroke / reading data files を説明する。

この wiki では、Unicode 18.0 周辺で UAX \#60 が `Data for Non Han Ideographic Scripts` から `Data for Large East Asian Scripts` へ title 変更され、Small Seal data の syntax / description update と接続する点を追う。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2023-03-11 | WG2 | [WG2 N5209](../documents/wg2-n5209.md) | Michel Suignard が Small Seal source references、modern CJK equivalents、radical data を持つ multi-source database 形式を提示した。 |
| 2026-04-03 | UTC | [L2/26-095](../documents/utc-l2-26-095.md) | Michelle Perham が PRI \#520 / Draft UAX \#60 を public review issue 一覧に含めた。 |
| 2026-04-03 | UTC | [L2/26-108](../documents/utc-l2-26-108.md) | Michel Suignard が Draft UAX \#60 Revision 2 を提出し、Jurchen、Nüshu、Seal、Tangut data files と property categories を説明した。 |
| 2026-04-11 | UTC | [L2/26-099](../documents/utc-l2-26-099.md) | CJK & Unihan Working Group recommendations が PRI \#520 / Draft UAX \#60 feedback として、`kSEAL_Rad` delimiter、`kSEAL_THXSrc` syntax、description 文字列の修正を action item 化した。 |
| 2026-04-15 | UTC | [L2/26-102](../documents/utc-l2-26-102.md) | RMG report が Unicode 18.0 beta に入れる調整として、UAX \#60 title を [Data for Non Han Ideographic Scripts](../documents/utc-l2-26-108.md) から `Data for Large East Asian Scripts` に変える action を記録した。 |
| 2026-07-07 | PRI | [PRI \#549](../documents/pri-549.md) | UAX \#42 Revision 39 public review が close し、Seal / Jurchen / Tangut data attributes が UCD XML representation に反映された。 |

## 主な論点

### Small Seal data との接続

UAX \#60 は Small Seal Script そのものの encoding proposal ではないが、Small Seal に付随する data property の仕様面に関係する。[L2/26-108](../documents/utc-l2-26-108.md) は `kSEAL_CCZSrc`、`kSEAL_DYCSrc`、`kSEAL_QJZSrc`、`kSEAL_THXSrc`、`kSEAL_MCJK`、`kSEAL_Rad` を Seal property として説明する。

[WG2 N5209](../documents/wg2-n5209.md) は、TCA / China proposal と Cook source mapping を比較する過程で、source references、modern CJK equivalents、radical modern form、alternate radical、radical number を持つ Small Seal database 形式を示した。[WG2 N5344R2](../documents/wg2-n5344r2.md) は Small Seal encoding proposal 側で、これらの source references、modern CJK equivalents、radical values を proposed database としてまとめる。[L2/26-099](../documents/utc-l2-26-099.md) では、`kSEAL_Rad` と `kSEAL_THXSrc` の syntax / description correction が PRI feedback の処理として扱われた。

[PRI \#549](../documents/pri-549.md) の UAX \#42 Revision 39 は、同じ Seal data を XML UCD representation の attributes として扱う。Small Seal は proposal / chart / data file だけでなく、`ucdxml` schema にも現れるため、tooling は UAX \#60 と UAX \#42 の両方を確認する必要がある。

### UAX \#38 との対応

UAX \#60 は、Han の Unihan database に近い役割を non-Han ideographic scripts に対して果たす。sources は normative、その他の radical-stroke / reading / numeric / related data は provisional とされるため、実装で使う場合は property ごとの status を分けて読む必要がある。

### 対象 scripts の違い

Jurchen と Tangut は radical-stroke / numeric value を持ち、Jurchen と Nüshu は reading data を持つ。Seal は Small Seal proposal の source evidence と CJK reference に強く接続し、Tangut は既存 source references と new source additions を含む。ひとつの annex でも、script ごとに data の性質は異なる。

### Unicode 18.0 release 管理との関係

`L2/26-102` は UAX \#60 title change を Unicode 18.0 beta deliverables の調整項目として記録している。したがって UAX \#60 は、Small Seal proposal、Unicode 18.0 beta data、draft annex update の接点にある。

## 関連文書

- [L2/26-099](../documents/utc-l2-26-099.md) - CJK & Unihan Working Group recommendations。
- [L2/26-102](../documents/utc-l2-26-102.md) - Release Management Group report to UTC \#187。
- [L2/26-108](../documents/utc-l2-26-108.md) - Draft UAX \#60 Revision 2。
- [PRI \#549](../documents/pri-549.md) - UAX \#42 Unicode Character Database in XML Revision 39 public review。
- [L2/26-095](../documents/utc-l2-26-095.md) - PRI \#520 を含む Public Review Issues 一覧。
- [WG2 N5209](../documents/wg2-n5209.md) - Small Seal source mapping comparison と database considerations。
- [WG2 N5344R2](../documents/wg2-n5344r2.md) - Small Seal proposal と proposed database。

## 関連トピック

- [Han Ideographic Scripts](../families/han-ideographic-scripts.md)
- [Unicode 18.0 Change Sources](unicode-18-change-sources.md)
- [Unicode Properties and Algorithms](unicode-properties-and-algorithms.md)
- [Small Seal Script](small-seal-script.md)

## 出典

- `utc-l2-26-099` - <https://www.unicode.org/L2/L2026/26099-cjk-unihan-wg-utc187.pdf>
- `utc-l2-26-102` - <https://www.unicode.org/L2/L2026/26102-rmg-report-utc187.pdf>
- `utc-l2-26-108` - <https://www.unicode.org/L2/L2026/26108-uax60-2-draft-pri520.pdf>
- `pri-549` - <https://www.unicode.org/review/pri549/>
- `utc-l2-26-095` - <https://www.unicode.org/L2/L2026/26095-public-review-issues.html>
- `wg2-n5209` - <https://www.unicode.org/wg2/docs/n5209-ConsiderationsSmallSeal.pdf>
- `wg2-n5344r2` - <https://www.unicode.org/wg2/docs/n5344R2-SmallSealProposal.pdf>
