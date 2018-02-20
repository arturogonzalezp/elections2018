# coding=utf-8
from __future__ import unicode_literals
from elections.storage.connection import Connection
from elections.utils.e_tweet import ElectionsTweet

db = Connection()
db.cursor.execute('SELECT * FROM MinedData')
result = db.cursor.fetchall()
for row in result:
    tweet = ElectionsTweet(row[0],row[1],row[2])
    # Clean tweet
    tweet.clean_main_text()
    tweet.sentiment = ElectionsTweet.get_sentiment(tweet.clean_text)
    tweet.emojis = ElectionsTweet.get_emojis(tweet.clean_text)
    print ('@' + tweet.info['user']['screen_name'] + ' tweeted:\n' + tweet.clean_text)
    print ('Emojis: [ ' + ' , '.join(tweet.emojis) + ' ]')
    print ('Sentiment: ' + str(tweet.sentiment))
    print ('*********************************************\n')
db.cursor.close()
db.connection.close()
    