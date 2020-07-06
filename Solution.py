import tweepy
from textblob import TextBlob

#Get from Twitter Developers
con_key = ""
con_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(con_key, con_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
 
search_term = input("Enter term to analyse:\n")

tweets = api.search(search_term)

polarity = 0.0
subjectivity = 0.0

for tweet in tweets:
  analysis = TextBlob(tweet.text)
  polarity+= analysis.sentiment.polarity
  subjectivity+= analysis.sentiment.subjectivity

subjectivity/= len(tweets)
polarity/= len(tweets)


print("\n"+search_term+"'s public perception is "+str(round(polarity,2))+" on a scale of -1 to 1")
print("Tweets on "+search_term+" are "+str(round(subjectivity*100,2))+" percent subjective.")