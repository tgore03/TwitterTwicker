from tweet_to_file import *
import json
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans


#Global vars
tfidf = [{}]
words_set = {}
total = 0
tweets = None
arr_tf = []
#Assigning index to every word in the list
index_word = {}
zerosOnEveryRecipe = [[]]



def load_data_from_file():
    print "load_data()"
    global tweets
    tweets = json.load(open('data.json'))['tweetno']

def load_data_from_json(jsondata):
    global tweets
    tweets = data['tweetno']


def get_tweets():
    print "get_tweets()"
    global tweets, word_set, arr_tf, tfidf

    for item in tweets:
        sentence = item.get("text").split()
        term_frequency = {}
        tweet_length = 0
        for word in sentence:
            if not word.startswith('http'):
                if word in words_set:
                    words_set[word] += 1.0
                else:
                    words_set[word] = 1.0
                tweet_length+=1.0
                if word in term_frequency:
                    term_frequency[word] += 1.0
                else:
                    term_frequency[word] = 1.0
        for k,v in term_frequency.items():
            #print k,v
            term_frequency[k] = v/tweet_length
            #print k,v
        arr_tf.append(term_frequency)

    total_tweets = len(arr_tf)
	#print len(words_set) # 4881
	#print len(arr_tf)	 # 1000

    print "tf obtained"


    idf = {}
    for word in words_set:
        doc_word_freq = 0
        for item in arr_tf:
            if word in item:
                doc_word_freq += 1
            #print doc_word_freq
        idf[word] = math.log(total_tweets/doc_word_freq)
	#print len(idf) #4881
    print "idf obtained"

	#tfidf = []
    for item in arr_tf:
        temp_tfidf = {}
        for k, v in item.items():
            idf_val = idf[k]
            temp_tfidf[k] = idf[k]*v
            tfidf.append(temp_tfidf)

    print "tfidf obtained"

	#print tfidf
	#for i in tfidf:
		#for k,v in i.items():
			#print k, v

    print tfidf[1]


##get_tweets()


def AllWord():
    global tfidf, word_set, index_word
    print "AllWord()"
    tf_vecs = tfidf
    #print tf_vecs
    everyWord = []
    alldicts = []

    #print words_set
    #getting a list of words.
    for k,v in words_set.items():
        #alldicts.append(dicts)
        everyWord.append(k)

    print len(everyWord)

    i = 0
    for word in everyWord:
        index_word[word] = i
        i = i+1

##AllWord()

#zerosOnEveryRecipe = np.zeros([len(tfidf),len(index_word)])
def addingToZerosArr():
    global tfidf, index_word, arr_tf, zerosOnEveryRecipe
    print "addingToZerosArr()"
    i = 0;
    ind = 0;

    zerosOnEveryRecipe = np.zeros([len(tfidf),len(index_word)])

    v = True;

    for tw in arr_tf:
        for word, val in tw.items():
            index = index_word[word]
            zerosOnEveryRecipe[i][index] = arr_tf[i][word]

        i = i + 1

    #print len(zerosOnEveryRecipe[1])
    #print zerosOnEveryRecipe[0].tolist()

##addingToZerosArr()

def KmeansAnalysis():
    print "KmeansAnalysis()"

    global zerosOnEveryRecipe
    arrayOfIntrest = np.array(zerosOnEveryRecipe)

    count = 0
    kmeans = KMeans(n_clusters = 8) #make ten clusters
    #while(count < 100):
    kmeans.fit(arrayOfIntrest)  #fit the data - learning
    centroids = kmeans.cluster_centers_  #grab the centroids
    labels = kmeans.labels_  # and the labels
    #print len(centroids[0])
    print len(labels)
    print labels.tolist()
    count = count + 1


#KmeansAnalysis()





#**********************************************************************#

#Start of Program
print "Program start"
#getTrainingSet()
load_data_from_file()
get_tweets()

AllWord()
addingToZerosArr()
KmeansAnalysis()
