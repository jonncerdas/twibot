import requests
import tweepy
from newspaper import Article
import random
import os

qod_categories = [
    'inspire',
    'management',
    'sports',
    'life',
    'funny',
    'love',
    'art',
    'students'
]

category = random.choice(qod_categories)

params = {
    'category': category,
    'language':'en'
}

resp = requests.get(url='https://quotes.rest/qod', params=params).json()

qod = '"{}" {} \n #{} #quote'.format(resp['contents']['quotes'][0]['quote'], resp['contents']['quotes'][0]['author'], category)

auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_TOKEN_SECRET'])

api = tweepy.API(auth)

api.update_status(status=qod)


