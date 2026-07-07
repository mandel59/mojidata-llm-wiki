---
type: Topic
title: Kana
description: "仮名の追加符号化、歴史的仮名、変体仮名、小書き仮名、合略仮名を追跡する topic。"
slug: kana
bodies: [UTC, WG2]
documents: [utc-l2-07-421, utc-l2-08-117, utc-l2-08-358, utc-l2-09-062, utc-l2-15-239, utc-l2-15-343, utc-l2-16-188, utc-l2-16-334, utc-l2-16-354, utc-l2-16-358r, utc-l2-17-014, utc-l2-17-091, utc-l2-19-381, utc-l2-19-382, utc-l2-20-152, utc-l2-20-233, utc-l2-20-280, utc-l2-20-209r, utc-l2-23-112, utc-l2-23-118, utc-l2-23-123, utc-l2-23-127, utc-l2-24-150, utc-l2-24-279, utc-l2-25-035, utc-l2-25-036, utc-l2-25-042, utc-l2-25-060, utc-l2-25-151r]
status: active
tags: [kana, hiragana, katakana, hentaigana]
timestamp: 2026-07-08T00:00:00+09:00
---

# Kana

## 概要

Kana は、Hiragana / Katakana / Hentaigana / Small Kana Extension / Kana Extended-A などに関わる仮名の標準化議論を束ねる topic である。近年の論点は、歴史的資料を写すための合略仮名（合字的な kana ligatures）、小書き仮名、明治期の alternate Katakana などに分かれる。

この topic では、仮名文字・仮名由来文字・仮名を使う表記体系に関わる Unicode / ISO/IEC 10646 上の論点を扱う。日本語史資料に限らず、Ryukyuan languages の superscript Katakana や Taiwanese Kana なども kana usage として関連するが、個別の大きな proposal は別 topic に分ける余地がある。

## 経緯

