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
    @staticmethod
    def insert_wordcloud(word_clouds):
        if(Connection.mode == 'PROD'):
            db = Connection()
            for candidate_username,word_cloud in word_clouds.items():
                db.cursor.execute("UPDATE Politician SET politician_json = '" + json.dumps(word_cloud) + "' WHERE Politician.username = '" + candidate_username[1:] + "'")
            print('Saved in db')
            db.cursor.close()
            db.connection.close()
        elif(Connection.mode == 'DEV'):
            for user,word_cloud in word_clouds.items():
                print(user + ': ')
                for word,count in word_cloud.items():
                    print(word,count)
    @staticmethod
    def get_all_mined_tweets():
        db = Connection()
        db.cursor.execute('SELECT * FROM MinedData')
        db_tweets = db.cursor.fetchall()
        db.cursor.close()
        db.connection.close()
        return db_tweets
    @staticmethod
    def insert_analyzed_tweet(tweet):
        db = Connection()
        raw_tweet = json.dumps(tweet.info)
        candidate_id = 0
        if(tweet.candidate_username == 'lopezobrador_'):
            candidate_id = 3
        elif(tweet.candidate_username == 'RicardoAnayaC'):
            candidate_id = 1
        elif(tweet.candidate_username == 'JoseAMeadeK'):
            candidate_id = 2
        elif(tweet.candidate_username == 'Mzavalagc'):
            candidate_id = 4
        elif(tweet.candidate_username == 'JaimeRdzNL'):
            candidate_id = 5

        db.cursor.execute("INSERT INTO `Tweet` (`sentiment`, `sentiment_percentage`,`raw_tweet`,`politician_id`) VALUES (%s, %s,%s,%s)", (tweet.overall_status,str(tweet.sentiment), json.dumps(tweet.info),str(candidate_id)))
        db.cursor.execute("DELETE FROM `MinedData` WHERE id=%s", (str(tweet.db_id)))

        if(tweet.overall_status == 'Positive'):
            db.cursor.execute('UPDATE Politician SET politician_pts=politician_pts+1 WHERE id=' + str(candidate_id))
        if(tweet.overall_status == 'Negative'):
            db.cursor.execute('UPDATE Politician SET politician_nts=politician_nts+1 WHERE id=' + str(candidate_id))
        if(tweet.overall_status == 'Neutral'):
            db.cursor.execute('UPDATE Politician SET politician_na=politician_na+1 WHERE id=' + str(candidate_id))
        db.cursor.close()
        db.connection.close()