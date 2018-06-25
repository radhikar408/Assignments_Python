#Q.3- Using Tweepy library try to extract tweets from Twitter.

import tweepy
consumer_key="PtmW3YkLUm7os5pYZEjdgAXOx"
consumer_secret="SeVyhIwTtih8fKskz0aVftV1sa8LWpCxKhrKzWAvNQz6K8SZBb"

access_token="1011130643999313920-tU0w1W8HSSq9rYyAPcbRJ5r8Grvu1x"
access_token_secret="xQCbkt7540dfgA8og0szqFPJP2XcoN7fsbD94yp9KkdHm"


auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api=tweepy.API(auth)
tweets=api.search('#IndiaInvited',lang='en',count= 10,tweet_mode="extended")

for tweet in tweets:
	print("-----------")
	print(tweet.full_text)
	print("----------")
	