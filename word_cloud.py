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
from elections.storage.manager import Manager

twitter_api = TwitterAPI()
stop_words = set(stopwords.words('spanish'))
stop_words_english = set(stopwords.words('english'))
common_words = ['rt','...','jaja', 'ja', 'jajaja', 'jajajaja', 'haha', 'hahaha', 'lol']
consumer = CandidatesConsumer(twitter_api)

def delete_stopwords(candidate_tweets):
    for tweet in candidate_tweets:
        clean_tweet_text = ElectionsTweet.remove_emojis(tweet.text)
        clean_tweet_text = ElectionsTweet.remove_usernames(clean_tweet_text)
        clean_tweet_text = ElectionsTweet.remove_urls(clean_tweet_text)
        clean_tweet_text = ElectionsTweet.remove_punctuations(clean_tweet_text)
        clean_tweet_text = clean_tweet_text.lower()
        word_tokens = word_tokenize(clean_tweet_text)
        for w in word_tokens:
            if w not in stop_words and w not in common_words and w != '' and w not in stop_words_english:
                filtired_tweets.append(w)

candidates_wordcloud = {}

for candidate in consumer.candidates:
    candidates_wordcloud[candidate] = {}
    candidate_tweets = consumer.get_all_tweets(candidate)
    print('Downloaded total of ' + str(len(candidate_tweets)) + ' tweets from ' + candidate)
    filtired_tweets = []
    delete_stopwords(candidate_tweets)
    unaccented_tweets = [unicodedata.normalize('NFKD', x).encode('ASCII', 'ignore') for x in filtired_tweets]
    wcloud = Counter(unaccented_tweets)
    counter = 0
    for w,i  in sorted(wcloud.items(), key=lambda x: x[1],reverse=True):
        if counter != 15:
            if w != '':
                #print(w, i)
                candidates_wordcloud[candidate][w] = i
                counter = counter + 1
        else:
            break

Manager.insert_wordcloud(candidates_wordcloud)