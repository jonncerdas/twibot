import tweepy
import requests
from newspaper import Article
import os

auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_TOKEN_SECRET'])

api = tweepy.API(auth)

url = 'https://www.nationalgeographic.com/photography/photo-of-the-day/'
article = Article(url)
article.download()
article.parse()

filename = 'temp.jpg'
request = requests.get(article.top_image, stream=True)

if request.status_code == 200:
    with open(filename, 'wb') as image:
        for chunk in request:
            image.write(chunk)


    media = api.media_upload(filename)
    tweet = "Great scifi author or greatest scifi author? #williamgibson"
    post_result = api.update_status(status=tweet, media_ids=[media.media_id])


