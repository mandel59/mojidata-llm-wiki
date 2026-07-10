---
type: Source Document
title: "Evidences of Urgently Needed Characters"
description: "China が G-source UNC characters の実用例、対応する繁体字・既符号化字、辞書出典を示し、analogously simplified ideographs の存在を補強した evidence 文書。"
resource: https://www.unicode.org/irg/docs/n1532r-GSourceEvidenceUNC.pdf
entry_id: irg-n1532r
doc_number: IRG N1532R
document_type: data
registry: irg
date: "2008-12-31"
source: China
documents: [irg-n1532, irg-n2837, irg-n2868, irg-n2923r]
topics: [g-source-glyph-and-reference-issues, irg-source-data-and-representative-glyphs]
people: [china, irg]
tags: [document, irg, g-source, unc, evidence, personal-names, place-names]
timestamp: 2026-07-10T00:00:00+09:00
---

# IRG N1532R

## 要約

`IRG N1532R` は、China が提出した G-source UNC characters の evidence 集である。IRG Meeting \#31 の要求を受けて `IRG N1532` を改訂し、analogously simplified ideographs が実在することを示す画像を追加した。

対象文字の多くについて、中国公安部のID systemで人名・姓・地名に使われていること、対応する繁体字または既符号化字を示す。加えて《中华字海》《现代汉语词典》《辞海》のページを掲げ、字形だけでなくsourceと意味・用途を追跡できる形にしている。本書自体はevidence dataであり、文字の採択を記録した決定文書ではない。

## データ内容

冒頭2ページはanalogously simplified ideographsの原画像と辞書参照の一覧で、残るページは各候補を`NUM`、`G_SOURCE`、`CHINA_NOTE`の列で整理する。noteは主に、公安部のID systemにおけるsurname、given name、place nameとしての使用と、簡化元となる繁体字・既符号化字を記録する。例外的に、新しいchemical elementの名称として使われる文字も含む。

`G_SOURCE`には`G_GFHZB00`から`G_GFHZB05`のような値のほか、`G_IDC225`、`G_IDC606`、`G_IDC623`などが現れる。辞書画像の一覧では《中华字海》のpage numberを中心に、《现代汉语词典》と《辞海》も併用する。このため文書は、行政上の実用例、analogous simplificationの対応関係、出版物のsource referenceという異なる種類のevidenceを一つの表に束ねている。

後にGXC-sourceとして扱われるExtension Dの4 charactersについては、《现代汉语词典》第5版のpageと同一page内のhead-character positionに基づくreference形式の由来となった。これは、旧来のserial value由来のGXC referencesとは意味が異なる。

## 後続決定

本書のstatusはmember submissionで、actions requiredはIRG editorsによるreviewである。したがって、ここに収録された文字がこの文書によって採択されたとは解釈しない。採択、符号位置、最終source mappingは、後続のIRG editorial recordsやrepertoire文書で確認する必要がある。

2025年の`IRG N2837`は、本書由来のExtension D GXC 4 charactersを、page / head-character position形式が成立している例として参照した。一方、Extensions C / EのGXC valuesは別のserial valuesを変形したものだったため、GXC全体のreference semanticsを揃える議論へ接続した。`IRG N2868`と`IRG N2923R`では、どの辞書edition / printingをoriginal submissionの根拠とみなすかが改めて検討されている。

## 論点

### evidenceの種類

公安部のID systemにおける実用、簡化元との対応、辞書掲載は、それぞれ別の主張を支える。実用例はurgent needを、対応字はanalogous simplificationを、辞書ページはsource referenceを裏づけるため、後続作業では一つの根拠として混同せずに読む必要がある。

### source referenceの持続性

page / position形式は掲載箇所を直接確認しやすい一方、辞書のeditionが変われば値も変わる。後続GXC議論では、現在参照しやすいeditionへ更新するか、original submission時のeditionを保存するかが争点となった。本書は、その議論に先行する具体的なpage evidenceとして位置づけられる。

## 関連文書

- `IRG N1532` - 本書の改訂前版。
- [IRG N2837](irg-n2837.md) - 本書由来のGXC reference形式と、Extensions C / Eの値との差を指摘した提案。
- [IRG N2868](irg-n2868.md) - GXCを含むsource referencesについてoriginal editionを再検討したfeedback。
- [IRG N2923R](irg-n2923r.md) - 辞書edition / printingを踏まえた後続のbulk G-source proposal。
- [G-source Glyph and Source Reference Issues](../topics/g-source-glyph-and-reference-issues.md)
- [IRG Source Data and Representative Glyphs](../topics/irg-source-data-and-representative-glyphs.md)

## 出典

- `irg-n1532r` - <https://www.unicode.org/irg/docs/n1532r-GSourceEvidenceUNC.pdf>
