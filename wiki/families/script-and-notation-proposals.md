---
type: Synthesis
title: Script and Notation Proposals
description: "Han / emoji 以外の script proposal、historic / technical symbols、notation characters、proposal pipeline を束ねる synthesis。"
slug: script-and-notation-proposals
members: [script-encoding-pipeline, kana, shaaldaa-script, maya-hieroglyph-encoding, chinese-folk-music-notation, indic-script-notation-and-rendering, leibnizian-and-historic-mathematical-symbols]
topics: [script-encoding-pipeline, kana, shaaldaa-script, maya-hieroglyph-encoding, chinese-folk-music-notation, indic-script-notation-and-rendering, leibnizian-and-historic-mathematical-symbols]
tags: [family, script, notation, symbols]
timestamp: 2026-07-08T00:00:00+09:00
---

# Script and Notation Proposals

## 概要

Script and Notation Proposals は、Han / ideographic 系と emoji 以外の script、notation、historic / technical symbols の proposal chain を束ねる family である。

この family では、個別 script の repertoire 提案だけでなく、SEW / UTC / WG2 の pipeline、format control や combining mark を含む notation proposal、historic source に基づく symbol proposalを同じ読み口で扱う。個別の採否や ballot status は各 topic に寄せ、このページでは横断的な論点と入口を示す。

## メンバー

| Topic | 状態 | 一言 |
| --- | --- | --- |
| [Script Encoding Pipeline](../topics/script-encoding-pipeline.md) | active | UTC \#187 SEW report と WG2 Amendment 1 文書を入口に、script proposal の progression、保留、安定性論点を追う。 |
| [Kana](../topics/kana.md) | active | 仮名の追加符号化、歴史的仮名、変体仮名、小書き仮名、合略仮名、Taiwanese Kana を追う。 |
| [Shaaldaa Script](../topics/shaaldaa-script.md) | proposed | Oromo 用 Shaaldaa script の UCS 符号化提案と ISO/IEC 10646 Amendment 1 candidate としての扱い。 |
| [Maya Hieroglyph Encoding](../topics/maya-hieroglyph-encoding.md) | proposed | Codical Maya と Classic Maya Hieroglyphs Extended-A の staged / unified encoding。 |
| [Chinese Folk Music Notation](../topics/chinese-folk-music-notation.md) | proposed | Chinese folk music / Xiqu / Quyi notation の musical symbols と format controls。 |
| [Indic Script Notation and Rendering](../topics/indic-script-notation-and-rendering.md) | active | Indic scripts における Vedic notation、combining marks、rendering guidance。 |
| [Leibnizian and Historic Mathematical Symbols](../topics/leibnizian-and-historic-mathematical-symbols.md) | proposed | Leibnizian ambiguous signs と historic mathematical sources 用 symbols。 |

## 横断テーマ

- Proposal は repertoire、character property、font / rendering behavior、data file 更新、ISO ballot text のどこで扱うべきかを切り分ける必要がある。
- Historic / scholarly evidence に基づく proposal では、source corpus、transcription practice、既存文字での表現可能性が繰り返し論点になる。
- Notation 系 proposal では、plain text character、combining mark、format control、higher-level markup の境界が採否に直接影響する。
- Script proposal の progression は UTC の SEW review、UTC minutes、WG2 agenda / disposition / amendment draft が別々に現れるため、文書番号の別表記と後続会合を合わせて追う必要がある。

## 周辺だがメンバー外

- [Han Ideographic Scripts](han-ideographic-scripts.md) - Han / ideographic 系は source data、IRG review、Unihan property と強く結びつくため別 family に置く。
- [Emoji](emoji.md) - emoji repertoire は proposal intake という点では近いが、ESR / UTS \#51 / CLDR の pipeline が中心であるため別 family に置く。
- [Text Model and Core Specification](text-model-and-core-specification.md) - COMPOSE / overstriking、spacing algorithm、set notation など text model 側に寄る論点は別 family で扱う。

## 出典

- `utc-l2-26-100` - UTC \#187 Script Encoding Working Group Report。
- `wg2-n5362` - ISO/IEC 10646 Amendment 1 working draft。
- `utc-l2-26-130` - Chinese folk music notation と COMPOSE / format control の重なりを示す proposal。
- `utc-l2-26-145` / `utc-l2-26-146` - Maya hieroglyph encoding proposals。
- `utc-l2-26-140` through `utc-l2-26-143` - Leibnizian / historic mathematical symbols and variants。
