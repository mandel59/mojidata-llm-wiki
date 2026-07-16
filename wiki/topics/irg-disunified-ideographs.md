---
type: Topic
title: IRG Disunified Ideographs
description: "IRG Meeting #45 以降の CJK ideograph disunification と、その決定経路をまとめる IRG reference page。"
slug: irg-disunified-ideographs
bodies: [UTC, WG2, IRG]
documents: [irg-n2491r, irg-n2517, irg-n2552, irg-n2654r, irg-n2710r, irg-n2811, irg-n2892, irg-n2909, irg-n2911]
topics: [ucv-nucv-lists, irg-source-data-and-representative-glyphs, cjk-horizontal-extensions]
meetings: [irg-meeting-66]
people: [irg]
status: active
tags: [irg, cjk, disunification, unification]
timestamp: 2026-07-12T00:00:00+09:00
---

# IRG Disunified Ideographs

## 概要

[IRG Disunified Ideographs](https://www.unicode.org/irg/disunified.html) は、IRG Meeting \#45 以降の CJK ideograph disunification を会合ごとに逆時系列でまとめる公式 reference page である。pending / implemented を分け、source reference、original / new code point、関係する UTC・IRG・WG2 文書、UTC consensus、source change note、target Unicode version を一つの decision trail として示す。

IRG Meeting \#66 は、この web page を旧 `IWDS Series 4` の replacement として accept した。個々の disunification の根拠を確認するときは、この一覧を入口に、表中の recommendation、UTC consensus、version target を一次文書へ遡る。

## 経緯

| 年月日 | Body | 文書・資料 | できごと |
| --- | --- | --- | --- |
| 2021-10-08 | IRG | [IRG N2491R](../documents/irg-n2491r.md) | Meeting \#45 から \#56 までの disunified ideographs を文書として整理した。 |
| 2025-11-17 | IRG | [IRG N2892](../documents/irg-n2892.md) | 対象範囲を Meeting \#65 まで更新した。 |
| 2026-02-16 | IRG | [IRG Disunified Ideographs](https://www.unicode.org/irg/disunified.html) | web page の表示上の最終更新日。pending と implemented の表から decision trail を参照できる。 |
| 2026-03-19 | IRG | [IRG N2909](../documents/irg-n2909.md) | M66.05 が web page を `IWDS Series 4` の replacement として accept した。 |

## 主な論点

### pending と implemented

ページは、承認経路または target release が進行中の項目を `Pending Disunifications`、Unicode Standard への反映を追える項目を `Implemented Disunifications` として分ける。互換漢字が original code point の場合は、`≡` に続けて canonical equivalent の CJK Unified Ideograph も示す。

### decision trail

disunification は IRG recommendation だけで完結せず、WG2 recommendation、UTC consensus、Unicode version target、既存 source reference の変更を伴う場合がある。このページはそれらを横断して確認する索引であり、各 body の決定時点を区別して読む必要がある。

### UCV / NUCV との関係

[UCV and NUCV Lists](ucv-nucv-lists.md) が component variation の unifiable / non-unifiable boundary を例示するのに対し、IRG Disunified Ideographs page は個別 code point の disunification と実装状況を記録する。Meeting \#66 では、この page の採択と NUCV exception note が同じ recommendation 群で扱われた。

## 関連文書

- [IRG N2491R](../documents/irg-n2491r.md) - Meeting \#45 から \#56 までの初期 source-remapping list。
- [IRG N2909](../documents/irg-n2909.md) - Meeting \#66 recommendations。
- [IRG N2911](../documents/irg-n2911.md) - Meeting \#66 CJK editorial group report。
- [IRG N2892](../documents/irg-n2892.md) - Meeting \#45 から \#65 までの IRG Disunified Ideographs。

## 関連トピック

- [UCV and NUCV Lists](ucv-nucv-lists.md)
- [IRG Source Data and Representative Glyphs](irg-source-data-and-representative-glyphs.md)
- [CJK Horizontal Extensions](cjk-horizontal-extensions.md)

## 出典

- IRG, [IRG Disunified Ideographs](https://www.unicode.org/irg/disunified.html)
- `irg-n2909` - <https://www.unicode.org/irg/docs/n2909-Recommendations.pdf>
- `irg-n2911` - <https://www.unicode.org/irg/docs/n2911-MiscEditorialReport.pdf>
- `irg-n2892` - <https://www.unicode.org/irg/docs/n2892-Disunified.pdf>