| 日付 | Body | 文書 | できごと |
| --- | --- | --- | --- |
| 1999-07-15 | UTC | [L2/99-238](https://www.unicode.org/L2/L1999/99238-non-kanji2.pdf) | JCS Committee が JIS X 0213 系の非漢字追加として、linguistic signs、dentist signs、enclosed numbers、publishing signs、Katakana などを UTC に提出。 |
| 1999-09-13 | WG2 | [WG2 N2092](https://www.unicode.org/wg2/docs/n2092.pdf) | Japan NB が kana / punctuation を含む 48 characters の追加を WG2 に提出。 |
| 2008-01-14 | UTC / WG2 | [L2/07-421](../documents/utc-l2-07-421.md) / [WG2 N3388](https://www.unicode.org/wg2/docs/n3388.pdf) | Nozomu Kato が YE に関する 2 kana characters の符号化を提案。 |
| 2008-02-28 | UTC / WG2 | [L2/08-117](../documents/utc-l2-08-117.md) / [WG2 N3394](https://www.unicode.org/wg2/docs/n3394.pdf) | UTC / L2 が Japan NB に review を求め、個別符号化か obsolete kana / hentaigana の大きな枠組みで扱うかを論点化。 |
| 2008-10-14 | UTC / WG2 | [L2/08-358](../documents/utc-l2-08-358.md) / [WG2 N3528](https://www.unicode.org/wg2/docs/n3528.pdf) | Japan NB が HIRAGANA LETTER YE は支持し、KATAKANA LETTER ORIGINAL E は時点では反対と回答。YE と hentaigana を混同しないことを求めた。 |
| 2009-01-28 | UTC | [L2/09-062](../documents/utc-l2-09-062.md) | Nozomu Kato が、あ行 E とヤ行 YE の歴史的区別、カタカナ エと江の関係を日本語史背景として整理。 |
| 2015-10-09 | UTC / WG2 | [L2/15-239](../documents/utc-l2-15-239.md) / [WG2 N4674](https://www.unicode.org/wg2/docs/n4674-Japan_Hentaigana_Proposal-a.zip) | Japan NB が 299 文字の Japanese HENTAIGANA 初期 proposal を提出。 |
| 2015-12-15 | UTC | [L2/15-343](../documents/utc-l2-15-343.md) | Japan NB が Hentaigana revised proposal を提出。phonetic value と mother ideograph に基づく命名・統合の整理を示す。 |
| 2016-07-15 | UTC | [L2/16-188](../documents/utc-l2-16-188.md) | Japan NB が Hentaigana revised repertoire を提出。`HENTAIGANA LETTER E-1` withdrawal と U+1B001 name alias の流れに接続する。 |
| 2016-11-04 | UTC | [L2/16-334](../documents/utc-l2-16-334.md) | CheonHyeong Sim が small WI / WE の Hiragana / Katakana 4 文字を提案。 |
| 2016-11-06 | UTC | [L2/16-354](../documents/utc-l2-16-354.md) | Ryusei Yamaguchi が phonetic extension system として 12 文字の Kana small letters を提案。 |
| 2016-11-07 | UTC / WG2 | [L2/16-358R](../documents/utc-l2-16-358r.md) / [WG2 N4803](https://www.unicode.org/wg2/docs/n4803-small-kana-fdbk.pdf) | Ken Lunde が 2 件の small kana proposal への feedback を出し、UTC \#149 で受理された 7 文字を示す。 |
| 2017-01-17 | UTC | [L2/17-014](../documents/utc-l2-17-014.md) | Japan NB / Tetsuji Orita が ARCHAIC HIRAGANA YE は HENTAIGANA「江」の用法の一つだと整理。 |
| 2017-04-07 | UTC / WG2 | [L2/17-091](../documents/utc-l2-17-091.md) / [WG2 N4826](https://www.unicode.org/wg2/docs/n4826-JNB-SmallKanaCharacters.pdf) | Japan NB が Small Kana Characters に関する contribution を提出。PDAM 1.2 の 9 small kana だけを選ぶ根拠が不明で、より広い repertoire または modifier model を検討すべきと主張。 |
| 2019-11-21 | UTC | [L2/19-381](../documents/utc-l2-19-381.md) | Abraham Gross が Missing Japanese Kana として YI / WU / YE 系 kana と KATAKANA LETTER SMALL WU を提案。 |
| 2019-11-22 | UTC | [L2/19-382](../documents/utc-l2-19-382.md) | Alexander Zapryagaev が Late Middle Japanese の final -t を転写する HENTAIGANA LETTER SMALL TU-2 を提案。 |
| 2020-06-25 | UTC | [L2/20-152](../documents/utc-l2-20-152.md) | Abraham Gross が HIRAGANA LETTER ARCHAIC WU の origin character を U+6C59 汙とする annotation を推奨。 |
| 2020-09-18 | UTC | [L2/20-233](../documents/utc-l2-20-233.md) | Eiso Chan が Taiwanese Kana proposal に feedback を出し、Min Nan naming、U+0323 / U+0305 の扱い、縦書きと shakuhachi notation の衝突を指摘。 |
| 2020-11-10 | UTC | [L2/20-280](../documents/utc-l2-20-280.md) | Fredrick R. Brennan が Taiwanese Kana の tone marks を Kana Extended-B として符号化する proposal を提出。 |
| 2021-01-04 | UTC | [L2/20-209R](../documents/utc-l2-20-209r.md) | Fredrick R. Brennan が revised final proposal を提出し、Minnan tone / nasalized tone marks 13 文字と U+0323 / U+0305 の利用を整理。 |
| 2023-04-25 | UTC | [L2/23-112](../documents/utc-l2-23-112.md) | Gen Kojitani が missing kana ligatures を広く提案。合略仮名を複数 kana の単なる連綿と区別する criteria を提示。 |
| 2023-05-08 | UTC | [L2/23-118](../documents/utc-l2-23-118.md) | Gen Kojitani が Ryukyuan languages 用 superscript katakana letters 8 characters を提案。 |
| 2023-05-25 | UTC | [L2/23-123](../documents/utc-l2-23-123.md) | Eiso Chan が `L2/23-118` へ feedback を出し、usage stability、vertical layout、提出主体などの確認を求めた。 |
| 2023-05-31 | UTC | [L2/23-127](../documents/utc-l2-23-127.md) | Eiso Chan が明治期資料に現れる alternate Katakana NE / WI を紹介。 |
| 2024-06-21 | UTC | [L2/24-150](../documents/utc-l2-24-150.md) | Gen Kojitani が `L2/23-112` を reduced set として改訂し、3 kana ligatures を提案。 |
| 2024-12-31 | UTC | [L2/24-279](../documents/utc-l2-24-279.md) | CheonHyeong Sim が KATAKANA DIGRAPH YORI を追加提案。 |
| 2025-01-13 | UTC | [L2/25-035](../documents/utc-l2-25-035.md) | CheonHyeong Sim が small kana と Bopomofo small letters の Vertical Orientation value 変更を要請。 |
| 2025-01-15 | UTC | [L2/25-036](../documents/utc-l2-25-036.md) | CheonHyeong Sim が KATAKANA LETTER SMALL ARCHAIC YE を提案。昭和期の Micronesian / Marshallese transliteration 資料を根拠とする。 |
| 2025-01-16 / 2025-02-24 | UTC | [L2/25-042](../documents/utc-l2-25-042.md), [L2/25-060](../documents/utc-l2-25-060.md) | Kentaro Bimbatti が KATAKANA LETTER SMALL NE を提案し、広告・看板・表紙資料の attestations を追加。 |
| 2025-05-23 | UTC | [L2/25-151R](../documents/utc-l2-25-151r.md) | Eiso Chan が KATAKANA LETTER ALTERNATE NE / WI を提案。明治期活字・教科書資料を根拠とし、current Katakana / Hentaigana との統合不可を主張。 |

## 主な論点

### YE と hentaigana の境界

[L2/07-421](../documents/utc-l2-07-421.md) / `WG2 N3388` は、historical Japanese の /e/ と /ye/ の区別を扱うために HIRAGANA LETTER YE と KATAKANA LETTER ORIGINAL E を提案した。UTC / L2 は [L2/08-117](../documents/utc-l2-08-117.md) で Japan NB review を求め、Japan NB は [L2/08-358](../documents/utc-l2-08-358.md) で HIRAGANA LETTER YE には賛成したが、KATAKANA LETTER ORIGINAL E にはさらなる調査が必要だとして反対した。[L2/09-062](../documents/utc-l2-09-062.md) は、その背景として、あ行 E とヤ行 YE の歴史的区別、カタカナ エと江の関係を日本語資料で説明する。

重要なのは、Japan NB が YE の追加を hentaigana 一般の符号化とは別問題として扱うよう求めた点である。江（U+6C5F）由来の字形は hentaigana とも重なるため、歴史的音価 /ye/ を表す文字なのか、既存 hiragana え の異体字なのかを区別する必要があった。

[L2/17-014](../documents/utc-l2-17-014.md) は、この境界を逆方向から整理する。Japan NB / Tetsuji Orita は、/e/ と /je/ の歴史的区別は万葉仮名・片仮名で確認できるが、10 世紀半ば以前の平仮名資料は少ないため、ARCHAIC HIRAGANA YE は HENTAIGANA「江」の用法の一つとして扱うのが適切だと述べた。

### 変体仮名の repertoire と統合基準

Japan NB の [L2/15-239](../documents/utc-l2-15-239.md) / `WG2 N4674` は、Japanese HENTAIGANA 299 文字を初期 proposal として提出した。後続の [L2/15-343](../documents/utc-l2-15-343.md) と [L2/16-188](../documents/utc-l2-16-188.md) は、この repertoire を phonetic value と mother ideograph で整理する。たとえば 江、衣、盈、縁、要などを母字とする E 系 hentaigana は同じ現代仮名「え」に対応し得るが、字形・母字・文献用途は異なる。

この系譜は、単に未符号化 kana を増やす話ではなく、歴史資料を plain text でどこまで再現するか、glyph variation と encoded character の境界をどう決めるかという問題である。

### 小書き仮名の model

[L2/16-334](../documents/utc-l2-16-334.md) と [L2/16-354](../documents/utc-l2-16-354.md) は、small WI / WE / WO / N などを含む additional small kana の個別 proposal である。[L2/16-358R](../documents/utc-l2-16-358r.md) は両 proposal の関係と証拠を確認し、UTC \#149 で HIRAGANA LETTER SMALL WI / WE / WO、KATAKANA LETTER SMALL WI / WE / WO / N の 7 文字が受理されたことを示す。

[L2/17-091](../documents/utc-l2-17-091.md) は Small Kana Characters に対する Japan NB の慎重な立場を示す。Japan NB は、近代日本語資料の調査で PDAM に含まれない多数の small kana usage が見つかること、9 文字だけを選ぶ根拠が不明であること、全 kana に対応する小書き字を符号化するのか modifier 的な方式を考えるのかを検討すべきことを述べた。

2019 年の [L2/19-381](../documents/utc-l2-19-381.md) と [L2/19-382](../documents/utc-l2-19-382.md) は、YI / WU / YE 系の missing kana や HENTAIGANA LETTER SMALL TU-2 を提案し、historical phonology / transcription 用の small kana という別の根拠系を示した。[L2/20-152](../documents/utc-l2-20-152.md) は、`L2/19-381` の HIRAGANA LETTER ARCHAIC WU について、encoding 後に origin character annotation を補う扱いを示す。2025 年の `L2/25-036` と `L2/25-042` / `L2/25-060` はこの問題の続きにある。前者は KATAKANA LETTER SMALL ARCHAIC YE、後者は現代的・表示的な small NE の usage を根拠にするため、同じ Small Kana Extension でも「歴史的 transcription」と「現代の書体・広告表現」の証拠評価が異なる。

### 合略仮名と vertical-only implication

[L2/23-112](../documents/utc-l2-23-112.md) と `L2/24-150` は、合略仮名を複数 kana の sequence ではなく、単一文字として扱う条件を整理する。`L2/24-150` は、手書き縦書き資料の連綿と、活字資料で単一文字として印刷された合略仮名を区別し、reduced set として 3 文字を提案した。

`L2/24-279` は、その流れから漏れた KATAKANA DIGRAPH YORI を再提案する文書である。CJK & Unihan WG が hiragana ligatures には vertical-only implication への懸念を持ちつつ、katakana ligatures にはより前向きだった、という整理を根拠にしている。

### alternate Katakana NE / WI

[L2/23-127](../documents/utc-l2-23-127.md) と `L2/25-151R` は、明治期活字・教科書資料に現れる current Katakana とは別字形の NE / WI を扱う。提案は KATAKANA LETTER ALTERNATE NE と KATAKANA LETTER ALTERNATE WI を Kana Extended-A に置くことを求め、子（U+5B50）由来の NE、井（U+4E95）由来の WI と説明する。

この提案は Hentaigana とも関係するが、Katakana repertoire の歴史的字種として扱う点が特徴である。`L2/25-151R` は、これらを current Katakana NE / WI や Hentaigana と統合できないと主張し、同時に 子 / 井 との confusable pair として扱う必要にも触れている。

### Ryukyuan superscript Katakana

[L2/23-118](../documents/utc-l2-23-118.md) は、Ryukyuan languages / Shimakutuba orthography 用の KATAKANA LETTER SUPERSCRIPT A / I / U / E / O / TU / HU / N を Small Kana Extension に置くことを提案した。これは「仮名を使う日本語以外の Japonic languages の表記」を扱う点で kana topic に入るが、既存 small kana とは baseline placement と typography が異なる。

[L2/23-123](../documents/utc-l2-23-123.md) は、この proposal に対して usage stability、running text、vertical layout、UAX \#50、地方政府公式 orthography と Japan NB / Okinawa Prefecture の提出主体などを確認すべきだと指摘した。この論点は、kana repertoire そのものだけでなく、地域言語表記政策を Unicode proposal としてどう担保するかに関わる。

### Taiwanese Kana / Minnan tone marks

[L2/20-280](../documents/utc-l2-20-280.md) と [L2/20-209R](../documents/utc-l2-20-209r.md) は、Taiwanese Hokkien / Min Nan を kana と tone marks で注記する Taiwanese Kana の proposal である。最終案は Kana Extended-B U+1AFF0..U+1AFFF に、Minnan tone marks と nasalized tone marks 13 文字を置く。現行 Unicode code chart でも、Kana Extended-B は Minnan Chinese を annotate する furigana extensions の tone marks として説明される。

この論点は、日本語の仮名追加ではなく、kana-derived annotation system の符号化である。Japanese colonial-period dictionaries、Mojikyo の legacy support、modern dictionary / Wikipedia usage が evidence として使われる一方、character names では `Taiwanese` / `Hokkien` ではなく `Minnan` が採用される。

[L2/20-233](../documents/utc-l2-20-233.md) は、この proposal に対する feedback として、language name、U+0323 COMBINING DOT BELOW、U+0305 COMBINING OVERLINE、vertical layout、shakuhachi notation との衝突を指摘した。したがって Taiwanese Kana は、repertoire だけでなく UAX \#50 / font layout / combining mark behavior も併せて追う必要がある。

## 関連文書

- [L2/07-421](../documents/utc-l2-07-421.md) - HIRAGANA LETTER YE / KATAKANA LETTER ORIGINAL E。
- [L2/08-117](../documents/utc-l2-08-117.md) / [L2/08-358](../documents/utc-l2-08-358.md) / [L2/09-062](../documents/utc-l2-09-062.md) / [L2/17-014](../documents/utc-l2-17-014.md) - YE proposal、Japan NB feedback、E / YE 背景、HENTAIGANA「江」と ARCHAIC HIRAGANA YE の整理。
- [L2/15-239](../documents/utc-l2-15-239.md) / [L2/15-343](../documents/utc-l2-15-343.md) / [L2/16-188](../documents/utc-l2-16-188.md) - Hentaigana proposal と revised repertoire。
- [L2/16-334](../documents/utc-l2-16-334.md) / [L2/16-354](../documents/utc-l2-16-354.md) / [L2/16-358R](../documents/utc-l2-16-358r.md) / [L2/17-091](../documents/utc-l2-17-091.md) - Small Kana Characters の proposal、feedback、Japan NB contribution。
- [L2/19-381](../documents/utc-l2-19-381.md) / [L2/19-382](../documents/utc-l2-19-382.md) / [L2/20-152](../documents/utc-l2-20-152.md) - missing kana、Late Middle Japanese transcription 用 kana、ARCHAIC WU の origin character annotation。
- [L2/20-233](../documents/utc-l2-20-233.md) / [L2/20-280](../documents/utc-l2-20-280.md) / [L2/20-209R](../documents/utc-l2-20-209r.md) - Taiwanese Kana / Minnan tone marks proposal と feedback。
- [L2/23-112](../documents/utc-l2-23-112.md) - missing Kana-Ligatures の広い proposal。
- [L2/23-118](../documents/utc-l2-23-118.md) / [L2/23-123](../documents/utc-l2-23-123.md) - Ryukyuan superscript Katakana proposal と feedback。
- [L2/23-127](../documents/utc-l2-23-127.md) - alternate Katakana NE / WI の introduction。
- [L2/24-150](../documents/utc-l2-24-150.md) - missing three Kana-Ligatures。
- [L2/24-279](../documents/utc-l2-24-279.md) - KATAKANA DIGRAPH YORI。
- [L2/25-035](../documents/utc-l2-25-035.md) - small kana / Bopomofo small letters の Vertical Orientation。
- [L2/25-036](../documents/utc-l2-25-036.md) - KATAKANA LETTER SMALL ARCHAIC YE。
- [L2/25-042](../documents/utc-l2-25-042.md) / [L2/25-060](../documents/utc-l2-25-060.md) - KATAKANA LETTER SMALL NE。
- [L2/25-151R](../documents/utc-l2-25-151r.md) - KATAKANA LETTER ALTERNATE NE / WI。

## 関連トピック

- [CJK Hybrid Characters](cjk-hybrid-characters.md)
- [CJK Security Confusables](cjk-security-confusables.md)

## 出典

- `utc-l2-07-421` - <https://www.unicode.org/L2/L2007/07421-e-ye.pdf>
- `utc-l2-08-117` - <https://www.unicode.org/L2/L2008/08117-kana-letter.pdf>
- `utc-l2-08-358` - <https://www.unicode.org/L2/L2008/08358-n3528.pdf>
- `utc-l2-09-062` - <https://www.unicode.org/L2/L2009/09062-e-ye-info.pdf>
- `utc-l2-15-239` - <https://www.unicode.org/L2/L2015/15239-hentaigana.pdf>
- `utc-l2-15-343` - <https://www.unicode.org/L2/L2015/15343-hentaigana-revised.pdf>
- `utc-l2-16-188` - <https://www.unicode.org/L2/L2016/16188-rev-hentaigana-rep.pdf>
- `utc-l2-16-334` - <https://www.unicode.org/L2/L2016/16334-kana-small.pdf>
- `utc-l2-16-354` - <https://www.unicode.org/L2/L2016/16354-kana-small-ltr.pdf>
- `utc-l2-16-358r` - <https://www.unicode.org/L2/L2016/16358r-small-kana-fdbk.pdf>
- `utc-l2-17-014` - <https://www.unicode.org/L2/L2017/17014-hentaigana-comments.pdf>
- `utc-l2-17-091` - <https://www.unicode.org/L2/L2017/17091-sc2-n4523-small-kana.pdf>
- `utc-l2-19-381` - <https://www.unicode.org/L2/L2019/19381-missing-kana.pdf>
- `utc-l2-19-382` - <https://www.unicode.org/L2/L2019/19382-mid-japanese-kana.pdf>
- `utc-l2-20-152` - <https://www.unicode.org/L2/L2020/20152-archaic-wu-origin.pdf>
- `utc-l2-20-233` - <https://www.unicode.org/L2/L2020/20233-kana-fdbk-shakuhachi.pdf>
- `utc-l2-20-280` - <https://www.unicode.org/L2/L2020/20280-taiwan-kana.pdf>
- `utc-l2-20-209r` - <https://www.unicode.org/L2/L2020/20209r-taiwan-kana.pdf>
- Unicode code chart, Kana Extended-B - <https://www.unicode.org/charts/PDF/U1AFF0.pdf>
- `utc-l2-23-112` - <https://www.unicode.org/L2/L2023/23112-missing-kana-ligatures.pdf>
- `utc-l2-23-118` - <https://www.unicode.org/L2/L2023/23118-ryukyu-kana.pdf>
- `utc-l2-23-123` - <https://www.unicode.org/L2/L2023/23123-ryukyu-kana-feedback.pdf>
- `utc-l2-23-127` - <https://www.unicode.org/L2/L2023/23127-katakana.pdf>
- `utc-l2-24-150` - <https://www.unicode.org/L2/L2024/24150-three-kana-ligatures.pdf>
- `utc-l2-24-279` - <https://www.unicode.org/L2/L2024/24279-proposal-to-encode-kana-ligature.pdf>
- `utc-l2-25-035` - <https://www.unicode.org/L2/L2025/25035-vo-small-kana-and-bopomofo.pdf>
- `utc-l2-25-036` - <https://www.unicode.org/L2/L2025/25036-encode-one-small-kana.pdf>
- `utc-l2-25-042` - <https://www.unicode.org/L2/L2025/25042-katakana-letter-small-ne.pdf>
- `utc-l2-25-060` - <https://www.unicode.org/L2/L2025/25060-katakana-letter-small-ne.pdf>
- `utc-l2-25-151r` - <https://www.unicode.org/L2/L2025/25151r-katakana-ne-wi.pdf>
