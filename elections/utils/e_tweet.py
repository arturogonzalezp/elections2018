# coding=utf-8
import json
import nltk
import re
import emoji

class ElectionsTweet:
    def __init__(self, db_id, raw_tweet, created_at):
        self.db_id = db_id
        self.info = json.loads(raw_tweet)
        self.created_at = created_at
        self.sentiment = 0.5
        self.clean_text = self.get_text()
    
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
    def get_emojis(text):
        emojis_list = map(lambda x: ''.join(x.split()), emoji.UNICODE_EMOJI.keys())
        r = re.compile('|'.join(re.escape(p) for p in emojis_list))
        return list(set(r.findall(text)))

    @staticmethod
    def get_hashtags(text):
        return re.findall(r'#(\w+)', text)

    @staticmethod
    def get_sentiment(text):
        return 1.0