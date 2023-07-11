import json
from data_collection.collection import search
from datetime import datetime, timedelta

today = datetime.utcnow().date()  # to concatenate in the file name the date of today
yesterday = today - timedelta(days=1)

json_file = open("tweets_lebanon_" + str(yesterday) + ".json", "w",
                 encoding='utf-8')  # encoding and decoding to get the text in arabic
tweets_print = json.dumps(search("lebanon OR لبنان", yesterday, today), indent=4, default=str, ensure_ascii=False)
json_file.write(tweets_print)
