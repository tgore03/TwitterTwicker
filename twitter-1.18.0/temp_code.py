from tweet_to_file import *
import json
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans


#initialize variables
tfidf = [{}]
words_set = {}
total = 0
tweets = None
arr_tf = []
index_word = {}
zerosOnEveryRecipe = None
kmeans = None

dictionary = []       #List of all unique words
vector_matrix = None    #zero vector with columns=len(dictionary) & rows=#of tweets
tfidf_for_each_tweet = []    #tfidf value of each word in each tweet.
no_of_tweets = 0
no_of_words_in_tweet = None




#get training data from file
tweets = json.load(open('data.json'))['tweetno']

#compute tf value
#for each tweet
for tweet in tweets:
    term_frequency = {} #to store tf value for current tweet
    no_of_words = 0
    no_of_tweets += 1   #get total number of tweets

    #for each word in tweet
    for word in tweet.get("text").split():
        ## Eliminate punctuations and hashtags and other illegitimate words.
        
        if word.startswith('http'):
            continue
        elif word in term_frequency:
            term_frequency[word] += 1.0
        else:
            term_frequency[word] = 1.0
            
        no_of_words += 1
        
        #Also start populating the dictionary
        if word not in dictionary:
            dictionary.append(word)

    #calculate tf value for each word in current tweet
    for k,v in term_frequency.items():
        term_frequency[k] = v/no_of_words
        tfidf_for_each_tweet.append(term_frequency)


#compute idf & then tfidf value
#for each tweet
for i in range(0, no_of_tweets-1):
    #for each word in tweet
    for word in tfidf_for_each_tweet[i]:
        no_of_tweets_word_belongs_to=0
         
        #check how many documents that word belongs to
        for j in range(0, no_of_tweets-1):
            if word in tfidf_for_each_tweet[i]:
                no_of_tweets_word_belongs_to+=1
        tf =1
        #calculate idf for that word
        idf = math.log(no_of_tweets / no_of_tweets_word_belongs_to)
        #calculate tfidf for that word
        tfidf_for_each_tweet[i][word] = tf*idf
    print tfidf_for_each_tweet[i]



        
            

    

