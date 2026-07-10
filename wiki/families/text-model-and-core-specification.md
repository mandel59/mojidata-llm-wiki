---
type: Synthesis
title: Text Model and Core Specification
description: "Unicode text model、core specification guidance、UAX / UTR / UTS draft、ISO/IEC 10646 publication flow を束ねる synthesis。"
slug: text-model-and-core-specification
members: [east-asian-quotation-marks, east-asian-spacing, arabic-mark-rendering, egyptian-hieroglyph-data-and-unikemet, mathematical-text-support, plain-text-composition-and-overstriking, unicode-set-notation, iso-10646-edition-and-code-charts]
topics: [east-asian-quotation-marks, east-asian-spacing, arabic-mark-rendering, egyptian-hieroglyph-data-and-unikemet, mathematical-text-support, plain-text-composition-and-overstriking, unicode-set-notation, iso-10646-edition-and-code-charts]
tags: [family, text-model, core-spec, iso-10646]
timestamp: 2026-07-08T00:00:00+09:00
---

# Text Model and Core Specification

## 概要

Text Model and Core Specification は、個別 character proposal ではなく、Unicode text model、core specification guidance、UAX / UTR / UTS draft、ISO/IEC 10646 publication artifact に関わる topic を束ねる family である。

この family では、spacing、quotation mark guidance、Arabic mark rendering、data file guidance、set notation、COMPOSE / overstriking、code chart / DIS / amendment flow を、実装・仕様文書・publication の境界にまたがる論点として読む。Emoji や script proposal から参照される場合でも、主題が text model や publication machinery であればこの family に寄せる。

## メンバー

| Topic | 状態 | 一言 |
| --- | --- | --- |
| [East Asian Quotation Marks](../topics/east-asian-quotation-marks.md) | proposed-text-update | East Asian text における quotation marks の core spec guidance、縦横組、地域差。 |
| [East Asian Spacing](../topics/east-asian-spacing.md) | draft-utr | UTR \#59 draft の East Asian visible spacing algorithm と property data。 |
| [Arabic Mark Rendering](../topics/arabic-mark-rendering.md) | draft-uax | UAX \#53 / AMTRA による Arabic combining marks の rendering order と property data。 |
| [Egyptian Hieroglyph Data and Unikemet](../topics/egyptian-hieroglyph-data-and-unikemet.md) | draft-uax | UAX \#57 / Unikemet.txt による Egyptian hieroglyphs の catalog、source、function、Core data。 |
| [Mathematical Text Support](../topics/mathematical-text-support.md) | active | UTR \#25 を入口にした数学文字、Math property、math data files、plain-text math と markup の境界。 |
| [Plain-Text Composition and Overstriking](../topics/plain-text-composition-and-overstriking.md) | proposed | COMPOSE character、overstriking、format controls と Unicode text model の境界。 |
| [Unicode Set Notation](../topics/unicode-set-notation.md) | draft-uts | UTS \#61 draft の machine-readable Unicode set notation。 |
| [ISO/IEC 10646 Edition and Code Charts](../topics/iso-10646-edition-and-code-charts.md) | active | WG2 / SC2 における ISO/IEC 10646 7th edition、DIS progression、code charts、Amendment 1 project。 |

## 横断テーマ

- Unicode character encoding と higher-level markup / rendering engine の責任範囲をどこで線引きするか。
- UAX / UTR / UTS draft と core specification text update のどちらに置くべき guidance か。
- Algorithm / data file / property syntax と、readable specification prose の同期をどう保つか。
- UTC document、WG2 disposition、SC2 ballot / DIS document、code chart artifact が同じ変更を別段階で記録するため、body と時点を分けて読む必要がある。

## 周辺だがメンバー外

- [Unicode Properties and Algorithms](../topics/unicode-properties-and-algorithms.md) - PAG report を中心に properties / algorithms を広く扱う topic であり、emoji family との接続も強い。
- [Unicode Release Coordination and Publication](../topics/unicode-release-coordination-and-publication.md) - Unicode release 全体の coordination を扱う topic であり、この family の publication 論点と重なる。
- [UAX \#60 Data for Large East Asian Scripts](../topics/uax60-large-east-asian-scripts.md) - data file / property syntax の論点は重なるが、Han / ideographic family と Small Seal data への接続が強い。
- [Script and Notation Proposals](script-and-notation-proposals.md) - COMPOSE や format control、historic mathematical symbols が proposal の一部になる場合でも、個別 script / notation repertoire の読み口は別 family に置く。

## 出典

- `utc-l2-26-128` - East Asian quotation marks の core specification update proposal。
- `utc-l2-25-100` / `utc-l2-26-096` - East Asian visible spacing algorithm と UTC \#187 PAG report。
- `utc-l2-26-106` - UAX \#53 Arabic Mark Rendering proposed update。
- `utc-l2-26-107` - UAX \#57 Unikemet proposed update。
- `pri-533` - UTR \#25 Unicode Support for Mathematics Revision 16 public review。
- `utc-l2-26-111` - UTS \#61 Unicode Set Notation draft。
- `utc-l2-26-139` - COMPOSE / overstriking proposal。
- `wg2-n5362` / `wg2-n5363r` - ISO/IEC 10646 Amendment 1 working draft と disposition material。
