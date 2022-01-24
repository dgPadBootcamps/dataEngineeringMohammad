from google.cloud import storage

STORAGE_CLIENT = storage.Client.from_service_account_json("../data-engineering-batch1-545fd8f0e73f.json")
# The name for the new bucket
BUCKET_NAME = "dgpad-mhmd-test"
