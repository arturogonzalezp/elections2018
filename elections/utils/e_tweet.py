# coding=utf-8
import json
import nltk
import re
import emoji

class ElectionsTweet:
    def __init__(self, db_id, raw_tweet, created_at):
        self.db_id = db_id
        self.info = json.loads(raw_tweet)
        self.text = self.info['text']
        self.created_at = created_at
        self.sentiment = 0.5
        self.clean_text = self.info['text']
    
    def clean_main_text(self):
        self.clean_text = ElectionsTweet.remove_usernames(self)
    
    @staticmethod
    def remove_usernames(tweet):
        text = re.sub(r'(\A|\s)@(\w+)','',tweet.clean_text)
        return text.strip()

    @staticmethod
    def get_emojis(text):
        emojis_list = map(lambda x: ''.join(x.split()), emoji.UNICODE_EMOJI.keys())
        r = re.compile('|'.join(re.escape(p) for p in emojis_list))
        return list(set(r.findall(text)))

    @staticmethod
    def get_sentiment(text):
        return 1.0