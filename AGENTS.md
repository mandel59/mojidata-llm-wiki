# Unicode LLM Wiki - Agent Schema

このリポジトリは UTC、WG2、IRG の Document Registry を入口に、Unicode 標準化の議論を LLM が読み、要約し、相互リンク付きの wiki として維持するためのものです。

Jxck/tc39-llm-wiki の考え方に合わせて、raw source、wiki、schema を分離します。ただしこのリポジトリでは、外部取得リソースの実体は Git に入れません。コミットするのは目録と wiki だけです。

## レイヤ

- **Remote registries** - `unicode.org` 上の公開 Document Registry。UTC、WG2、IRG の文書番号、表題、source、日付、文書 URL の一次入口。
- **Catalog** - `catalog/registries/`。Registry から抽出した目録。Git にコミットしてよい。
- **Local cache** - `.cache/unicode-registry/` と `.cache/unicode-docs/`。Registry HTML と文書実体のキャッシュ。Git にコミットしない。
- **The wiki** - `wiki/`。LLM が作成・更新する Markdown knowledge base。
- **The schema** - この `AGENTS.md`。ページ形式、出典の優先順位、操作手順を定義する。

## ディレクトリ構成

```text
config/
  registries.json                 Document Registry の起点 URL と抽出設定
schema/
  concept_types.json              concept type ごとの required fields と relation schema
catalog/
  registries/
    utc/documents.jsonl           UTC Document Registry 由来の目録
    utc/registers.json            同期した register ページ一覧
    wg2/documents.jsonl           WG2 Document Registry 由来の目録
    wg2/registers.json
    irg/documents.jsonl           IRG Document Register 由来の目録
    irg/registers.json
wiki/
  index.md                        OKF bundle root index
  log.md                          OKF 形式の作業ログ
  topics/<slug>.md                論点・文字集合・script・block などの精読ページ
  documents/<entry-id>.md         重要文書の要約ページ
  events/<slug>.md                勧告、action item、状態変更などの出来事
  meetings/<body>/<meeting>.md    UTC/WG2/IRG 会合単位の要約
  people/<slug>.md                人物・組織・member body
  families/<slug>.md              関連トピック横断の synthesis
tools/
  sync_registries.py              Registry を読んで catalog を再生成
  fetch_documents.py              目録に基づいて文書実体を .cache/ に取得
  check_catalog.py                目録の機械検査
  check_events.py                 event ページと参照整合性の検査
  generate_event_indexes.py       event metadata から index を生成
  rewrite_event_timelines.py      event metadata から marker block の timeline を更新
  query_wiki.py                   wiki concept graph を機械的にクエリ
  document_sections.py            Markdown concept page の目次表示と section 抽出
  check_okf.py                    wiki の OKF v0.1 互換検査
  wiki_store.py                   wiki frontmatter、concept graph、schema validation の共通処理
  unicode_registry.py             Registry parser と共通処理
.cache/
  unicode-registry/               Registry HTML の非 Git キャッシュ
  unicode-docs/                   PDF/DOCX/XLSX/HTML 等の非 Git キャッシュ
```

`.cache/`、`raw/`、`downloads/` は `.gitignore` で除外する。文書実体を誤ってコミットしない。

## OKF 互換性

`wiki/` は Open Knowledge Format (OKF) v0.1 の knowledge bundle として扱う。

