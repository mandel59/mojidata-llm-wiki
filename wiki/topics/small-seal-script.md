---
type: Topic
title: Small Seal Script
description: Shuowen Jiezi に基づく小篆を UCS / Unicode に独立 script として符号化する議論。
slug: small-seal-script
bodies: [UTC, WG2]
documents: [utc-l2-22-279, utc-l2-25-049, utc-l2-25-111, utc-l2-26-102, wg2-n4634, wg2-n4688, wg2-n5105, wg2-n5108, wg2-n5209, wg2-n5211, wg2-n5230, wg2-n5294r3, wg2-n5306, wg2-n5307r, wg2-n5312, wg2-n5313r, wg2-n5317r3, wg2-n5318r, wg2-n5327, wg2-n5337, wg2-n5341, wg2-n5344r2, wg2-n5346, wg2-n5348r, wg2-n5354, wg2-n5355, wg2-n5369]
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
| 2014-09 | WG2 / UTC | [WG2 N4634](../documents/wg2-n4634.md) / `L2/14-242` | TCA / China による Small Seal Script encoding proposal。 |
| 2015-10 | WG2 / UTC | [WG2 N4688](../documents/wg2-n4688.md) / `L2/15-281` | `Shuowen Jiezi` ベースの proposal 改訂。大容量 chart 付き。 |
| 2016-04 | WG2 / UTC | `WG2 N4716` / `L2/16-092` | Suzuki Toshiya が source-based variation selector の適用を提案。 |
| 2017-07 | WG2 | `WG2 N4835` | SC2/WG2 Small Seal Script ad hoc meeting の agenda / logistics。 |
| 2019-06 | WG2 / UTC | [WG2 N5105](../documents/wg2-n5105.md), [WG2 N5108](../documents/wg2-n5108.md) / `L2/19-228`, `L2/19-245` | TCA / China proposal appendix 改訂と WG2 \#68 での Seal Script discussion report。 |
| 2022-11 | UTC | `L2/22-279` | Richard Cook による UCS Seal Script Source Mapping Data。以後の repertoire 整理の土台になる。 |
| 2023-03 | WG2 | [WG2 N5209](../documents/wg2-n5209.md) | Michel Suignard が Small Seal encoding initiative の consideration と表形式 dataset を提示。 |
| 2023-04 | WG2 | [WG2 N5211](../documents/wg2-n5211.md) | Suzuki Toshiya と Richard Cook が 14-column Seal Script glyph comparison chart documentation を archival reference として登録した。 |
| 2023-06 | WG2 | [WG2 N5230](../documents/wg2-n5230.md) | TCA が N5209 への feedback として THX 未収録 55 entries の分類、modern CJK 対応値 2,883 件の修正データを提示した。 |
| 2024-06 | WG2 | [WG2 N5273](../documents/wg2-n5273.md) | TCA and China experts が N5209 の 55 entries を 8 duplicates と 47 separately encodable entries に分け、DYC 由来 2 entries の追加を提案した。 |
| 2025-01 | WG2 / UTC | [WG2 N5294R3](../documents/wg2-n5294r3.md) / `L2/25-049` | 11,140 code points の mature repertoire として整理。THX / CCZ / QJZ / DYC の 4 source model と database record を提示。 |
| 2025-03 | WG2 / UTC | `WG2 N5306` / `L2/25-111` | 残る unification / disunification issue を約 450 要素として整理し、最終 proposal 前の review に進む。 |
| 2025-05 | WG2 | [WG2 N5312](../documents/wg2-n5312.md) | TCA and China が N5294R2 / N5294R3 に対し、17 variant sets、19 separate-code candidates、mapping errors、24 THX glyph corrections を返した。 |
| 2025-06 | WG2 | [WG2 N5307R](../documents/wg2-n5307r.md), [WG2 N5313R](../documents/wg2-n5313r.md), [WG2 N5327](../documents/wg2-n5327.md), [WG2 N5337](../documents/wg2-n5337.md) | Mapping principles と revised feedback をめぐり、Guwen / Zhouwen / Zhengzhuan、source replacement、Shuowen radical system の扱いが整理された。 |
| 2025-06 | WG2 | [WG2 N5317R3](../documents/wg2-n5317r3.md), [WG2 N5318R](../documents/wg2-n5318r.md), [WG2 N5341](../documents/wg2-n5341.md) | TCA / China feedback を disposition し、Four-Column Small Seal Script proposal と code chart / dataset をまとめる。 |
| 2025-06 | WG2 | `WG2 N5304` | [WG2 M72.13 Small Seal future edition candidate](../events/wg2-m72-13-small-seal-future-candidate.md)。 |
| 2025-10 | WG2 | [WG2 N5346](../documents/wg2-n5346.md) | TCA and China が N5341 code chart に 43 code point issues と 3,121 modern CJK equivalent corrections を返した。 |
| 2026-01 | WG2 | [WG2 N5344R2](../documents/wg2-n5344r2.md) | Small Seal WG が revised proposal を提出。11,328 characters を `3D000..3FC3F` の `Small Seal` block に置く案へ更新。 |
| 2026-03 | WG2 | [WG2 N5348R](../documents/wg2-n5348r.md), [WG2 N5355](../documents/wg2-n5355.md) | modern CJK 対応値、`liding`（隷定）、`zhèngzhuàn`（正篆）/ `chóngwén`（重文）に関する feedback と clarification。 |
| 2026-06 | WG2 | `WG2 N5354`, `WG2 N5369` | [WG2 M73.01 Small Seal CD4 disposition](../events/wg2-m73-01-small-seal-cd4-disposition.md)。M73.04 は 7th edition DIS への進行を勧告。 |

