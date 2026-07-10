---
type: Topic
title: G-source Glyph and Source Reference Issues
description: "IRG Section 9.1 に集まった G-source representative glyph と source reference correction の個別論点。"
slug: g-source-glyph-and-reference-issues
bodies: [IRG]
documents: [irg-n891, irg-n1519, irg-n2837, irg-n2864r, irg-n2868, irg-n2919r, irg-n2923r, irg-n2930, irg-n2954, irg-n2955, irg-n2956, irg-n2957, irg-n2958, irg-n2959, irg-n2962]
topics: [irg-source-data-and-representative-glyphs, v-source-representative-glyph-issues, cjk-horizontal-extensions]
people: [roy-wang, kushim-jiang, ma-shijie, lin-anning, china, sat, irg]
status: active
tags: [irg, g-source, source-reference, representative-glyphs]
timestamp: 2026-07-08T00:00:00+09:00
---

# G-source Glyph and Source Reference Issues

## 概要

G-source glyph / source reference issues は、すでに encoded された CJK Unified Ideographs について、current representative glyph と source evidence、または current source reference と original evidence が合っているかを見直す IRG の論点である。

親トピックの [IRG Source Data and Representative Glyphs](irg-source-data-and-representative-glyphs.md) は G / T / K / UK / V / SAT source と Unihan property 全体を扱う。このページでは、IRG Meeting \#66 で一部 accepted / 一部 pending になった [IRG N2919R](../documents/irg-n2919r.md)、[IRG N2923R](../documents/irg-n2923r.md)、[IRG N2930](../documents/irg-n2930.md) と、IRG Meeting \#67 agenda の Section 9.1 に接続する `IRG N2954` から `IRG N2962` までの G-source 中心の proposal / feedback chain を分離して追う。

## 経緯

| 年月日 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2002-04-18 | IRG | [IRG N891](../documents/irg-n891.md) | China が Extension C1 candidate list を提出し、後続の `GZFY-00932` source history に関わる `zjw00932` などの entries を含めた。 |
| 2008-11-06 | IRG | [IRG N1519](../documents/irg-n1519.md) | China が CJK_D candidates の evidence package を提出し、`Hanyu Fangyan Da Cidian` などの source evidence と candidate review 情報を示した。 |
| 2025-04-03 | IRG | [IRG N2837](../documents/irg-n2837.md) | Judith Chen が82 GXC-source charactersを辞書のpage / position形式へ更新するよう提案した。 |
| 2025-09-16 | IRG | [IRG N2868](../documents/irg-n2868.md) | Dong Wenjie がGCH / GXC / GCYについてoriginal submission時のeditionとprintingに基づく再検討を求めた。 |
| 2025-09-28 | IRG | [IRG N2864R](../documents/irg-n2864r.md) | China が9種類・1,538 charactersのG-source referencesとsource description / syntaxの更新を提案した。 |
| 2026-03-09 | IRG | [IRG N2919R](../documents/irg-n2919r.md) | Wang Xieyang が 3 G-source glyph changes と 10 source reference changes を提案した。Meeting \#66 では U+250A9 / U+25805 glyph revisions は in principle accepted、U+26C25 と reference changes は継続確認になった。 |
| 2026-03-10 | IRG | [IRG N2923R](../documents/irg-n2923r.md) | Dong Wenjie が 329 G-source reference updates と 9 horizontal extension candidates を提案した。Meeting \#66 では further discussion / China response 待ちになった。 |
| 2026-03-14 | IRG | [IRG N2930](../documents/irg-n2930.md) | Boris Zhang / Wang Xieyang が U+236AC、U+24A1E、U+24E82 の `GU` references を `GHC` references へ変更する提案を出した。Meeting \#66 で accepted になった。 |
| 2026-04-03 | IRG | [IRG N2954](../documents/irg-n2954.md) | Roy Wang が U+2CCA3 / `GZFY-00932` の current glyph と source evidence の不一致を指摘し、glyph normalization または `GU` reference への変更を提案した。 |
| 2026-04-04 | IRG | [IRG N2955](../documents/irg-n2955.md) | Dong Wenjie が `IRG N2954` に feedback し、original evidence に合わせて glyph を直し、source reference は維持する方向を支持した。 |
| 2026-05-04 | IRG | [IRG N2956](../documents/irg-n2956.md) | Roy Wang が Extension C の GBK-source 5 characters について、glyph update と source reference update の混在した修正案を出した。 |
| 2026-05-05 | IRG | [IRG N2957](../documents/irg-n2957.md) | Kushim Jiang が `IRG N2956` に feedback し、character ごとに glyph change と source reference change を分けて扱うべきだと述べた。 |
| 2026-06-10 | IRG | [IRG N2958](../documents/irg-n2958.md) | Ma Shijie が多数の G-source glyph revisions を提案し、normal form、taboo form、source evidence、glyph convention の関係を問題にした。 |
| 2026-06-10 | IRG | [IRG N2959](../documents/irg-n2959.md) | Ma Shijie が SAT-source glyph issues を提出した。G-source ではないが、representative glyph correction queue として同じ Section 9.1 に接続する。 |
| 2026-07-04 | IRG | [IRG N2962](../documents/irg-n2962.md) | Lin Anning が 9 G-source glyphs の revision request を提出し、G-source convention と original evidence に基づく修正を求めた。 |

