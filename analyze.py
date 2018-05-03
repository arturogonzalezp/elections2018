# coding=utf-8
from __future__ import unicode_literals
from elections.storage.connection import Connection
from elections.utils.e_tweet import ElectionsTweet
from elections.storage.manager import Manager

for row in Manager.get_all_mined_tweets():
    tweet = ElectionsTweet(row[0],row[1],row[2],row[3])
    # Clean tweet
    tweet.clean_main_text()
    tweet.emojis = ElectionsTweet.get_emojis(tweet.get_text())
    tweet.hashtags = ElectionsTweet.get_hashtags(tweet.get_text())
    tweet.sentiment = ElectionsTweet.get_sentiment(tweet.get_text())
    tweet.emojiSentiment = ElectionsTweet.get_emoji_sentiment(tweet.emojis)
    tweet.overall_status = ElectionsTweet.get_tweet_status(tweet.sentiment)
    print ('Original Tweet:\n@' + tweet.info['user']['screen_name'] + ': ' + tweet.get_text() + '\n')
    print ('Clean Tweet: \n@' + tweet.info['user']['screen_name'] + ': ' + tweet.clean_text + '\n')
    print ('Emojis: [ ' + ' , '.join(tweet.emojis) + ' ]')
    print ('Database ID: ' + str(tweet.db_id))
    print ('Hashtags: [ ' + ' , '.join(tweet.hashtags) + ' ]')
    print ('Sentiment: ' + str(tweet.sentiment))
    print ('Emoji Sentiment: ' + str(tweet.emojiSentiment))
    print ('Overall tweet status: ' + tweet.overall_status)
    print ('*********************************************\n')
    Manager.insert_analyzed_tweet(tweet)
    