## 主な論点

### 独立 script として扱うか

Small Seal は modern Hanzi の書体差ではなく、`Oracle Bone script`、`Bronze inscriptions`、`Warring States scripts` などと同じく古代漢字の発展段階に属する文字集合として説明されている。`WG2 N5306` と [WG2 N5344R2](../documents/wg2-n5344r2.md) は、Small Seal が modern Hanzi と一対一対応しないこと、構造が異なることを理由に、UCS 上で独立符号化すべきだと整理している。

[WG2 N4634](../documents/wg2-n4634.md) はこの根拠を初期 proposal の段階で示し、Tenghuaxie version を基準に 10,516 characters を独立 script として提案した。[WG2 N5105](../documents/wg2-n5105.md) では appendix が 11,093 characters に改訂され、Tenghuaxie serial number、original glyph、representative glyph、modern CJK equivalent、Shuowen radical を含む table structure が整えられた。

[WG2 N4688](../documents/wg2-n4688.md) は N4634 を 14-volume appendix 付きの complete proposal へ進め、11,108 characters を提案した。後続の N5105 は、N4688 の repeated characters 15 件を削除して 11,093 characters に整理する。

### 4 source model

最近の提案は、`THX` を主たる ordering / repertoire の基準にしつつ、`CCZ`、`QJZ`、`DYC` を同じ code chart 上に並べる four-column layout を採用している。[WG2 N5294R3](../documents/wg2-n5294r3.md) は 11,108 THX entries と、QJZ / DYC 由来の追加候補から 11,140 code points を構成した。[WG2 N5344R2](../documents/wg2-n5344r2.md) では整理後の proposal が 11,328 characters になり、range も `38000..3AC4A` から `3D000..3FC3F` に移っている。

[WG2 N5209](../documents/wg2-n5209.md) は TCA / China の THX-based proposal と Richard Cook の [L2/22-279](../documents/utc-l2-22-279.md) を比較し、X / THX、K / QJZ、D / DYC の source mapping を同じ database で扱う道筋を示した。[WG2 N5211](../documents/wg2-n5211.md) は、X / D / K の 14-column comparison chart と source caveats を documentation 化した。[WG2 N5230](../documents/wg2-n5230.md) は、TCA 側から THX 未収録 55 entries と modern CJK 対応値を見直し、[WG2 N5273](../documents/wg2-n5273.md) はそれを 8 duplicates、47 separately encodable entries、追加 DYC 2 entries へ整理した。ここで整理された `kSEAL_THXSrc`、`kSEAL_MCJK`、`kSEAL_Rad` などの data idea は、後続の proposal と UAX \#60 に接続する。

### Unification / disunification

初期整理では variant set と重複 source の扱いが大きな論点だった。`WG2 N5306` は最終 proposal 前に約 450 要素の review が必要とし、`WG2 N5317R3` は TCA / China feedback に基づいて actionable dispositions を作った。WG2 \#72 での処理は [WG2 M72.13 Small Seal future edition candidate](../events/wg2-m72-13-small-seal-future-candidate.md) に集約する。

[WG2 N5108](../documents/wg2-n5108.md) は、2019 年時点で Zhuanwen / Guwen / Zhouwen を基本的に disunify し、同じ semantics を持つ非常に似た glyph は radical が異なっても unify するという discussion summary を残した。同時に、他 versions と taxonomy / ordering の追加議論が必要で、CD / CDAM text に入れるには早いと整理している。

[WG2 N5307R](../documents/wg2-n5307r.md) は、同じ written form 内での component / explanation / structure 差を見て unified / disunified を判断する principles を示し、Zhengzhuan、Guwen、Zhouwen のような異なる written forms は別 characters として扱う。

