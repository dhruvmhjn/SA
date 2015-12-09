import json
import tweepy
import io

access_token = "3904981821-aG4hTxXMrdFtwMtPh9h3s1KM3I7ZxeZzkHWlX1F"
access_token_secret = "ka1caG2BWXRP1vNCd34WBA3e7nn0b2jnXQQ0EKoMn54ck"
consumer_key = "jvngcbJOm7YFCmMiGDIjqfvYd"
consumer_secret = "FBTYg8GEvENy6RI6CnMPGVkbZC5dwsEQIAUwohOHRRZ4Zn0pYM"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# class followingobject:
# {
	# String user_id;
	
	# String following_ids[];
# }

tweets_data_path = 'G:/Academic/Fall 15/SNC/Project/twitter_data.txt'
follow_data_path = 'G:/Academic/Fall 15/SNC/Project/following.txt'

tweets_file = open(tweets_data_path, "r")
follow_file = io.open(follow_data_path, 'wb')


for line in tweets_file:
    try:
        tweet = json.loads(line)
	print tweet['user']['id']
	ids = []
	current_cursor = ""
	for page in tweepy.Cursor(api.friends_ids, id=tweet['user']['id']).pages():

		cursor = tweepy.Cursor(api.followers_ids, id=tweet['user']['id'],  
		cursor =  current_cursor)
	current_cursor = cursor.iterator.next_cursor
	ids.extend(page)
	#print page
	print ids
	#followingobject fo = new followingobject(tweet['user']['id'], ids);
	json.dump([tweet['user']['id'], ids], follow_file)
	json.dumps([1, 'simple', 'list'], follow_file)
	#print len(ids)
    except:
        continue
follow_file.close()