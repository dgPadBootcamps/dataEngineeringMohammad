import re


def clean_data(tweet: str):
    clean_tweet = tweet.lower()
    clean_tweet = re.sub("#[0-9\u0621-\u063A\u0640-\u066C\u0671-\u0674a-zA-Z_]+", "", clean_tweet)
    clean_tweet = re.sub("#[A-Za-z0-9_]+", "", clean_tweet)
    clean_tweet = re.sub("@[A-Za-z0-9_]+", "", clean_tweet)
    clean_tweet = re.sub(r"http\S+", "", clean_tweet)
    clean_tweet = re.sub(r"www.\S+", "", clean_tweet)
    clean_tweet = clean_tweet.replace("\n", "")
    clean_tweet = clean_tweet.replace("/ ", "")
    clean_tweet = clean_tweet.replace(":", "")
    clean_tweet = clean_tweet.replace(".", "")
    clean_tweet = clean_tweet.replace("/", "")
    clean_tweet = clean_tweet.replace("•", "")
    clean_tweet = clean_tweet.replace(",", "")
    clean_tweet = clean_tweet.replace("'", "")
    clean_tweet = clean_tweet.replace('"', "")
    return clean_tweet
