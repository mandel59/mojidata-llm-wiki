---
type: Topic
title: "UAX #60 Data for East Asian Scripts"
description: "Unicode 18.0 で新設された UAX #60 と Jurchen / Nüshu / Seal / Tangut data files。"
slug: uax60-large-east-asian-scripts
bodies: [UTC, WG2]
documents: [utc-l2-26-095, utc-l2-26-099, utc-l2-26-102, utc-l2-26-108, utc-l2-26-218, pri-520, pri-549, wg2-n5209, wg2-n5344r2]
topics: [unicode-18-change-sources, unicode-properties-and-algorithms, small-seal-script]
status: released
tags: [uax60, east-asian-scripts, data-files, small-seal, unicode-18]
timestamp: 2026-10-11T00:00:00+09:00
events: [uax60-unicode-18-first-published-version]
---

# UAX \#60 Data for East Asian Scripts

## 概要

UAX \#60 Data for East Asian Scripts は Unicode 18.0 で新設された technical annex で、Jurchen、Nüshu、Seal、Tangut の source / radical-stroke / reading data files を説明する。[L2/26-108](../documents/utc-l2-26-108.md) は public review draft、確定版と正式データは [Revision 3 確定 event](../events/uax60-unicode-18-first-published-version.md) から辿れる。

