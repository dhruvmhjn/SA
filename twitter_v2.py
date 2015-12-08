import tweepy

access_token = "3904981821-aG4hTxXMrdFtwMtPh9h3s1KM3I7ZxeZzkHWlX1F"
access_token_secret = "ka1caG2BWXRP1vNCd34WBA3e7nn0b2jnXQQ0EKoMn54ck"
consumer_key = "jvngcbJOm7YFCmMiGDIjqfvYd"
consumer_secret = "FBTYg8GEvENy6RI6CnMPGVkbZC5dwsEQIAUwohOHRRZ4Zn0pYM"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
ids = []
current_cursor = ""
for page in tweepy.Cursor(api.friends_ids, screen_name="dhruvmhjn").pages():

	cursor = tweepy.Cursor(api.followers_ids, screen_name="dhruvmhjn",  
	cursor =  current_cursor)
current_cursor = cursor.iterator.next_cursor
#print repr(cursor)
#print current_cursor
ids.extend(page)
#print page
print ids

print len(ids)