from google_cloud.constants import STORAGE_CLIENT, BUCKET_NAME


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    bucket = STORAGE_CLIENT.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )


upload_blob(BUCKET_NAME, "C:/Users/MOHD/Documents/dgPad/dgPad2/data_saving/test", "tweets-data")
