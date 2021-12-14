import tweepy

consumer_key = 'PXRZkFBsot70MtByCe9lWApif'
consumer_secret = 'sp67sK8loc8QkdZmvM1636dd63TV3SBgk8MCvpDqpOUHeL78Cp'
key = '1429310907545387008-MRXkvMZ34wkHb8hB0n5dlJXeCJmMW9'
secret = 'i2r9R4pDQRUYS0bMh6qF0FKpCB200dViC1EAt0casuWJs'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

hashtag = "MetGala"
tweetNumber = 3

tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

for tweet in tweets:
    tweet.retweet()
