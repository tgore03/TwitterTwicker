import json


def get_tweets():
	data = json.load(open('data.json'))
	#words_set = set()
	tweets = data['tweetno']
	total = 0
	arr_tf = []
	for item in tweets:
		sentence = item.get("text").split()
		term_frequency = {}
		tweet_length = 0
		for word in sentence:
			if not word.startswith('http'):
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
	
	print len(arr_tf)	

	

get_tweets()