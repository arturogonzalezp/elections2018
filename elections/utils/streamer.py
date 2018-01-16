import tweepy
class TweetsStreamer(tweepy.StreamListener):
    counter = 0
    def on_status(self, status):
        self.counter += 1
        print(str(self.counter) + ") " + status.text)