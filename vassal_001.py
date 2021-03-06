import os

import requests
import tweepy
from newspaper import Article

auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'],
                           os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_TOKEN'],
                      os.environ['ACCESS_TOKEN_SECRET'])

api = tweepy.API(auth)

URL = 'https://www.nationalgeographic.com/photography/photo-of-the-day/'
article = Article(URL)
article.download()
article.parse()

FILENAME = 'temp.jpg'
request = requests.get(article.top_image, stream=True)

if request.status_code == 200:
    with open(FILENAME, 'wb') as image:
        for chunk in request:
            image.write(chunk)

    media = api.media_upload(FILENAME)
    TWEET = "Great scifi author or greatest scifi author? #williamgibson"
    post_result = api.update_status(status=TWEET, media_ids=[media.media_id])