[WG2 N5312](../documents/wg2-n5312.md) と [WG2 N5313R](../documents/wg2-n5313r.md) は、この principles を実際の variant sets / 457 disunification cases に適用した TCA / China feedback である。[WG2 N5327](../documents/wg2-n5327.md) は、微妙な style difference を別符号化の根拠にしすぎることへの懸念と、source replacement / Annex documentation の必要性を示し、[WG2 N5337](../documents/wg2-n5337.md) は Shuowen radical system と source tradition を重視する TCA 側の response を返した。

### Modern CJK 対応値

`kSEAL_MCJK` のような modern CJK 対応値は検索・索引に有用だが、対応が常に一意ではない。[WG2 N5348R](../documents/wg2-n5348r.md) では Kushim Jiang と CheonHyeong Sim の feedback により、modern CJK value の修正候補が議論された。TCA / China experts は、Small Seal と modern CJK の形、発音、意味が一致する場合はその modern CJK を優先し、一致しない場合は `zhèngzì`（正字）を用いるという方針を示した。

`WG2 N5355` はこの `zhèngzì`（正字）の意味を補足し、対応する modern equivalent がない `chóngwén`（重文）では、関連する `zhèngzhuàn`（正篆）の modern equivalent を retrieval 用の indexing form として使う、という整理を示している。

[WG2 N5346](../documents/wg2-n5346.md) は、[WG2 N5341](../documents/wg2-n5341.md) code chart review で 3,121 entries の modern CJK equivalent correction を提示した。ここでは、一般的に使われる現代漢字よりも Small Seal glyph に近い CJK character form を採用する方針が示され、`kSEAL_MCJK` は検索・索引用 data として継続的に修正される対象であることが明確になる。

### 名称と property

[WG2 N5344R2](../documents/wg2-n5344r2.md) では script property と character names は ISO 15924 に合わせて `Seal` を使う案だった。WG2 \#73 の CD.4 disposition による名称・property 変更は [WG2 M73.01 Small Seal CD4 disposition](../events/wg2-m73-01-small-seal-cd4-disposition.md) に集約する。具体的には、`WG2 N5369` が `3D000..3FC3F` の names を `SMALL SEAL CHARACTER-XXXXX` に変え、6 characters の `kSEAL_Rad`、20 characters の `kSEAL_MCJK`、U+3F80E の glyph correction を採択した。

Unicode 18.0 draft release page と beta review page では、Seal が Unicode 18.0 の 4 new scripts の一つとして扱われ、Seal block は `3D000..3FC3F`、新 data file として `SealSources.txt` が示されている。Unicode 18.0 全体の変更点資料は [Unicode 18.0 Change Sources](unicode-18-change-sources.md) にまとめる。

## 現状

2026-06-26 の WG2 \#73 recommendations 時点では、Small Seal は ISO/IEC 10646 7th edition CD4 の disposition に含まれており、M73.04 はその変更を含む DIS text を SC2 secretariat に回すことを勧告している。M73.04 の target は DIS 2026-10-01、IS 2027-06-01。

## 関連文書

- [WG2 N5344R2](../documents/wg2-n5344r2.md) - revised proposal
- [WG2 N4634](../documents/wg2-n4634.md) - initial proposal
- [WG2 N4688](../documents/wg2-n4688.md) - 2015 complete proposal
- [WG2 N5105](../documents/wg2-n5105.md) - proposal appendix update
- [WG2 N5108](../documents/wg2-n5108.md) - WG2 \#68 discussion report
- [WG2 N5209](../documents/wg2-n5209.md) - source mapping comparison and database considerations
- [WG2 N5211](../documents/wg2-n5211.md) - 14-column Seal Script glyph comparison chart documentation
- [WG2 N5230](../documents/wg2-n5230.md) - TCA feedback to N5209 and modern CJK correction data
- [WG2 N5273](../documents/wg2-n5273.md) - N5209 への TCA / China response
- [WG2 N5294R3](../documents/wg2-n5294r3.md) - 11,140 code point repertoire and database model
- [WG2 N5312](../documents/wg2-n5312.md) - N5294R2 / N5294R3 への TCA / China feedback
- [WG2 N5307R](../documents/wg2-n5307r.md) - Small Seal glyph mapping principles
- [WG2 N5313R](../documents/wg2-n5313r.md) - N5306 への revised feedback
- [WG2 N5327](../documents/wg2-n5327.md) - N5313R への comment
- [WG2 N5337](../documents/wg2-n5337.md) - N5327 への TCA response
- [WG2 N5341](../documents/wg2-n5341.md) - code charts and data set
- [WG2 N5346](../documents/wg2-n5346.md) - N5341 code chart feedback and modern CJK corrections
- [WG2 N5348R](../documents/wg2-n5348r.md) - modern CJK / `zhèngzì`（正字）feedback summary
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
- [Suzuki Toshiya](../people/suzuki-toshiya.md)
- [WG2](../people/wg2.md)
- [UTC](../people/utc.md)
- [China](../people/china.md)
- [TCA](../people/tca.md)

