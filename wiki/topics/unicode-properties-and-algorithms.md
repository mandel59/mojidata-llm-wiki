---
type: Topic
title: Unicode Properties and Algorithms
description: "UTC #187 PAG report を中心にした Unicode properties、algorithm text、security data の更新論点。"
slug: unicode-properties-and-algorithms
bodies: [UTC]
documents: [utc-l2-26-092, utc-l2-26-093, utc-l2-26-096, utc-l2-25-100, utc-l2-26-070r, utc-l2-26-109, utc-l2-26-110, utc-l2-26-111, utc-l2-26-137, utc-l2-26-138, utc-l2-26-139]
topics: [unicode-18-change-sources, cjk-security-confusables, script-encoding-pipeline, indic-script-notation-and-rendering, plain-text-composition-and-overstriking]
meetings: [utc-meeting-187, utc-meeting-188]
status: active
tags: [properties, algorithms, ucd, uax14, uax29, uax31, uax44, uts10, uts39, uts61, security]
timestamp: 2026-07-08T00:00:00+09:00
---

# Unicode Properties and Algorithms

## 概要

Unicode properties and algorithms は、文字追加だけでは決まらない UCD property 値、annex text、security data、collation data、segmentation behavior を調整する論点である。UTC \#187 では [L2/26-096](../documents/utc-l2-26-096.md) PAG report が主要文書で、Unicode 18.0 beta review に入れる property / algorithm changes を束ねた。

この topic は、CJK、emoji、script proposals とは別に、実装結果に直接影響する data / algorithm updates を追う入口である。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2025-04-04 | UTC | `L2/25-100` | UTR \#59 East Asian Spacing の draft public review document が登録された。 |
| 2026-03-27 | UTC | `L2/26-070R` | Multiple variation selectors を non-conformant とする revised document が提出された。 |
| 2026-04-03 | UTC | `L2/26-110`, `L2/26-111` | UAX \#31 / UAX \#44、UTS \#61 の proposed updates が登録された。 |
| 2026-04-14 | UTC | `L2/26-109` | UTS \#10 Unicode Collation Algorithm の proposed update が登録された。 |
| 2026-04-16 | UTC | [L2/26-096](../documents/utc-l2-26-096.md) | PAG が UTC \#187 に properties feedback と recommendations を提出した。 |
| 2026-04-21/23 | UTC | [L2/26-093](../documents/utc-l2-26-093.md) | UTC \#187 minutes が Unicode 18.0 beta review の action items として PAG report を扱った。 |
| 2026-06-09 | UTC | [L2/26-137](../documents/utc-l2-26-137.md), [L2/26-138](../documents/utc-l2-26-138.md), [L2/26-139](../documents/utc-l2-26-139.md) | UTC \#188 候補として Joining_Type for LTR scripts、consecutive anusvaras、COMPOSE proposal が登録された。 |

## 主な論点

### UCD property と line breaking

PAG report は、Arabic marks の Diacritic property、U+FE51 / U+2012 / U+2013 / U+00AD の Line_Break 値、LB12a text を Unicode 18.0 に合わせて調整する。実装者は release note だけでなく beta UCD と UAX \#14 text を確認する必要がある。

### Segmentation と derived properties

UAX \#29 GB9c と UAX \#44 の InCB=Linker derivation は、新規文字追加と連動して更新される。文字追加 proposal が独立に見えても、grapheme cluster behavior や derived property に実装差が出る場合がある。

### Collation と CLDR alignment

UTS \#10 / DUCET / CLDR alignment では Tibetan contractions、U+FFFE / U+FFFF weights などが扱われた。Unicode release と CLDR release の両方に関わるため、collation は UTC 文書だけで完結しない。

### Security / confusables

UTS \#39 では casefolding wording、Identifier_Type、mid-priority confusables data、Cyrillic Extended-D などが扱われる。CJK-specific な confusables は [CJK Security Confusables](cjk-security-confusables.md) に分けるが、PAG report は broader security data の hub である。

### UTS \#61

Unicode Set Notation は UTS \#61 として draft status に進められた。set notation は properties / regular expression / tooling に関わるため、単独 proposal ではなく properties and algorithms の一部として扱う。

### UTC \#188 候補の text model issues

[L2/26-137](../documents/utc-l2-26-137.md) は LTR joining scripts に対する Joining_Type property の意味を問い、[L2/26-138](../documents/utc-l2-26-138.md) は Indic scripts の valid consecutive anusvaras と rendering behavior を扱う。[L2/26-139](../documents/utc-l2-26-139.md) は COMPOSE character による overstriking を plain text として扱う proposal であり、grapheme cluster、security、normalization、font shaping に影響し得る。

## 関連文書

- [L2/26-096](../documents/utc-l2-26-096.md) - PAG report for UTC \#187。
- [L2/26-092](../documents/utc-l2-26-092.md) - UTC \#187 Agenda。
- [L2/26-093](../documents/utc-l2-26-093.md) - UTC \#187 Meeting Minutes。
- `L2/25-100` - UTR \#59 East Asian Spacing。
- `L2/26-070R` - multiple variation selectors conformance。
- `L2/26-109` - UTS \#10 Unicode Collation Algorithm proposed update。
- `L2/26-110` - UAX \#31 / UAX \#44 proposed update。
- `L2/26-111` - UTS \#61 Unicode Set Notation draft。
- [L2/26-137](../documents/utc-l2-26-137.md) - Joining_Type for left-to-right scripts。
- [L2/26-138](../documents/utc-l2-26-138.md) - consecutive anusvaras in Indic scripts。
- [L2/26-139](../documents/utc-l2-26-139.md) - COMPOSE / overstriking proposal。

## 関連トピック

- [Unicode 18.0 Change Sources](unicode-18-change-sources.md)
- [Unicode Release Coordination and Publication](unicode-release-coordination-and-publication.md)
- [CJK Security Confusables](cjk-security-confusables.md)
- [Script Encoding Pipeline](script-encoding-pipeline.md)
- [Indic Script Notation and Rendering](indic-script-notation-and-rendering.md)
- [Plain-Text Composition and Overstriking](plain-text-composition-and-overstriking.md)

## 出典

- `utc-l2-26-096` - <https://www.unicode.org/L2/L2026/26096-pag-report-utc187.pdf>
- `utc-l2-25-100` - <https://www.unicode.org/L2/L2025/25100-utr59-1-draft-pri510.pdf>
- `utc-l2-26-070r` - <https://www.unicode.org/L2/L2026/26070r-multiple-variation-selectors-non-conformant.pdf>
- `utc-l2-26-109` - <https://www.unicode.org/L2/L2026/26109-uts10-54-update-pri542.pdf>
- `utc-l2-26-110` - <https://www.unicode.org/L2/L2026/26110-uax31-44-update-pri535.pdf>
- `utc-l2-26-111` - <https://www.unicode.org/L2/L2026/26111-uts61-1-draft-pri523.pdf>
- `utc-l2-26-137` - <https://www.unicode.org/L2/L2026/26137-left-right.pdf>
- `utc-l2-26-138` - <https://www.unicode.org/L2/L2026/26138-consecutive-anusvaras.pdf>
- `utc-l2-26-139` - <https://www.unicode.org/L2/L2026/26139-compose.pdf>
