# pylint: disable=missing-docstring
import os

from google.cloud import storage as gcs


def hello_world(request):
    bucket_name = os.environ.get("BUCKET_NAME")
    file_name = os.environ.get("FILE_NAME", "sample.txt")

    client = gcs.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    content = blob.download_as_text()

    return content
