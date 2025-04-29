import os
from fastapi import FastAPI, responses
from tweet_api import TweetAuth
from openweather_data import OpenWeatherData

app = FastAPI()

#Load Variables
openweather_api_key = os.getenv("OPENWEATHER_KEY")
consumer_key = os.getenv('X_API_Key')
consumer_secret = os.getenv('X_API_Secret_Key')
access_token = os.getenv('X_Access_Token')
access_token_secret = os.getenv('X_Access_Token_Secret')
client_id = os.getenv('X_Client_ID')
bearer_token = os.getenv('X_Bearer_Token_Key')
openweather_text = OpenWeatherData(openweather_key=openweather_api_key)


@app.get('/post_tweet/')
async def post_tweet():
    try:
        texto = await openweather_text.get_city_info("-21.1783", "-47.8067")
        tweet = TweetAuth(consumer_key, consumer_secret, access_token, access_token_secret, client_id, bearer_token).create_tweet(texto)
        res = {"status": tweet}

        return responses.JSONResponse(content=res)
    
    except Exception as e:

        err = {'Error': f"{e}"}

        return responses.JSONResponse(err)