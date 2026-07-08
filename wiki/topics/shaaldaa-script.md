---
type: Topic
title: Shaaldaa Script
description: "Oromo 用 Shaaldaa script の UCS 符号化提案と ISO/IEC 10646 Amendment 1 candidate としての扱い。"
slug: shaaldaa-script
aliases: [Shaaldaa, Sheek Bakrii Saphaloo]
bodies: [UTC, WG2]
documents: [utc-l2-24-109, utc-l2-26-040r2, utc-l2-26-100, wg2-n5354, wg2-n5361r, wg2-n5362, wg2-n5365]
topics: [script-encoding-pipeline, iso-10646-edition-and-code-charts]
meetings: [utc-meeting-187, wg2-meeting-73]
status: proposed
tags: [script, shaaldaa, oromo, amendment, wg2]
timestamp: 2026-07-08T00:00:00+09:00
---

# Shaaldaa Script

## 概要

Shaaldaa Script は、Sheikh Bakri Sapalo が Oromo 用に作った writing system を UCS に符号化する提案である。[L2/26-040R2](../documents/utc-l2-26-040r2.md) は、旧称 `Sheek Bakrii Saphaloo` の [L2/24-109](../documents/utc-l2-24-109.md) を community feedback に基づいて改訂し、script name、digit category、glyph variation evidence、numeric values などを更新した。

UTC 側では [L2/26-100](../documents/utc-l2-26-100.md) が SEW recommendation の中で character names / annotations の処理対象として扱う。WG2 側では [WG2 N5361R](../documents/wg2-n5361r.md) / [WG2 N5362](../documents/wg2-n5362.md) の Amendment 1 starting repertoire に現れ、[WG2 N5354](../documents/wg2-n5354.md) が WG2 \#73 の script additions group に含めた。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2024-04-18 | UTC | [L2/24-109](../documents/utc-l2-24-109.md) | Oreen Yousuf / Daniel Yacob が `Sheek Bakrii Saphaloo` script proposal を提出した。 |
| 2026-04-13 | UTC | [L2/26-040R2](../documents/utc-l2-26-040r2.md) | Oreen Yousuf / Daniel Yacob が Shaaldaa revised proposal を提出し、名称・digits・glyph evidence などを更新した。 |
| 2026-04-17 | UTC | [L2/26-100](../documents/utc-l2-26-100.md) | SEW が Shaaldaa / Cossic name changes を UTC \#187 の処理対象に含めた。 |
| 2026-06-23 | WG2 | [WG2 N5365](../documents/wg2-n5365.md) | SEI liaison contribution が Shaaldaa を WG2 current submissions の一つとして報告した。 |
| 2026-06-26 | WG2 | [WG2 N5354](../documents/wg2-n5354.md) | WG2 \#73 が Shaaldaa を script additions / possible additions group の中で扱った。 |
| 2026-06-29 | WG2 / UTC | [WG2 N5361R](../documents/wg2-n5361r.md) | Shaaldaa が Unicode 18.0 後の provisionally assigned future repertoire に含まれた。 |

## 主な論点

### Ethiopic 型の encoding model

[L2/26-040R2](../documents/utc-l2-26-040r2.md) は、Shaaldaa を Indic-style combining model ではなく Ethiopic 型の syllabic model で符号化する。vowel series、pure consonants、geminated forms を separate encoded characters として扱うため、repertoire は大きいが、既存の文字単位と資料上の使われ方に近い。

### 名前変更と revision tracking

旧 proposal title の `Sheek Bakrii Saphaloo` と、新 proposal の `Shaaldaa` は同一 lineage の文書である。catalog や wiki で検索するときは [L2/24-109](../documents/utc-l2-24-109.md) と [L2/26-040R2](../documents/utc-l2-26-040r2.md) を related documents としてまとめて扱う必要がある。

### Amendment 1 candidate と採択の区別

[WG2 N5361R](../documents/wg2-n5361r.md) に掲載されたことは provisionally assigned data であり、final encoding ではない。[WG2 N5362](../documents/wg2-n5362.md) の Amendment 1 project proposal と [WG2 N5354](../documents/wg2-n5354.md) の recommendations を合わせ、body と時点を分けて追う。

## 関連文書

- [L2/26-040R2](../documents/utc-l2-26-040r2.md) - Shaaldaa revised proposal。
- [L2/24-109](../documents/utc-l2-24-109.md) - Sheek Bakrii Saphaloo initial proposal。
- [L2/26-100](../documents/utc-l2-26-100.md) - UTC \#187 SEW recommendations。
- [WG2 N5365](../documents/wg2-n5365.md) - SEI liaison contribution。
- [WG2 N5361R](../documents/wg2-n5361r.md) - provisionally assigned future repertoire。
- [WG2 N5362](../documents/wg2-n5362.md) - Amendment 1 project proposal。
- [WG2 N5354](../documents/wg2-n5354.md) - WG2 \#73 recommendations。

## 関連トピック

- [Script Encoding Pipeline](script-encoding-pipeline.md)
- [ISO/IEC 10646 Edition and Code Charts](iso-10646-edition-and-code-charts.md)

## 出典

- `utc-l2-26-040r2` - <https://www.unicode.org/L2/L2026/26040r2-shaaldaa-proposal.pdf>
- `wg2-n5354` - <https://www.unicode.org/wg2/docs/n5354-Mtg73-Paris-Recs-rev5.pdf>
- `wg2-n5361r` - <https://www.unicode.org/wg2/docs/n5361R-ProvisionnallyAssigned.pdf>
- `wg2-n5362` - <https://www.unicode.org/wg2/docs/n5362-proposal_to_start_new_amendment_of_10646.pdf>
- `wg2-n5365` - <https://www.unicode.org/wg2/docs/n5365-SEILiaisonReport-June2026_WG2.pdf>