## 出典

- `wg2-n4634` - <http://www.unicode.org/wg2/docs/n4634.pdf>
- `utc-l2-14-242` / alias of `wg2-n4634` - <https://www.unicode.org/L2/L2014/14242-n4634.pdf>
- `wg2-n4688` - <http://www.unicode.org/wg2/docs/n4688%20Small%20Seal%20Script.zip>
- `utc-l2-15-281` / alias of `wg2-n4688` - <https://www.unicode.org/L2/L2015/15281-n4688-small-seal.pdf>
- `wg2-n5105` - <https://unicode.org/wg2/docs/n5105_smallseal%20Appendix%20update_V2%20.pdf>
- `utc-l2-19-228` / alias of `wg2-n5105` - <https://www.unicode.org/L2/L2019/19228-n5105-small-seal-update.pdf>
- `wg2-n5108` - <https://unicode.org/wg2/docs/n5108-Seal-da_rev3.pdf>
- `utc-l2-19-245` / alias of `wg2-n5108` - <https://www.unicode.org/L2/L2019/19245-n5108-seal-report.pdf>
- `wg2-n5209` - <https://www.unicode.org/wg2/docs/n5209-ConsiderationsSmallSeal.pdf>
- `wg2-n5211` - <https://www.unicode.org/wg2/docs/n5211-14-columnchart-documentation.pdf>
- `wg2-n5230` - <https://www.unicode.org/wg2/docs/n5230-TCA%20Feedback%20to%20N5209.pdf>
- `wg2-n5273` - <https://www.unicode.org/wg2/docs/n5273-Response%20to%20WG2N5209seal_20240606.pdf>
- `utc-l2-22-279` - <https://www.unicode.org/L2/L2022/22279-ucs-seal-map.pdf>
- `utc-l2-25-049` - <https://www.unicode.org/L2/L2025/25049r-considerations-small-seal.pdf>
- `utc-l2-25-111` - <https://www.unicode.org/L2/L2025/25111-converging-small-seal.pdf>
- `wg2-n5294r3` - <https://www.unicode.org/wg2/docs/n5294R3-ConsiderationsSmallSeal.pdf>
- `wg2-n5306` - <https://www.unicode.org/wg2/docs/n5306-ConvergingSmallSeal.pdf>
- `wg2-n5312` - <https://www.unicode.org/wg2/docs/n5312-Feedback%20to%20N5294R2%20&%20N5294R3.pdf>
- `wg2-n5313r` - <https://www.unicode.org/wg2/docs/n5313R-Feedback%20to%20N5306.pdf>
- `wg2-n5327` - <https://www.unicode.org/wg2/docs/n5327-mpsuzuki-comment-on-n5313r.pdf>
- `wg2-n5337` - <https://www.unicode.org/wg2/docs/n5337-Feedback%20to%20N5327.pdf>
- `wg2-n5304` - <https://www.unicode.org/wg2/docs/n5304-Mtg72-Niigata-Recs-rev5-final.pdf>
- `wg2-n5317` - <https://www.unicode.org/wg2/docs/n5317R3-SmallSealFeedback.pdf>
- `wg2-n5318` - <https://www.unicode.org/wg2/docs/n5318R-Proposal%20to%20encode%20Four-Column%20Small%20Seal%20Script%20in%20UCS.pdf>
- `wg2-n5341` - <https://www.unicode.org/wg2/docs/n5341-SmallSealChart.pdf>
- `wg2-n5344r2` - <https://www.unicode.org/wg2/docs/n5344R2-SmallSealProposal.pdf>
- `wg2-n5346` - <https://www.unicode.org/wg2/docs/n5346-FeedbackToN5341.pdf>
- `wg2-n5348r` - <https://www.unicode.org/wg2/docs/n5348R-SmallSealFeedback.pdf>
- `wg2-n5354` - <https://www.unicode.org/wg2/docs/n5354-Mtg73-Paris-Recs-rev5.pdf>
- `wg2-n5355` - <https://www.unicode.org/wg2/docs/n5355-SealNormalizedForm.pdf>
- `wg2-n5369` - <https://www.unicode.org/wg2/docs/n5369-CD7th-4-DOC.pdf>
- Unicode 18.0 draft release page - <https://www.unicode.org/versions/Unicode18.0.0/>
- Unicode 18.0 beta review page - <https://www.unicode.org/versions/beta-18.0.0.html>
