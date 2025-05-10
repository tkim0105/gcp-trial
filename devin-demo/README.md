# Devin Demo - GCP Cloud Functions + Pulumi

このプロジェクトは、Pulumi を使って GCP Cloud Functions と Cloud Storage バケットを IaC で構築し、バケット内のテキストファイルの内容を HTTP 経由で返すデモです。

## ディレクトリ構成

```
devin-demo/
├── __main__.py                # Pulumiインフラ定義（バケット・関数など）
├── function/
│   ├── main.py                # Cloud Functions本体（GCSからファイルを読む）
│   └── requirements.txt       # Cloud Functions用依存パッケージ
├── requirements.txt           # Pulumi用依存パッケージ
├── sample.txt                 # バケットにアップロードするテキストファイル
├── Pulumi.yaml                # Pulumiプロジェクト設定
├── Pulumi.dev.yaml            # Pulumiスタック設定（GCPプロジェクトIDなど）
└── README.md                  # このファイル
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
3. レスポンスとして `sample.txt` の内容が返れば成功
