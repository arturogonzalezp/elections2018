import tweepy
import os
from elections.storage.manager import Manager
TWEET_BUFFER_SIZE = int(os.environ.get('TWEET_BUFFER_SIZE'))

class TweetsStreamer(tweepy.StreamListener):
    def set_candidate(self, candidate_username):
        self.candidate_username = candidate_username
    def on_connect(self):
        # Called once connected to streaming server
        print ('Connected to streamer')
        self.manager = Manager(TWEET_BUFFER_SIZE,self.candidate_username)
        self.tweet_counter = 0
    def keep_alive(self):
        # Called when a keep-alive arrived
        print ('Keep Alive function')
    def on_status(self, status):
        # Called when a new status arrives
        if not status.retweeted and 'RT @' not in status.text and status.lang == 'es':
            self.tweet_counter += 1
            #print ('Tweet (' + str(self.tweet_counter) + ') by: @' + status.user.screen_name + ': ' + status.text)
            print ('Tweet (' + str(self.tweet_counter) + ') by: @' + status.user.screen_name)
            self.manager.insert_tweet(status)
    def on_exception(self, exception):
        # Called when an unhandled exception occurs.
        print ('On Exception')
    def on_delete(self, status_id, user_id):
        # Called when a delete notice arrives for a status
        print ('On Delete')
    def on_event(self, status):
        # Called when a new event arrives
        print ('On Event')
    def on_direct_message(self, status):
        # Called when a new direct message arrives
        print ('On Direct Message')
    def on_friends(self, friends):
        # Called when a friends list arrives
        print ('On Friends')
    def on_limit(self, track):
        # Called when a limitation notice arrives
        print ('On Limit')
    def on_error(self, status_code):
        # Called when a non-200 status code is returned
        print ('On Error')
    def on_timeout(self):
        # Called when stream connection times out
        print ('On Timeout')
    def on_disconnect(self, notice):
        # Called when twitter sends a disconnect notice
        print ('On Disconnect')
    def on_warning(self, notice):
        #Called when a disconnection warning message arrives
        print ('On Warning')