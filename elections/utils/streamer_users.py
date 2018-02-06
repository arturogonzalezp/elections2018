import tweepy
from elections.storage.manager import Manager
from accounts import Accounts

class UserStreamer(tweepy.StreamListener):
    def on_connect(self):
        """Called once connected to streaming server"""
        print ('On Connect')
        self.manager = Manager(10)
        self.accounts = Accounts()
    
    def on_status(self, status):
        if(self.accounts.check_user(status.user.screen_name)):
            print ("@" + status.user.screen_name + ": " + status.text)