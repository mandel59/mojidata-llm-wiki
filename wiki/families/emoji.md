---
type: Synthesis
title: Emoji
description: "Emoji repertoire、UTS #51、ESR intake、CLDR keyword / RGI data、interoperability を束ねる synthesis。"
slug: emoji
members: [emoji-interoperability-and-intake, emoji-repertoire-proposals, unicode-18-change-sources, unicode-release-coordination-and-publication, unicode-properties-and-algorithms]
topics: [emoji-interoperability-and-intake, emoji-repertoire-proposals, unicode-18-change-sources, unicode-release-coordination-and-publication, unicode-properties-and-algorithms]
documents: [utc-l2-25-230r, utc-l2-25-252, utc-l2-25-253, utc-l2-25-254, utc-l2-25-255, utc-l2-25-256, utc-l2-25-257, utc-l2-25-258, utc-l2-25-259, utc-l2-26-008r, utc-l2-26-048, utc-l2-26-098, utc-l2-26-104]
tags: [family, emoji, uts51, cldr, esr]
timestamp: 2026-07-08T00:00:00+09:00
---

# Emoji

## 概要

Emoji family は、emoji character / sequence の追加、UTS \#51 specification、RGI data、CLDR keyword / short name、vendor interoperability、proposal intake を束ねる synthesis である。

この family では、個別 emoji proposal を [Emoji Repertoire Proposals](../topics/emoji-repertoire-proposals.md) に寄せ、review process / CLDR / interoperability の読み方を [Emoji Interoperability and Intake](../topics/emoji-interoperability-and-intake.md) に寄せる。Unicode release 全体の中での位置づけは [Unicode 18.0 Change Sources](../topics/unicode-18-change-sources.md) と [Unicode Release Coordination and Publication](../topics/unicode-release-coordination-and-publication.md) に接続する。

## メンバー

| Topic | 状態 | 一言 |
| --- | --- | --- |
| [Emoji Interoperability and Intake](../topics/emoji-interoperability-and-intake.md) | active | ESR report を入口に、vendor design divergence、CLDR keyword intake、Emoji 19.0 intake を追う。 |
| [Emoji Repertoire Proposals](../topics/emoji-repertoire-proposals.md) | active | Emoji 18.0 の個別 proposal、ESR short list、final candidate names を追う。 |
| [Unicode 18.0 Change Sources](../topics/unicode-18-change-sources.md) | active | Unicode 18.0 beta / release の change source として emoji charts / UTS \#51 / ESR report を位置づける。 |
| [Unicode Release Coordination and Publication](../topics/unicode-release-coordination-and-publication.md) | active | RMG / beta review / publication artifact の中で emoji data と UTS updates を扱う。 |
| [Unicode Properties and Algorithms](../topics/unicode-properties-and-algorithms.md) | active | Variation sequences、CLDR alignment、data files など実装側の algorithm / data connection を扱う。 |

## 横断テーマ

- emoji proposal は popularity だけでなく、interoperability、expected use、image distinctiveness、open-endedness、already representable などで評価される。
- character name、CLDR short name、keywords、vendor glyph design は別レイヤであり、同じ concept でもそれぞれの更新タイミングが違う。
- UTS \#51 は repertoire だけでなく、RGI emoji set、ZWJ sequences、tag sequences、skin tone modifiers、fallback guidance を定義する。
- Emoji additions は code point count だけでなく、modifier sequences や RGI sequence count の増加として release impact を持つ。
- Emoji 18.0 の U+1FAEB のように、short list 後に final character name / concept が差し替わることがある。

## 周辺だがメンバー外

- [Plain-Text Composition and Overstriking](../topics/plain-text-composition-and-overstriking.md) - COMPOSE proposal は emoji-like composites を例にするが、主題は Unicode text model であり、この family の中心ではない。
- [Script Encoding Pipeline](../topics/script-encoding-pipeline.md) - SEW proposal pipeline であり、emoji の ESR / UTS \#51 pipeline とは別系統として扱う。

## 関連 family

- [Han Ideographic Scripts](han-ideographic-scripts.md) - large data / source evidence / release synchronization の discipline は共有するが、対象 repertoire と review process は別。
- [Script and Notation Proposals](script-and-notation-proposals.md) - script proposal pipeline は SEW / WG2 を中心に進み、emoji の ESR / UTS \#51 pipeline と分けて読む。
- [Text Model and Core Specification](text-model-and-core-specification.md) - emoji sequence や variation data と接するが、主題は text model、algorithm、publication artifact である。

## 出典

- `utc-l2-25-230r` - <https://www.unicode.org/L2/L2025/25230r-esr-report-utc185.pdf>
- `utc-l2-26-008r` - <https://www.unicode.org/L2/L2026/26008r-esr-report-utc186.pdf>
- `utc-l2-26-098` - <https://www.unicode.org/L2/L2026/26098-esr-report-utc187.pdf>
- `utc-l2-26-104` - <https://www.unicode.org/L2/L2026/26104-uts51-30-update-pri543.pdf>