## 主な論点

### Meeting \#66 での分岐

[IRG N2919R](../documents/irg-n2919r.md) は glyph changes と source reference changes を混在して提案した。IRG Meeting \#66 editorial report [IRG N2911](../documents/irg-n2911.md) では、U+250A9 / U+25805 の glyph revisions は in principle accepted になったが、U+26C25 は further investigation、10 source reference changes は [IRG N2923R](../documents/irg-n2923r.md) 側の bulk changes と合わせて further discussion になった。

[IRG N2923R](../documents/irg-n2923r.md) は 329 reference updates と 9 horizontal extension candidates を扱うため、単発の glyph correction より review cost が高い。Meeting \#66 では China response 待ちとなり、Appendix B の horizontal extension candidates は別 proposal か revised `IRG N2929R` への merge が検討対象になった。

### `GU` references から `GHC` references への correction

[IRG N2930](../documents/irg-n2930.md) は、3 characters の `GU` references を `Hanyu Da Cidian` に対応する `GHC` references へ移す提案であり、IRG Meeting \#66 で accepted になった。これは representative glyph correction ではなく source reference correction なので、Unicode data では `kIRG_GSource` の value update として現れる。

### U+2CCA3 / GZFY-00932

[IRG N2954](../documents/irg-n2954.md) は、U+2CCA3 の current G-source representative glyph が `Hanyu Fangyan Dacidian` の evidence と合わないとする。提案は、glyph を evidence 側に寄せる案と、current glyph を維持したまま source reference を `GU-2CCA3` のような補助的 reference に変える案を並べる。

[IRG N891](../documents/irg-n891.md) は China の Extension C1 submission、[IRG N1519](../documents/irg-n1519.md) は China の CJK_D evidence package であり、どちらも後続の U+2CCA3 / `GZFY-00932` feedback で source history をたどる根拠になる。

[IRG N2955](../documents/irg-n2955.md) は、Extension C phase の `IRG N891` と CJK_D evidence review の `IRG N1519` の経緯を引き、誤った evidence が紛れたことを説明する。そのうえで、source reference は `GZFY-00932` のまま、representative glyph を original evidence に合わせる方向を支持する。

### Extension C の GBK-source evidence

[IRG N2956](../documents/irg-n2956.md) は、U+2AE99、U+2B0AF、U+2B26F、U+2B622、U+2B720 の 5 characters を扱う。提案の焦点は一様ではなく、glyph update、GBK source reference update、または `GU` reference への置換を character ごとに検討している。

[IRG N2957](../documents/irg-n2957.md) は、5 characters を一括処理せず、glyph を直すべきものと source reference だけを直すべきものを分ける。これは、source evidence mismatch が見つかったときに、encoded character identity、representative glyph、source reference のどこを更新するかという判断手順を明確にする feedback である。

### G-source glyph convention と original evidence

