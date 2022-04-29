from ast import keyword
from sys import api_version
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import tweepy

%load fix_extract_dataframe.py
%load fix_clean_tweets_dataframe.py

from fix_extract_dataframe import ExtractTweets
from fix_clean_tweets_dataframe import TweetCleanser

def percentage(part,whole):
 return 100 * float(part)/float(whole)
keyword= input("Please enter keyword or hashtag to search:")
noOfTweet = input('Please enter how many tweets to analyze: ')
tweets = tweepy.Cursor(api_version.search, q=keyword).items(noOfTweet)
positive = 0
negative = 0
neutral = 0
polarity = 0
tweet_list = []
neutral_list = []
negative_list = []
positive_list = []
for tweet in tweets:
 
 #print(tweet.text)
 tweet_list.append(tweet.text)
 analysis = TextBlob(tweet.text)
 score = SentimentIntensityAnalyzer().polarity_scores(tweet.text)
 neg = score['neg']
 neu = score['neu']
 pos = score['pos']
 comp = score['compound']
 polarity += analysis.sentiment.polarity
 
 if neg > pos:
    negative_list.append(tweet.text)
 negative += 1
 elif pos > neg:
positive_list.append(tweet.text)
positive += 1
 
elif pos == neg:
neutral_list.append(tweet.text)
neutral += 1
positive = percentage(positive, noOfTweet)
negative = percentage(negative, noOfTweet)
neutral = percentage(neutral, noOfTweet)
polarity = percentage(polarity, noOfTweet)
positive = format(positive, '.1f')
negative = format(negative, '.1f')
neutral = format(neutral, '.1f')