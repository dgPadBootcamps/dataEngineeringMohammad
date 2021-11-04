import twitter as tw
import csv


def read_tweets(search):
    item = tw.TwitterSearchScraper(search, False)

    tweets = []  # the list of the data

    for i, tweet in enumerate(item.get_items()):
        if i > 10:
            break

        tweets.append({"id": tweet.id, "userName": tweet.user.username, "Tweet": tweet.content, "likes": tweet.likeCount})
    return tweets


def save_tweets(search):
    header = [' TweetId', 'UserName', 'Content', 'LikesNumber']  # The header of the data props

    # open the file in the write mode
    with open('CoronaLebanon.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)  # the csv writer

        # write the header
        writer.writerow(header)
        # write the fetched data
        writer.writerows(read_tweets(search))

        return "Saved"

