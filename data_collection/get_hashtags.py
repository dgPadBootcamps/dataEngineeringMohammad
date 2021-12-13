import json
import operator
from data_collection.collection import search
from datetime import datetime, timedelta

today = datetime.utcnow().date()  # to concatenate in the file name the date of today
yesterday = today - timedelta(days=1)


def get_hashtags(word_search):
    tweets = search(word_search, yesterday, today)
    hashtags = {}
    for tweet in tweets:
        for hashtag in tweet['hashtags']:
            if hashtag in hashtags:
                hashtags[hashtag] = hashtags[hashtag] + 1
            else:
                hashtags[hashtag] = 1

    hashtags = sorted(hashtags.items(), key=operator.itemgetter(1), reverse=True)[:10]
    # top_hashtags = list(hashtags.items())
    # for i in range(0, 10 - 1):
    #     for j in range(i + 1, 10):
    #         if top_hashtags[i][1] < top_hashtags[j][1]:
    #             maximum = top_hashtags[i]
    #             top_hashtags[i] = top_hashtags[j]
    #             top_hashtags[j] = maximum
    #     hashtags = dict(top_hashtags)
    return hashtags


json_file = open("hashtags.json", "w", encoding='utf-8')  # encoding and decoding to get the text in arabic
tags = json.dumps(get_hashtags("lebanon OR لبنان"), indent=4, default=str, ensure_ascii=False)
json_file.write(tags)
