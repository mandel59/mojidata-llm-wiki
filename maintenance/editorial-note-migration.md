# 編集ノート移行の進捗

2026-11-02。**全体の移行は継続中。検索候補の精査と、記事全文の精査は別に数える。**

## 対象と今回の結果

- Wiki 全633ファイルを検索。concept article は623ページ、index / log は10ページ。
- 初回検索185ページ・254行に、補足検索で32ページ・59行を追加。候補は計217ページ・313行。
- 候補行と周辺文脈の精査は217ページすべて終了。84ページを整理し、78件を近接ノートへ移した。133ページは読者に必要な本文として残した。
- 前回の a2bbc17 は65ページ・69件の移行。今回との対象ページには重複があるため、ページ数を単純加算しない。
- 既存73ノートは保持。今回の編集後は151ノート。会合結果のページが既にある公開待ち記述は、そのページへの案内に整理した。
- 検索ルール、全ファイルの状態、確認時の SHA-256、候補ごとの判断・理由は [管理データ](editorial-note-migration.json) に記録する。

## 進捗

| 区分 | ページ数 |
| --- | ---: |
| 候補精査・変更・検証済み | 84 |
| 候補精査済み・本文に残す | 133 |
| 検索候補なし・全文精査済み | 41 |
| 検索候補なし・全文精査は未実施 | 365 |
| 対象外の index / log | 10 |

全文を読んだ範囲まで確認記録を残した記事は **48 / 623ページ**。候補の周辺だけを確認したページは、全文精査済みへ昇格させていない。全文精査の未完了は575ページで、そのうち365ページは検索候補がなかったページ。全文精査は、記事本文全体に編集作業記述が混入していないかの確認を指す。

## 本文に残す判断

- 原資料が述べる未確認・調査計画や、IRG / UTC / WG2 自身の Action Item。
- 提案・feedback・勧告・採択の違い、body と記録時点の違い、歴史資料の解釈限界。
- 資料間の数値不一致、要約の対象資料、旧 catalog / 旧版に基づくことの注意。
- 記事の対象範囲、関連ページへの案内、canonical / alias / Todo 等の技術用語への検索一致。

採否を調べていないことから、会合で未決定だったと推論しない。ノートを除いても、読者に必要な注意と根拠が本文に残るようにする。

## 次の確認範囲

1. topics / families / people / meetings の全文を読み、検索語に出ない編集上の判断・作業記録を確認する。
2. documents / events も全文精査する。delta 41ページと family 4ページの全文精査は完了。候補行を確認した217ページも、未読部分を残したまま全件完了とは扱わない。
3. 新規・更新されたページは管理データの SHA-256 と照合し、変更後の内容を再確認する。
4. 全文精査と検証が終わるまで、この移行を全件完了にはしない。

| ディレクトリ | 全文精査済み | 未完了 |
| --- | ---: | ---: |
| topics | 0 | 55 |
| families | 4 | 0 |
| people | 0 | 22 |
| meetings | 0 | 15 |
| documents | 2 | 455 |
| events | 1 | 28 |
| delta | 41 | 0 |

## 検証

73 unit tests、catalog / OKF / wiki review / event 検査、document / event index の生成差分検査が成功。全633ファイルと台帳の対応、候補行と基準コミットの一致、ノート保持・行位置、移行後の本文に空の節がないことを確認した。

## 候補ページ別の判断

以下は検索候補を精査した範囲。全文精査の状態は管理データの full_text_review を参照する。候補の baseline_line / text は基準コミット a2bbc17 の原文を示す。

