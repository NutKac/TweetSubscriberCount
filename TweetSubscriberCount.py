import urllib
import json
from twython import Twython
import math

# Twitter keys
CONSUMER_KEY = 'redacted'
CONSUMER_SECRET = 'redacted'
ACCESS_KEY = 'redacted'
ACCESS_SECRET = 'redacted'

# The name of the channel
channel = 'CHANELNAME'

# Youtube API key
key = 'redacted'

# Subscriber goal
goal = 100000

# Subscriber goal in tweet
subgoal = '100K'

# Twitter username of youtube channel
twittername = '@NutKac'

data = urllib.urlopen('https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername='+channel+'&key='+key).read()
subs = json.loads(data)['items'][0]['statistics']['subscriberCount']
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
togoal = (goal - int(subs))

# Tweet
tweet = '.' + twittername + ' has ' + format(int(subs)) + ' subscribers. ' +  format(int(togoal)) + ' subscribers to ' + subgoal + '.'

api.update_status(status = tweet)
