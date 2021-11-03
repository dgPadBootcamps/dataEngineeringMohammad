import twitter as tw
import csv

item = tw.TwitterSearchScraper("corona lebanon", False)

tweets = []  # the list of the data

for i, tweet in enumerate(item.get_items()):
    if i > 10:
        break

    tweets.append([tweet.id, tweet.user.username, tweet.content, tweet.likeCount])  # the props of the data I need

header = [' TweetId', 'UserName', 'Content', 'LikesNumber']  # The header of the data props

# open the file in the write mode
with open('CoronaLebanon.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)  # the csv writer

    # write the header
    writer.writerow(header)
    # write the fetched data
    writer.writerows(tweets)
