import tweepy
from elections.storage.manager import Manager
BUFFER_SIZE = 20

class TweetsStreamer(tweepy.StreamListener):
    def on_connect(self):
        """Called once connected to streaming server"""
        print ('On Connect')
        self.manager = Manager(BUFFER_SIZE)
    def keep_alive(self):
        """Called when a keep-alive arrived"""
        print ('Keep Alive')
    def on_status(self, status):
        """Called when a new status arrives"""
        print ("Tweet by: @" + status.user.screen_name)
        self.manager.insert_tweet(status)
    def on_exception(self, exception):
        """Called when an unhandled exception occurs."""
        print ('On Exception')
    def on_delete(self, status_id, user_id):
        """Called when a delete notice arrives for a status"""
        print ('On Delete')
    def on_event(self, status):
        """Called when a new event arrives"""
        print ('On Event')
    def on_direct_message(self, status):
        """Called when a new direct message arrives"""
        print ('On Direct Message')
    def on_friends(self, friends):
        """Called when a friends list arrives"""
        print ('On Friends')
    def on_limit(self, track):
        """Called when a limitation notice arrives"""
        print ('On Limit')
    def on_error(self, status_code):
        """Called when a non-200 status code is returned"""
        print ('On Error')
    def on_timeout(self):
        """Called when stream connection times out"""
        print ('On Timeout')
    def on_disconnect(self, notice):
        """Called when twitter sends a disconnect notice"""
        print ('On Disconnect')
    def on_warning(self, notice):
        """Called when a disconnection warning message arrives"""
        print ('On Warning')