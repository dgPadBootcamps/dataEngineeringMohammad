from data_collection.data import Data
from data_collection import twitter
from data_cleaning.clean import clean_data


def search(keyword, yesterday, today):
    tweets_list = []
    query = "(" + keyword + ")" + " since:" + str(yesterday) + " until:" + str(today)
    item = twitter.TwitterSearchScraper(query, False).get_items()
    for i, tweet in enumerate(item):
        tweet.content = clean_data(tweet.content)
        List = Data(tweet)
        tweets_list.append(List.data_list())
    return tweets_list
