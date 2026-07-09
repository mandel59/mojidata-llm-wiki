---
type: Topic
title: "Leke Script"
description: "Eastern Pwo Karen 用 Leke / Chicken Scratch script の Unicode encoding proposal chain。"
slug: leke-script
aliases: ["Chicken Scratch script"]
bodies: [UTC, WG2]
documents: [utc-l2-13-116, utc-l2-26-129, wg2-n5354, wg2-n5361r, wg2-n5362]
topics: [script-encoding-pipeline]
meetings: [utc-meeting-188, wg2-meeting-73]
status: proposed
tags: [script, proposal, leke, karen, abugida]
timestamp: 2026-07-09T00:00:00+09:00
---

# Leke Script

## 概要

Leke Script は、Pwo Eastern Karen を書く Leke / Chicken Scratch script を Unicode / UCS に符号化する proposal chain である。2013 年の [L2/13-116](../documents/utc-l2-13-116.md) が revised proposal として提出され、2026 年の [L2/26-129](../documents/utc-l2-26-129.md) がそれを拡張した current complete proposal として再提出した。

2026 年時点の Leke proposal は、55 characters を扱い、consonants、medial consonants、vowel signs、final consonant signs、tone marks、digits、punctuation を含む。WG2 \#73 では [WG2 N5361R](../documents/wg2-n5361r.md) / [WG2 N5362](../documents/wg2-n5362.md) の Amendment 1 starting repertoire の中に Leke が現れるが、provisional assignment と最終 encoding は分けて追う必要がある。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2013-05-07 | UTC / WG2 | [L2/13-116](../documents/utc-l2-13-116.md) | Erich Fickle / Martin Hosken が、Eastern Pwo Karen 用 Leke script の revised proposal を提出した。 |
| 2026-05-14 | UTC | [L2/26-129](../documents/utc-l2-26-129.md) | Frank van de Kasteelen が、2013 年案を拡張した Leke complete proposal を提出した。 |
| 2026-06-26 | WG2 | [WG2 N5354](../documents/wg2-n5354.md) | WG2 \#73 が Leke を first amendment / possible additions group の一部として扱い、Amendment 1 project subdivision に接続した。 |

## 主な論点

### 2013 proposal から 2026 proposal への再整理

`L2/13-116` は 55 characters を提案し、Leke には final consonants がないという説明のもとで、vowelized consonant や tone mark placement を扱った。`L2/26-129` は、同じく 55 characters 規模だが、medial consonants、final consonant signs、tone marks、Brahmi model を明示し、current usage と complete proposal の形に整理し直している。

### combining behavior と mark placement

Leke は abugida であり、consonant に vowel signs、final consonant signs、tone marks、medial signs を組み合わせる。`L2/26-129` は、logical order、mark category、contextual placement、vowel / tone の stacking を整理する必要を示す。これは [Script Encoding Pipeline](script-encoding-pipeline.md) で扱う text model / stability 論点にも接続する。

### provisional repertoire と採択状態

`WG2 N5361R` に Leke が provisionally assigned future repertoire として現れることは、final encoding ではない。[WG2 N5354](../documents/wg2-n5354.md) は Amendment 1 project subdivision と first amendment candidate groups を勧告したが、各 script の final repertoire は UTC / WG2 / SC2 の後続 review と ballot で変わり得る。

## 関連文書

- [L2/13-116](../documents/utc-l2-13-116.md)
- [L2/26-129](../documents/utc-l2-26-129.md)
- [WG2 N5354](../documents/wg2-n5354.md)
- [WG2 N5361R](../documents/wg2-n5361r.md)
- [WG2 N5362](../documents/wg2-n5362.md)

## 関連トピック

- [Script Encoding Pipeline](script-encoding-pipeline.md)
- [Script and Notation Proposals](../families/script-and-notation-proposals.md)

## 出典

- `utc-l2-13-116` - <https://www.unicode.org/L2/L2013/13116-leke-revised.pdf>
- `utc-l2-26-129` - <https://www.unicode.org/L2/L2026/26129-leke-proposal.pdf>
- `wg2-n5354` - <https://www.unicode.org/wg2/docs/n5354-Mtg73-Paris-Recs-rev5.pdf>
- `wg2-n5361r` - <https://www.unicode.org/wg2/docs/n5361R-ProvisionnallyAssigned.pdf>
- `wg2-n5362` - <https://www.unicode.org/wg2/docs/n5362-proposal_to_start_new_amendment_of_10646.pdf>
