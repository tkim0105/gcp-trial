# JavaScript Cloud Functions Demo

このプロジェクトは、Google Cloud Functions を JavaScript で実装し、Pulumi を使用してデプロイするデモプロジェクトです。

## プロジェクト構成

```
cloud-functions-demo-js/
├── function/                 # Cloud Functionsのソースコード
│   ├── index.js             # メインの関数実装
│   └── package.json         # Node.js依存関係の定義
├── __main__.py             # Pulumiのインフラストラクチャ定義
├── Pulumi.yaml             # Pulumiのプロジェクト設定
├── Pulumi.dev.yaml         # 開発環境用のPulumi設定
├── requirements.txt        # Python依存関係の定義
└── sample.txt             # テスト用のサンプルファイル
```

## 機能

- Cloud Storage バケットからファイルを読み取り
- HTTP エンドポイントとして公開
- ファイルの内容をレスポンスとして返す

## 前提条件

- Google Cloud Platform (GCP) アカウント
- GCP プロジェクト（`gcp-dev-trial`）
- Node.js 18 以上
- Python 3.9 以上
- Pulumi CLI

## セットアップ

1. 依存関係のインストール

```bash
# Python依存関係のインストール
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Node.js依存関係のインストール
cd function
npm install
cd ..
```

2. Pulumi の初期化

```bash
pulumi stack init dev
```

3. デプロイ

```bash
pulumi up
```

## 使用方法

デプロイ後、以下の URL で関数にアクセスできます：

```
https://asia-northeast1-gcp-dev-trial.cloudfunctions.net/js-hello-function
```

関数は以下の動作を行います：

1. Cloud Storage バケットから`sample.txt`ファイルを読み取り
2. ファイルの内容をレスポンスとして返す

## 環境変数

関数は以下の環境変数を使用します：

- `BUCKET_NAME`: ファイルを格納する Cloud Storage バケット名
- `FILE_NAME`: 読み込むファイル名（デフォルト: `sample.txt`）

## 注意事項

- このデモでは、関数へのアクセスを`allUsers`に許可しています（本番環境では適切なアクセス制御を設定してください）
- 東京リージョン（asia-northeast1）にデプロイされます
