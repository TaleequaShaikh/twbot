import tweepy
import time
consumer_key = 'PXRZkFBsot70MtByCe9lW'
consumer_secret = 'sp67sK8loc8QkdZmvM1636dd63TV3SBgk8MCvpDqpOUHeL'
key = '1429310907545387008-MRXkvMZ34wkHb8hB0n5dlJXeCJ'
secret = 'i2r9R4pDQRUYS0bMh6qF0FKpCB200dViC1EAt0cas'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)


FILE_NAME = 'Last_seen.txt' #this function will get the id from Last_seen.txt and print it
def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id
#id = read_last_seen(FILE_NAME)
#print(id)

def store_last_seen(FILE_NAME, last_seen_id): #this function will store the last_seen_id and overwrite all the content in last_seen.txt
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return
#store_last_seen(FILE_NAME, '1430383677758795777')        

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended') #Returns the 20 most recent mentions, including retweets.
    for tweet in reversed(tweets):
        if '#randomtweet' in tweet.full_text.lower():
            print("Replied To ID" + str(tweet.id) )
            api.update_status("@" + tweet.user.screen_name + " Good Luck For #100Rick&Morty!", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)

while True:
    reply()
    time.sleep(30)            
