# GCP Cloud Functions + Pulumi サンプルプロジェクト

このプロジェクトは、Pulumi を使って GCP Cloud Functions と Cloud Storage バケットを IaC で構築し、バケット内のテキストファイルの内容を HTTP 経由で返すサンプルです。

## ディレクトリ構成

```
cloud-functions-demo/
├── __main__.py                # Pulumiインフラ定義（バケット・関数など）
├── function/
│   ├── main.py                # Cloud Functions本体（GCSからファイルを読む）
│   └── requirements.txt       # Cloud Functions用依存パッケージ
├── requirements.txt           # Pulumi用依存パッケージ
├── sample.txt                 # バケットにアップロードするテキストファイル
├── Pulumi.yaml                # Pulumiプロジェクト設定
├── Pulumi.dev.yaml            # Pulumiスタック設定（GCPプロジェクトIDなど）
└── venv/                      # Python仮想環境（Git管理対象外）
```

## セットアップ手順

1. 依存パッケージのインストール（ローカル開発用）
   ```bash
   pip install -r requirements.txt
   ```
2. Pulumi の GCP プロジェクト設定
   ```bash
   pulumi config set gcp:project [YOUR_PROJECT_ID]
   ```
3. Cloud Functions 用依存パッケージの確認
   - `function/requirements.txt` に `google-cloud-storage` が記載されていること

## デプロイ手順

```bash
pulumi up
```

- 内容を確認し、`yes` でデプロイ
- `--yes` オプションで確認を省略可能

## 動作確認

1. デプロイ後、出力された `function_url` を確認
2. 以下のコマンドで Cloud Function を実行
   ```bash
   curl "[function_url]"
   # 認証が必要な場合
   ID_TOKEN=$(gcloud auth print-identity-token)
   curl -H "Authorization: Bearer ${ID_TOKEN}" "[function_url]"
   ```
3. レスポンスとして `sample.txt` の内容（例: `Hello from GCP Cloud Storage!`）が返れば成功

## 補足

- バケット名やファイル名は `__main__.py` の環境変数で指定
- IAM 権限の設定により、関数の公開範囲を柔軟に変更可能
- venv/ ディレクトリは Git 管理対象外

---

Pulumi と GCP Cloud Functions の連携や、Cloud Storage 連携の学習・検証用にご活用ください。
