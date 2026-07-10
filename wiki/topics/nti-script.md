---
type: Topic
title: "N'ti Script"
description: "Soninke 用 N'ti / Nti script の Unicode encoding proposal chain と LTR joining model。"
slug: nti-script
aliases: ["N’ti", "N'ti", Nti]
bodies: [UTC]
documents: [utc-l2-23-203, utc-l2-26-028r, utc-l2-26-087, utc-l2-26-100, utc-l2-26-137]
topics: [script-encoding-pipeline, unicode-properties-and-algorithms]
status: proposed
tags: [script, proposal, nti, soninke, joining-type]
timestamp: 2026-07-09T00:00:00+09:00
---

# N'ti Script

## 概要

N'ti / Nti は Soninke 用の left-to-right joining alphabet を Unicode に追加する proposal chain である。2023 年の African scripts usage survey で unencoded script として記録され、2026 年に preliminary proposal `L2/26-028R`、revised proposal `L2/26-087` が提出された。

この topic の中心論点は、community usage evidence と repertoire だけでなく、word 内で letters が join / fuse する LTR script を Unicode の `Joining_Type` と shaping model へどう接続するかである。2026-07-09 時点の local catalog では、採択決定は未確認である。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2023-09-21 | UTC | [L2/23-203](../documents/utc-l2-23-203.md) | Oreen Yousuf らが African scripts status report で N'ti を unencoded script として扱い、font、books、online videos、user community contact を usage evidence として記録した。 |
| 2026-01-15 | UTC | [L2/26-028R](../documents/utc-l2-26-028r.md) | Oreen Yousuf / Ibrahima Ceesay が preliminary proposal を提出し、Soninke 用 N'ti script、27 letters、8 combining diacritics、punctuation、digits、LTR joining behavior を示した。 |
| 2026-04-13 | UTC | [L2/26-087](../documents/utc-l2-26-087.md) | Oreen Yousuf / Ibrahima Ceesay が revised proposal を提出し、[L2/26-028R](../documents/utc-l2-26-028r.md) を supersede して GIILONDE letter extender と joining behavior の説明を追加した。 |
| 2026-04-17 | UTC | [L2/26-100](../documents/utc-l2-26-100.md) | SEW が N'ti を joining behavior / encoding model に追加検討が必要な script proposal として扱った。 |
| 2026-06-09 | UTC | [L2/26-137](../documents/utc-l2-26-137.md) | Roozbeh Pournader が N'ti や Ndiko Jonam のような LTR joining scripts を背景に `Joining_Type` の `L` / `R` semantics を検討した。 |

## 主な論点

### Community evidence と script identity

`L2/23-203` は N'ti の font、books、online videos、children learning、user community contact を usage evidence として記録する。`L2/26-028R` / `L2/26-087` はさらに official request letters、Keyman keyboard、regional teaching / daily use の説明を加える。

Script name は community usage では N'ti / N’ti だが、Unicode script name では apostrophe を含められないため `Nti` が使われる。作成年・creator 表記は `L2/23-203` が 1985 年・Dama Konte、2026 年 proposal が 1966 年・Adama / Dama Konte としており、後続 proposal で整理が進んだ点として扱う。

### Repertoire の変化

`L2/26-028R` は placeholder code points で 27 letters、8 combining diacritics、N'TI PUNCTUATION XUPU、digits を示した。`L2/26-087` は proposed range を U+1CB80..U+1CBAF に移し、GIILONDE letter extender を追加して、letters、marks、punctuation、digits を含む repertoire とした。

### LTR joining model

N'ti は left-to-right に書くが、word 内の letters は baseline で join / fuse する。proposal は Arabic のような positional shapes はないと説明する一方、font shaping と line breaking では joining behavior を model 化する必要がある。

### Joining_Type semantics

`L2/26-137` は N'ti / Ndiko Jonam のような LTR joining scripts に対し、visually right-joining characters を `Joining_Type=L` とする既存 Phags-pa practice を維持するか、視覚方向どおり `R` とするかを比較する。これは N'ti だけの採否ではなく、future script encoding の property model を決める論点である。

## 関連文書

- [L2/23-203](../documents/utc-l2-23-203.md) - African scripts usage / implementation status report。
- [L2/26-028R](../documents/utc-l2-26-028r.md) - preliminary N'ti proposal。
- [L2/26-087](../documents/utc-l2-26-087.md) - revised N'ti proposal。
- [L2/26-100](../documents/utc-l2-26-100.md) - SEW recommendations for UTC \#187。
- [L2/26-137](../documents/utc-l2-26-137.md) - `Joining_Type` for LTR scripts。

## 関連トピック

- [Script Encoding Pipeline](script-encoding-pipeline.md)
- [Unicode Properties and Algorithms](unicode-properties-and-algorithms.md)

## 出典

- `utc-l2-23-203` - <https://www.unicode.org/L2/L2023/23203-update-african-scripts.pdf>
- `utc-l2-26-028r` - <https://www.unicode.org/L2/L2026/26028r-nti-proposal.pdf>
- `utc-l2-26-087` - <https://www.unicode.org/L2/L2026/26087-nti-proposal.pdf>
- `utc-l2-26-100` - <https://www.unicode.org/L2/L2026/26100-sew-report-utc187.pdf>
- `utc-l2-26-137` - <https://www.unicode.org/L2/L2026/26137-left-right.pdf>
