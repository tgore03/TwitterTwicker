# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

def getTrainingSet():

    # Variables that contains the user credentials to access Twitter API 
    ACCESS_TOKEN = '927683752532365313-tBAFC5zBzRpG7PcF8K9Hq9fPltGLyhe'
    ACCESS_SECRET = '4fHIQYa3CMOAJJqt4HqjQamVoJu4LvZWha3x8KczLCb1x'
    CONSUMER_KEY = 'pIboRFJU8EN17UVyis1qCuOtS'
    CONSUMER_SECRET = '52XINB2kmqBPdlNv1WCHreoJI9vpmBtyfqywBnSFUQnbrMUmFO'

    oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

    # Initiate the connection to Twitter Streaming API
    twitter_stream = TwitterStream(auth=oauth)

    # Get a sample of the public data following through Twitter
    iterator = twitter_stream.statuses.filter(track="Google", language="en")

    # Print each tweet in the stream to the screen 
    # Here we set it to stop after getting 1000 tweets. 
    # You don't have to set it to stop, but can continue running 
    # the Twitter API to collect data for days or even longer. 
    tweet_count = 1000
    data = "{\n\"tweetno\": ["
    data_dict = {}
    data_dict["tweetno"] = []

    for tweet in iterator:
        #print tweet_count
        tweet_count -= 1
        # Twitter Python Tool wraps the data returned by Twitter 
        # as a TwitterDictResponse object.
        # We convert it back to the JSON format to print/score
        
        data_dict["tweetno"].append(tweet)
        
        # The command below will do pretty printing for JSON data, try it out
        # print json.dumps(tweet, indent=4)
           
        if tweet_count <= 0:
            break 
    #output data to file.
    with open('data.json', 'w') as outfile:
        json.dump(data_dict, outfile)

