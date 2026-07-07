# Registry Manifests

このディレクトリ配下に `utc/`、`wg2/`、`irg/` の目録を生成します。

`documents.jsonl` は 1 行 1 文書です。主なフィールド:

- `entry_id` - wiki から参照する安定 ID
- `registry` - `utc` / `wg2` / `irg`
- `doc_number` - 表示用文書番号
- `subject` - Registry の subject
- `source` - Registry の source
- `date` - Registry の日付
- `document_url` - 公開文書 URL。未公開・reserved・unused の場合は `null`
- `register_url` - その行を抽出した register URL

Registry の行として抽出できないが、後続文書の revision lineage や action item から追跡する必要がある例外文書は `config/derived_documents.json` に追加します。この manual overlay は `tools/sync_registries.py` が registry ごとの `documents.jsonl` へ `catalog_source: derived` として合流します。

Derived entry は通常の catalog entry と同じ必須フィールドに加えて、根拠を示す `provenance` を持たせます。`tools/check_catalog.py` は `config/derived_documents.json` と合流済み catalog の両方を検査し、overlay が未合流、または後で生成済み registry entry と重複するようになった場合にエラーにします。
