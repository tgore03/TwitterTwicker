import json
from pprint import pprint

def get_tweets():
	data = json.load(open('data.json'))
	words_set = set()
	tweets = data['tweetno']
	for item in tweets:
		sentence = item.get("text").split()
		#print sentence
		for word in sentence:
			if not word.startswith('http'):
				words_set.add(word)

	print words_set

get_tweets()