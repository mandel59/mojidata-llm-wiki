---
type: Source Document
title: "Clarification on Pending Characters in IRG N2861"
description: "TCA が IRG N2861 で pending だった U+2976E と U+20885 について、U+2976E は glyph を 已 から 巳 に戻し、U+20885 は current glyph を維持すると整理した follow-up。"
resource: https://www.unicode.org/irg/docs/n2927r-TSourceGlyphChanges.pdf
entry_id: irg-n2927r
doc_number: IRG N2927R
document_type: feedback
registry: irg
date: "2026-03-16"
source: TCA
documents: [irg-n2860, irg-n2861, irg-n2909, irg-n2911, utc-l2-26-099, wg2-n5354]
topics: [t-source-representative-glyph-issues, irg-source-data-and-representative-glyphs, unihan-database-maintenance, unicode-18-change-sources]
people: [tca, irg]
meetings: [irg-meeting-66, utc-meeting-187, wg2-meeting-73]
tags: [document, irg, t-source, representative-glyphs, feedback]
timestamp: 2026-07-08T00:00:00+09:00
---

# IRG N2927R

## 要約

`IRG N2927R` は、TCA が [IRG N2861](irg-n2861.md) で pending とした二つの T-source characters に follow-up した文書である。結論は、U+2976E は glyph を変更し、U+20885 は変更しない、という二分である。

U+2976E については、MOE が right part を 已 から 巳 に戻すことに同意した。U+20885 については、Variants Dictionary に 夂、文、攵 の三 component forms があるが、文 が standard form であるため current glyph を維持するとした。

## フィードバック内容

| 対象 | T-source | 結論 | 根拠 |
| --- | --- | --- | --- |
| U+2976E | T7-4529 | glyph を変更する。right part を 已 から 巳 に戻す。 | IRG \#36 で UCS 2003 glyph へ戻すよう求められた経緯と、MOE が《集韻》(去聲・七志) に基づいて revert に同意したこと。 |
| U+20885 | T5-3669 | current glyph を維持する。 | Variants Dictionary には 夂 / 文 / 攵 の forms があるが、文 を standard form とするため。 |

## 後続決定

[IRG N2911](irg-n2911.md) は、IRG Meeting \#66 editorial group が U+2976E の T-source glyph change を受け入れ、U+20885 の T-source glyph は変更しないと記録している。[IRG N2909](irg-n2909.md) M66.12 も同じ結論を recommendation として整理した。

[L2/26-099](utc-l2-26-099.md) は、U+2976E の T-source representative glyph change を UTC \#187 の CJK & Unihan action item に取り込んだ。WG2 \#73 の [WG2 N5354](wg2-n5354.md) は、この種の selected CJK additions and changes を ISO/IEC 10646 CD / DIS progression に接続している。

## 論点

### pending issue の解消

`IRG N2927R` は、新しい encoded character を提案する文書ではなく、前回文書で pending だった representative glyph questions を member body が解消する文書である。対象ごとに「変更」と「維持」を分けているため、T-source issue を一括で glyph change と読まない。

### variant evidence と standard form

U+20885 では複数 component forms があることを認めつつ、standard form として current glyph を維持している。この判断は、evidence に variant が存在することと、representative glyph を変更することが同義ではないことを示す。

## 関連文書

- [IRG N2860](irg-n2860.md) - 25 T-source glyphs の revision request。
- [IRG N2861](irg-n2861.md) - `IRG N2860` への TCA response。
- [IRG N2911](irg-n2911.md) - Meeting \#66 editorial report。
- [IRG N2909](irg-n2909.md) - Meeting \#66 recommendations。
- [L2/26-099](utc-l2-26-099.md) - UTC \#187 CJK & Unihan recommendations。
- [WG2 N5354](wg2-n5354.md) - WG2 \#73 recommendations。
- [T-source Representative Glyph Issues](../topics/t-source-representative-glyph-issues.md)

## 出典

- `irg-n2927r` - <https://www.unicode.org/irg/docs/n2927r-TSourceGlyphChanges.pdf>
- `irg-n2860` - <https://www.unicode.org/irg/docs/n2860-TSourceGlyphIssues.pdf>
- `irg-n2861` - <https://www.unicode.org/irg/docs/n2861-IRGN2860Feedback.pdf>
