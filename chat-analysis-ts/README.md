# Chat Analysis System

Google Chat のメッセージを分析するためのシステムです。Cloud Functions、BigQuery、Looker Studio を組み合わせて、チャットメッセージの分析と可視化を実現します。

## プロジェクト構成

```
chat-analysis-ts/
├── function/                 # Cloud Functionsのソースコード
│   ├── src/                 # TypeScriptソース
│   ├── package.json         # 関数用の依存関係
│   └── tsconfig.json        # 関数用のTypeScript設定
├── index.ts                 # Pulumiのインフラストラクチャ定義
├── Pulumi.yaml             # Pulumiのプロジェクト設定
├── Pulumi.dev.yaml         # 開発環境用のPulumi設定
└── package.json            # プロジェクトの依存関係
```

## 前提条件

- Google Cloud Platform (GCP) アカウント
- GCP プロジェクト（`gcp-dev-trial`）
- Node.js 18 以上
- Pulumi CLI

## セットアップ

1. 依存関係のインストール

```bash
# プロジェクトの依存関係をインストール
npm install

# Cloud Functions用の依存関係をインストール
cd function
npm install
cd ..
```

2. Pulumi の初期化

```bash
# 開発用スタックの作成
pulumi stack init dev

# GCPプロジェクトの設定
pulumi config set gcp:project gcp-dev-trial
```

3. デプロイ

```bash
# Cloud Functionsのビルド
cd function
npm run build
cd ..

# インフラストラクチャのデプロイ
pulumi up
```

## 開発

### ローカルでのテスト

Cloud Functions をローカルでテストするには：

```bash
cd function
npm run dev
```

### デプロイ

変更をデプロイするには：

1. Cloud Functions のコードをビルド
2. Pulumi でデプロイ

```bash
cd function
npm run build
cd ..
pulumi up
```

## 環境変数

Cloud Functions は以下の環境変数を使用します：

- `NODE_ENV`: 実行環境（production/development）

## 注意事項

- このプロジェクトは東京リージョン（asia-northeast1）にデプロイされます
- Cloud Functions は公開アクセス可能に設定されています（本番環境では適切なアクセス制御を設定してください）

## 今後の開発予定

1. Google Chat API との連携
2. BigQuery へのデータ保存
3. Looker Studio での可視化
