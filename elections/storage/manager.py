import json
from elections.storage.connection import Connection
FILE_NAME = "local-storage.json"

class Manager:
    def __init__(self,buffer_size, candidate_username):
        self.candidate_username = candidate_username
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
                print ('Saved in dev mode for candidate: ' + self.candidate_username)
            self.buffer = []
    def save_local(self):
        temp_buffer = []
        for tweet in self.buffer:
            temp_buffer.append(tweet._json)
        Connection.write_to_file(self.candidate_username + '-' + FILE_NAME, self.tweets_to_json(temp_buffer))
    def save(self):
        db = Connection()
        for tweet in self.buffer:
            tweet_str = self.tweet_to_json(tweet).encode('string_escape')
            db.cursor.execute("INSERT INTO MinedData (raw_tweet,candidate_username) VALUES ('" + tweet_str + "','" + self.candidate_username + "')")
        db.cursor.close()
        db.connection.close()
    def tweet_to_json(self,tweet):
        return json.dumps(tweet._json)
    
    def tweets_to_json(self,tweets):
        return json.dumps(tweets)