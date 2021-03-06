import json
import math

def get_tweets(data):

        words_set = {}
        tweets = data['tweetno']
        total = 0
        arr_tf = []
        for item in tweets:
                sentence = item.get("text").split()
                term_frequency = {}
                tweet_length = 0
                for word in sentence:
                        if not word.startswith('http'):
                                if word in words_set:
                                        words_set[word] += 1
                                else:
                                        words_set[word] = 1
                                tweet_length+=1.0
                                if word in term_frequency:
                                        term_frequency[word] += 1.0
                                else:
                                        term_frequency[word] = 1
                for k,v in term_frequency.items():
                        #print k,v
                        v = v/tweet_length
                        #print k,v
                arr_tf.append(term_frequency)   

        total_tweets = len(arr_tf)
        #print len(words_set) # 4881
        #print len(arr_tf)       # 1000

        idf = {}
        for word in words_set:
                doc_word_freq = 0
                for item in arr_tf:
                        if word in item:
                                doc_word_freq += 1
                #print doc_word_freq
                idf[word] = math.log(total_tweets/doc_word_freq)
        #print len(idf) #4881

        tfidf = []
        for item in arr_tf:
                temp_tfidf = {}
                for k, v in item.items():
                        idf_val = idf[k]
                        temp_tfidf[k] = idf[k]*v
                tfidf.append(temp_tfidf)


        #j = 1;
        #print tfidf
        #for i in tfidf:
        #       for k,v in i.items():
                        #print k, v
                #print "***************************** %d",(j)
                #j=j+1
        #print tfidf

        return tfidf

#Program start
data = json.load(open('data.json'))
get_tweets(data)
