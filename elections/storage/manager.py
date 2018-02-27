import json
from elections.storage.connection import Connection
FILE_NAME = "local_storage.json"

class Manager:
    def __init__(self,buffer_size):
        self.buffer_size = buffer_size
        self.buffer = []
        print ('Manager created with a buffer size of ' + str(self.buffer_size) + " tweets")
    def insert_tweet(self,tweet):
        self.buffer.append(tweet)
        if(len(self.buffer) == self.buffer_size):
            if(Connection.mode == 'PROD'):
                self.save()
            elif(Connection.mode == 'DEV'):
                self.save_local()
                print ('Saved in dev mode')
            self.buffer = []
    def save_local(self):
        temp_buffer = []
        for tweet in self.buffer:
            temp_buffer.append(tweet._json)
        Connection.write_to_file(FILE_NAME, self.tweets_to_json(temp_buffer))
    def save(self):
        db = Connection()
        for tweet in self.buffer:
            tweet_str = self.tweet_to_json(tweet).encode('string_escape')
            db.cursor.execute("INSERT INTO MinedData (raw_tweet) VALUES ('" + tweet_str + "')")
        db.cursor.close()
        db.connection.close()
    def tweet_to_json(self,tweet):
        return json.dumps(tweet._json)
    
    def tweets_to_json(self,tweets):
        return json.dumps(tweets)