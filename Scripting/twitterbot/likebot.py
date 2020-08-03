import tweepy
import time

auth = tweepy.OAuthHandler('nmrU7IGRXdUYkVqW8ytPNptp5', 'rFNq6H7AYB87rDLSqKeHCVXhgBU5ruvdcxFdy848txWnS3N6Vj')
auth.set_access_token('1631261864-FlnpaWgGrhRvj5HlZZghbukBKjH3iLbaRck5dUf', 'tQhpZqwAezj4tDExhnguO4CvRy2g8WJQsq7DGt0buzC7J')

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLinitError:
        time.sleep(300)

search_string = 'python'
numberoftweets = 2

for tweet in tweepy.Cursor(api.search,search_string).items(numberoftweets):
    try:
        #tweet.favorite()
        tweet.retweet()

        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

'''
def limit_handler(cursor):
    try:
    while True:
        yield cursor.next()
    except tweepy.RateLinitError:
        time.sleep(2000)

gnerous bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == ''
        follower.follow()
        break
    print(follower.name)  # we get all our followers id


'''