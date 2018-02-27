# coding=utf-8
import tweepy
import os
from elections.storage.connection import Connection

FILE_NAME = "candidates.txt"
MAX_TWEETS = 200

class CandidatesConsumer():
    def __init__(self, twitter_api):
        self.twitter_api = twitter_api
        self.candidates = Connection.read_from_file(FILE_NAME)

    def get_all_tweets(self, candidate):
        all_tweets = []

        new_tweets = self.twitter_api.api.user_timeline(screen_name = candidate,count = MAX_TWEETS)
        all_tweets.extend(new_tweets)
        oldest_tweet = all_tweets[-1].id - 1
        
        while len(new_tweets) > 0:
        
            new_tweets = self.twitter_api.api.user_timeline(screen_name = candidate,count=MAX_TWEETS, max_id=oldest_tweet)

            all_tweets.extend(new_tweets)
            
            oldest_tweet = all_tweets[-1].id - 1

        return all_tweets