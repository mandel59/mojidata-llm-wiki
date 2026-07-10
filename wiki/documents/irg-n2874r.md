---
type: Source Document
title: "Feedback on IRG N2840"
description: "China が IRG N2840 の4組を再検討し、既存文字の安定性とsource evidenceを踏まえてG-source glyph、reference、radicalの修正案を示したfeedback。"
resource: https://www.unicode.org/irg/docs/n2874r-IRGN2840Feedback.pdf
entry_id: irg-n2874r
doc_number: IRG N2874R
document_type: feedback
registry: irg
date: "2026-03-23"
source: China
documents: [irg-n2840, irg-n2864r]
topics: [g-source-glyph-and-reference-issues, irg-source-data-and-representative-glyphs]
people: [china, irg]
tags: [document, irg, g-source, feedback, representative-glyph, source-reference, duplicate-encoding]
timestamp: 2026-07-10T00:00:00+09:00
---

# IRG N2874R

## 要約

`IRG N2874R` は、[IRG N2840](irg-n2840.md) が指摘した4組のduplicate glyphについて、Chinaがoriginal sourcesと既存利用の安定性を照合したfeedbackである。同じglyphを二つのcode pointsで使う状態は可能な限り直す一方、URO、とくにGBKで長く使われてきた文字は、source evidenceに合う既存glyphを慎重に維持するという方針を示す。

その方針に従い、U+34A8とU+821Dは変更せず、対になるExtension B charactersを修正する。残る2組では新しいevidenceに沿うglyph・referenceの割当てを受け入れ、U+204F2についてはradical valueの変更も求める。

本文はIRG \#65でのconsiderationを求めるmember feedbackであり、IRGまたはWG2の採択結果を記録したdecision documentではない。

## フィードバック内容

### 判断原則

文書は、duplicate-encoded ideographsや誤ったextended glyphsによるglyph duplicationがNLPを難しくするという `IRG N2840` の問題提起を支持する。そのうえで、G-source glyph revisionには二つの条件を置く。

- UROのglyphは慎重に扱い、original evidenceと一致するglyphを既存code pointに保持する。
- 二つのcode pointsが同じglyphを使う状態は、source evidenceに基づいて可能な限り解消する。

つまりduplicate glyphの解消だけを優先して既存文字を動かすのではなく、evidenceと実装上の安定性を合わせて、組のどちらを変更するかを決める。

### 4組へのresponse

| 対象 | Chinaのresponse | glyphとreferenceの扱い |
| --- | --- | --- |
| U+34A8 / U+20457 | U+34A8はGBKで30年間広く使われ、`G5-3329` のoriginal glyphとも一致するため変更しない。 | U+20457側のglyphを区別し、referenceを `GKX-0121.39` から `GHZR-10281.02` へ変更する。 |
| U+821D / U+246C9 | U+821Dはoriginal evidenceに合い、G5はauthoritative sourceであるためglyph・referenceを変更しない。 | U+246C9を対になるvariant glyphで表し、referenceを `GCESI-00535` とする。このreference変更は `IRG N2864R` に含まれる。 |
| U+204F2 / U+23515 | `IRG N2840` の提案を受け入れ、連続する新しいevidenceに従って両文字を区別する。 | U+204F2を `GHZR-10237.05`、U+23515を `GHZR-10237.06` に対応させる。さらにU+204F2のradical valueを入 `11.10` から木 `75.8` へ変えるよう求める。 |
| U+249BC / U+249E9 | U+249BCのglyph revisionと `GHZR-21200.09` へのreference変更を受け入れ、もう一方を別variantとして保持する。 | U+249E9のreference変更は `IRG N2864R` で扱われ、本feedbackは両code pointsを区別するglyph assignmentを示す。 |

PDFの表にはglyph画像が含まれるため、具体的な字形は一次資料で確認する必要がある。本ページでは画像を文字名やreferenceだけから推定せず、どのcode pointを維持し、どちらを修正するかというresponseの境界を記録する。

### glyph、reference、radicalの分離

本書ではrepresentative glyphの変更、`kIRG_GSource` referenceの変更、radical propertyの変更を別の操作として扱う。とくにU+246C9とU+249E9では、reference updateをbulk proposalである [IRG N2864R](irg-n2864r.md) に置き、glyphの組合せを本feedbackで説明する。U+204F2についても、glyph・referenceへのresponseに加えてradical変更を明示するため、一つの修正が他のdata変更を自動的に決定するわけではない。

## 後続決定

`IRG N2874R` のheaderは `Actions required: To be considered by IRG` としており、この文書自体は採択記録ではない。4組へのChinaのresponseと、IRG / WG2が最終的に承認した変更は区別する必要がある。

後続のrecommendation、meeting record、Unicode data updateは、それぞれの一次資料で確認すべきである。また [IRG N2864R](irg-n2864r.md) も1,538 charactersのreference updatesを求めるmember submissionであり、そこへreference変更が収録されたことだけでは採択を証明しない。

## 論点

### duplicate glyphと安定性

U+34A8の扱いは、duplicate glyphを解消する場合でも、GBKでの長期利用とoriginal evidenceに一致する既存glyphを優先する例である。問題のある組を見つけた後に、どちらのcode pointを変更するかをsource historyと実装状況から選ぶ必要がある。

### 個別feedbackとbulk reference update

[IRG N2840](irg-n2840.md) は4組のglyph問題を提起し、本書はそれに対するChinaの個別responseを与える。一方、[IRG N2864R](irg-n2864r.md) は多数のG-source referencesをまとめたproposalである。U+246C9やU+249E9が両方に現れても、個別glyph analysis、bulk reference update、会合でのdecisionを同じ段階として扱わない。

## 関連文書

- [IRG N2840](irg-n2840.md) - 本feedbackの対象となった4組のglyph revision proposal。
- [IRG N2864R](irg-n2864r.md) - U+246C9とU+249E9のreference updatesを含むbulk proposal。
- [G-source Glyph and Source Reference Issues](../topics/g-source-glyph-and-reference-issues.md)
- [IRG Source Data and Representative Glyphs](../topics/irg-source-data-and-representative-glyphs.md)

## 出典

- `irg-n2874r` - <https://www.unicode.org/irg/docs/n2874r-IRGN2840Feedback.pdf>
- `irg-n2840` - <https://www.unicode.org/irg/docs/n2840-GSourceGlyphIssues.pdf>
- `irg-n2864r` - <https://www.unicode.org/irg/docs/n2864r-GSourceChanges.pdf>
