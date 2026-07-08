---
type: Topic
title: Small Seal Script
description: Shuowen Jiezi に基づく小篆を UCS / Unicode に独立 script として符号化する議論。
slug: small-seal-script
bodies: [UTC, WG2]
documents: [utc-l2-14-242, utc-l2-15-281, utc-l2-22-279, utc-l2-25-049, utc-l2-25-111, utc-l2-26-102, wg2-n4634, wg2-n4688, wg2-n5209, wg2-n5294, wg2-n5306, wg2-n5317r3, wg2-n5318r, wg2-n5344, wg2-n5348, wg2-n5354, wg2-n5355, wg2-n5369]
status: in-ballot-pipeline
tags: [script, seal, cjk, ideographic]
timestamp: 2026-07-06T21:31:45+09:00
---

# Small Seal Script

## 概要

Small Seal Script は、`Shuowen Jiezi` に基づく小篆を UCS / Unicode に独立した script として符号化する提案である。議論の中心は、modern Han の書体差として扱うのではなく、古代漢字研究のための独立した文字集合として扱うべきか、また `Shuowen Jiezi` の複数版本をどう統合するかにある。

提案は TCA と China による初期 proposal から始まり、Richard Cook の source mapping、Suzuki Toshiya の 14-column comparison、Michel Suignard による repertoire / database 整理を経て、WG2 \#72 で将来版候補になった。その後、WG2 \#73 では ISO/IEC 10646 7th edition CD4 の disposition に Small Seal の名称・property 修正が入っており、DIS へ進む流れに載っている。

## 経緯

| 年月 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 2014-09 | WG2 / UTC | `WG2 N4634` / `L2/14-242` | TCA / China による Small Seal Script encoding proposal。 |
| 2015-10 | WG2 / UTC | `WG2 N4688` / `L2/15-281` | `Shuowen Jiezi` ベースの proposal 改訂。大容量 chart 付き。 |
| 2016-04 | WG2 / UTC | `WG2 N4716` / `L2/16-092` | Suzuki Toshiya が source-based variation selector の適用を提案。 |
| 2017-07 | WG2 | `WG2 N4835` | SC2/WG2 Small Seal Script ad hoc meeting の agenda / logistics。 |
| 2019-06 | WG2 / UTC | `WG2 N5105`, `WG2 N5108` / `L2/19-228`, `L2/19-245` | TCA / China proposal appendix 改訂と WG2 \#68 での Seal Script discussion report。 |
| 2022-11 | UTC | `L2/22-279` | Richard Cook による UCS Seal Script Source Mapping Data。以後の repertoire 整理の土台になる。 |
| 2023-03 | WG2 | `WG2 N5209` | Michel Suignard が Small Seal encoding initiative の consideration と表形式 dataset を提示。 |
| 2025-01 | WG2 / UTC | `WG2 N5294` / `L2/25-049` | 11,140 code points の mature repertoire として整理。THX / CCZ / QJZ / DYC の 4 source model と database record を提示。 |
| 2025-03 | WG2 / UTC | `WG2 N5306` / `L2/25-111` | 残る unification / disunification issue を約 450 要素として整理し、最終 proposal 前の review に進む。 |
| 2025-06 | WG2 | [WG2 N5317R3](../documents/wg2-n5317r3.md), [WG2 N5318R](../documents/wg2-n5318r.md), [WG2 N5341](../documents/wg2-n5341.md) | TCA / China feedback を disposition し、Four-Column Small Seal Script proposal と code chart / dataset をまとめる。 |
| 2025-06 | WG2 | `WG2 N5304` | [WG2 M72.13 Small Seal future edition candidate](../events/wg2-m72-13-small-seal-future-candidate.md)。 |
| 2026-01 | WG2 | `WG2 N5344` | Small Seal WG が revised proposal を提出。11,328 characters を `3D000..3FC3F` の `Small Seal` block に置く案へ更新。 |
| 2026-03 | WG2 | `WG2 N5348`, `WG2 N5355` | modern CJK 対応値、`liding`（隷定）、`zhèngzhuàn`（正篆）/ `chóngwén`（重文）に関する feedback と clarification。 |
| 2026-06 | WG2 | `WG2 N5354`, `WG2 N5369` | [WG2 M73.01 Small Seal CD4 disposition](../events/wg2-m73-01-small-seal-cd4-disposition.md)。M73.04 は 7th edition DIS への進行を勧告。 |

## 主な論点

### 独立 script として扱うか

Small Seal は modern Hanzi の書体差ではなく、`Oracle Bone script`、`Bronze inscriptions`、`Warring States scripts` などと同じく古代漢字の発展段階に属する文字集合として説明されている。`WG2 N5306` と `WG2 N5344` は、Small Seal が modern Hanzi と一対一対応しないこと、構造が異なることを理由に、UCS 上で独立符号化すべきだと整理している。

### 4 source model

最近の提案は、`THX` を主たる ordering / repertoire の基準にしつつ、`CCZ`、`QJZ`、`DYC` を同じ code chart 上に並べる four-column layout を採用している。`WG2 N5294` は 11,108 THX entries と、QJZ / DYC 由来の追加候補から 11,140 code points を構成した。`WG2 N5344` では整理後の proposal が 11,328 characters になり、range も `38000..3AC4A` から `3D000..3FC3F` に移っている。

### Unification / disunification

初期整理では variant set と重複 source の扱いが大きな論点だった。`WG2 N5306` は最終 proposal 前に約 450 要素の review が必要とし、`WG2 N5317R3` は TCA / China feedback に基づいて actionable dispositions を作った。WG2 \#72 での処理は [WG2 M72.13 Small Seal future edition candidate](../events/wg2-m72-13-small-seal-future-candidate.md) に集約する。

