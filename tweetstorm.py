# -*- coding: utf-8 -*-
"""
Criado em Ter 9 de janeiro de 2018 às 18:17:00

@author: lfaraujo
"""
import config, sys, tweepy

#Sets up the API authentication with the config file data
def get_api():
  auth = tweepy.OAuthHandler(config.AUTHDATA['consumer_key'], config.AUTHDATA['consumer_secret'])
  auth.set_access_token(config.AUTHDATA['access_token'], config.AUTHDATA['access_token_secret'])
  return tweepy.API(auth)

#Given a string, breaks it into a list of tweets with size of 140 chars tops
def tweetchop(msg):
	words = msg.split() #list of words in the big string "msg"
	tweet = '' #tweet string whose length is smaller than 140 chars
	list = [] #final list of tweets to be returned from this function
	
	if len(words[0]) > 140:
	
	#it'saonewordstringthatasmartassistryingtobrakmycodeorthespacebarisbroken
		for i in range(0, len(words[0]), 135):
			tweet = words[0][i: i + 135]
			list.append(tweet)
		
	else:
	
	#iterates word by word not to have a broken/nonsense sentence in the tweet
		for i in range(len(words)):
			tweet += words[i]
			if len(tweet + words[i]) > 135: #considered 135 as max length for indexing
				list.append(tweet)
				tweet = ''
			else:
				if i == len(words) - 1:
					list.append(tweet)
				else:
					tweet += ' '
					
	#indexing of the tweets: (adds tweet#/total tweets: in the beginning of each tweet)
	for i in range(len(list)):
		list[i] = str(i + 1) + '/' + str(len(list)) + ': ' + list[i]
	
	#print(list) debug
	return(list)

def main():
	api = get_api()
	longstring = sys.argv[1]
	print(longstring)
	tweets = tweetchop(longstring)
	for i in range(len(tweets)):
		status = status = api.update_status(status=tweets[i])
	
if __name__ == "__main__":
	main()