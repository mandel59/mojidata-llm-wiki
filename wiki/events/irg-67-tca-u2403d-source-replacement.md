---
type: "Event"
title: "IRG #67 TCA U+2403D source replacement"
description: "TCA が IRG #67 の討議を受け、U+2403D の horizontal extension proposal の source / glyph を差し替えた出来事。"
slug: "irg-67-tca-u2403d-source-replacement"
date: "2026-10-12"
bodies: ["IRG"]
documents: ["irg-n2972", "irg-n2972r", "irg-n2946"]
topics: ["cjk-horizontal-extensions", "t-source-representative-glyph-issues"]
people: ["tca", "irg"]
meetings: ["irg-meeting-67"]
status: "revised"
tags: ["event", "t-source", "horizontal-extension", "glyph"]
timestamp: "2026-10-14T00:00:00+09:00"
events: ["irg-67-horizontal-extension-dispositions"]
---

# IRG \#67 TCA U+2403D source replacement

## 概要

TCA は2026-10-12 の討議を受け、700字の T-source horizontal extension proposal の No.420（U+2403D）について、source を TA-5952 から T9-7C28 へ、submitted glyph も対応する字形へ差し替えた。[IRG N2972R](../documents/irg-n2972r.md) p.1 の Revised Note が、T9-7C28 の glyph と U+2403D が同一だと TCA が同意した経緯を記録する。

これは TCA の提出案の変更である。IRG 全体の700字の正式 acceptance や、Unicode / ISO data への反映完了を示す出来事ではない。

## 背景

[IRG N2972](../documents/irg-n2972.md) は人名文字・CNS 11643 Web を根拠に、既存 Extension B の700字へ source references と glyphs を追加する案だった。U+2403D は source-owner が glyph を説明する対象にもなっていた。

## 結果

2026-10-13 の R revision は p.1 に旧案 / 改訂案の比較を示し、更新 font と mapping text の PDF attachments を指定する。全体の対象数は700のまま。実際の source data は全件を TA-source とまとめず、この T9-source への差替えを含めて読む。

## 影響範囲

[CJK Horizontal Extensions](../topics/cjk-horizontal-extensions.md) では source-owner の glyph 確認により、既存 source を再利用する案へ変わる事例となる。[T-source Representative Glyph Issues](../topics/t-source-representative-glyph-issues.md) では提案者の字形と source-owner の同一性判断を分けて追う。

## 関連ページ

- [IRG Meeting \#67](../meetings/irg/irg-meeting-67.md)
- [TCA](../people/tca.md)
- [IRG N2972R](../documents/irg-n2972r.md)

後続の正式な受入勧告は [IRG \#67 horizontal extension disposition](../events/irg-67-horizontal-extension-dispositions.md)に記録する。提出案の変更日と勧告日は分けて読む。

## 出典

- `irg-n2972r` - <https://www.unicode.org/irg/docs/n2972r-TCAHorizontalExtension.pdf>（registry date: 2026-10-13。本文が記録する討議日は2026-10-12）
- `irg-n2972` - <https://www.unicode.org/irg/docs/n2972-TCAHorizontalExtension.pdf>
- `irg-n2946` - <https://www.unicode.org/irg/docs/n2946-Recommendations.pdf>（registry date: 2026-10-15）
