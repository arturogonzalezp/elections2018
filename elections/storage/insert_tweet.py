import pymysql
import tweepy
from open_connection import Connection

def insert(buffer):
    db = Connection()
    conn = db.connect()
    cur = conn.cursor()
    for x in buffer:
        string = "(" + x.text + ")"
        encoded = string.encode('utf-8', 'ignore')
        final = encoded.replace('\n', '')
        cur.execute("INSERT INTO raw_tweets (tweet) VALUES ('" + final + "')")
    cur.close()
    conn.close()
        