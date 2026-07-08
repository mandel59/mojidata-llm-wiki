---
type: Topic
title: V-source Representative Glyph Issues
description: V-source / Nom glyph evidence、Vietnam NB confirmation、representative glyph change と Unihan property update の論点。
slug: v-source-representative-glyph-issues
bodies: [IRG, UTC]
documents: [utc-l2-26-068, utc-l2-26-099, irg-n2909, irg-n2911, irg-n2928, irg-n2935, irg-n2953]
topics: [irg-source-data-and-representative-glyphs, unihan-database-maintenance]
people: [vietnam, ng-koon-hang, irg, utc]
status: active
tags: [irg, utc, v-source, nom, representative-glyphs, unihan]
timestamp: 2026-07-08T00:00:00+09:00
---

# V-source Representative Glyph Issues

## 概要

V-source representative glyph issues は、Vietnam / Nom evidence に基づく CJK Unified Ideographs の代表 glyph、source evidence、Unihan property values をどう更新するかという論点である。V-source は IRG の member body source であり、glyph change は code chart glyph だけでなく `kRSUnicode`、`kTotalStrokes`、Vietnamese reading / evidence confirmation に波及することがある。

親トピックの [IRG Source Data and Representative Glyphs](irg-source-data-and-representative-glyphs.md) は G / T / K / UK / V / SAT / U source 全体を扱う。このページでは、U+268A1 / U+268A2 の unresolved issue と、U+2B8A0 の UTC \#187 accepted change を並べ、V-source で「追加 evidence 待ち」と「Unicode 18.0 target の data update」が分かれる点を追う。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2026-02-10 | UTC | [L2/26-068](../documents/utc-l2-26-068.md) | Vietnam が U+2B8A0 の V-source glyph、`kRSUnicode`、`kTotalStrokes` の変更提案を提出した。 |
| 2026-03-10 | IRG | [IRG N2928](../documents/irg-n2928.md) | Ng Koon Hang が U+268A1 / U+268A2 の現行 component が意図されたものか、U+810A 脊 に戻すべきかを照会した。 |
| 2026-03-19 | IRG | [IRG N2911](../documents/irg-n2911.md), [IRG N2909](../documents/irg-n2909.md) | Meeting \#66 editorial report と M66.15 が、Vietnam は現行 glyph を意図通りと確認したが、追加 evidence があれば将来 glyph change を提案できると整理した。 |
| 2026-03-25 | IRG | [IRG N2953](../documents/irg-n2953.md) | `IRG N2928` の follow-up として、現行形を支持する evidence と、脊 component への normalized form を示す evidence が追加された。 |
| 2026-04-11 | UTC | [L2/26-099](../documents/utc-l2-26-099.md) | CJK & Unihan Working Group が U+2B8A0 の V-source representative glyph change と `kRSUnicode` / `kTotalStrokes` 変更を Unicode Version 18.0 target で受け入れるよう勧告した。 |
| 2026-07-05 | IRG | [IRG N2935](../documents/irg-n2935.md) | Meeting \#67 agenda が U+268A1 / U+268A2 issue を Section 9.1 の "Redux" issue として置き、`IRG N2953` を follow-up input にした。 |

## 主な論点

### Vietnam NB confirmation と追加 evidence

[IRG N2928](../documents/irg-n2928.md) は、U+268A1 / U+268A2 の現行 component を、semantic component 脊 の variant と見るべきかを問う。IRG \#66 では Vietnam が original evidence を確認し、current representative glyph は意図されたものだとしたが、同時に glyph change suggestion は意味的に合理的で、十分な supporting evidence があれば変更提案が可能だと整理された。

[IRG N2953](../documents/irg-n2953.md) は、`Bảng tra chữ Nôm` が現行形を支持する一方、`Giúp đọc Nôm và Hán Việt` には U+268A1 の normalized form ⿰屋脊 があるとする。このため、V-source glyph issue では「source owner が意図した glyph」と「別 evidence に現れる normalized glyph」を両方見て判断する必要がある。

### Glyph change と Unihan property update の結合

U+2B8A0 の case は、代表 glyph の変更が `kRSUnicode` と `kTotalStrokes` の変更を伴う例である。[L2/26-099](../documents/utc-l2-26-099.md) Section 20 は、V-source representative glyph を ⿰亻𱽗 に変更し、`kRSUnicode` を 9.7 から 9.9、`kTotalStrokes` を 8 から 11 に変える action item を置いた。

U+268A1 / U+268A2 はまだ glyph change の採否が記録されていないため、U+2B8A0 のような UTC data update と同じ扱いにはできない。topic では、accepted change と evidence-gathering issue を分けて読む。

### IRG review queue と UTC data update

IRG 側の V-source glyph issue は、Meeting \#67 agenda の Section 4.9 / 9.1 に残っている。一方、UTC 側で accepted された V-source glyph / property change は Unihan database と code chart action item へ変換される。したがって、IRG document だけでなく、UTC CJK & Unihan Working Group recommendations と会合 minutes でどの時点の状態かを確認する必要がある。

## 関連文書

- [L2/26-068](../documents/utc-l2-26-068.md) - U+2B8A0 の V-source glyph / property change proposal。
- [L2/26-099](../documents/utc-l2-26-099.md) - UTC \#187 CJK & Unihan Working Group recommendations。
- [IRG N2928](../documents/irg-n2928.md) - U+268A1 / U+268A2 glyph enquiry。
- [IRG N2953](../documents/irg-n2953.md) - `IRG N2928` follow-up evidence。
- [IRG N2909](../documents/irg-n2909.md) - IRG Meeting \#66 recommendations。
- [IRG N2911](../documents/irg-n2911.md) - IRG Meeting \#66 editorial report。
- [IRG N2935](../documents/irg-n2935.md) - IRG Meeting \#67 agenda。

## 関連トピック

- [IRG Source Data and Representative Glyphs](irg-source-data-and-representative-glyphs.md)
- [Unihan Database Maintenance](unihan-database-maintenance.md)
- [G-source Glyph and Source Reference Issues](g-source-glyph-and-reference-issues.md)
- [IRG Working Set 2024](irg-working-set-2024.md)

## 関連人物・組織

- [Vietnam](../people/vietnam.md)
- [Ng Koon Hang](../people/ng-koon-hang.md)
- [IRG](../people/irg.md)
- [UTC](../people/utc.md)

## 出典

- `utc-l2-26-068` - <https://www.unicode.org/L2/L2026/26068-v-source-character-u2b8a0.pdf>
- `utc-l2-26-099` - <https://www.unicode.org/L2/L2026/26099-cjk-unihan-wg-utc187.pdf>
- `irg-n2909` - <https://www.unicode.org/irg/docs/n2909-Recommendations.pdf>
- `irg-n2911` - <https://www.unicode.org/irg/docs/n2911-MiscEditorialReport.pdf>
- `irg-n2928` - <https://www.unicode.org/irg/docs/n2928-VSourceGlyphIssues.pdf>
- `irg-n2935` - <https://www.unicode.org/irg/docs/n2935-ScheduleAgenda.html>
- `irg-n2953` - <https://www.unicode.org/irg/docs/n2953-IRGN2928Followup.pdf>
