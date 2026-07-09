---
type: Organization
title: UTC
description: Unicode Standard の技術的な検討と承認を担う Unicode Technical Committee。
slug: utc
bodies: [UTC, IRG, WG2]
documents: [utc-l2-07-159, utc-l2-08-284, irg-n1534, irg-n1535, irg-n2369r, irg-n2439, irg-n2935, utc-l2-22-279, utc-l2-25-049, utc-l2-25-111, utc-l2-25-199, utc-l2-26-082, utc-l2-26-086, utc-l2-26-092, utc-l2-26-093, utc-l2-26-099, utc-l2-26-102, pri-547, pri-548, utc-l2-26-105, utc-l2-26-112, utc-l2-26-127, utc-l2-26-133, utc-l2-26-134, utc-l2-26-136, utc-l2-26-147, utc-l2-26-148]
topics: [unicode-18-change-sources, cjk-horizontal-extensions, irg-source-data-and-representative-glyphs, unihan-database-maintenance, unihan-data-format-and-property-syntax, uax45-u-source-ideographs, cjk-security-confusables, ideographic-punctuation-proposals, small-seal-script]
tags: [organization, standards-body, utc]
timestamp: 2026-07-08T00:00:00+09:00
---

# UTC

## 概要

UTC は、Unicode Standard の技術的な検討と承認を担う Unicode Consortium の標準化 body である。UTC 文書は `L2/yy-nnn` の番号で公開され、script / character proposals、UAX / UTS updates、UCD data changes、working group reports、meeting minutes を扱う。IRG や WG2 の文書と同じ proposal / feedback が UTC registry にも登録されることがある。

## 標準化での役割

