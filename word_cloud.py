# coding=utf-8
from elections.utils.candidates_consumer import CandidatesConsumer
from elections.utils.e_tweet import ElectionsTweet
from elections.api.config import TwitterAPI
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import unicodedata

twitter_api = TwitterAPI()

stop_words = set(stopwords.words('spanish'))
counter = 0

consumer = CandidatesConsumer(twitter_api)
print(consumer.candidates)
for candidate in consumer.candidates:
    candidate_tweets = consumer.get_all_tweets(candidate)
    print(len(candidate_tweets))
    filtired_tweets = []
    for tweet in candidate_tweets:
        word_tokens = word_tokenize(tweet.text)
        filtired_tweet = [w for w in word_tokens if not w in stop_words]
        filtired_tweet = []
        for w in word_tokens:
            if w not in stop_words:
                filtired_tweets.append(w)

unaccented_tweets = [unicodedata.normalize('NFKD', x).encode('ASCII', 'ignore') for x in filtired_tweets]
print(unaccented_tweets)