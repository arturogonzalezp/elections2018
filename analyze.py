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
    tweet.emojis = ElectionsTweet.get_emojis(tweet.get_text())
    tweet.hashtags = ElectionsTweet.get_hashtags(tweet.get_text())
    tweet.sentiment = ElectionsTweet.get_sentiment(tweet.clean_text)
    print ('Original Tweet:\n@' + tweet.info['user']['screen_name'] + ': ' + tweet.get_text() + '\n')
    print ('Clean Tweet: \n@' + tweet.info['user']['screen_name'] + ': ' + tweet.clean_text + '\n')
    print ('Emojis: [ ' + ' , '.join(tweet.emojis) + ' ]')
    print ('Database ID: ' + str(tweet.db_id))
    print ('Hashtags: [ ' + ' , '.join(tweet.hashtags) + ' ]')
    print ('Sentiment: ' + str(tweet.sentiment))
    print ('*********************************************\n')
db.cursor.close()
db.connection.close()
    