### Modern CJK 対応値

`kSEAL_MCJK` のような modern CJK 対応値は検索・索引に有用だが、対応が常に一意ではない。`WG2 N5348` では Kushim Jiang と CheonHyeong Sim の feedback により、modern CJK value の修正候補が議論された。TCA / China experts は、Small Seal と modern CJK の形、発音、意味が一致する場合はその modern CJK を優先し、一致しない場合は `zhèngzì`（正字）を用いるという方針を示した。

`WG2 N5355` はこの `zhèngzì`（正字）の意味を補足し、対応する modern equivalent がない `chóngwén`（重文）では、関連する `zhèngzhuàn`（正篆）の modern equivalent を retrieval 用の indexing form として使う、という整理を示している。

### 名称と property

`WG2 N5344` では script property と character names は ISO 15924 に合わせて `Seal` を使う案だった。WG2 \#73 の CD.4 disposition による名称・property 変更は [WG2 M73.01 Small Seal CD4 disposition](../events/wg2-m73-01-small-seal-cd4-disposition.md) に集約する。具体的には、`WG2 N5369` が `3D000..3FC3F` の names を `SMALL SEAL CHARACTER-XXXXX` に変え、6 characters の `kSEAL_Rad`、20 characters の `kSEAL_MCJK`、U+3F80E の glyph correction を採択した。

Unicode 18.0 draft release page と beta review page では、Seal が Unicode 18.0 の 4 new scripts の一つとして扱われ、Seal block は `3D000..3FC3F`、新 data file として `SealSources.txt` が示されている。Unicode 18.0 全体の変更点資料は [Unicode 18.0 Change Sources](unicode-18-change-sources.md) にまとめる。

## 現状

2026-06-26 の WG2 \#73 recommendations 時点では、Small Seal は ISO/IEC 10646 7th edition CD4 の disposition に含まれており、M73.04 はその変更を含む DIS text を SC2 secretariat に回すことを勧告している。M73.04 の target は DIS 2026-10-01、IS 2027-06-01。

## 関連文書

- [WG2 N5344](../documents/wg2-n5344.md) - revised proposal
- [WG2 N5348](../documents/wg2-n5348.md) - modern CJK / `zhèngzì`（正字）feedback summary
- [WG2 N5355](../documents/wg2-n5355.md) - `zhèngzhuàn`（正篆）/ `chóngwén`（重文）clarification
- [WG2 N5369](../documents/wg2-n5369.md) - CD.4 disposition of comments
- [WG2 meeting \#72](../meetings/wg2/wg2-meeting-72.md)
- [WG2 meeting \#73](../meetings/wg2/wg2-meeting-73.md)
- [Unicode 18.0 Change Sources](unicode-18-change-sources.md)
- [Han Ideographic Scripts](../families/han-ideographic-scripts.md)

## 関連出来事

- [WG2 M72.13 Small Seal future edition candidate](../events/wg2-m72-13-small-seal-future-candidate.md)
- [WG2 M73.01 Small Seal CD4 disposition](../events/wg2-m73-01-small-seal-cd4-disposition.md)

## 関連人物・組織

- [Michel Suignard](../people/michel-suignard.md)
- [Richard Cook](../people/richard-cook.md)
- [WG2](../people/wg2.md)
- [UTC](../people/utc.md)
- [China](../people/china.md)
- [TCA](../people/tca.md)

## 出典

- `utc-l2-14-242` - <https://www.unicode.org/L2/L2014/14242-n4634.pdf>
- `utc-l2-15-281` - <https://www.unicode.org/L2/L2015/15281-n4688-small-seal.pdf>
- `utc-l2-22-279` - <https://www.unicode.org/L2/L2022/22279-ucs-seal-map.pdf>
- `utc-l2-25-049` - <https://www.unicode.org/L2/L2025/25049r-considerations-small-seal.pdf>
- `utc-l2-25-111` - <https://www.unicode.org/L2/L2025/25111-converging-small-seal.pdf>
- `wg2-n5294` - <https://www.unicode.org/wg2/docs/n5294R3-ConsiderationsSmallSeal.pdf>
- `wg2-n5306` - <https://www.unicode.org/wg2/docs/n5306-ConvergingSmallSeal.pdf>
- `wg2-n5304` - <https://www.unicode.org/wg2/docs/n5304-Mtg72-Niigata-Recs-rev5-final.pdf>
- `wg2-n5317` - <https://www.unicode.org/wg2/docs/n5317R3-SmallSealFeedback.pdf>
- `wg2-n5318` - <https://www.unicode.org/wg2/docs/n5318R-Proposal%20to%20encode%20Four-Column%20Small%20Seal%20Script%20in%20UCS.pdf>
- `wg2-n5344` - <https://www.unicode.org/wg2/docs/n5344R2-SmallSealProposal.pdf>
- `wg2-n5348` - <https://www.unicode.org/wg2/docs/n5348R-SmallSealFeedback.pdf>
- `wg2-n5354` - <https://www.unicode.org/wg2/docs/n5354-Mtg73-Paris-Recs-rev5.pdf>
- `wg2-n5355` - <https://www.unicode.org/wg2/docs/n5355-SealNormalizedForm.pdf>
- `wg2-n5369` - <https://www.unicode.org/wg2/docs/n5369-CD7th-4-DOC.pdf>
- Unicode 18.0 draft release page - <https://www.unicode.org/versions/Unicode18.0.0/>
- Unicode 18.0 beta review page - <https://www.unicode.org/versions/beta-18.0.0.html>
