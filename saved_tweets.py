import json
from tweets_data import read_tweets
import datetime

today = datetime.date.today()  # to concatenate in the file name the date of today

json_file = open("tweets_lebanon_" + str(today) + ".json", "w",
                 encoding='utf-8')  # encoding and decoding to get the text in arabic
tweets_print = json.dumps(read_tweets(), indent=4, default=str, ensure_ascii=False)
json_file.write(tweets_print)
json_file.close()
