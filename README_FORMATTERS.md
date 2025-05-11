# Python コードフォーマッター

このリポジトリでは、以下のPythonコードフォーマッターとリンターを使用しています：

- [Black](https://black.readthedocs.io/en/stable/) - コードフォーマッター
- [Flake8](https://flake8.pycqa.org/en/latest/) - リンター
- [isort](https://pycqa.github.io/isort/) - インポート文の整理

## セットアップ

開発環境にフォーマッターをインストールするには：

```bash
pip install -r requirements-dev.txt
```

## pre-commitフックのインストール

コミット前に自動的にフォーマットを適用するには：

```bash
pre-commit install
```

## 手動実行

各ツールを手動で実行するには：

```bash
# コード全体をフォーマット
black .

# インポート文を整理
isort .

# リンターでコードをチェック
flake8
```

## 設定ファイル

- `pyproject.toml` - BlackとisortのConfiguration
- `.flake8` - Flake8のConfiguration
- `.pre-commit-config.yaml` - pre-commitフックの設定
