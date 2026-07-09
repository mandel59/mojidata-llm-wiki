---
type: Source Document
title: Preliminary proposal to encode 131 CJK components for GF 3001-1997 and GF 0014-2009
description: China による CJK components preliminary proposal の要約。
resource: https://www.unicode.org/irg/docs/n2733r-CJKComponents4IDS.pdf
entry_id: irg-n2733r
doc_number: IRG N2733R
document_type: proposal
registry: irg
date: "2024-10-13"
source: China
documents: [irg-n1081, irg-n1133, irg-n2702, irg-n2799]
topics: [cjkv-components]
tags: [document, proposal, components, cjk]
timestamp: 2026-07-06T21:58:00+09:00
---

# IRG N2733R

## 要約

`IRG N2733R` は、China による CJK components encoding の preliminary proposal である。GF 3001-1997 と GF 0014-2009 の two Chinese specifications を支えるため、131 CJK components の追加を提案した。

文書は、WS2017 期に実際の字形レベル IDS を簡潔に記述するため components encoding の必要性が出たこと、U+31EF `IDEOGRAPHIC DESCRIPTION CHARACTER SUBTRACTION` の導入後も仕様互換のため component encoding が必要であることを背景に置く。Tangut components が IDS description と character structure analysis のために符号化されていることも比較対象として挙げる。2004-2005 年の [IRG N1081](irg-n1081.md) / [IRG N1133](irg-n1133.md) は、component encoding / decomposition rules の前史として topic 側で扱う。

## 論点

### IDS と specification compatibility

主目的は、GF 3001-1997 と GF 0014-2009 にある component inventory を UCS で扱えるようにし、IDS 記述や構造分析の互換性を確保することにある。ここではまだ China source 中心で、HKSAR / TCA / Vietnam などを含む CJKV 全体の整理にはなっていない。

### 後続文書への接続

IRG \#63 Recommendation M63.17 は、この proposal を受けて CJK components block の符号化は useful かつ long overdue とし、TCA と HKSAR に追加 components data の検討・提供を促した。[IRG N2799](irg-n2799.md) はこの方針を受け、multi-source の CJKV components proposal へ拡張している。

## 出典

- `irg-n2733r` - <https://www.unicode.org/irg/docs/n2733r-CJKComponents4IDS.pdf>
- `irg-n1081` - <https://www.unicode.org/irg/docs/n1081-CJKComponents.pdf>
- `irg-n1133` - <https://www.unicode.org/irg/docs/n1133-CJKComponents.pdf>
- `irg-n2702` - <https://www.unicode.org/irg/docs/n2702-Recommendations.pdf>
- topic: [CJKV Components](../topics/cjkv-components.md)
