"""JavaScript Cloud Functions用のPulumi設定ファイル
このファイルでは、GCPのCloud FunctionsとCloud Storageのリソースを定義します。
"""

import pulumi
from pulumi_gcp import cloudfunctions, storage

# Cloud Storageバケットの作成
# バケットは関数のソースコードとサンプルファイルを保存するために使用
bucket = storage.Bucket(
    "function-bucket", location="US", uniform_bucket_level_access=True
)

# 関数のソースコードをアップロード
# functionディレクトリ内のJavaScriptコードをZIPアーカイブとしてアップロード
source_archive = storage.BucketObject(
    "function-source", bucket=bucket.name, source=pulumi.FileArchive("function")
)

# Cloud Functionの作成
# Node.js 18ランタイムを使用し、HTTPトリガーで関数を実行可能に設定
function = cloudfunctions.Function(
    "js-hello-function",
    name="js-hello-function",
    runtime="nodejs18",  # Node.js 18ランタイムを使用
    source_archive_bucket=bucket.name,
    source_archive_object=source_archive.name,
    entry_point="helloWorld",  # JavaScriptの関数名（index.jsでエクスポートした関数名）
    trigger_http=True,  # HTTPトリガーを有効化
    region="asia-northeast1",  # 東京リージョンにデプロイ
    environment_variables={
        "BUCKET_NAME": bucket.name,  # バケット名を環境変数として設定
        "FILE_NAME": "sample.txt",  # 読み込むファイル名を環境変数として設定
    },
)

# 関数の実行権限を設定
# 全てのユーザーにCloud Functionsの実行権限を付与
invoker = cloudfunctions.FunctionIamMember(
    "js-hello-function-invoker",  # 名前も更新
    project=function.project,
    region=function.region,
    cloud_function=function.name,
    role="roles/cloudfunctions.invoker",
    member="allUsers",  # 全てのユーザーにアクセスを許可
)

# バケットにテキストファイルをアップロード
# 関数が読み込むサンプルテキストファイルをアップロード
text_object = storage.BucketObject(
    "sample-text",
    bucket=bucket.name,
    source=pulumi.FileAsset("sample.txt"),  # プロジェクト直下のsample.txtをアップロード
    name="sample.txt",
)

# 関数のURLを出力
# デプロイ後にこのURLで関数にアクセス可能
pulumi.export("function_url", function.https_trigger_url)
