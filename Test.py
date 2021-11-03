import twitter as tw

item = tw.TwitterSearchScraper("corona lebanon", False)

tweets = []

for i, tweet in enumerate(item.get_items()):
    if i > 10:
        break

    tweets.append([tweet.id, tweet.user.username, tweet.content, tweet.likeCount])

print(tweets)
