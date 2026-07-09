# Unicode Public Review Issues Catalog

このディレクトリは Unicode Public Review Issues (PRI) の公開ページから生成した目録を置きます。

- `documents.jsonl` - current/open issues と resolved issues を `PRI #<number>` 単位で正規化した catalog。
- `registers.json` - 同期した PRI ページ URL と抽出件数。

`document_url` は、current/open と新しい resolved issue では title link の issue description を指します。古い resolved issue で description が resolved 一覧ページ本文に埋め込まれている場合は、resolved ページの fragment URL を指します。
