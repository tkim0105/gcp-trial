import logging
import os

from google.cloud import storage as gcs

logging.basicConfig(level=logging.INFO)


def hello_world(request):
    """
    Cloud Function that reads a file from Google Cloud Storage and returns its content.
    
    Args:
        request: HTTP request object
        
    Returns:
        The content of the file as a string
    """
    bucket_name = os.environ.get("BUCKET_NAME")
    file_name = os.environ.get("FILE_NAME", "sample.txt")

    logging.info("Devin demo: Start reading file: %s from bucket: %s", file_name, bucket_name)

    client = gcs.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    content = blob.download_as_text()

    logging.info("Devin demo: File content: %s", content)

    return content
