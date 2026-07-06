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
catalog/
  registries/
    utc/documents.jsonl           UTC Document Registry 由来の目録
    utc/registers.json            同期した register ページ一覧
    wg2/documents.jsonl           WG2 Document Registry 由来の目録
    wg2/registers.json
    irg/documents.jsonl           IRG Document Register 由来の目録
    irg/registers.json
wiki/
  README.md                       wiki の入口
  log.md                          append-only の作業ログ
  topics/<slug>.md                論点・文字集合・script・block などの精読ページ
  documents/<entry-id>.md         重要文書の要約ページ
  meetings/<body>/<meeting>.md    UTC/WG2/IRG 会合単位の要約
  people/<slug>.md                人物・組織・member body
  families/<slug>.md              関連トピック横断の synthesis
tools/
  sync_registries.py              Registry を読んで catalog を再生成
  fetch_documents.py              目録に基づいて文書実体を .cache/ に取得
  check_catalog.py                目録の機械検査
  unicode_registry.py             Registry parser と共通処理
.cache/
  unicode-registry/               Registry HTML の非 Git キャッシュ
  unicode-docs/                   PDF/DOCX/XLSX/HTML 等の非 Git キャッシュ
```

`.cache/`、`raw/`、`downloads/` は `.gitignore` で除外する。文書実体を誤ってコミットしない。

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
kind: topic
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
title: IRG Meeting #66 Recommendations and Action Items
entry_id: irg-n2909
doc_number: IRG N2909
registry: irg
date: "2026-03-19"
source: IRG Convenor
topics: [irg-meeting-66, ws2024]
tags: [document, recommendations]
---
```

本文:

1. `## 要約` - 3〜8 行。
2. `## 決定・Action Item` - 決定事項、担当、期限があれば表にする。
3. `## 論点` - 後続文書や他 body との関係。
4. `## 出典` - `catalog` の `entry_id`、`document_url`、取得日ではなく registry 上の日付。

### `wiki/meetings/<body>/<meeting>.md`

会合単位で、agenda、minutes、recommendations、action items、activity report を束ねる。

本文:

1. `## 概要` - 会合番号、日付、場所、body。
2. `## 主要議題` - topic へのリンク付き。
3. `## 決定事項` - recommendation / consensus / action items。
4. `## 後続確認` - 次回以降に追うべき文書番号。
5. `## 出典`

## 操作

### Update Catalog

Document Registry から目録を更新する。文書実体は取得しない。

```sh
python3 tools/sync_registries.py --registry all --latest-only
python3 tools/check_catalog.py
```

広く過去分を取り込むときは `--latest-only` を外す。更新後は `catalog/registries/*/documents.jsonl` と `registers.json` の差分を見る。新規・変更された文書番号だけを `wiki/log.md` に記録する。

### Materialize Documents

wiki 作成に必要な文書だけを `.cache/` に取得する。

```sh
python3 tools/fetch_documents.py --registry wg2 --grep "Small Seal" --limit 10
python3 tools/fetch_documents.py --registry irg --doc "IRG N2909"
```

取得した実体は Git に入れない。wiki には公開 URL と `entry_id` を出典として残す。

### Ingest Topic

1. `catalog/registries/*/documents.jsonl` を検索して対象文書群を特定する。
2. 必要な文書だけ `.cache/` に取得する。
3. proposal、minutes、recommendations、action items、activity reports の順に読む。
4. `wiki/topics/<slug>.md` または `wiki/documents/<entry-id>.md` を作成・更新する。
5. 関連 topic、meeting、family へ相互リンクする。
6. `wiki/log.md` に一行追記する。

### Summarise Meeting

1. 会合番号で agenda / minutes / recommendations / action items を catalog から探す。
2. 必要なら activity reports も追加する。
3. `wiki/meetings/<body>/<meeting>.md` に、議題、決定、未決、後続文書をまとめる。
4. 関連 topic ページへリンクを戻す。

### Query

1. `wiki/README.md` と `catalog/registries/*/documents.jsonl` を入口に検索する。
2. 回答は出典付きで書く。
3. 再利用価値がある整理なら、ユーザ確認後に wiki ページとして file back する。

### Lint

- 目録 JSONL が壊れていないか `python3 tools/check_catalog.py` で見る。
- wiki の主張に出典があるか確認する。
- topic、document、meeting、family の相互リンク漏れを見る。
- UTC/WG2/IRG 間で同一トピックの状態が食い違う場合、時点と body を明示しているか確認する。

## コミット規約

- 目録更新: `[catalog] update Unicode registry manifests`
- wiki 追加・更新: `[wiki] ingest small seal script discussion`
- tool 変更: `[tools] improve Unicode registry parser`
- schema 変更: `[schema] update source handling policy`

外部文書実体、Registry HTML cache、変換済みテキスト cache はコミットしない。

