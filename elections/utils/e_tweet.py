# coding=utf-8
import json
import nltk
import re
import emoji
from elections.storage.connection import Connection
from string import punctuation
from elections.utils.sentiment_analyzer import SentimentAnalyzer

sentiment_analyzer = SentimentAnalyzer()
upperbound = 0.7
lowerbound = 0.3

class ElectionsTweet:
    def __init__(self, db_id, raw_tweet, created_at, candidate_username):
        self.db_id = db_id
        self.info = json.loads(raw_tweet)
        self.created_at = created_at
        self.sentiment = 0.5
        self.clean_text = self.get_text()
        self.candidate_username = candidate_username
    
    def get_text(self):
        if self.info['truncated']:
            return self.info['extended_tweet']['full_text']
        else:
            return self.info['text']

    def clean_main_text(self):
        self.clean_text = ElectionsTweet.remove_urls(self.clean_text)
        self.clean_text = ElectionsTweet.remove_usernames(self.clean_text)
        self.clean_text = ElectionsTweet.remove_emojis(self.clean_text)
        self.clean_text = ElectionsTweet.remove_hashtags(self.clean_text)

    @staticmethod
    def remove_hashtags(text):
        for hashtag in ElectionsTweet.get_hashtags(text):
            text = text.replace('#' + hashtag,'')
        return text

    @staticmethod
    def remove_emojis(text):
        for e in ElectionsTweet.get_emojis(text):
            text = text.replace(e,'')
        return text

    @staticmethod
    def remove_urls(text):
        return re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', text)

    @staticmethod
    def remove_usernames(text):
        text = re.sub(r'(\A|\s)@(\w+)','',text)
        return text.strip()
    
    @staticmethod
    def remove_punctuations(text):
        return ''.join(c for c in text if c not in punctuation)

    @staticmethod
    def get_emojis(text):
        emojis_list = map(lambda x: ''.join(x.split()), emoji.UNICODE_EMOJI.keys())
        r = re.compile('|'.join(re.escape(p) for p in emojis_list))
        return list(set(r.findall(text)))

    @staticmethod
    def get_hashtags(text):
        return re.findall(r'#(\w+)', text)

    @staticmethod
    def get_sentiment(text):
        return sentiment_analyzer.analyze_sentiment(text)

    @staticmethod
    def get_emoji_sentiment(emoji_list):
        emojis = json.load(open('elections/files/emoji-sentiment-list.json'))
        emojiSentiment = 0
        for e in emojis:
            emojiCode = e['sequence']

            if (len(emojiCode) == 4):
                emojiCode = '\U0000'+emojiCode
            else:
                emojiCode = '\U000'+emojiCode

            emojiDecoded = emojiCode.decode('unicode-escape')
            if(emojiDecoded in emoji_list):
                emojiSentiment = emojiSentiment + e['sentiment']
            
            emojiSentiment = emojiSentiment / max(len(emoji_list), 1)
            
        return emojiSentiment
    @staticmethod
    def get_tweet_status(sentiment):
        if(sentiment >= upperbound):
            return 'Positive'
        elif(sentiment <= lowerbound):
            return 'Negative'
        else:
            return 'Neutral'  