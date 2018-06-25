#Q.3- Using Tweepy library try to extract tweets from Twitter.

import tweepy
consumer_key="PtmW3YkLUmabc23jgkk34llfgj"
consumer_secret="SeVyhIwTtisghqw2l6nfmvhWAvNQz12gd34jZBb"

access_token="1rtkjiiu783920-tU0w1W8HSS126344jsdfztfopgt"
access_token_secret="xQdhfgrkhcnm12p4567hdgHm"


auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api=tweepy.API(auth)
tweets=api.search('#IndiaInvited',lang='en',count= 10,tweet_mode="extended")

for tweet in tweets:
	print("-----------")
	print(tweet.full_text)
	print("----------")
	