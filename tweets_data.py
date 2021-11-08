import twitter as tw
import datetime

today = datetime.date.today()  # call the today date
yesterday = today - datetime.timedelta(days=1)  # call tomorrow date

item = tw.TwitterSearchScraper("(lebanon OR لبنان) since:" + str(yesterday) + "until:" + str(today), False)
# concatenate to give today and tomorrow values to the format
tweets = []


def read_tweets():  # a function return the data list
    for i, tweet in enumerate(item.get_items()):
        tweets.append({"TweetNumber": str(i + 1),
                       "id": str(tweet.id),
                       "Text": tweet.content,
                       "tweet_date": tweet.date,
                       "hashtags": tweet.hashtags if tweet.hashtags is not None else [],
                       "mentions": tweet.mentionedUsers if tweet.mentionedUsers is not None else [],
                       "User": {"User_Id": tweet.user.id,
                                "UserName": tweet.user.username,
                                "display_name": tweet.user.displayname,
                                "description": tweet.user.description,
                                "followers_count": tweet.user.followersCount,
                                "following_count": tweet.user.friendsCount,
                                "WebsiteURL": tweet.user.url,
                                "is_Verified": tweet.user.verified,
                                "joined_date": tweet.user.created.date(),
                                "statuses_count": tweet.user.statusesCount,
                                "location": tweet.user.location
                                },
                       "is_retweet": tweet.retweetedTweet,
                       "retweet_count": tweet.retweetCount,
                       "quote_count": tweet.quoteCount,
                       "reply_count": tweet.replyCount,
                       "language": tweet.lang,
                       "has_media": tweet.media,
                       "favorite_count": tweet.user.favouritesCount,
                       "tweet_location": tweet.place})

    return tweets
