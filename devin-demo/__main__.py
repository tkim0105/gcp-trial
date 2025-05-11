"""A Python Pulumi program for Devin demo"""

import pulumi
from pulumi_gcp import cloudfunctions, storage

# ソースコードをアップロードするための一時的なバケット
bucket = storage.Bucket(
    "devin-function-bucket",
    location="asia-northeast1",
    uniform_bucket_level_access=True,
)

# 関数のソースコードをアップロード
source_archive = storage.BucketObject(
    "devin-function-source", bucket=bucket.name, source=pulumi.FileArchive("function")
)

# Cloud Functionのデプロイ
function = cloudfunctions.Function(
    "devin-hello-function",
    name="devin-hello-function",
    runtime="python39",
    source_archive_bucket=bucket.name,
    source_archive_object=source_archive.name,
    entry_point="hello_world",
    trigger_http=True,
    region="asia-northeast1",
)

# 関数の呼び出し権限を設定
invoker = cloudfunctions.FunctionIamMember(
    "devin-function-invoker",
    project=function.project,
    region=function.region,
    cloud_function=function.name,
    role="roles/cloudfunctions.invoker",
    member="allUsers",
)

pulumi.export("function_url", function.https_trigger_url)
