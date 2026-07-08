---
type: Topic
title: Unicode Set Notation
description: "UTS #61 draft が定義する、Unicode specifications と tools で finite sets of code points / strings を表す machine-readable notation。"
slug: unicode-set-notation
aliases: ["UTS #61", "UnicodeSet"]
bodies: [UTC]
documents: [utc-l2-26-111, utc-l2-26-092, utc-l2-26-096]
topics: [unicode-properties-and-algorithms]
meetings: [utc-meeting-187]
status: draft-uts
tags: [uts61, unicode-set, properties, algorithms, tooling]
timestamp: 2026-07-08T00:00:00+09:00
---

# Unicode Set Notation

## 概要

Unicode Set Notation は、Unicode specifications と tools で有限の code point / string sets を machine-readable に表す notation を定義する UTS \#61 draft の論点である。[L2/26-111](../documents/utc-l2-26-111.md) が Proposed Draft UTS \#61 として登録された。

この topic は、properties / algorithms の文書が集合をどう書くか、ICU / UTS \#35 由来の UnicodeSet 構文を Unicode Standard 側でどう参照可能にするかを追う。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2026-04-03 | UTC | [L2/26-111](../documents/utc-l2-26-111.md) | Robin Leroy が Proposed Draft UTS \#61 "Unicode Set Notation" draft 4 を登録した。 |
| 2026-04-17 | UTC | [L2/26-092](../documents/utc-l2-26-092.md) | UTC \#187 agenda が UTS \#61 を Properties & Algorithms public review issues の一つとして置いた。 |
| 2026-04-16 | UTC | [L2/26-096](../documents/utc-l2-26-096.md) | PAG report が Unicode Set Notation を draft status に進める項目として記録した。 |

## 主な論点

### Unicode specifications の集合表記

UAX \#14、UAX \#29、UAX \#31、UAX \#44、UTS \#51 などは、algorithm や conformance text の中で character sets を参照する。UTS \#61 は、これらを plain prose や実装依存の regex fragment ではなく、共通の set notation で書くための仕様である。

### property queries と set operations

Draft は escaped / named / bracketed elements、property queries、difference / intersection などを定義する。実装 API は構文全体を完全実装しない場合でも、どの subset を support するかを明示する必要がある。

### style guide と escaping

Unicode specifications では、POSIX-style property queries を避け、`\p` を基本にし、regex match / property comparison / version qualifier を仕様本文で使わないことが推奨される。Higher-level syntax で `#` が comment marker になる場合は escape する、という実務的な注意も含まれる。

## 関連文書

- [L2/26-111](../documents/utc-l2-26-111.md) - Proposed Draft UTS \#61, Unicode Set Notation。
- [L2/26-092](../documents/utc-l2-26-092.md) - UTC \#187 Agenda。
- [L2/26-096](../documents/utc-l2-26-096.md) - UTC \#187 PAG report。

## 関連トピック

- [Unicode Properties and Algorithms](unicode-properties-and-algorithms.md)

## 出典

- `utc-l2-26-111` - <https://www.unicode.org/L2/L2026/26111-uts61-1-draft-pri523.pdf>
- `utc-l2-26-092` - <https://www.unicode.org/L2/L2026/26092.htm>
- `utc-l2-26-096` - <https://www.unicode.org/L2/L2026/26096-pag-report-utc187.pdf>

