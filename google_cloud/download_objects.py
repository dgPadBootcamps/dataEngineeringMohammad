from google_cloud.constants import STORAGE_CLIENT, BUCKET_NAME


def download_blob(bucket_name, source_blob_name):
    bucket = STORAGE_CLIENT.bucket(bucket_name)

    blob = bucket.blob(source_blob_name)
    json_str = blob.download_as_string()
    return json_str


#download_blob(BUCKET_NAME, "tweets-data/*")
