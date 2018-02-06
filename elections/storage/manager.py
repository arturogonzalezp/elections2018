import json
import re
from elections.storage.connection import Connection

class Manager:
    def __init__(self,buffer_size):
        self.buffer_size = buffer_size
        self.buffer = []
    def insert_tweet(self,tweet):
        self.buffer.append(tweet)
        if(self.buffer.__len__() == self.buffer_size):
            self.save()
            self.buffer = []

    def save(self):
        db = Connection()
        for tweet in self.buffer:
            tweet_str = re.escape(self.tweet_to_json(tweet))
            db.cursor.execute("INSERT INTO MinedData (raw_tweet, tweet_id) VALUES ('" + tweet_str + "', '" + tweet.id_str + "')")
        db.cursor.close()
        db.connection.close()
    def tweet_to_json(self,tweet):
        return json.dumps(tweet._json)