[IRG N2958](../documents/irg-n2958.md) と [IRG N2962](../documents/irg-n2962.md) は、単発の source reference mismatch ではなく、G-source glyph convention と original evidence の関係を広く点検する。normal form / taboo form の扱い、component normalization、GB/T 11460-2025 との整合、機械的に拡縮されたように見える component の扱いなどが論点になる。

この種の文書は、current glyph と evidence が違うことだけでは結論にならない。IRG は、source evidence に忠実に寄せるのか、member body の chart convention に合わせるのか、または source reference を別 collection へ移すのかを character ごとに決める必要がある。

### SAT-source issue との境界

[IRG N2959](../documents/irg-n2959.md) は SAT-source glyphs を扱うため、G-source topic の中核ではない。ただし、current representative glyph と source evidence の整合、radical / stroke data の修正、Meeting \#67 Section 9.1 の review queue という点では同じ作業単位に属する。G-source 固有の責任主体と SAT-source 固有の責任主体を混同しないよう、ここでは隣接案件として扱う。

## 関連文書

- [IRG N2919R](../documents/irg-n2919r.md) - 3 G-source glyphs と 10 references の proposal。
- [IRG N891](../documents/irg-n891.md) - China Extension C1 submission。
- [IRG N1519](../documents/irg-n1519.md) - China CJK_D candidate evidence package。
- [IRG N2923R](../documents/irg-n2923r.md) - 329 G-source reference updates と 9 horizontal extension candidates。
- [IRG N2930](../documents/irg-n2930.md) - 3 `GU` references を `GHC` references へ移す proposal。
- [IRG N2954](../documents/irg-n2954.md) - U+2CCA3 の G-source representative glyph issue。
- [IRG N2955](../documents/irg-n2955.md) - `IRG N2954` への feedback。
- [IRG N2956](../documents/irg-n2956.md) - Extension C の GBK-source glyph / reference issues。
- [IRG N2957](../documents/irg-n2957.md) - `IRG N2956` への feedback。
- [IRG N2958](../documents/irg-n2958.md) - G-source glyph revision request。
- [IRG N2959](../documents/irg-n2959.md) - SAT-source glyph issue document。
- [IRG N2962](../documents/irg-n2962.md) - 9 G-source glyphs の revision request。

## 関連トピック

- [IRG Source Data and Representative Glyphs](irg-source-data-and-representative-glyphs.md)
- [V-source Representative Glyph Issues](v-source-representative-glyph-issues.md)
- [CJK Horizontal Extensions](cjk-horizontal-extensions.md)
- [Unihan Database Maintenance](unihan-database-maintenance.md)
- [IRG Meeting \#67](../meetings/irg/irg-meeting-67.md)

## 出典

- `irg-n2954` - <https://www.unicode.org/irg/docs/n2954-GSourceIssue.pdf>
- `irg-n2955` - <https://www.unicode.org/irg/docs/n2955-IRGN2954Feedback.pdf>
- `irg-n2919r` - <https://www.unicode.org/irg/docs/n2919r-GSourceChanges.pdf>
- `irg-n2923r` - <https://www.unicode.org/irg/docs/n2923r-GSourceChanges.pdf>
- `irg-n2930` - <https://www.unicode.org/irg/docs/n2930-GSourceChanges.pdf>
- `irg-n891` - <https://www.unicode.org/irg/docs/n0891-China-ExtensionC1-sub.pdf>
- `irg-n1519` - <https://www.unicode.org/irg/docs/n1519-GSourceEvidenceExtensionD.pdf>
- `irg-n2956` - <https://www.unicode.org/irg/docs/n2956-GSourceIssues.pdf>
- `irg-n2957` - <https://www.unicode.org/irg/docs/n2957-IRGN2956Feedback.pdf>
- `irg-n2958` - <https://www.unicode.org/irg/docs/n2958-GSourceGlyphIssues.pdf>
- `irg-n2959` - <https://www.unicode.org/irg/docs/n2959-SSourceGlyphIssues.pdf>
- `irg-n2962` - <https://www.unicode.org/irg/docs/n2962-GSourceGlyphIssues.pdf>
