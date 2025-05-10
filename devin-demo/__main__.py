"""A Python Pulumi program for Devin demo"""

import pulumi
from pulumi_gcp import cloudfunctions, storage

bucket = storage.Bucket(
    "devin-function-bucket", location="asia-northeast1", uniform_bucket_level_access=True
)

source_archive = storage.BucketObject(
    "devin-function-source", bucket=bucket.name, source=pulumi.FileArchive("function")
)

function = cloudfunctions.Function(
    "devin-hello-function",  # 関数名を明示的に設定
    name="devin-hello-function",
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
    "devin-function-invoker",
    project=function.project,
    region=function.region,
    cloud_function=function.name,
    role="roles/cloudfunctions.invoker",
    member="user:t-kim@ssmarket.co.jp",
)

text_object = storage.BucketObject(
    "devin-sample-text",
    bucket=bucket.name,
    source=pulumi.FileAsset("sample.txt"),
    name="sample.txt",
)

pulumi.export("function_url", function.https_trigger_url)
