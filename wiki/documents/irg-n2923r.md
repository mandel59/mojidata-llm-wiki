---
type: Source Document
title: "Proposal for updating G-source references for 329 characters and G-source horizontal extensions for 9 characters"
description: "Dong Wenjie が GXH / GGH / GXC / GRM / GDZ / GWZ source references の syntax と実参照を見直し、329 characters の G-source reference updates と 9 characters の horizontal extensions を提案した文書。"
resource: https://www.unicode.org/irg/docs/n2923r-GSourceChanges.pdf
entry_id: irg-n2923r
doc_number: IRG N2923R
document_type: proposal
registry: irg
date: "2026-03-10"
source: DONG, Wenjie
documents: [irg-n743, irg-n891, irg-n1519, irg-n1528, irg-n1532r, irg-n2837, irg-n2864r, irg-n2868, irg-n2909, irg-n2911, irg-n2919r, irg-n2929, irg-n2930]
topics: [g-source-glyph-and-reference-issues, irg-source-data-and-representative-glyphs, cjk-horizontal-extensions]
people: [china, irg]
meetings: [irg-meeting-66, irg-meeting-67]
tags: [document, irg, g-source, source-reference, horizontal-extension, proposal]
timestamp: 2026-07-08T00:00:00+09:00
---

# IRG N2923R

## 要約

`IRG N2923R` は、G-source references for 329 characters と G-source horizontal extensions for 9 characters を提案する大規模な source-reference review document である。対象は GXH、GGH、GXC、GRM、GDZ、GWZ sources で、original source usage をより正確に反映するために reference syntax と実参照を見直すことを目的とする。

文書は、GXH / GGH / GXC について original proposal 時に使われた辞書 edition / printing を特定し、page number と ordinal number に基づく syntax へ整理する。GRM / GDZ / GWZ については、既存 dot syntax が有効な情報を分けていないとして、code point suffix による syntax change または source usage の abandonment と supplemental references を選択肢にする。

## 提案内容

| Source | 対象 | 提案の要点 |
| --- | --- | --- |
| GXH | 4 characters | Xinhua Dictionary (1998 Revised Edition) を reference とし、`GXH-xxxx.yy` 型の page / ordinal syntax を提案する。 |
| GGH | 226 characters | Gǔdài Hànyǔ Cídiǎn 1st Edition, Shenyang printing を reference とし、GGH references を page / ordinal syntax へ整理する。 |
| GXC | 83 characters | Xiàndài Hànyǔ Cídiǎn Revised Edition 3rd Edition をより適切な reference とし、GXC references を整理する。 |
| GRM / GDZ / GWZ | 3 / 1 / 12 characters | dot syntax の意味が薄いとして、code point suffix による syntax change または supplemental references への置換を提案する。 |
| Horizontal extensions | 9 characters | GGH-source 6 characters、GXC-source 3 characters を horizontal extension 候補として Appendix B に示す。 |

文書には proposed source reference values の plain text attachment と、evidence ZIP が付く。catalog では evidence ZIP も related link として記録されている。

## 後続決定

[IRG N2911](irg-n2911.md) は、`IRG N2919R` と `IRG N2923R` に含まれる 342 G-source reference changes について、further discussion が必要であり、IRG Meeting \#66 では action しなかったと記録している。China は Meeting \#67 に response を提出する予定とされた。

同じ report は、`IRG N2923R` Appendix B の 9 horizontal extension candidates について、China が別 proposal を準備するか、revised `IRG N2929R` に merge することを検討するよう求めている。したがって、この文書は accepted changes ではなく、large-scale source reference redesign と horizontal extension candidate list として読む。

## 論点

### original proposal history と source syntax

`IRG N2923R` は、source reference value を現行辞書版に合わせるのではなく、Ext. C / Ext. E submission の時点で実際に使われた edition / printing に戻って検討する。これは source reference が単なる bibliographic label ではなく、encoding proposal history を再現する identifier でもあることを示す。

### bulk update の review cost

329 reference updates と 9 horizontal extensions は、個別 glyph issue より review cost が高い。IRG Meeting \#66 が immediate action を取らず China response 待ちにしたのは、source syntax redesign、evidence stability、existing data compatibility をまとめて検討する必要があるためである。

## 関連文書

- [IRG N2911](irg-n2911.md) - Meeting \#66 editorial report。
- [IRG N2909](irg-n2909.md) - Meeting \#66 recommendations。
- [IRG N2919R](irg-n2919r.md) - 3 G-source glyphs and 10 references。
- [IRG N2930](irg-n2930.md) - accepted 3 G-source reference changes。
- [IRG N2929](irg-n2929.md) - G-source horizontal extensions for 9156 characters。
- [G-source Glyph and Source Reference Issues](../topics/g-source-glyph-and-reference-issues.md)
- [CJK Horizontal Extensions](../topics/cjk-horizontal-extensions.md)

## 出典

- `irg-n2923r` - <https://www.unicode.org/irg/docs/n2923r-GSourceChanges.pdf>
- `irg-n2923r` evidence ZIP - <https://www.unicode.org/irg/docs/n2923r-Evidence.zip>
