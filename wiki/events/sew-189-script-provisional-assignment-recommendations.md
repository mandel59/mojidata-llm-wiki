---
type: Event
title: "SEW #189 script provisional assignment recommendations"
description: "SEW が Maya、N’ti、Ndiko Jonam、KORE SEBELI の provisional assignment を UTC #189 に勧告した段階。"
slug: sew-189-script-provisional-assignment-recommendations
date: 2026-10-23
bodies: [UTC]
documents: [utc-l2-26-239, utc-l2-26-145, utc-l2-26-145r3, utc-l2-26-087, utc-l2-26-055r, utc-l2-26-132, utc-l2-26-132r]
topics: [script-encoding-pipeline, maya-hieroglyph-encoding, nti-script, kore-sebeli-script]
meetings: [utc-meeting-189]
status: recommended
tags: [event, script, recommendation, sew]
timestamp: "2026-10-25T00:00:00+09:00"
---

# SEW \#189 script provisional assignment recommendations

## 概要

SEW は2026-10-23付の L2/26-239 で、Maya、N’ti、Ndiko Jonam、KORE SEBELI の provisional assignment を UTC \#189 に勧告した。これは SEW review の節目であり、2026-10-26〜28に予定される UTC 会合の採択結果ではない。

| Script | 勧告した文字数・範囲 | 根拠 |
| --- | --- | --- |
| Maya | 513文字。Mayan Hieroglyphs に481、Mayan Hieroglyph Format Controls に32。 | L2/26-145R3、§1.1 / SEW-189-C1 |
| N’ti | 47文字、U+1CB80..U+1CBA4 / U+1CBA6..U+1CBAF。 | L2/26-087、§1.2 / SEW-189-C2 |
| Ndiko Jonam | 69文字、U+1CB30..U+1CB49 / U+1CB51..U+1CB71 / U+1CB76..U+1CB7F。 | L2/26-055R、§1.3 / SEW-189-C3 |
| KORE SEBELI | 93文字、U+15B00..U+15B52 / U+15B56..U+15B5F。 | L2/26-132R、§1.4 / SEW-189-C4 |

## 背景

Maya は Version 1.6 の repertoire と format-control model が review を経た。N’ti / Ndiko Jonam / KORE SEBELI は UTC \#188 から SEW へ差し戻された legal clearance 等を再確認したもので、SEW は把握する限り Unicode の legal requirements を満たすと報告する。

## 結果

SEW は pipeline 更新と compliant fonts の提出支援を勧告した。KORE SEBELI の U+15B1B は KORE SEBELI CAPITAL LETTER OU WITH THREE DOTS ABOVE とする修正も含む。Maya Extended-A は別 proposal として in process に残る。

2026-10-25 時点で status は recommended。SEW-189-C1〜C4 を UTC の numbered consensus と読み替えず、Unicode の version への正式な収録決定とも区別する。

## 影響範囲

各 script の最新版 proposal と、UTC に求められた処置を結びつける入口になる。

<!-- editorial: 後続確認は [UTC Meeting \#189](../meetings/utc/utc-meeting-189.md) の minutes で行う。 -->

## 関連ページ

- [L2/26-239](../documents/utc-l2-26-239.md)
- [Codical Maya](../documents/utc-l2-26-145.md)
- [KORE SEBELI](../documents/utc-l2-26-132.md)
- [N’ti Script](../topics/nti-script.md)
- [Script Encoding Pipeline](../topics/script-encoding-pipeline.md)

## 出典

- `utc-l2-26-239` - <https://www.unicode.org/L2/L2026/26239-sew-report-utc189.pdf>（registry date: 2026-10-24）
- `utc-l2-26-145r3` - <https://www.unicode.org/L2/L2026/26145r3-codical-maya.pdf>（registry date: 2026-10-19）
- `utc-l2-26-132r` - <https://www.unicode.org/L2/L2026/26132r-kore-sebeli-proposal.pdf>（registry date: 2026-10-23）
- `utc-l2-26-087` - <https://www.unicode.org/L2/L2026/26087-nti-proposal.pdf>（registry date: 2026-04-13）
- `utc-l2-26-055r` - <https://www.unicode.org/L2/L2026/26055r-ndiko-jonam-proposal.pdf>（registry date: 2026-07-21）
