import pymysql
from connection import Connection

class Manager:
    buffer_size = 10
    
    def insert_tweet(self, buffer):
        db = Connection()
        for tweet in buffer:
            string = "(" + tweet.text + ")".encode('utf-8').replace('\n','')
            db.cursor.execute("INSERT INTO mined_data (raw_tweet, tweet_id) VALUES ('" + string + "', '" + tweet.id_str + "')")
            
        db.cursor.close()
        db.connection.close()