| ページ | 結果 | 判断 |
| --- | --- | --- |
| [documents/irg-n003.md](../wiki/documents/irg-n003.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [documents/irg-n034.md](../wiki/documents/irg-n034.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [documents/irg-n080.md](../wiki/documents/irg-n080.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [documents/irg-n131.md](../wiki/documents/irg-n131.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [documents/irg-n1528.md](../wiki/documents/irg-n1528.md) | 本文に残す | 一次資料の記載内容、文書の役割、決定主体・時点の違い、または解釈上の注意。読者に必要な本文。 |
| [documents/irg-n1531.md](../wiki/documents/irg-n1531.md) | 本文に残す | 一次資料の記載内容、文書の役割、決定主体・時点の違い、または解釈上の注意。読者に必要な本文。 |
| [documents/irg-n1532r.md](../wiki/documents/irg-n1532r.md) | 本文に残す | 一次資料の記載内容、文書の役割、決定主体・時点の違い、または解釈上の注意。読者に必要な本文。 |
| [documents/irg-n189.md](../wiki/documents/irg-n189.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [documents/irg-n2171.md](../wiki/documents/irg-n2171.md) | 本文に残す | 一次資料の記載内容、文書の役割、決定主体・時点の違い、または解釈上の注意。読者に必要な本文。 |
| [documents/irg-n2491r.md](../wiki/documents/irg-n2491r.md) | 本文に残す | 一次資料の記載内容、文書の役割、決定主体・時点の違い、または解釈上の注意。読者に必要な本文。 |
| [documents/irg-n2656.md](../wiki/documents/irg-n2656.md) | 本文に残す | 一次資料の記載内容、文書の役割、決定主体・時点の違い、または解釈上の注意。読者に必要な本文。 |
| [documents/irg-n2689.md](../wiki/documents/irg-n2689.md) | 本文に残す | 一次資料の記載内容、文書の役割、決定主体・時点の違い、または解釈上の注意。読者に必要な本文。 |
| [documents/irg-n2702.md](../wiki/documents/irg-n2702.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [documents/irg-n2733r.md](../wiki/documents/irg-n2733r.md) | 本文に残す | 一次資料の記載内容、文書の役割、決定主体・時点の違い、または解釈上の注意。読者に必要な本文。 |
| [documents/irg-n2765.md](../wiki/documents/irg-n2765.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [documents/irg-n2786.md](../wiki/documents/irg-n2786.md) | 本文に残す | 一次資料の記載内容、文書の役割、決定主体・時点の違い、または解釈上の注意。読者に必要な本文。 |
| [documents/irg-n2826.md](../wiki/documents/irg-n2826.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [documents/irg-n2828.md](../wiki/documents/irg-n2828.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [documents/irg-n2834.md](../wiki/documents/irg-n2834.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [documents/irg-n2835r.md](../wiki/documents/irg-n2835r.md) | 本文に残す | 資料自身が報告する source 未確認件数と置換方針であり、wiki の調査状況ではない。 |
| [documents/irg-n2840.md](../wiki/documents/irg-n2840.md) | 本文に残す | 一次資料の記載内容、文書の役割、決定主体・時点の違い、または解釈上の注意。読者に必要な本文。 |
| [documents/irg-n2868.md](../wiki/documents/irg-n2868.md) | 本文に残す | 原文が示す今後の調査方針。標準化側の計画なので本文に残す。 |
| [documents/irg-n2874r.md](../wiki/documents/irg-n2874r.md) | 移行・整理 | 具体的な字形を一次資料で確認する注意は残し、要約作成時の制約を移す。 |
| [documents/irg-n2888.md](../wiki/documents/irg-n2888.md) | 本文に残す | 一次資料の記載内容、文書の役割、決定主体・時点の違い、または解釈上の注意。読者に必要な本文。 |
| [documents/irg-n2889r2.md](../wiki/documents/irg-n2889r2.md) | 移行・整理 | 採否・反映の調査予定であり、一次文書が記録する結論とは分ける。 |
| [documents/irg-n2892.md](../wiki/documents/irg-n2892.md) | 本文に残す | 一次資料の記載内容、文書の役割、決定主体・時点の違い、または解釈上の注意。読者に必要な本文。 |
| [documents/irg-n2899.md](../wiki/documents/irg-n2899.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [documents/irg-n2909.md](../wiki/documents/irg-n2909.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [documents/irg-n2910.md](../wiki/documents/irg-n2910.md) | 本文に残す | 一次資料の記載内容、文書の役割、決定主体・時点の違い、または解釈上の注意。読者に必要な本文。 |
| [documents/irg-n2911.md](../wiki/documents/irg-n2911.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [documents/irg-n2914r.md](../wiki/documents/irg-n2914r.md) | 本文に残す | 一次資料の記載内容、文書の役割、決定主体・時点の違い、または解釈上の注意。読者に必要な本文。 |
| [documents/irg-n2916.md](../wiki/documents/irg-n2916.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [documents/irg-n2918.md](../wiki/documents/irg-n2918.md) | 移行・整理 | 採否・反映の調査予定であり、一次文書が記録する結論とは分ける。 |
| [documents/irg-n2925.md](../wiki/documents/irg-n2925.md) | 移行・整理 | 既存の会合記録への案内に整理する。 |
| [documents/irg-n2928.md](../wiki/documents/irg-n2928.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [documents/irg-n2929r.md](../wiki/documents/irg-n2929r.md) | 移行・整理 | 採否・反映の調査予定であり、一次文書が記録する結論とは分ける。 / agenda の掲載事実を本文に残す。 |
| [documents/irg-n2931.md](../wiki/documents/irg-n2931.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [documents/irg-n2933.md](../wiki/documents/irg-n2933.md) | 本文に残す | 一次資料の記載内容、文書の役割、決定主体・時点の違い、または解釈上の注意。読者に必要な本文。 |
| [documents/irg-n2934r.md](../wiki/documents/irg-n2934r.md) | 本文に残す | 一次資料の記載内容、文書の役割、決定主体・時点の違い、または解釈上の注意。読者に必要な本文。 |
| [documents/irg-n2935.md](../wiki/documents/irg-n2935.md) | 移行・整理 | 入力文書と採択の区別を本文に残し、調査予定を移す。 |
| [documents/irg-n2939r.md](../wiki/documents/irg-n2939r.md) | 移行・整理 | 採否・反映の調査予定であり、一次文書が記録する結論とは分ける。 |
| [documents/irg-n2940.md](../wiki/documents/irg-n2940.md) | 移行・整理 | 採否・反映の調査予定であり、一次文書が記録する結論とは分ける。 |
| [documents/irg-n2941.md](../wiki/documents/irg-n2941.md) | 移行・整理 | 採否・反映の調査予定であり、一次文書が記録する結論とは分ける。 |
| [documents/irg-n2943.md](../wiki/documents/irg-n2943.md) | 移行・整理 | 採否・反映の調査予定であり、一次文書が記録する結論とは分ける。 |
| [documents/irg-n2945.md](../wiki/documents/irg-n2945.md) | 移行・整理 | 採否・反映の調査予定であり、一次文書が記録する結論とは分ける。 |
| [documents/irg-n2952.md](../wiki/documents/irg-n2952.md) | 移行・整理 | recommendations は既にページ化済み。公開待ちの記述を解消し、既存の会合記録を案内する。 |
| [documents/irg-n2953.md](../wiki/documents/irg-n2953.md) | 移行・整理 | agenda と採否の違いは残す。既存ページがあるので available 待ちの記述を解消する。 |
| [documents/irg-n2962r2.md](../wiki/documents/irg-n2962r2.md) | 本文に残す | 一次資料の記載内容、文書の役割、決定主体・時点の違い、または解釈上の注意。読者に必要な本文。 |
| [documents/irg-n2968.md](../wiki/documents/irg-n2968.md) | 本文に残す | 旧文書・旧 catalog を根拠とする要約だと示す出典の注意。隠すと現行 Registry の記録と誤認する。 |
| [documents/irg-n2969.md](../wiki/documents/irg-n2969.md) | 移行・整理 | 既存の結果文書への案内に整理する。agenda の討議完了を採択とは書かない。 |
| [documents/irg-n2969r.md](../wiki/documents/irg-n2969r.md) | 移行・整理 | 既存の正式な会合記録への案内に整理する。 |
| [documents/irg-n2971.md](../wiki/documents/irg-n2971.md) | 移行・整理 | 採否・反映の調査予定であり、一次文書が記録する結論とは分ける。 |
| [documents/irg-n2972.md](../wiki/documents/irg-n2972.md) | 移行・整理 | agenda と採択の違いを残し、採否の調査予定を移す。 |
| [documents/irg-n2972r.md](../wiki/documents/irg-n2972r.md) | 移行・整理 | TA / T9 の集計上の注意は本文に残し、反映の照合予定を移す。 |
| [documents/irg-n2973.md](../wiki/documents/irg-n2973.md) | 移行・整理 | 提案時点と会合結果を分け、既存の結果文書を案内する。 |
| [documents/irg-n2975.md](../wiki/documents/irg-n2975.md) | 移行・整理 | source-owner 同意と標準データ反映の違いを残し、確認作業を移す。 |
| [documents/irg-n2977.md](../wiki/documents/irg-n2977.md) | 移行・整理 | 採否・反映の調査予定であり、一次文書が記録する結論とは分ける。 |
| [documents/irg-n2983.md](../wiki/documents/irg-n2983.md) | 移行・整理 | 採否・反映の調査予定であり、一次文書が記録する結論とは分ける。 |
| [documents/irg-n2984.md](../wiki/documents/irg-n2984.md) | 移行・整理 | 採否・反映の調査予定であり、一次文書が記録する結論とは分ける。 |
| [documents/irg-n2985.md](../wiki/documents/irg-n2985.md) | 移行・整理 | 修正案と正式決定・実装反映の違いを本文に残し、照合予定を移す。 |
| [documents/irg-n2986.md](../wiki/documents/irg-n2986.md) | 移行・整理 | 添付資料の性質は本文に残し、採否の照合予定を移す。 |
| [documents/irg-n2987.md](../wiki/documents/irg-n2987.md) | 移行・整理 | 採否・反映の調査予定であり、一次文書が記録する結論とは分ける。 |
| [documents/irg-n2988.md](../wiki/documents/irg-n2988.md) | 移行・整理 | 参照先が画像表であることは残し、レンダリングして確認した編集作業を移す。 / 既存の正式な会合記録への案内に整理する。 |
| [documents/irg-n2989.md](../wiki/documents/irg-n2989.md) | 移行・整理 | 既存の正式な会合記録への案内に整理する。 |
| [documents/irg-n391.md](../wiki/documents/irg-n391.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [documents/irg-n394r.md](../wiki/documents/irg-n394r.md) | 本文に残す | 改訂案と正式承認の違いという資料解釈上の限界。 |
| [documents/pri-259.md](../wiki/documents/pri-259.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [documents/pri-534.md](../wiki/documents/pri-534.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [documents/pri-544.md](../wiki/documents/pri-544.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [documents/pri-545.md](../wiki/documents/pri-545.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [documents/pri-547.md](../wiki/documents/pri-547.md) | 本文に残す | 技術用語・property 名・符号化モデルの説明。canonical / alias 等の検索一致であり編集メモではない。 |
| [documents/pri-550.md](../wiki/documents/pri-550.md) | 移行・整理 | digest 作成時の指示を、読者に必要な同時期の references update という関係へ整理する。 |
| [documents/pri-554.md](../wiki/documents/pri-554.md) | 本文に残す | 一次資料の記載内容、文書の役割、決定主体・時点の違い、または解釈上の注意。読者に必要な本文。 |
| [documents/utc-l2-10-198.md](../wiki/documents/utc-l2-10-198.md) | 本文に残す | 一次資料の記載内容、文書の役割、決定主体・時点の違い、または解釈上の注意。読者に必要な本文。 |
| [documents/utc-l2-19-015.md](../wiki/documents/utc-l2-19-015.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [documents/utc-l2-19-328.md](../wiki/documents/utc-l2-19-328.md) | 本文に残す | 原文に記録された UTC への Recommendation M。wiki 編集者の TODO ではない。 |
| [documents/utc-l2-20-180.md](../wiki/documents/utc-l2-20-180.md) | 本文に残す | 一次資料の記載内容、文書の役割、決定主体・時点の違い、または解釈上の注意。読者に必要な本文。 |
| [documents/utc-l2-20-209r.md](../wiki/documents/utc-l2-20-209r.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [documents/utc-l2-23-127.md](../wiki/documents/utc-l2-23-127.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [documents/utc-l2-24-246.md](../wiki/documents/utc-l2-24-246.md) | 移行・整理 | 95 / 106 の資料内不一致は本文に残し、更新漏れという未確定の解釈を移す。 |
| [documents/utc-l2-25-220.md](../wiki/documents/utc-l2-25-220.md) | 本文に残す | 一次資料の記載内容、文書の役割、決定主体・時点の違い、または解釈上の注意。読者に必要な本文。 |
| [documents/utc-l2-25-230r.md](../wiki/documents/utc-l2-25-230r.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [documents/utc-l2-26-050r.md](../wiki/documents/utc-l2-26-050r.md) | 本文に残す | 技術用語・property 名・符号化モデルの説明。canonical / alias 等の検索一致であり編集メモではない。 |
| [documents/utc-l2-26-079.md](../wiki/documents/utc-l2-26-079.md) | 移行・整理 | 採否・反映の調査予定であり、一次文書が記録する結論とは分ける。 |
| [documents/utc-l2-26-087.md](../wiki/documents/utc-l2-26-087.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [documents/utc-l2-26-092.md](../wiki/documents/utc-l2-26-092.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [documents/utc-l2-26-093.md](../wiki/documents/utc-l2-26-093.md) | 移行・整理 | minutes の対象外という事実は本文に残し、未調査から pending と分類した編集判断を移す。 |
| [documents/utc-l2-26-095.md](../wiki/documents/utc-l2-26-095.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [documents/utc-l2-26-097.md](../wiki/documents/utc-l2-26-097.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [documents/utc-l2-26-101.md](../wiki/documents/utc-l2-26-101.md) | 本文に残す | 一次資料の記載内容、文書の役割、決定主体・時点の違い、または解釈上の注意。読者に必要な本文。 |
| [documents/utc-l2-26-102.md](../wiki/documents/utc-l2-26-102.md) | 移行・整理 | 当時の予定日の不一致は残す。正式公開の報告が既にあるので、draft / beta を常に優先する旧編集方針は解消する。 |
| [documents/utc-l2-26-105.md](../wiki/documents/utc-l2-26-105.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [documents/utc-l2-26-106.md](../wiki/documents/utc-l2-26-106.md) | 本文に残す | 技術用語・property 名・符号化モデルの説明。canonical / alias 等の検索一致であり編集メモではない。 |
| [documents/utc-l2-26-107.md](../wiki/documents/utc-l2-26-107.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [documents/utc-l2-26-108.md](../wiki/documents/utc-l2-26-108.md) | 本文に残す | 一次資料の記載内容、文書の役割、決定主体・時点の違い、または解釈上の注意。読者に必要な本文。 |
| [documents/utc-l2-26-112.md](../wiki/documents/utc-l2-26-112.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [documents/utc-l2-26-131.md](../wiki/documents/utc-l2-26-131.md) | 移行・整理 | 採否・反映の調査予定であり、一次文書が記録する結論とは分ける。 |
| [documents/utc-l2-26-132.md](../wiki/documents/utc-l2-26-132.md) | 移行・整理 | 採否・反映の調査予定であり、一次文書が記録する結論とは分ける。 / SEW 勧告と UTC 採否の区別、会合ページへの案内を残す。 |
| [documents/utc-l2-26-135.md](../wiki/documents/utc-l2-26-135.md) | 移行・整理 | 採否・反映の調査予定であり、一次文書が記録する結論とは分ける。 / 日付と勧告段階は本文に残し、採否の照合予定を移す。 |
| [documents/utc-l2-26-137.md](../wiki/documents/utc-l2-26-137.md) | 移行・整理 | 採否・反映の調査予定であり、一次文書が記録する結論とは分ける。 |
| [documents/utc-l2-26-145.md](../wiki/documents/utc-l2-26-145.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [documents/utc-l2-26-146.md](../wiki/documents/utc-l2-26-146.md) | 本文に残す | 旧版・WG2 版と未公開改訂版の範囲を示す出典の注意。 |
| [documents/utc-l2-26-181r.md](../wiki/documents/utc-l2-26-181r.md) | 本文に残す | 技術用語・property 名・符号化モデルの説明。canonical / alias 等の検索一致であり編集メモではない。 |
| [documents/utc-l2-26-207.md](../wiki/documents/utc-l2-26-207.md) | 本文に残す | 技術用語・property 名・符号化モデルの説明。canonical / alias 等の検索一致であり編集メモではない。 |
| [documents/utc-l2-26-208.md](../wiki/documents/utc-l2-26-208.md) | 移行・整理 | 採否・反映の調査予定であり、一次文書が記録する結論とは分ける。 |
| [documents/utc-l2-26-212.md](../wiki/documents/utc-l2-26-212.md) | 移行・整理 | 日付と勧告段階は本文に残し、採否の照合予定を移す。 |
| [documents/utc-l2-26-214.md](../wiki/documents/utc-l2-26-214.md) | 移行・整理 | 日付と勧告段階は本文に残し、採否の照合予定を移す。 |
| [documents/utc-l2-26-217.md](../wiki/documents/utc-l2-26-217.md) | 移行・整理 | feedback の性質は本文に残し、disposition の確認作業を移す。 / 日付と勧告段階は本文に残し、採否の照合予定を移す。 |
| [documents/utc-l2-26-219.md](../wiki/documents/utc-l2-26-219.md) | 移行・整理 | 会合への入力資料という性質と採択との違いは本文に残し、編集時点と確認予定を移す。 |
| [documents/utc-l2-26-221.md](../wiki/documents/utc-l2-26-221.md) | 本文に残す | 技術用語・property 名・符号化モデルの説明。canonical / alias 等の検索一致であり編集メモではない。 |
| [documents/utc-l2-26-223.md](../wiki/documents/utc-l2-26-223.md) | 本文に残す | 技術用語・property 名・符号化モデルの説明。canonical / alias 等の検索一致であり編集メモではない。 |
| [documents/utc-l2-26-225.md](../wiki/documents/utc-l2-26-225.md) | 本文に残す | 技術用語・property 名・符号化モデルの説明。canonical / alias 等の検索一致であり編集メモではない。 |
| [documents/utc-l2-26-227.md](../wiki/documents/utc-l2-26-227.md) | 移行・整理 | 採否・反映の調査予定であり、一次文書が記録する結論とは分ける。 |
| [documents/utc-l2-26-231.md](../wiki/documents/utc-l2-26-231.md) | 移行・整理 | 会合への入力資料という性質と採択との違いは本文に残し、編集時点と確認予定を移す。 |
| [documents/utc-l2-26-233.md](../wiki/documents/utc-l2-26-233.md) | 移行・整理 | 会合への入力資料という性質と採択との違いは本文に残し、編集時点と確認予定を移す。 |
| [documents/utc-l2-26-234.md](../wiki/documents/utc-l2-26-234.md) | 移行・整理 | 会合への入力資料という性質と採択との違いは本文に残し、編集時点と確認予定を移す。 |
| [documents/utc-l2-26-235.md](../wiki/documents/utc-l2-26-235.md) | 移行・整理 | 会合への入力資料という性質と採択との違いは本文に残し、編集時点と確認予定を移す。 |
| [documents/utc-l2-26-236.md](../wiki/documents/utc-l2-26-236.md) | 移行・整理 | 会合への入力資料という性質と採択との違いは本文に残し、編集時点と確認予定を移す。 |
| [documents/utc-l2-26-237.md](../wiki/documents/utc-l2-26-237.md) | 移行・整理 | 会合への入力資料という性質と採択との違いは本文に残し、編集時点と確認予定を移す。 |
| [documents/utc-l2-26-238.md](../wiki/documents/utc-l2-26-238.md) | 移行・整理 | 会合への入力資料という性質と採択との違いは本文に残し、編集時点と確認予定を移す。 |
| [documents/utc-l2-26-239.md](../wiki/documents/utc-l2-26-239.md) | 移行・整理 | 会合への入力資料という性質と採択との違いは本文に残し、編集時点と確認予定を移す。 |
| [documents/utc-l2-26-240.md](../wiki/documents/utc-l2-26-240.md) | 移行・整理 | 会合への入力資料という性質と採択との違いは本文に残し、編集時点と確認予定を移す。 |
| [documents/utc-l2-26-241.md](../wiki/documents/utc-l2-26-241.md) | 移行・整理 | 会合への入力資料という性質と採択との違いは本文に残し、編集時点と確認予定を移す。 |
| [documents/utc-l2-26-245.md](../wiki/documents/utc-l2-26-245.md) | 本文に残す | 技術用語・property 名・符号化モデルの説明。canonical / alias 等の検索一致であり編集メモではない。 |
| [documents/utc-l2-26-247.md](../wiki/documents/utc-l2-26-247.md) | 本文に残す | 技術用語・property 名・符号化モデルの説明。canonical / alias 等の検索一致であり編集メモではない。 |
| [documents/utc-l2-26-257.md](../wiki/documents/utc-l2-26-257.md) | 移行・整理 | 採否・反映の調査予定であり、一次文書が記録する結論とは分ける。 |
| [documents/utc-l2-26-258.md](../wiki/documents/utc-l2-26-258.md) | 移行・整理 | 採否・反映の調査予定であり、一次文書が記録する結論とは分ける。 |
| [documents/utc-l2-26-259.md](../wiki/documents/utc-l2-26-259.md) | 移行・整理 | 採否・反映の調査予定であり、一次文書が記録する結論とは分ける。 |
| [documents/utc-l2-26-260.md](../wiki/documents/utc-l2-26-260.md) | 移行・整理 | 会合への入力資料という性質と採択との違いは本文に残し、編集時点と確認予定を移す。 |
| [documents/utc-l2-26-261.md](../wiki/documents/utc-l2-26-261.md) | 移行・整理 | 会合への入力資料という性質と採択との違いは本文に残し、編集時点と確認予定を移す。 |
| [documents/utc-l2-26-262.md](../wiki/documents/utc-l2-26-262.md) | 移行・整理 | 会合への入力資料という性質と採択との違いは本文に残し、編集時点と確認予定を移す。 |
| [documents/utc-l2-26-263.md](../wiki/documents/utc-l2-26-263.md) | 移行・整理 | 会合への入力資料という性質と採択との違いは本文に残し、編集時点と確認予定を移す。 |
| [documents/utc-l2-26-264.md](../wiki/documents/utc-l2-26-264.md) | 移行・整理 | 会合への入力資料という性質と採択との違いは本文に残し、編集時点と確認予定を移す。 |
| [documents/utc-l2-26-265.md](../wiki/documents/utc-l2-26-265.md) | 移行・整理 | 会合への入力資料という性質と採択との違いは本文に残し、編集時点と確認予定を移す。 |
| [documents/utc-l2-26-266.md](../wiki/documents/utc-l2-26-266.md) | 移行・整理 | 会合への入力資料という性質と採択との違いは本文に残し、編集時点と確認予定を移す。 |
| [documents/utc-l2-26-267.md](../wiki/documents/utc-l2-26-267.md) | 移行・整理 | 会合への入力資料という性質と採択との違いは本文に残し、編集時点と確認予定を移す。 |
| [documents/utc-l2-26-268.md](../wiki/documents/utc-l2-26-268.md) | 移行・整理 | 会合への入力資料という性質と採択との違いは本文に残し、編集時点と確認予定を移す。 |
| [documents/utc-l2-26-269.md](../wiki/documents/utc-l2-26-269.md) | 移行・整理 | 会合への入力資料という性質と採択との違いは本文に残し、編集時点と確認予定を移す。 |
| [documents/utc-l2-26-270.md](../wiki/documents/utc-l2-26-270.md) | 移行・整理 | 会合への入力資料という性質と採択との違いは本文に残し、編集時点と確認予定を移す。 |
| [documents/utc-l2-26-271.md](../wiki/documents/utc-l2-26-271.md) | 移行・整理 | 会合への入力資料という性質と採択との違いは本文に残し、編集時点と確認予定を移す。 |
| [documents/utc-l2-26-272.md](../wiki/documents/utc-l2-26-272.md) | 移行・整理 | 会合への入力資料という性質と採択との違いは本文に残し、編集時点と確認予定を移す。 |
| [documents/utc-l2-26-273.md](../wiki/documents/utc-l2-26-273.md) | 移行・整理 | 会合への入力資料という性質と採択との違いは本文に残し、編集時点と確認予定を移す。 |
| [documents/wg2-n4634.md](../wiki/documents/wg2-n4634.md) | 移行・整理 | 同一文書の別番号という事実は残し、ページ統合の編集方針を移す。 |
| [documents/wg2-n4688.md](../wiki/documents/wg2-n4688.md) | 本文に残す | 11,108文字と11,116 entries の区別を説明する根拠。本文の採用値の理由を読者から隠さない。 |
| [documents/wg2-n5296.md](../wiki/documents/wg2-n5296.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [documents/wg2-n5301.md](../wiki/documents/wg2-n5301.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [documents/wg2-n5304.md](../wiki/documents/wg2-n5304.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [documents/wg2-n5306.md](../wiki/documents/wg2-n5306.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [documents/wg2-n5339.md](../wiki/documents/wg2-n5339.md) | 本文に残す | 技術用語・property 名・符号化モデルの説明。canonical / alias 等の検索一致であり編集メモではない。 |
| [documents/wg2-n5353.md](../wiki/documents/wg2-n5353.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [documents/wg2-n5354.md](../wiki/documents/wg2-n5354.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [events/irg-4-officer-role-restriction-withdrawal.md](../wiki/events/irg-4-officer-role-restriction-withdrawal.md) | 本文に残す | 過去の役割分担を全時期へ広げないための史料解釈上の限界。 |
| [events/sew-189-script-provisional-assignment-recommendations.md](../wiki/events/sew-189-script-provisional-assignment-recommendations.md) | 移行・整理 | SEW 勧告そのものの記述と、UTC 採否の確認作業を分ける。 |
| [events/uax60-unicode-18-first-published-version.md](../wiki/events/uax60-unicode-18-first-published-version.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [families/emoji.md](../wiki/families/emoji.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [families/han-ideographic-scripts.md](../wiki/families/han-ideographic-scripts.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [families/script-and-notation-proposals.md](../wiki/families/script-and-notation-proposals.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [families/text-model-and-core-specification.md](../wiki/families/text-model-and-core-specification.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [meetings/irg/irg-meeting-1.md](../wiki/meetings/irg/irg-meeting-1.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [meetings/irg/irg-meeting-2.md](../wiki/meetings/irg/irg-meeting-2.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [meetings/irg/irg-meeting-3.md](../wiki/meetings/irg/irg-meeting-3.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [meetings/irg/irg-meeting-4.md](../wiki/meetings/irg/irg-meeting-4.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [meetings/irg/irg-meeting-5.md](../wiki/meetings/irg/irg-meeting-5.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [meetings/irg/irg-meeting-6.md](../wiki/meetings/irg/irg-meeting-6.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [meetings/irg/irg-meeting-66.md](../wiki/meetings/irg/irg-meeting-66.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [meetings/irg/irg-meeting-67.md](../wiki/meetings/irg/irg-meeting-67.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [meetings/irg/irg-meeting-7.md](../wiki/meetings/irg/irg-meeting-7.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [meetings/utc/utc-meeting-187.md](../wiki/meetings/utc/utc-meeting-187.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [meetings/utc/utc-meeting-188.md](../wiki/meetings/utc/utc-meeting-188.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [meetings/utc/utc-meeting-189.md](../wiki/meetings/utc/utc-meeting-189.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [meetings/wg2/wg2-meeting-72.md](../wiki/meetings/wg2/wg2-meeting-72.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [meetings/wg2/wg2-meeting-73.md](../wiki/meetings/wg2/wg2-meeting-73.md) | 移行・整理 | 決定文書への案内を本文に残し、catalog での取得準備状況を移す。 / 文書の存在と役割は本文に残す。未掲載の観測・確認作業は概要近接ノートに集約済み。 |
| [people/china.md](../wiki/people/china.md) | 移行・整理 | source-owner feedback の役割は本文に残し、会合決定の調査状況を同じ表セル内へ移す。 |
| [people/japan.md](../wiki/people/japan.md) | 移行・整理 | 参加再開という報告内容は残し、担当範囲の調査状況を移す。 |
| [people/kim-kyongsok.md](../wiki/people/kim-kyongsok.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [people/suzuki-toshiya.md](../wiki/people/suzuki-toshiya.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [topics/arabic-mark-rendering.md](../wiki/topics/arabic-mark-rendering.md) | 本文に残す | 技術用語・property 名・符号化モデルの説明。canonical / alias 等の検索一致であり編集メモではない。 |
| [topics/cjk-abbreviated-and-simplified-ideographs.md](../wiki/topics/cjk-abbreviated-and-simplified-ideographs.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [topics/cjk-horizontal-extensions.md](../wiki/topics/cjk-horizontal-extensions.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [topics/cjk-multi-syllabic-and-abbreviation-characters.md](../wiki/topics/cjk-multi-syllabic-and-abbreviation-characters.md) | 移行・整理 | subtopic としての位置づけは概要に既述。ページの維持・分離予定を移す。 |
| [topics/cjk-strokes-variation-sequences.md](../wiki/topics/cjk-strokes-variation-sequences.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [topics/cjkv-components.md](../wiki/topics/cjkv-components.md) | 移行・整理 | 由来・日付の制約は本文に残し、独立ページを作らない編集判断を移す。 |
| [topics/dai-xaau-script.md](../wiki/topics/dai-xaau-script.md) | 本文に残す | 各版で repertoire が異なるという資料自身の差異。 |
| [topics/early-irg-history.md](../wiki/topics/early-irg-history.md) | 移行・整理 | 精読完了の作業記録を読者向けの対象範囲の説明へ整理する。 / 未精読という編集作業の状況を移す。catalog の登録内容と歴史的な比較の限界は残す。 |
| [topics/east-asian-spacing.md](../wiki/topics/east-asian-spacing.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [topics/egyptian-hieroglyph-data-and-unikemet.md](../wiki/topics/egyptian-hieroglyph-data-and-unikemet.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [topics/emoji-repertoire-proposals.md](../wiki/topics/emoji-repertoire-proposals.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [topics/g-source-glyph-and-reference-issues.md](../wiki/topics/g-source-glyph-and-reference-issues.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [topics/ideographic-variation-database.md](../wiki/topics/ideographic-variation-database.md) | 本文に残す | 技術用語・property 名・符号化モデルの説明。canonical / alias 等の検索一致であり編集メモではない。 |
| [topics/irg-disunified-ideographs.md](../wiki/topics/irg-disunified-ideographs.md) | 本文に残す | 公式 web page の Pending / Implemented 区分と、body・release を分ける読み方。 |
| [topics/irg-indexing-rules.md](../wiki/topics/irg-indexing-rules.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [topics/irg-urgently-needed-ideographs.md](../wiki/topics/irg-urgently-needed-ideographs.md) | 移行・整理 | 表の討議完了という記録は本文に残し、正式採択の調査状況を同じセル内の近接ノートへ移す。 |
| [topics/irg-working-process-and-liaison.md](../wiki/topics/irg-working-process-and-liaison.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [topics/iso-10646-edition-and-code-charts.md](../wiki/topics/iso-10646-edition-and-code-charts.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [topics/j-source.md](../wiki/topics/j-source.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [topics/japanese-historical-ideographs.md](../wiki/topics/japanese-historical-ideographs.md) | 移行・整理 | 採否・反映の調査予定であり、一次文書が記録する結論とは分ける。 / minutes の範囲は本文に残し、pending という編集上の仮分類を移す。 |
| [topics/japanese-place-name-ideographs.md](../wiki/topics/japanese-place-name-ideographs.md) | 移行・整理 | 採否・反映の調査予定であり、一次文書が記録する結論とは分ける。 / 未確認を pending と分類した編集判断を移す。UTC #187 の decision set に含まれない事実は本文に残す。 |
| [topics/jmj-horizontal-extension-review-path.md](../wiki/topics/jmj-horizontal-extension-review-path.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [topics/kana.md](../wiki/topics/kana.md) | 移行・整理 | 関連する表記体系は本文に残し、将来のページ分割案を移す。 |
| [topics/kore-sebeli-script.md](../wiki/topics/kore-sebeli-script.md) | 本文に残す | 技術用語・property 名・符号化モデルの説明。canonical / alias 等の検索一致であり編集メモではない。 |
| [topics/kzvariant.md](../wiki/topics/kzvariant.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [topics/leibnizian-and-historic-mathematical-symbols.md](../wiki/topics/leibnizian-and-historic-mathematical-symbols.md) | 移行・整理 | 完了した照合作業の記録を削除し、SEW の勧告と RMG の収録提案は本文に残す。 |
| [topics/mathematical-text-support.md](../wiki/topics/mathematical-text-support.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [topics/maya-hieroglyph-encoding.md](../wiki/topics/maya-hieroglyph-encoding.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [topics/nti-script.md](../wiki/topics/nti-script.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [topics/script-encoding-pipeline.md](../wiki/topics/script-encoding-pipeline.md) | 本文に残す | 一次資料の記載内容、文書の役割、決定主体・時点の違い、または解釈上の注意。読者に必要な本文。 |
| [topics/t-source-representative-glyph-issues.md](../wiki/topics/t-source-representative-glyph-issues.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [topics/uax45-u-source-ideographs.md](../wiki/topics/uax45-u-source-ideographs.md) | 移行・整理 | 受理された decision set の範囲は本文に残し、catalog / cache による未確認・仮分類を移す。 |
| [topics/uax60-large-east-asian-scripts.md](../wiki/topics/uax60-large-east-asian-scripts.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |
| [topics/ucv-nucv-lists.md](../wiki/topics/ucv-nucv-lists.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [topics/unicode-18-change-sources.md](../wiki/topics/unicode-18-change-sources.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [topics/unicode-properties-and-algorithms.md](../wiki/topics/unicode-properties-and-algorithms.md) | 本文に残す | 技術用語・property 名・符号化モデルの説明。canonical / alias 等の検索一致であり編集メモではない。 |
| [topics/unicode-release-coordination-and-publication.md](../wiki/topics/unicode-release-coordination-and-publication.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [topics/unicode-set-notation.md](../wiki/topics/unicode-set-notation.md) | 本文に残す | 一次資料の記載内容、文書の役割、決定主体・時点の違い、または解釈上の注意。読者に必要な本文。 |
| [topics/unihan-data-format-and-property-syntax.md](../wiki/topics/unihan-data-format-and-property-syntax.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [topics/unihan-database-maintenance.md](../wiki/topics/unihan-database-maintenance.md) | 本文に残す | 記事の対象範囲と関連 topic / event / 文書への読者向け案内。 |
| [topics/v-source-representative-glyph-issues.md](../wiki/topics/v-source-representative-glyph-issues.md) | 本文に残す | 補足検索の候補を周辺文脈と照合。一次資料の内容、読者向け案内・解釈限界を本文に残す。 |

ノート本文への分類・ID・日付の一律追加は要求しない。この台帳は移行作業の管理用であり、通常の執筆方法を制約しない。
