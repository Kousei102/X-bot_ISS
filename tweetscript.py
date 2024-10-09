import os
import tweepy
from datetime import datetime
import requests

# secretsで設定した値をとる
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']
OPENCAGE_API_KEY = os.environ['OPENCAGE_API_KEY']  # OpenCageのAPIキー

# オブジェクト作成
client = tweepy.Client(
    consumer_key = CONSUMER_KEY,
    consumer_secret = CONSUMER_SECRET,
    access_token = ACCESS_TOKEN,
    access_token_secret = ACCESS_TOKEN_SECRET
)

# 現在時刻を取得
nowtime = datetime.now()
formatted_time = nowtime.strftime("%H:%M:%S")

# ISSの位置情報を取得
response = requests.get('http://api.open-notify.org/iss-now.json')
data = response.json()
latitude = data['iss_position']['latitude']
longitude = data['iss_position']['longitude']

# 逆ジオコーディングを使って場所の名前を取得
geocoding_url = f"https://api.opencagedata.com/geocode/v1/json?q={latitude}+{longitude}&key={OPENCAGE_API_KEY}"
geo_response = requests.get(geocoding_url)
geo_data = geo_response.json()

if geo_data['results']:
    location = geo_data['results'][0]['formatted']  # 最初の結果から場所の名前を取得
else:
    location = "海の上"

# ツイート内容を作成
if location == "海の上":
    tweet_text = f"時刻: {formatted_time}\n緯度: {latitude}, 経度: {longitude}\n場所: {location}です"
else:
    tweet_text = f"時刻: {formatted_time}\n緯度: {latitude}, 経度: {longitude}\n場所: {location}の付近です"

# ツイートを送信
client.create_tweet(text=tweet_text)

print("ツイートが送信されました！")