Draft title は `Data for Non Han Ideographic Scripts`、RMG 調整後の呼称は `Data for Large East Asian Scripts` だったが、final title は `Data for East Asian Scripts` になった。document stage ごとの title を区別し、Small Seal data の syntax / description update と接続して追う。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2023-03-11 | WG2 | [WG2 N5209](../documents/wg2-n5209.md) | Michel Suignard が Small Seal source references、modern CJK equivalents、radical data を持つ multi-source database 形式を提示した。 |
| 2026-04-03 | UTC | [L2/26-095](../documents/utc-l2-26-095.md) | Michelle Perham が PRI \#520 / Draft UAX \#60 を public review issue 一覧に含めた。 |
| 2026-04-03 | UTC | [L2/26-108](../documents/utc-l2-26-108.md) | Michel Suignard が Draft UAX \#60 Revision 2 を提出し、Jurchen、Nüshu、Seal、Tangut data files と property categories を説明した。 |
| 2026-04-11 | UTC | [L2/26-099](../documents/utc-l2-26-099.md) | CJK & Unihan Working Group recommendations が PRI \#520 / Draft UAX \#60 feedback として、`kSEAL_Rad` delimiter、`kSEAL_THXSrc` syntax、description 文字列の修正を action item 化した。 |
| 2026-04-15 | UTC | [L2/26-102](../documents/utc-l2-26-102.md) | RMG report が Unicode 18.0 beta に入れる調整として、UAX \#60 title を [Data for Non Han Ideographic Scripts](../documents/utc-l2-26-108.md) から `Data for Large East Asian Scripts` に変える action を記録した。 |
| 2026-07-07 | PRI | [PRI \#549](../documents/pri-549.md) | UAX \#42 Revision 39 public review が close し、Seal / Jurchen / Tangut data attributes が UCD XML representation に反映された。 |
| 2026-07-07 closing | PRI | [PRI \#520 / L2/26-108](../documents/utc-l2-26-108.md) | draft の review closing date。Resolved Issues で解決済みを確認し、仕様の確定は後続 event で追う。 |
| 2026-09-02 specification date | Unicode Consortium | [UAX \#60 Revision 3 確定](../events/uax60-unicode-18-first-published-version.md) | 初の承認済み公開版と正式データへの接続。 |
| 2026-09-29 | UTC | [L2/26-218](../documents/utc-l2-26-218.md) | 重複 glyph のため省略された Seal source references を補う `kSEAL_AdditionalSrc` を提案した。 |

## 主な論点

### Small Seal data との接続

UAX \#60 は Small Seal Script そのものの encoding proposal ではないが、Small Seal に付随する data property の仕様面に関係する。[L2/26-108](../documents/utc-l2-26-108.md) は `kSEAL_CCZSrc`、`kSEAL_DYCSrc`、`kSEAL_QJZSrc`、`kSEAL_THXSrc`、`kSEAL_MCJK`、`kSEAL_Rad` を Seal property として説明する。

[WG2 N5209](../documents/wg2-n5209.md) は、TCA / China proposal と Cook source mapping を比較する過程で、source references、modern CJK equivalents、radical modern form、alternate radical、radical number を持つ Small Seal database 形式を示した。[WG2 N5344R2](../documents/wg2-n5344r2.md) は Small Seal encoding proposal 側で、これらの source references、modern CJK equivalents、radical values を proposed database としてまとめる。[L2/26-099](../documents/utc-l2-26-099.md) では、`kSEAL_Rad` と `kSEAL_THXSrc` の syntax / description correction が PRI feedback の処理として扱われた。

[PRI \#549](../documents/pri-549.md) の UAX \#42 Revision 39 は、同じ Seal data を XML UCD representation の attributes として扱う。Small Seal は proposal / chart / data file だけでなく、`ucdxml` schema にも現れるため、tooling は UAX \#60 と UAX \#42 の両方を確認する必要がある。

[L2/26-218](../documents/utc-l2-26-218.md) は、SealSources.txt で重複 glyph のため省略された THX / CCZ / QJZ / DYC source references と code point の対応を、新しい provisional property で表す proposal である。これは Unicode 18.0.0 の既存 property ではなく、UTC の後続審議を待つ。

### UAX \#38 との対応

UAX \#60 は、Han の Unihan database に近い役割を non-Han ideographic scripts に対して果たす。sources は normative、その他の radical-stroke / reading / numeric / related data は provisional とされるため、実装で使う場合は property ごとの status を分けて読む必要がある。

### 対象 scripts の違い

Jurchen と Tangut は radical-stroke / numeric value を持ち、Jurchen と Nüshu は reading data を持つ。Seal は Small Seal proposal の source evidence と CJK reference に強く接続し、Tangut は既存 source references と new source additions を含む。ひとつの annex でも、script ごとに data の性質は異なる。

### Unicode 18.0 release 管理との関係

[PRI \#520 / L2/26-108](../documents/utc-l2-26-108.md) は解決済みの draft review、[Revision 3 確定 event](../events/uax60-unicode-18-first-published-version.md) は確定仕様と正式データの節目である。review closing date、仕様日付、Unicode 全体の release date を分けて読む。

`L2/26-102` は UAX \#60 title change を Unicode 18.0 beta deliverables の調整項目として記録した。Final Unicode 18.0 は UAX \#60 を正式 component とし、`JurchenSources.txt` と `SealSources.txt` を新規追加、既存 `NushuSources.txt` / `TangutSources.txt` と同じ versioned data group に置いた。

`SealSources.txt` の `kSEAL_THXSrc`、`kSEAL_CCZSrc`、`kSEAL_DYCSrc`、`kSEAL_QJZSrc` は normative source properties である。block / script name の `Seal` と、chart / core text の `Small Seal` を混同しない。

## 関連文書

- [L2/26-099](../documents/utc-l2-26-099.md) - CJK & Unihan Working Group recommendations。
- [L2/26-102](../documents/utc-l2-26-102.md) - Release Management Group report to UTC \#187。
- [L2/26-108 / PRI \#520](../documents/utc-l2-26-108.md) - Draft UAX \#60 Revision 2 と、解決済み review の後続確認。
- [PRI \#549](../documents/pri-549.md) - UAX \#42 Unicode Character Database in XML Revision 39 public review。
- [L2/26-095](../documents/utc-l2-26-095.md) - PRI \#520 を含む Public Review Issues 一覧。
- [WG2 N5209](../documents/wg2-n5209.md) - Small Seal source mapping comparison と database considerations。
- [WG2 N5344R2](../documents/wg2-n5344r2.md) - Small Seal proposal と proposed database。
- [L2/26-218](../documents/utc-l2-26-218.md) - SealSources.txt の proposed additional source property。

## 関連トピック

- [Han Ideographic Scripts](../families/han-ideographic-scripts.md)
- [Unicode 18.0 Change Sources](unicode-18-change-sources.md)
- [Unicode Properties and Algorithms](unicode-properties-and-algorithms.md)
- [Small Seal Script](small-seal-script.md)

## 出典

- `pri-520` - <https://www.unicode.org/review/pri520/>。registry 上の closing date: 2026-07-07。
- PRI Resolved Issues - <https://www.unicode.org/review/resolved.html> (2026-10-10 確認)。
- `utc-l2-26-099` - <https://www.unicode.org/L2/L2026/26099-cjk-unihan-wg-utc187.pdf>
- `utc-l2-26-102` - <https://www.unicode.org/L2/L2026/26102-rmg-report-utc187.pdf>
- `utc-l2-26-108` - <https://www.unicode.org/L2/L2026/26108-uax60-2-draft-pri520.pdf>
- `pri-549` - <https://www.unicode.org/review/pri549/>
- `utc-l2-26-095` - <https://www.unicode.org/L2/L2026/26095-public-review-issues.html>
- `wg2-n5209` - <https://www.unicode.org/wg2/docs/n5209-ConsiderationsSmallSeal.pdf>
- `wg2-n5344r2` - <https://www.unicode.org/wg2/docs/n5344R2-SmallSealProposal.pdf>
- `utc-l2-26-218` - <https://www.unicode.org/L2/L2026/26218-seal-property.pdf>
- UAX \#60 Revision 3, Data for East Asian Scripts - <https://www.unicode.org/reports/tr60/tr60-3.html> (2026-09-02)
- Unicode 18.0 UAX \#60 data - <https://www.unicode.org/Public/18.0.0/ucd/>
