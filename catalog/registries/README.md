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

