from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
try:
    import json
except ImportError:
    import simplejson as json
    
# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = '927683752532365313-tBAFC5zBzRpG7PcF8K9Hq9fPltGLyhe'
ACCESS_SECRET = '4fHIQYa3CMOAJJqt4HqjQamVoJu4LvZWha3x8KczLCb1x'
CONSUMER_KEY = 'pIboRFJU8EN17UVyis1qCuOtS'
CONSUMER_SECRET = '52XINB2kmqBPdlNv1WCHreoJI9vpmBtyfqywBnSFUQnbrMUmFO'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter API
twitter_api = Twitter(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_api.statuses.user_timeline(count =1, screen_name='tanmaygore_03')


global data_dict
tweet_count = 1
data_dict = {}
data_dict["tweetno"] = []

for tweet in iterator:
    if tweet.get("text") is None:
        #print "skipped a tweet"
        continue

    tweet_count -= 1
    data_dict["tweetno"].append(tweet)
    print tweet.get("text")

    if tweet_count <= 0:
        break

global new_tweets
new_tweets = data_dict['tweetno']