| 文書 | 役割 | 関連 topic |
| --- | --- | --- |
| `L2/22-279`, `L2/25-049`, `L2/25-111` | Small Seal Script の source mapping、repertoire 整理、converging proposal。 | [Small Seal Script](../topics/small-seal-script.md) |
| `L2/07-159`, `L2/08-284`, `IRG N1534`, `IRG N1535` | U-source database の public reference 化、Draft UTR \#45、Extension D source evidence。 | [UAX \#45 / U-Source Ideographs](../topics/uax45-u-source-ideographs.md) |
| `L2/26-092`, `L2/26-093` | UTC Meeting \#187 agenda / minutes。 | [UTC Meeting \#187](../meetings/utc/utc-meeting-187.md) |
| `L2/26-102` / [PRI \#547](../documents/pri-547.md) / [PRI \#548](../documents/pri-548.md) | Unicode 18.0 timeline、UCD / beta review、ISO/IEC 10646 7th edition synchronization、beta public review close。 | [Unicode 18.0 Change Sources](../topics/unicode-18-change-sources.md) |
| `IRG N2369R`, `IRG N2439`, `L2/25-199`, `IRG N2961` / `L2/26-147` | U-source horizontal extension、U-source UNC proposal、UAX \#45 Revision 31、40 CJK Unified Ideographs への `kIRG_USource` values と representative glyphs。 | [UAX \#45 / U-Source Ideographs](../topics/uax45-u-source-ideographs.md), [CJK Horizontal Extensions](../topics/cjk-horizontal-extensions.md) |
| `L2/26-099`, `L2/26-105`, `L2/26-112`, `L2/26-134`, `L2/26-148` | Unihan database、UAX \#38、UTS \#37、radical / stroke data の保守。 | [Unihan Database Maintenance](../topics/unihan-database-maintenance.md), [Unihan Data Format and Property Syntax](../topics/unihan-data-format-and-property-syntax.md) |
| `L2/26-082`, `L2/26-086`, `L2/26-127` | UTS \#39 confusables data の CJK review request と周辺 data listing。 | [CJK Security Confusables](../topics/cjk-security-confusables.md) |
| `L2/26-133`, `L2/26-136` | ideographic punctuation の追加提案。 | [Ideographic Punctuation Proposals](../topics/ideographic-punctuation-proposals.md) |
| `IRG N2935` | UTC CJK & Unihan Working Group / UTC Meeting \#187 を経た source data changes が Unicode Version 18.0 Beta review に反映された status を記録。 | [IRG Source Data and Representative Glyphs](../topics/irg-source-data-and-representative-glyphs.md) |

## 関連文書

- `utc-l2-07-159` - U-source database as versioned document
- `utc-l2-08-284` - Draft UTR \#45
- `irg-n1534`, `irg-n1535` - UTC Extension D source descriptions / evidence
- `irg-n2369r` - 2019 U-source horizontal extension
- `irg-n2439` - two U-source UNC ideographs
- `utc-l2-25-199` - UAX \#45 Revision 31 proposed update
- `utc-l2-26-147` - U-source horizontal extension
- `utc-l2-26-092` - UTC \#187 Agenda
- `utc-l2-26-093` - UTC \#187 meeting minutes
- `utc-l2-26-082` - request for review of CJK confusables
- `utc-l2-26-086` - mid-priority confusables data listing
- `utc-l2-26-099` - CJK & Unihan Working Group Recommendations for UTC \#187 Meeting
- `utc-l2-26-102` - Release Management Group Report to UTC \#187
- `pri-547` - Proposed Update UAX \#44, Unicode Character Database
- `pri-548` - Unicode 18.0.0 Beta public review
- `utc-l2-26-105` - Proposed Update UAX \#38, Unicode Han Database
- `utc-l2-26-112` - Proposed Update UTS \#37, Unicode Ideographic Variation Database
- `utc-l2-26-127` - second request for review of CJK confusables
- `utc-l2-26-133` - double ideographic full stop proposal
- `utc-l2-26-134` - RSIndex.txt syntax enhancement
- `utc-l2-26-136` - WHITE IDEOGRAPHIC COMMA proposal
- `utc-l2-26-148` - `kTotalStrokes` changes for 458 ideographs
- `utc-l2-22-279` - UCS Seal Script Source Mapping Data
- `utc-l2-25-049` - Small Seal considerations
- `utc-l2-25-111` - Converging Small Seal proposal

## 関連トピック

- [Small Seal Script](../topics/small-seal-script.md)
- [Unicode 18.0 Change Sources](../topics/unicode-18-change-sources.md)
- [UTC Meeting \#187](../meetings/utc/utc-meeting-187.md)
- [UTC Meeting \#188](../meetings/utc/utc-meeting-188.md)
- [CJK Horizontal Extensions](../topics/cjk-horizontal-extensions.md)
- [IRG Source Data and Representative Glyphs](../topics/irg-source-data-and-representative-glyphs.md)
- [Unihan Database Maintenance](../topics/unihan-database-maintenance.md)
- [Unihan Data Format and Property Syntax](../topics/unihan-data-format-and-property-syntax.md)
- [UAX \#45 / U-Source Ideographs](../topics/uax45-u-source-ideographs.md)
- [CJK Security Confusables](../topics/cjk-security-confusables.md)
- [Ideographic Punctuation Proposals](../topics/ideographic-punctuation-proposals.md)

## 出典

- `utc-l2-07-159` - <https://www.unicode.org/L2/L2007/07159-u-source-db.pdf>
- `utc-l2-08-284` - <https://www.unicode.org/L2/L2008/08284-utr45-1.pdf>
- `irg-n1534` - <https://www.unicode.org/irg/docs/n1534-USourceDescriptionsExtensionD.pdf>
- `irg-n1535` - <https://www.unicode.org/irg/docs/n1535-USourceEvidenceExtensionD.pdf>
- `irg-n2369r` - <https://www.unicode.org/irg/docs/n2369r-UnicodeHorizontalExtension.pdf>
- `irg-n2439` - <https://www.unicode.org/irg/docs/n2439-UNC-UTC.pdf>
- `irg-n2935` - <https://www.unicode.org/irg/docs/n2935-ScheduleAgenda.html>
- `utc-l2-25-199` - <https://www.unicode.org/L2/L2025/25199-uax45-31-update-pri522.pdf>
- `utc-l2-26-092` - <https://www.unicode.org/L2/L2026/26092.htm>
- `utc-l2-26-093` - <https://www.unicode.org/L2/L2026/26093.htm>
- `utc-l2-26-082` - <https://www.unicode.org/L2/L2026/26082-review-cjk-confusables.pdf>
- `utc-l2-26-086` - <https://www.unicode.org/L2/L2026/26086-mid-priority-confusables-data.pdf>
- `utc-l2-26-099` - <https://www.unicode.org/L2/L2026/26099-cjk-unihan-wg-utc187.pdf>
- `utc-l2-26-102` - <https://www.unicode.org/L2/L2026/26102-rmg-report-utc187.pdf>
- `pri-547` - <https://www.unicode.org/review/pri547/>
- `pri-548` - <https://www.unicode.org/review/pri548/>
- `utc-l2-26-105` - <https://www.unicode.org/L2/L2026/26105-uax38-40-update-pri534.pdf>
- `utc-l2-26-112` - <https://www.unicode.org/L2/L2026/26112-uts37-15-update-pri541.pdf>
- `utc-l2-26-127` - <https://www.unicode.org/L2/L2026/26127-2nd-cjk-confusables.pdf>
- `utc-l2-26-133` - <https://www.unicode.org/L2/L2026/26133-dbl-ideo-fs.pdf>
- `utc-l2-26-134` - <https://www.unicode.org/L2/L2026/26134-rsindex-syntax-change.pdf>
- `utc-l2-26-136` - <https://www.unicode.org/L2/L2026/26136-white-ideographic-comma.pdf>
- `utc-l2-26-147` - <https://www.unicode.org/L2/L2026/26147-irgn2961-unicodehorizontalextension.pdf>
- `utc-l2-26-148` - <https://www.unicode.org/L2/L2026/26148-ktotalstrokes-changes.pdf>
- `utc-l2-22-279` - <https://www.unicode.org/L2/L2022/22279-ucs-seal-map.pdf>
- `utc-l2-25-049` - <https://www.unicode.org/L2/L2025/25049r-considerations-small-seal.pdf>
- `utc-l2-25-111` - <https://www.unicode.org/L2/L2025/25111-converging-small-seal.pdf>