- bundle root は `wiki/`。
- 入口は `wiki/index.md`。`index.md` と `log.md` は OKF reserved filenames として扱う。
- `wiki/` 配下の `README.md` スタブは作らない。ディレクトリ一覧は各ディレクトリの `index.md` に置く。
- `index.md` は directory listing とし、root の `wiki/index.md` だけ `okf_version: "0.1"` frontmatter を持ってよい。
- `log.md` は `## YYYY-MM-DD` の date heading と flat list の entries を新しい日付順に置く。
- `index.md` と `log.md` 以外の `.md` は concept document とし、YAML frontmatter に非空の `type` を必ず持つ。
- 種別は `type` に統一し、`kind` は使わない。`entry_id`、`documents`、`topics`、`bodies` などは producer-defined extension として保持してよい。
- `slug` または `entry_id` を持つ concept document は、ファイル名 stem をその値に一致させる。
- `aliases` は YAML list とし、文書番号の別表記、複数 registry で同一文書に付いた番号、人物・組織・topic の別名、略称、旧称を入れる。primary identity は `slug` / `entry_id` のまま維持し、重複ページを避けたい場合は alias で同一 concept に寄せる。
- type ごとの required fields、list fields、relation fields は `schema/concept_types.json` で管理する。checker や query tool に type schema を重複して埋め込まない。
- 本文中の Markdown link は実在する wiki page または外部 URL に限る。まだページ化されていないが関連として残したい概念・文書・会合・人物・出来事は、本文リンクではなく frontmatter の `documents`、`topics`、`people`、`meetings`、`events` に slug / entry_id として記録する。
- frontmatter relation は未ページ化 target を許容する。`tools/query_wiki.py` の JSON 出力では、既存 concept へ解決できた relation は `links` に入り、未解決 relation は `unresolved_relations` に残る。
- `tags` は YAML list とする。外部根拠は本文末尾の `## 出典` に公開 URL と `entry_id` を残す。
- wiki 内リンクからローカル `.cache/`、`raw/`、`downloads/` へリンクしない。

## Wiki Data API

`tools/wiki_store.py` は wiki の programmatic access layer とする。Markdown frontmatter の split / parse、concept identity、concept graph、Markdown link resolution、schema validation、marker block 置換など、複数 tool で再利用する処理はここへ置く。

concept lookup は `id`、ファイル path、`title`、`doc_number`、frontmatter の `aliases` を対象にする。たとえば同じ Source Document が UTC `L2/...` と WG2 `N...` の両方で参照される場合は、canonical な `entry_id` のページを 1 つ作り、もう一方の文書番号を `aliases` に入れる。

`check_okf.py` は OKF bundle と `schema/concept_types.json` に基づく repository schema の検査に集中する。`check_events.py` は Event 固有の意味検査、たとえば event documents が catalog / derived documents に存在することの確認に集中する。topic / people / meeting / event relation は、未ページ化 target を残せるよう存在確認で失敗させない。`query_wiki.py`、`generate_event_indexes.py`、`rewrite_event_timelines.py` は `wiki_store.py` の API を使い、validation tool を共通 library として import しない。

## 出典の優先順位

- 会合での決定、recommendation、action item は、該当会合の minutes / recommendations / action items を一次ソースにする。
- 文書の存在、文書番号、表題、source、日付、公開 URL は `catalog/registries/*/documents.jsonl` を一次入口にする。
- WG2 の公式 working process 文書は ISO 側に限定公開される場合がある。公開 Registry に無い ISO-only 文書は、存在を示す公開ページ以上に踏み込まない。
- IRG の working set 状態や review assignment は、IRG home と IRG register、必要に応じて ORT への公開リンクで裏取りする。
- UTC と WG2 と IRG で同じ提案に関する記述が食い違う場合は、どの body のどの段階の記録かを明示する。単純に片方で上書きしない。

## 文書番号とリンク規約

- UTC: `L2/26-093` のような番号をそのまま使う。ページ slug は `utc-l2-26-093`。
- WG2: Registry 表示が `5354` だけでも wiki では `WG2 N5354` と表記する。ページ slug は `wg2-n5354`。
- IRG: `IRG N2909` のように表記する。ページ slug は `irg-n2909`。
- wiki から外部文書へは、目録の `entry_id` と `document_url` を出典に載せる。ローカル `.cache/` へのリンクは書かない。

## 言語規約

- 地の文は日本語。
- 文書番号、会議体名、Unicode property 名、UAX/UTS/TR 番号、script/block 名、規格名、人物名、member body 名は原文表記を保つ。
- 発言や決定文を引用するときは短く引用し、必要なら日本語で要約する。
- 不確かな推論は「推定」と書き、根拠文書を添える。

## ページ形式

### `wiki/topics/<slug>.md`

```yaml
---
title: Small Seal Script
slug: small-seal-script
type: Topic
bodies: [UTC, WG2, IRG]
documents: [wg2-n5348, utc-l2-26-147]
status: active
tags: [script, cjk]
---
```

本文:

