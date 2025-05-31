"""A Python Pulumi program"""

import pulumi
from pulumi_gcp import cloudfunctions, storage

# Cloud Storageバケットの作成
bucket = storage.Bucket(
    "function-bucket", location="US", uniform_bucket_level_access=True
)

# 関数のソースコードをアップロード
source_archive = storage.BucketObject(
    "function-source", bucket=bucket.name, source=pulumi.FileArchive("function")
)

# Cloud Functionの作成
function = cloudfunctions.Function(
    "hello-function",  # 関数名を明示的に設定
    name="hello-function",
    runtime="python39",
    source_archive_bucket=bucket.name,
    source_archive_object=source_archive.name,
    entry_point="hello_world",
    trigger_http=True,
    region="asia-northeast1",
    environment_variables={
        "BUCKET_NAME": bucket.name,
        "FILE_NAME": "sample.txt",
    },
)

invoker = cloudfunctions.FunctionIamMember(
    "hello-function-invoker",
    project=function.project,
    region=function.region,
    cloud_function=function.name,
    role="roles/cloudfunctions.invoker",  # どんな権限を与えるか
    member="user:t-kim@ssmarket.co.jp",

)

# バケットにテキストファイルをアップロード
text_object = storage.BucketObject(
    "sample-text",
    bucket=bucket.name,
    source=pulumi.FileAsset("sample.txt"),  # プロジェクト直下にsample.txtを用意
    name="sample.txt",
)

# 関数のURLを出力
pulumi.export("function_url", function.https_trigger_url)
