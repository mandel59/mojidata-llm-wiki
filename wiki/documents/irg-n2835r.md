---
type: Source Document
title: "Proposal for changing the source reference information for 1,417 G-Source characters"
description: "Boris Zhang が GHC / GCH / GCY-source 1,417 charactersのcode point型referenceを、根拠辞書中の位置に対応するreferenceへ置き換えるよう提案した文書。"
resource: https://www.unicode.org/irg/docs/n2835r-GSourceChanges.pdf
entry_id: irg-n2835r
doc_number: IRG N2835R
document_type: proposal
registry: irg
date: "2025-08-26"
source: ZHANG, Boris
documents: [irg-n2689, irg-n2837, irg-n2838, irg-n2864r, irg-n2868]
topics: [g-source-glyph-and-reference-issues, irg-source-data-and-representative-glyphs]
people: [boris-zhang, china, irg]
meetings: [irg-meeting-65]
tags: [document, irg, g-source, source-reference, unihan, proposal]
timestamp: 2026-07-10T00:00:00+09:00
---

# IRG N2835R

## 要約

`IRG N2835R` は、GHC 601、GCH 624、GCY 192、計1,417 charactersのG-source reference valuesを、characterのevidenceとなる辞書上の位置へ対応づけ直す個人提案である。`IRG N2689`によってUnicode 17.0 alpha reviewではこれらのreferenceがcode point型の値へ更新されたが、文書はその形式がsource内の位置を示さず紛らわしいとして再変更を求める。

基準資料は《汉语大词典》第一版、《辞海》1999年版普及本、《辭源》建國60週年紀念版である。辞書で確認できないcharacterについては、別のG-source evidenceが確認できればそのsourceへ移し、それもない場合は`GU-<code point>`へ移す。これはIRGとChinaによる検討を求めたproposalであり、変更の採択記録ではない。

## 提案内容

| 現行source | 件数 | 基準資料 | proposed referenceの考え方 |
| --- | ---: | --- | --- |
| GHC | 601 | 《汉语大词典》第一版 | 538 charactersを辞書中で確認し、volume・page・同一page内の順序を表す7-digit suffixへ更新する。未確認63のうち19はGHZR / GZH / GGFZ / GCE等の別sourceへ、残る44はGU-sourceへ移す。 |
| GCH | 624 | 《辞海》1999年版普及本 | 辞書のpageと同一page内のpositionを表す`GCH-dddd.dd`形式へ更新する。 |
| GCY | 192 | 《辭源》建國60週年紀念版 | 同書に対応するpage / position形式へ更新する。本文が詳述するExtensions B / Eの69 charactersでは37を辞書中で確認し、未確認32のうち28をGHZR / GZH / GHC等へ、4をGU-sourceへ移す。 |

GHCの`GHC-xxyyyyz`は、`xx`がvolume、`yyyy`がpage、末尾`z`が同一page上のcharacterを区別するdigitである。GCH / GCYは`dddd.dd`型で、pageとpage内positionを表す。したがって提案の中心は、source prefixの直後にUnicode code pointを置く暫定的な識別から、実際のpublishing sourceを辿れるreferenceへ戻すことにある。

本文はcharacterごとにlocation、old reference、proposed referenceを列挙する。catalogに関連リンクとして登録された1.4GBのevidence ZIPは辞書画像等を収める添付物であり、proposal本文そのものとは区別される。

## 後続決定

`IRG N2835R`の表紙は`Status: Individual Contribution`、`Action: For consideration by IRG and China`であり、本文単独から採択を読み取ることはできない。

`IRG N2838`は初版に対し、GHC suffixの付番、GCHで用いる《辞海》の版・刷、GCYの対象範囲やreference valuesなどを再検討した。revised版である本書はその指摘を一部反映したが、`IRG N2868`はoriginal submission当時の辞書edition / printingとの対応をさらに検討する必要があると論じた。

[IRG N2864R](irg-n2864r.md) は、本提案、`IRG N2837`、`IRG N2838`、`IRG N2868`等を統合し、GCH 624、GCY 192、GHC 601を含む1,538 charactersのChina member-body proposalへ再構成した。したがって`IRG N2864R`は本提案の後続整理だが、本書自体を採択記録へ変えるものではない。

## 論点

### source identityとreference syntax

GHC / GCH / GCYというprefixだけでは、個々のcharacterが辞書のどこに存在するかを示せない。code pointをsuffixにした値も一意ではあるが、publishing sourceの検証可能な位置情報にはならない。本提案はreferenceをvolume / page / positionに結び直す一方、同一page内のsuffix規則やeditionの特定が不正確なら新たな不整合を生むため、後続feedbackで値と書誌情報の双方が検証された。

### 辞書にないcharacterの扱い

基準辞書で見つからないcharacterを元のprefixに留めず、別の根拠資料があれば別sourceへ、なければGU-sourceへ移す方針を採る。この処理はreference valueの修正だけでなくsource identityの変更を伴うため、個別evidenceの確認が必要である。

## 関連文書

- `IRG N2689` - Unicode 17.0向けにGHC / GCH / GCYをcode point型referenceへ更新した先行提案。
- `IRG N2838` - 本提案のvaluesとsyntaxへのfeedback。
- [IRG N2837](irg-n2837.md) - 82 GXC-source charactersを辞書位置へ対応づける並行提案。
- [IRG N2868](irg-n2868.md) - source edition / printingとreference syntaxを再検討したfeedback。
- [IRG N2864R](irg-n2864r.md) - 本提案を含む1,538 G-source updatesの後続member-body proposal。
- [G-source Glyph and Source Reference Issues](../topics/g-source-glyph-and-reference-issues.md)
- [IRG Source Data and Representative Glyphs](../topics/irg-source-data-and-representative-glyphs.md)

## 出典

- `irg-n2835r` - <https://www.unicode.org/irg/docs/n2835r-GSourceChanges.pdf>
- `irg-n2835r` evidence ZIP - <https://www.unicode.org/irg/docs/n2835-Evidence.zip>
- `irg-n2838` - <https://www.unicode.org/irg/docs/n2838-IRGN2835Feedback.pdf>
- `irg-n2868` - <https://www.unicode.org/irg/docs/n2868-IRGN2835R-N2837-N2838Feedback.pdf>
- `irg-n2864r` - <https://www.unicode.org/irg/docs/n2864r-GSourceChanges.pdf>
