import json
import re
from elections.storage.connection import Connection
FILE_NAME = "local_storage.json"

class Manager:
    def __init__(self,buffer_size):
        self.buffer_size = buffer_size
        self.buffer = []
    def insert_tweet(self,tweet):
        self.buffer.append(tweet)
        if(self.buffer.__len__() == self.buffer_size):
            if(Connection.mode == 'PROD'):
                self.save()
            elif(Connection.mode == 'DEV'):
                self.save_local()
                print "saved"
            self.buffer = []
    def save_local(self):
        try:
            file = open(FILE_NAME, 'w')
        except IOError:
            print "Error opening file: " + FILE_NAME
        else:
            temp_buffer = []
            for tweet in self.buffer:
                temp_buffer.append(tweet._json)
            file.write(self.tweets_to_json(temp_buffer))
            file.close()
    def save(self):
        db = Connection()
        for tweet in self.buffer:
            tweet_str = re.escape(self.tweet_to_json(tweet))
            db.cursor.execute("INSERT INTO MinedData (raw_tweet, tweet_id) VALUES ('" + tweet_str + "', '" + tweet.id_str + "')")
        db.cursor.close()
        db.connection.close()
    def tweet_to_json(self,tweet):
        return json.dumps(tweet._json)
    
    def tweets_to_json(self,tweets):
        return json.dumps(tweets)