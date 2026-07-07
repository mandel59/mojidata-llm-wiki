---
type: Topic
title: East Asian Quotation Marks
description: "East Asian text における quotation marks の core spec guidance、縦横組、地域差。"
slug: east-asian-quotation-marks
bodies: [UTC]
documents: [utc-l2-26-128]
status: proposed-text-update
tags: [punctuation, quotation-marks, cjk, vertical-text, core-spec]
timestamp: 2026-07-08T00:00:00+09:00
---

# East Asian Quotation Marks

## 概要

East Asian Quotation Marks は、CJK / East Asian text における quotation marks の shape、width、vertical orientation、language-specific conventions を扱う topic である。UTC \#188 候補文書 [L2/26-128](../documents/utc-l2-26-128.md) は、Unicode Core Specification の East Asian usage text が現行実態を十分に区別していないとして、Chapter 6 の更新を提案した。

この論点は新規文字の追加ではなく、既存 punctuation の使い分けと implementation guidance の修正である。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2026-05-06 | UTC | [L2/26-128](../documents/utc-l2-26-128.md) | Night Koo が East Asian quotation marks の core spec text update を提案した。 |
| 2026-07-30 | UTC | [UTC Meeting \#188](../meetings/utc/utc-meeting-188.md) | UTC \#188 の agenda / minutes は未掲載だが、UTC \#187 後の候補文書として追跡する。 |

## 主な論点

### comma-like と bracket-like の分離

[L2/26-128](../documents/utc-l2-26-128.md) は、U+201C / U+201D などの comma-like quotation marks と、U+300C / U+300D、U+300A / U+300B などの bracket-like quotation marks を分けて説明する。特に East Asian Width と proportional / full-width rendering の違いが implementation guidance に関わる。

### 言語・地域差

Korean、Japanese、PRC Chinese、Traditional Chinese outside PRC、Sibe は、同じ quotation mark characters でも preferred marks、glyph shape、vertical text behavior が異なる。Unicode Core Specification がこれを単一の East Asian usage として説明すると、実装者や font designer に誤った一般化を与える。

### UAX \#50 と variation selector

Vertical text での substitution / rotation は UAX \#50 と接続する。また proposal は variation selector による narrow / wide / Sibe-specific style selection に触れるため、core spec text、UAX \#11、UAX \#50、Chapter 23.4 の整合が必要になる。

## 関連文書

- [L2/26-128](../documents/utc-l2-26-128.md) - East Asian quotation marks core spec update proposal。

## 関連トピック

- [Ideographic Punctuation Proposals](ideographic-punctuation-proposals.md)

## 出典

- `utc-l2-26-128` - <https://www.unicode.org/L2/L2026/26128-east-asian-quotation-marks.pdf>

