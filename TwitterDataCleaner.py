import json
import pandas as pd

tweets_data_path = 'TwitterData2.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

tweets = pd.DataFrame()
tweets['tweet'] = map(lambda tweet: tweet['text'] if 'text' in tweet else None, tweets_data)
tweets['created_at'] = map(lambda tweet: tweet['created_at'] if 'created_at' in tweet else None, tweets_data)
tweets['user_id'] = map(lambda tweet: tweet['user']['id'] if 'user' in tweet else None, tweets_data)
tweets['id_str'] = map(lambda tweet: tweet['user']['id_str'] if 'user' in tweet else None, tweets_data)
tweets['username'] = map(lambda tweet: tweet['user']['name'] if 'user' in tweet else None, tweets_data)
tweets['screen_name'] = map(lambda tweet: tweet['user']['screen_name'] if 'user' in tweet else None, tweets_data)
tweets['location'] = map(lambda tweet: tweet['user']['location'] if 'user' in tweet else None, tweets_data)
tweets['followers_count'] = map(lambda tweet: tweet['user']['followers_count'] if 'user' in tweet else None, tweets_data)
tweets['friends_count'] = map(lambda tweet: tweet['user']['friends_count'] if 'user' in tweet else None, tweets_data)
tweets['created_at'] = map(lambda tweet: tweet['user']['created_at'] if 'user' in tweet else None, tweets_data)
tweets['user_lang'] = map(lambda tweet: tweet['user']['lang'] if 'user' in tweet else None, tweets_data)
tweets['following'] = map(lambda tweet: tweet['user']['following'] if 'user' in tweet else None, tweets_data)

# tweets['geo'] = map(lambda tweet: tweet['geo'], tweets_data)
# tweets['coordinates'] = map(lambda tweet: tweet['coordinates'], tweets_data)
# tweets['retweet_count'] = map(lambda tweet: tweet['retweet_count'], tweets_data)
# tweets['favorite_count'] = map(lambda tweet: tweet['favorite_count'], tweets_data)
# tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
# if k1 in d and k2 in d[k1]
# tweets['country'] = map(lambda tweet: tweet['place']['country'] if 'place' in tweet and 'country' in tweet['place'] else None, tweets_data)

print (tweets)