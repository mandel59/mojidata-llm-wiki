---
type: Topic
title: KORE SEBELI Script
description: "Soso language 用 KORE SEBELI / Wakara script の Unicode encoding proposal chain。"
slug: kore-sebeli-script
aliases: ["Koré Sébèli", Wakara]
bodies: [UTC]
documents: [utc-l2-20-180, utc-l2-21-209, utc-l2-22-073, utc-l2-22-222, utc-l2-23-203, utc-l2-24-246, utc-l2-26-050r, utc-l2-26-132]
topics: [script-encoding-pipeline]
meetings: [utc-meeting-188]
status: proposed
tags: [script, proposal, kore-sebeli, soso, guinea]
timestamp: 2026-07-09T00:00:00+09:00
---

# KORE SEBELI Script

## 概要

KORE SEBELI / Koré Sébèli / Wakara は、Mohamed Bentoura Bangoura が Soso language 用に作成した contemporary Guinean script として UTC に提案されている script である。proposal chain は 2020 年の [L2/20-180](../documents/utc-l2-20-180.md) から 2026 年の [L2/26-050R](../documents/utc-l2-26-050r.md) / [L2/26-132](../documents/utc-l2-26-132.md) まで続く。

主な論点は、106 characters から 95 characters、さらに 93 / 91 count へ変化する repertoire、vowels / dotted letters の combining vs atomic model、horizontal left-to-right と traditional vertical direction の扱い、contemporary invented script としての community evidence である。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2020-07-20 | UTC | [L2/20-180](../documents/utc-l2-20-180.md) | Mohamed Bentoura Bangoura が initial stage version 03 として KORE SEBELI / Wakara を 106 characters で提案した。 |
| 2021-09-27 | UTC | [L2/21-209](../documents/utc-l2-21-209.md) | Mohamed Bentoura Bangoura が 106 characters model を維持した 2021 年版 proposal を提出した。 |
| 2022-03-18 | UTC | [L2/22-073](../documents/utc-l2-22-073.md) | Charles L. Riley が African scripts status report で、KORE SEBELI proposal は提出済みだが widespread usage evidence と script details がさらに必要と記録した。 |
| 2022-10-03 | UTC | [L2/22-222](../documents/utc-l2-22-222.md) | Mohamed Bentoura Bangoura が initial stage version 05 として 106 characters model、community samples、vertical samples を更新した。 |
| 2023-09-21 | UTC | [L2/23-203](../documents/utc-l2-23-203.md) | Oreen Yousuf らが African scripts status report で、KORE SEBELI は 2009 年作成で継続的に教えられ、students が hundreds に達すると記録した。 |
| 2024-10-28 | UTC | [L2/24-246](../documents/utc-l2-24-246.md) | Mohamed Bentoura Bangoura が version 08 として 95 characters model に再編したが、proposal summary form には 106 characters と残る箇所がある。 |
| 2026-04-13 | UTC | [L2/26-050R](../documents/utc-l2-26-050r.md) | Mohamed Bentoura Bangoura が version 12 の revised proposal を提出し、表紙・目次では 93 characters、本文 section では 91 characters とした。 |
| 2026-05-14 | UTC | [L2/26-132](../documents/utc-l2-26-132.md) | Mohamed Bentoura Bangoura の KORE SEBELI proposal が UTC \#188 候補文書として登録された。抽出テキスト上は April 2026 version 12 と同内容である。 |

## 主な論点

### repertoire の安定化

2020-2022 年版は 106 characters model で、12 digits、30 lowercase、29 capital letters、4 combining diacritics / tone marks、punctuation、mathematical signs、vowel sequences を含む。2024 年版は 95 characters に再編し、2026 年版は表紙・目次・summary form で 93 characters、本文 section で 91 characters とする。

このため、KORE SEBELI の proposal を読むときは、最新版の count だけでなく、どの count が code chart / names list / property table と整合しているかを確認する必要がある。

### combining marks から atomic dotted letters へ

初期版は vowel distinctions を combining diacritics / sequences として扱い、dot を含む consonant letters は letter shape の一部として atomic に扱う。2026 年版では dots が letter shape に属し、base letter + dots を single atomic character として canonical decomposition しないという説明が強くなる。

この変化は normalization、search、case mapping、font behavior に関係するため、SEW / UTC review では既存 combining mark との重複や decomposability の説明が焦点になる。

### direction と vertical samples

各 proposal は horizontal left-to-right を default / assigned direction とする一方、vertical direction を elderly / traditional use、divination / talismanic context、sample として示す。Unicode で script direction をどう扱うかは、encoding そのものと vertical layout guidance を切り分けて読む必要がある。

### contemporary script evidence

proposal は Soso language community、teachers / students、syllabary、handwritten samples、songs、national anthem sample、font use、school / publication plans を evidence として示す。contemporary invented script としては、community use と orthographic stability が後続 review の中心になる。

## 関連文書

- [L2/20-180](../documents/utc-l2-20-180.md) - 2020 年 initial proposal、106 characters。
- [L2/21-209](../documents/utc-l2-21-209.md) - 2021 年版 proposal、106 characters。
- [L2/22-073](../documents/utc-l2-22-073.md) - African scripts implementation status report。
- [L2/22-222](../documents/utc-l2-22-222.md) - 2022 年 version 05、106 characters。
- [L2/23-203](../documents/utc-l2-23-203.md) - African scripts usage / implementation status report。
- [L2/24-246](../documents/utc-l2-24-246.md) - 2024 年 version 08、95 characters。
- [L2/26-050R](../documents/utc-l2-26-050r.md) - 2026 年 version 12 revised proposal、93 / 91 count。
- [L2/26-132](../documents/utc-l2-26-132.md) - UTC \#188 候補として登録された 2026 年 proposal。

## 関連トピック

- [Script Encoding Pipeline](script-encoding-pipeline.md)
- [Script and Notation Proposals](../families/script-and-notation-proposals.md)

## 出典

- `utc-l2-20-180` - <https://www.unicode.org/L2/L2020/20180-kore.pdf>
- `utc-l2-21-209` - <https://www.unicode.org/L2/L2021/21209-kore-sebeli.pdf>
- `utc-l2-22-073` - <https://www.unicode.org/L2/L2022/22073-african-script-status.pdf>
- `utc-l2-22-222` - <https://www.unicode.org/L2/L2022/22222-kore-sebeli.pdf>
- `utc-l2-23-203` - <https://www.unicode.org/L2/L2023/23203-update-african-scripts.pdf>
- `utc-l2-24-246` - <https://www.unicode.org/L2/L2024/24246-kore-sebeli.pdf>
- `utc-l2-26-050r` - <https://www.unicode.org/L2/L2026/26050r-kore-sebeli-proposal.pdf>
- `utc-l2-26-132` - <https://www.unicode.org/L2/L2026/26132-kore-sebeli-proposal.pdf>
