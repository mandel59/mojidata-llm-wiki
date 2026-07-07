---
type: Topic
title: Emoji Interoperability and Intake
description: "UTC #187 ESR report を入口にした emoji interoperability、inclusion criteria、CLDR keyword intake。"
slug: emoji-interoperability-and-intake
bodies: [UTC]
documents: [utc-l2-26-092, utc-l2-26-093, utc-l2-26-098, utc-l2-26-104]
topics: [unicode-18-change-sources]
meetings: [utc-meeting-187]
status: active
tags: [emoji, interoperability, cldr, uts51, intake]
timestamp: 2026-07-08T00:00:00+09:00
---

# Emoji Interoperability and Intake

## 概要

Emoji interoperability and intake は、emoji proposal を単なる新規文字追加ではなく、vendor design divergence、search keywords、CLDR data、inclusion / exclusion criteria、future submission process として扱う論点である。UTC \#187 では [L2/26-098](../documents/utc-l2-26-098.md) ESR report が主要文書になる。

Unicode 18.0 / Emoji 18.0 の範囲では monarch butterfly feedback が具体例であり、Emoji 19.0 に向けては intake window と review priorities が示された。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2026-04-03 | UTC | `L2/26-104` | UTS \#51 Unicode Emoji proposed update が登録された。 |
| 2026-04-14 | UTC | [L2/26-098](../documents/utc-l2-26-098.md) | ESR が UTC \#187 に emoji interoperability / intake report を提出した。 |
| 2026-04-21/23 | UTC | [L2/26-092](../documents/utc-l2-26-092.md), [L2/26-093](../documents/utc-l2-26-093.md) | UTC \#187 が Emoji 18.0 alpha repertoire、UTS \#51 update、ESR report を議題にした。 |
| 2026-07-31 | UTC | [L2/26-098](../documents/utc-l2-26-098.md) | Emoji 19.0 submissions window の締切予定。 |

## 主な論点

### Interoperability issue としての monarch butterfly

ESR report は、U+1F98B BUTTERFLY の vendor designs が morpho / monarch に分かれていることを、monarch butterfly addition の根拠として扱う。既存 emoji の意味分担を整理し、vendor が現在の U+1F98B を morpho 側へ寄せられるようにする点が interoperability issue である。

### Inclusion / exclusion criteria の読み方

Monarch butterfly が exclusion factors に触れるという feedback に対して、ESR report は exclusion factor が inclusion factor や interoperability 上の根拠を自動的に無効化するわけではないと整理した。emoji proposal review は checklist 的な除外ではなく、実装差と利用者問題を総合して判断される。

### CLDR keyword intake

Emoji search behavior は Unicode character repertoire だけではなく CLDR keyword data に依存する。ESR と CLDR は keyword request の add / remove best practices を整理中で、将来の文書化が予定されている。

### Emoji 19.0 intake

Emoji 19.0 の review は 2026-04-02 に始まり、submissions は 2026-07-31 までとされる。UTC \#187 の ESR report は、18.0 の feedback 処理と次期 intake の境目にある資料として読む。

## 関連文書

- [L2/26-098](../documents/utc-l2-26-098.md) - ESR report for UTC \#187。
- [L2/26-092](../documents/utc-l2-26-092.md) - UTC \#187 Agenda。
- [L2/26-093](../documents/utc-l2-26-093.md) - UTC \#187 Meeting Minutes。
- `L2/26-104` - Proposed Update UTS \#51, Unicode Emoji。

## 関連トピック

- [Unicode 18.0 Change Sources](unicode-18-change-sources.md)
- [Unicode Release Coordination and Publication](unicode-release-coordination-and-publication.md)

## 出典

- `utc-l2-26-098` - <https://www.unicode.org/L2/L2026/26098-esr-report-utc187.pdf>
- `utc-l2-26-104` - <https://www.unicode.org/L2/L2026/26104-uts51-30-update-pri543.pdf>

