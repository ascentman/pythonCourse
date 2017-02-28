import tweepy
from tweepy.streaming import StreamListener

CONSUMER_KEY = '62DQSnyyPSVYv9TU9UKe8gqPw'
CONSUMER_SECRET = 'l85LOdo3UNDO7EFOXgPGDMw4DyKlhL4UV5VUicsi0AGrbUs2up'
ACCESS_TOKEN = '204483920-qaUDsIVnGqRmMhpw4ZQcrw0JzndIgugIZymobYkQ'
ACCESS_TOKEN_SECRET = 'sEwtMlXcZUkgcpq85bYEpUcwZMrxuwqLAwIUyZ8yWvYwa'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

#status = "Testing!"
#api.update_status(status=status)

user = api.me()
print('Name: ' + user.name)
print('Location: ' + user.location)

# input
print("Start!")
print("===========================")
print("Enter a country (e.g. USA):")
country = input()
print("Enter from date (e.g. 2017-02-20):")
set_from_date = input()
print("Enter max number of tweets (e.g. 5):")
n = input()

places = api.geo_search(query="%s" % country, granularity="country")
place_id = places[0].id

for tweet in tweepy.Cursor(api.search, q="place:%s" % place_id, since="%s" % set_from_date, result_type='popular').items(int(n)):
  print(tweet.text)
  print("location: ", tweet.place.name)
  print("created: ", str(tweet.created_at))
  print("popularity: ", str(tweet.favorite_count) + "\n")