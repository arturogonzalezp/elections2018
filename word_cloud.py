# coding=utf-8
from elections.utils.candidates_consumer import CandidatesConsumer
from elections.utils.e_tweet import ElectionsTweet
from elections.api.config import TwitterAPI
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import unicodedata
from collections import Counter

nltk.download('stopwords')
nltk.download('punkt')

twitter_api = TwitterAPI()

stop_words = set(stopwords.words('spanish'))

counter = 0

consumer = CandidatesConsumer(twitter_api)

def delete_stopwords(candidate_tweets):
    for tweet in candidate_tweets:
        clean_tweet_text = ElectionsTweet.remove_emojis(tweet.text)
        clean_tweet_text = ElectionsTweet.remove_usernames(clean_tweet_text)
        clean_tweet_text = ElectionsTweet.remove_urls(clean_tweet_text)
        clean_tweet_text = ElectionsTweet.remove_punctuations(clean_tweet_text)
        clean_tweet_text = clean_tweet_text.lower()
        word_tokens = word_tokenize(clean_tweet_text)
        filtired_tweet = [w for w in word_tokens if not w in stop_words]
        for w in word_tokens:
            if w not in stop_words:
                filtired_tweets.append(w)

print(consumer.candidates)
for candidate in consumer.candidates:
    candidate_tweets = consumer.get_all_tweets(candidate)
    print(len(candidate_tweets))
    filtired_tweets = []
    delete_stopwords(candidate_tweets)

unaccented_tweets = [unicodedata.normalize('NFKD', x).encode('ASCII', 'ignore') for x in filtired_tweets]
wcloud = Counter(unaccented_tweets)

counter = 0
for w,i  in sorted(wcloud.items(), key=lambda x: x[1],reverse=True):
    if (counter != 15):
        print(w, i)
        counter = counter + 1
    else:
        break