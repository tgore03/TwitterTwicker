import json
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans


tfidf = [{}]
#def get_tweets():
data = json.load(open('data.json'))
words_set = {}
tweets = data['tweetno']
total = 0
arr_tf = []
#Assigning index to every word in the list
index_word = {}


def get_tweets():
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

    idf = {}
    for word in words_set:
        doc_word_freq = 0
        for item in arr_tf:
            if word in item:
                doc_word_freq += 1
            #print doc_word_freq
        idf[word] = math.log(total_tweets/doc_word_freq)
	#print len(idf) #4881

	#tfidf = []
    for item in arr_tf:
        temp_tfidf = {}
        for k, v in item.items():
            idf_val = idf[k]
            temp_tfidf[k] = idf[k]*v
            tfidf.append(temp_tfidf)

	#print tfidf
	#for i in tfidf:
		#for k,v in i.items():
			#print k, v
			
    print arr_tf


get_tweets()


def AllWord():
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
   
AllWord() 


def addingToZerosArr():
    i = 0;
    ind = 0;

    zerosOnEveryRecipe = np.zeros([len(tfidf),len(index_word)])

    v = True;

    for tw in arr_tf:
    
        for word, val in tw.items():
        
            index = index_word[word]
        
            zerosOnEveryRecipe[i][index] = arr_tf[i][word]
       
        
        i = i + 1
    
       

    print len(zerosOnEveryRecipe[1])
    print zerosOnEveryRecipe[0].tolist()

addingToZerosArr()

def KmeansAnalysis():
    
    arrayOfIntrest = np.array(zerosOnEveryRecipe)

    count = 0
    kmeans = KMeans(n_clusters = 8) #make ten clusters
    #while(count < 100):
    kmeans.fit(arrayOfIntrest)  #fit the data - learning
    centroids = kmeans.cluster_centers_  #grab the centroids 
    labels = kmeans.labels_  # and the labels
    count = count + 1
    

KmeansAnalysis()





