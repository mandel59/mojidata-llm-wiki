# Catalog

`catalog/` は Git にコミットできる目録レイヤです。

Document Registry から抽出した文書番号、表題、source、日付、公開 URL を JSONL として保存します。文書実体は `.cache/` にだけ取得し、このディレクトリには置きません。

更新:

```sh
uv run python tools/sync_registries.py --registry all --latest-only
uv run python tools/check_catalog.py
```
