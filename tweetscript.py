print("Hello World")

import os
import tweepy

#secretsで設定した値をとる
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

#オブジェクト作成
client = tweepy.Client(
  consumer_key = CONSUMER_KEY,
  consumer_secret = CONSUMER_SECRET,
  access_token = ACCESS_TOKEN,
  access_token_secret = ACCESS_TOKEN_SECRET
)

import requests

response = requests.get('http://api.open-notify.org/iss-now.json')
data = response.json()
print(f"緯度：{data['iss_position']['latitude']}")
print(f"軽度：{data['iss_position']['longitude']}")

# ツイート内容を作成
tweet_text = f"ISSの現在の位置\n緯度：{data['iss_position']['latitude']}\n経度：{data['iss_position']['longitude']}"

#ツイートする
client.create_tweet(text=tweet_text)
