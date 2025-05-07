# pylint: disable=missing-docstring
import logging
import os

from google.cloud import storage as gcs

logging.basicConfig(level=logging.INFO)


def hello_world(request):
    bucket_name = os.environ.get("BUCKET_NAME")
    file_name = os.environ.get("FILE_NAME", "sample.txt")

    logging.info("Start reading file: %s from bucket: %s", file_name, bucket_name)

    client = gcs.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    content = blob.download_as_text()

    logging.info("File content: %s", content)

    return content
