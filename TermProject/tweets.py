import tweepy

access_token = "15422617-gcY3kWXL2KS03xRMnpFZYtMSKRqccsPlv5NHF6wfK"
access_token_secret = "0N0S70ra2GqLkQUY437w1FYR6wZSL4W1MaUWTcGAf04mO"
consumer_key = "vPFWrbaWYwUI7GpgSLJzavvgG"
consumer_secret = "zQ159a6dxPVuAaUssdVsB71IzWAQNoeqrlZtiWf3Vit2anUQED"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)