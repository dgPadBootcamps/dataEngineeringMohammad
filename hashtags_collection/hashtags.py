import json
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

    top_hashtags = list(hashtags.items())
    for i in range(0, len(top_hashtags) - 1):
        for j in range(i + 1, len(top_hashtags)):
            if top_hashtags[i][1] < top_hashtags[j][1]:
                maximum = top_hashtags[i]
                top_hashtags[i] = top_hashtags[j]
                top_hashtags[j] = maximum
    hashtags = top_hashtags[:10]
    return hashtags


def save_hashtags():
    json_file = open("hashtags.json", "w", encoding='utf-8')
    tags = json.dumps(get_hashtags("lebanon OR لبنان"), indent=4, default=str, ensure_ascii=False)
    json_file.write(tags)


save_hashtags()