1. `## 概要` - 何の議論か。
2. `## 経緯` - 年月順の表。文書番号、body、できごと、出典リンクを含める。
3. `## 主な論点` - 論点ごとに小見出し。未決・決着済みを明示する。
4. `## 関連文書` - `wiki/documents/` へのリンク、未要約なら文書番号のみ。
5. `## 関連トピック` - topic / family の相互リンク。
6. `## 出典` - 参照した `entry_id` と公開 URL。

### `wiki/documents/<entry-id>.md`

```yaml
---
title: "IRG Meeting #66 Recommendations and Action Items"
type: Source Document
entry_id: irg-n2909
doc_number: IRG N2909
document_type: recommendation
aliases: [IRG Meeting #66 Recommendations]
registry: irg
date: "2026-03-19"
source: IRG Convenor
topics: [irg-meeting-66, ws2024]
tags: [document, recommendations]
---
```

本文:

1. `## 要約` - 3〜8 行。
2. `## 提案内容` / `## 決定・Action Item` / `## 報告内容` - `document_type` に応じて、文書そのものが述べる内容を書く。提案文書では決定事項をここに書かない。
3. `## 後続決定` - 提案を取り上げた meeting / event がある場合、event / meeting へリンクし、このページでは決定概要を重複記述しない。未確認なら未確認と書く。
4. `## 論点` - 後続文書や他 body との関係。
5. `## 出典` - `catalog` の `entry_id`、`document_url`、取得日ではなく registry 上の日付。

`document_type` は文書そのものの性質を表す producer-defined extension であり、`proposal`、`recommendation`、`minutes`、`action-items`、`feedback`、`report`、`data`、`registry`、`notice`、`other` のいずれかを使う。`type: Source Document` は wiki concept type なので、提案・議事録・recommendation の区別には使わない。

### `wiki/events/<slug>.md`

出来事を canonical summary として独立させる。topic / meeting / people / family / document ページで同じ出来事の概要を説明し直さず、event へのリンクとそのページ固有の読み取りだけを書く。

```yaml
---
type: Event
title: WG2 M72.07 J-source glyph revert recommendation
description: "WG2 #72 が WG2 N5296 に基づき J-source glyph changes の revert を勧告した出来事。"
slug: wg2-m72-07-j-source-glyph-revert
date: "2025-06-27"
bodies: [WG2]
documents: [wg2-n5296, wg2-n5301, wg2-n5304]
topics: [j-source, irg-source-data-and-representative-glyphs]
people: [japan, wg2, michel-suignard]
status: adopted
tags: [event, j-source, glyph, recommendation]
timestamp: 2026-07-06T23:30:00+09:00
---
```

本文:

1. `## 概要` - 出来事そのものの canonical summary。
2. `## 背景` - 前提文書、会合、議論。
3. `## 結果` - recommendation、action item、status change、follow-up。
4. `## 影響範囲` - topic / people / meeting から見た意味。
5. `## 関連ページ` - wiki 内リンク。
6. `## 出典` - 参照した `entry_id` と公開 URL。

event は文書そのものではなく、文書・会合・勧告・action item・状態変更によって発生した意味のある出来事を表す。1 文書に複数 event がある場合も、複数文書で 1 event を構成する場合もある。

### `wiki/meetings/<body>/<meeting>.md`

会合単位で、agenda、minutes、recommendations、action items、activity report を束ねる。

本文:

1. `## 概要` - 会合番号、日付、場所、body。
2. `## 主要議題` - topic へのリンク付き。
3. `## 決定事項` - recommendation / consensus / action items。
4. `## 後続確認` - 次回以降に追うべき文書番号。
5. `## 出典`

## 操作

Python tools は `uv run python` で実行する。`python` / `python3` が PATH に無い環境があるため、直接呼び出しを前提にしない。`uv` の既定 cache や managed Python へのアクセスに失敗する場合は、`UV_CACHE_DIR=.tmp/uv-cache` と利用可能な Python への `UV_PYTHON` を指定してから実行する。

### Update Catalog

Document Registry から目録を更新する。文書実体は取得しない。

```sh
uv run python tools/sync_registries.py --registry all --latest-only
uv run python tools/check_catalog.py
```

