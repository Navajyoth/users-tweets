import oauth2 as oauth
import json

CONSUMER_KEY = "your consumer key"
CONSUMER_SECRET = "your consumer secret"
ACCESS_KEY = "your access key"
ACCESS_SECRET = "your acesss secret"

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

name =raw_input("Enter the User Twitter_Name: ")
no = raw_input("Enter no of tweets you want: ")
timeline_endpoint = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+name+"&count="+no
response, data = client.request(timeline_endpoint)

tweets = json.loads(data)

for tweet in tweets:
    #if tweet == {}:
     #  for i in tweet:
     #      print i['text']
          print tweet["text"]






