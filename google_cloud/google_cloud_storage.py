from google_cloud.constants import BUCKET_NAME, STORAGE_CLIENT

bucket = STORAGE_CLIENT.create_bucket(BUCKET_NAME)

print("Bucket {} created.".format(bucket.name))
