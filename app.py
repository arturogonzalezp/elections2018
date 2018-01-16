from __future__ import unicode_literals
from elections.api.config import TwitterAPI
from elections.utils.streamer import TweetsStreamer
twitter_api = TwitterAPI()
tweets_streamer = TweetsStreamer()
myStream = twitter_api.tweepy.Stream(auth = twitter_api.api.auth, listener=tweets_streamer)
myStream.filter(track=['Elecciones'])
print "Working..."