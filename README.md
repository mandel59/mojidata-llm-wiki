# Unicode LLM Wiki

UTC、WG2、IRG の公開 Document Registry を材料に、Unicode 関連の標準化議論を追うための LLM-Wiki です。

このリポジトリは、Jxck の記事「[Web 標準の議論を LLM-Wiki で追う](https://blog.jxck.io/entries/2026-06-29/tc39-llm-wiki.html)」で紹介されている TC39 LLM-Wiki の考え方を参考に作成しています。

このリポジトリでは、外部取得した HTML/PDF/DOCX/XLSX などの実体は Git に入れません。Git に入れるのは、取得元 URL、文書番号、表題、出典、日付、ローカルキャッシュの再現手順を持つ目録だけです。

## 基本方針

- `catalog/` はコミット対象の目録です。Document Registry から抽出した JSONL を置きます。
- `.cache/` はコミットしない取得キャッシュです。Registry HTML や文書実体を必要時だけ置きます。
- `wiki/` は LLM が維持する Markdown wiki です。議論の要約、人物、会合、トピック横断ページを置きます。
- `wiki/` は OKF v0.1 bundle として扱い、入口は `wiki/index.md` に置きます。
- `AGENTS.md` は運用 schema です。新しい LLM セッションは最初に読みます。

## 参照する公開 Registry

- UTC Document Registry: <https://www.unicode.org/L2/>
- WG2 Document Registry: <https://www.unicode.org/wg2/WG2-registry.html>
- IRG Document Register: <https://www.unicode.org/irg/IRG-register.html>

## セットアップ

Python 3.11+ の標準ライブラリだけで動くようにしています。

```sh
python3 -m unittest discover
python3 tools/check_catalog.py
python3 tools/check_okf.py
```

## 目録の更新

最新 register だけを同期する場合:

```sh
python3 tools/sync_registries.py --registry all --latest-only
python3 tools/check_catalog.py
```

全 register を root ページから辿る場合:

```sh
python3 tools/sync_registries.py --registry all
python3 tools/check_catalog.py
```

生成される主なファイル:

```text
catalog/registries/utc/documents.jsonl
catalog/registries/wg2/documents.jsonl
catalog/registries/irg/documents.jsonl
catalog/registries/*/registers.json
```

Registry HTML は `.cache/unicode-registry/` に保存されますが、Git には入りません。

## 文書実体の取得

目録から必要な文書だけをローカルキャッシュに materialize します。

```sh
python3 tools/fetch_documents.py --registry utc --grep "UTC #187"
python3 tools/fetch_documents.py --registry irg --doc "IRG N2909"
python3 tools/fetch_documents.py --registry wg2 --grep "Small Seal" --limit 10
```

文書実体は `.cache/unicode-docs/` に保存されます。これは Git に入りません。Wiki には、目録の `entry_id` と公開 URL を出典として残します。

PDF の本文抽出が必要な場合は、`pypdf` を一時依存として使います。抽出テキストも `.cache/` 配下に置くため Git には入りません。

```sh
UV_CACHE_DIR=.tmp/uv-cache uv run --with pypdf python tools/extract_pdf_text.py .cache/unicode-docs/wg2/*/*.pdf
```

## Wiki の育て方

1. `catalog/registries/*/documents.jsonl` から対象文書を探す。
2. 必要な文書だけ `tools/fetch_documents.py` で `.cache/` に取得する。
3. 議事録、recommendations、action items、proposal、activity report を読み、`wiki/` に要約・経緯・論点を追加する。
4. 更新したら OKF log 形式で `wiki/log.md` に追記する。
5. 目録と wiki はコミットしてよいが、`.cache/` はコミットしない。

詳細なページ形式と運用規約は [AGENTS.md](AGENTS.md) を参照してください。
