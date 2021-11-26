class Data:
    def __init__(self, item):
        self.id = item.id
        self.text = item.content
        self.date = item.date
        self.hashtags = item.hashtags if item.hashtags is not None else []
        self.mentions = item.mentionedUsers if item.mentionedUsers is not None else []
        self.username = item.user.username
        self.display_name = item.user.displayname
        self.user_description = item.user.description
        self.followers_count = item.user.followersCount
        self.following_count = item.user.friendsCount
        self.user_id = item.user.id
        self.websiteURL = item.user.linkUrl
        self.isVerified = item.user.verified
        self.statuses_count = item.user.statusesCount
        self.joined_date = item.user.created
        self.location = item.user.location
        self.isRetweet = (item.retweetedTweet is not None)
        self.retweet_count = item.retweetCount
        self.quote_count = item.quoteCount
        self.reply_count = item.replyCount
        self.language = item.lang
        self.has_media = (item.media is not None)
        self.favorite_count = item.likeCount
        self.tweet_location = item.place

    def data_list(self):
        tweets = ({
            "id": self.id,
            "Text": self.text,
            "tweet_date": self.date,
            "hashtags": self.hashtags,
            "mentions": self.mentions,
            "User": {"User_Id": self.user_id,
                     "UserName": self.username,
                     "display_name": self.display_name,
                     "description": self.user_description,
                     "followers_count": self.followers_count,
                     "following_count": self.following_count,
                     "WebsiteURL": self.websiteURL,
                     "is_Verified": self.isVerified,
                     "joined_date": self.joined_date,
                     "statuses_count": self.statuses_count,
                     "location": self.location},
            "is_retweet": self.isRetweet,
            "retweet_count": self.retweet_count,
            "quote_count": self.quote_count,
            "reply_count": self.reply_count,
            "language": self.language,
            "has_media": self.has_media,
            "favorite_count": self.favorite_count,
            "tweet_location": self.tweet_location})
        return tweets
