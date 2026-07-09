---
type: Event
title: WG2 M73.01 Small Seal CD4 disposition
description: "WG2 #73 が ISO/IEC 10646 7th edition CD4 disposition の一部として Small Seal の名称変更と property correction を記録した出来事。"
slug: wg2-m73-01-small-seal-cd4-disposition
date: "2026-06-26"
bodies: [WG2, SC2]
documents: [wg2-n5344r2, wg2-n5354, wg2-n5355, wg2-n5369]
topics: [small-seal-script]
people: [wg2]
meetings: [wg2-meeting-73]
status: adopted
tags: [event, small-seal, recommendation, ballot]
timestamp: 2026-07-06T23:50:00+09:00
---

# WG2 M73.01 Small Seal CD4 disposition

## 概要

WG2 Meeting \#73 は Recommendation M73.01 で、ISO/IEC 10646 7th edition CD.4 の disposition of comments `WG2 N5369` を受け入れることを勧告した。その significant changes には、Small Seal character names を `SEAL CHARACTER-XXXXX` から `SMALL SEAL CHARACTER-XXXXX` に変更すること、6 characters の `kSEAL_Rad` correction、20 characters の `kSEAL_MCJK` correction、U+3F80E の glyph correction が含まれる。

## 背景

[WG2 N5344R2](../documents/wg2-n5344r2.md) では script property と character names に `Seal` を使う案だった。WG2 \#73 の recommendations は、CD.4 disposition を通じて character names を `Small Seal` に寄せ、ISO/IEC 10646 7th edition DIS へ進める変更として記録した。

`WG2 N5355` は、`WG2 N5348R` で不明確とされた `zhèngzì`（正字）/ normalized form の意味を補足し、Small Seal の modern CJK 対応値は `zhèngzhuàn`（正篆）と `chóngwén`（重文）の関係で理解すべきだと整理した。`WG2 N5369` の `kSEAL_MCJK` correction は、この modern CJK correspondence principle を CD.4 disposition に反映したものとして読める。

## 結果

M73.01 は CD4 disposition の受け入れを勧告し、M73.04 はその変更を含む DIS text を SC2 secretariat に回すことを勧告した。target は DIS 2026-10-01、IS 2027-06-01 とされている。

### Name correction

| Range | Old | New |
| --- | --- | --- |
| `3D000..3FC3F` | `SEAL CHARACTER-XXXXX` | `SMALL SEAL CHARACTER-XXXXX` |

### kSEAL_Rad correction

| Code | Old `kSEAL_Rad` | New `kSEAL_Rad` |
| --- | --- | --- |
| U+3DDF7 | `157.3DDF1` | `158.3DDF7` |
| U+3DDF8 | `158.3DDF8` | `158.3DDF7` |
| U+3DDF9 | `158.3DDF8` | `158.3DDF7` |
| U+3DE44 | `168.3DE31` | `169.3DE44` |
| U+3DE45 | `169.3DE45` | `169.3DE44` |
| U+3DE46 | `169.3DE45` | `169.3DE44` |

### kSEAL_MCJK correction

| Code | Old `kSEAL_MCJK` | New `kSEAL_MCJK` |
| --- | --- | --- |
| U+3E894 | U+824E 艎 | U+26A84 𦪄 |
| U+3E9FB | U+9B1F 鬟 | U+29BF4 𩯴 |
| U+3EA95 | U+5D99 嶙 | U+21F64 𡽤 |
| U+3EB4D | U+787E 硾 | U+2558C 𥖌 |
| U+3EC24 | U+298B2 𩢲 | U+298EC 𩣬 |
| U+3EC25 | U+298CA 𩣊 | U+2992D 𩤭 |
| U+3EC28 | U+9A02 騂 | U+2994D 𩥍 |
| U+3EE45 | U+FA3E 慨 | U+6168 慨 |
| U+3EF54 | U+61C7 懇 | U+22846 𢡆 |
| U+3F153 | U+703C 瀼 | U+2416D 𤅭 |
| U+3F160 | U+6F35 漵 | U+6F4A 潊 |
| U+3F161 | U+6E2F 港 | U+23FD1 𣿑 |
| U+3F163 | U+6FD4 濔 | U+24164 𤅤 |
| U+3F167 | U+6E98 溘 | U+23E46 𣹆 |
| U+3F2DB | U+95E4 闤 | U+28DE4 𨷤 |
| U+3F80A | U+867B 虻 | U+8771 蝱 |
| U+3F8FD | U+587E 塾 | U+2150A 𡔊 |
| U+3FA4E | U+6235 戵 | U+947A 鑺 |
| U+3FAFB | U+8F54 轔 | U+283CF 𨏏 |
| U+3FB84 | U+25747 𥝇 | U+25745 𥝅 |

### Glyph correction

| Code | 内容 |
| --- | --- |
| U+3F80E | unified TH-Y version が original DYC source に合うよう glyph correction。 |

## 影響範囲

この event は、Small Seal の名称・property が ballot disposition の中で整理され、DIS へ進む流れに載った時点として扱う。repertoire / range の proposal 自体は [WG2 N5344R2](../documents/wg2-n5344r2.md) などの document pages と Small Seal topic で追跡する。

## 関連ページ

- [Small Seal Script](../topics/small-seal-script.md)
- [WG2 Meeting \#73](../meetings/wg2/wg2-meeting-73.md)
- [WG2](../people/wg2.md)

## 出典

- `wg2-n5354` - <https://www.unicode.org/wg2/docs/n5354-Mtg73-Paris-Recs-rev5.pdf>
- `wg2-n5344r2` - <https://www.unicode.org/wg2/docs/n5344R2-SmallSealProposal.pdf>
- `wg2-n5355` - <https://www.unicode.org/wg2/docs/n5355-SealNormalizedForm.pdf>
- `wg2-n5369` - <https://www.unicode.org/wg2/docs/n5369-CD7th-4-DOC.pdf>