`--latest-only` は既存の full manifest に最新 register の entries だけを差し替え merge する用途で使う。既存 manifest がある状態で過去年分が消える差分、または `document_count` が最新 register だけの件数へ大きく減る差分は異常なのでコミットしない。広く過去分を取り込むときは `--latest-only` を外す。更新後は `catalog/registries/*/documents.jsonl` と `registers.json` の差分を見る。新規・変更された文書番号だけを `wiki/log.md` に記録する。

### Materialize Documents

wiki 作成に必要な文書だけを `.cache/` に取得する。

```sh
uv run python tools/fetch_documents.py --registry wg2 --grep "Small Seal" --limit 10
uv run python tools/fetch_documents.py --registry irg --doc "IRG N2909"
```

取得した実体は Git に入れない。wiki には公開 URL と `entry_id` を出典として残す。

### Ingest Topic

1. `catalog/registries/*/documents.jsonl` を検索して対象文書群を特定する。
2. 必要な文書だけ `.cache/` に取得する。
3. proposal、minutes、recommendations、action items、activity reports の順に読む。
4. `wiki/topics/<slug>.md` または `wiki/documents/<entry-id>.md` を作成・更新する。
5. 関連 topic、meeting、family、people、event を frontmatter relation に記録する。相手ページが存在する場合だけ本文 Markdown link も追加する。
6. `wiki/log.md` に一行追記する。

### Summarise Meeting

1. 会合番号で agenda / minutes / recommendations / action items を catalog から探す。
2. 必要なら activity reports も追加する。
3. `wiki/meetings/<body>/<meeting>.md` に、議題、決定、未決、後続文書をまとめる。
4. 関連 topic / people / event を frontmatter relation に記録する。相手ページが存在する場合だけ本文 Markdown link も追加する。

### Ingest Event

1. 出来事を構成する文書、会合、recommendation、action item を catalog と wiki から特定する。
2. `wiki/events/<slug>.md` に canonical summary を作成する。
3. 関連する topic / meeting / people / family / document ページでは、frontmatter relation に event slug を記録する。相手ページが存在する場合は、重複説明を event link と短い文脈説明へ縮約する。
4. `uv run python tools/generate_event_indexes.py` で `wiki/events/index.md` を更新する。
5. timeline を機械更新する場合は `uv run python tools/rewrite_event_timelines.py --topic <slug>` で dry-run し、`<!-- events:start -->` / `<!-- events:end -->` の marker block があるページだけ `--write` で更新する。
6. `uv run python tools/check_events.py` と `uv run python tools/check_okf.py` を実行する。

### Query

1. `uv run python tools/query_wiki.py events` で event を日付順に確認する。
2. `uv run python tools/query_wiki.py list --type Topic` や `--topic <slug>` / `--people <slug>` / `--document <entry_id>` / `--alias <name>` で concept metadata を絞り込む。
3. `uv run python tools/query_wiki.py related <slug-or-alias> --depth 1` で frontmatter と Markdown 内部リンクから関連 concept を辿る。
4. `uv run python tools/document_sections.py toc <slug-or-alias>` で Markdown page の見出し一覧を出し、`uv run python tools/document_sections.py section <slug-or-alias> <heading>` で特定 section だけを読む。
5. 必要なら `--format json` で機械処理用に出力する。
6. `wiki/index.md` と `catalog/registries/*/documents.jsonl` も入口に検索する。
7. 回答は出典付きで書く。
8. 再利用価値がある整理なら、ユーザ確認後に wiki ページとして file back する。

### Lint

- 目録 JSONL が壊れていないか `uv run python tools/check_catalog.py` で見る。
- wiki が OKF v0.1 の最小条件を満たすか `uv run python tools/check_okf.py` で見る。
- event metadata と参照整合性を `uv run python tools/check_events.py` で見る。
- wiki の主張に出典があるか確認する。
- topic、document、meeting、family の relation 漏れを見る。本文 Markdown link は実在ページに限り、未ページ化 target は frontmatter relation として残す。
- UTC/WG2/IRG 間で同一トピックの状態が食い違う場合、時点と body を明示しているか確認する。

## コミット規約

- 目録更新: `[catalog] update Unicode registry manifests`
- wiki 追加・更新: `[wiki] ingest small seal script discussion`
- tool 変更: `[tools] improve Unicode registry parser`
- schema 変更: `[schema] update source handling policy`

外部文書実体、Registry HTML cache、変換済みテキスト cache はコミットしない。
