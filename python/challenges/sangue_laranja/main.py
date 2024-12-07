from collections import OrderedDict

import requests
from fastapi import FastAPI

# Create api
app = FastAPI()

url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url).json()


@app.get('/users/websites')
def user_websites():

    websites = list(map(
                        lambda site: 
                        {'website': site.get('website')}, response))
    return {'websites': websites}


@app.get('/users/detail')
def user_detail():
    user_detail = list(map(lambda user: {
                'name': user.get('name'),
                'email': user.get('email'),
                'company': user.get('company').get('name')
                }, response))

    user_detail = sorted(user_detail, key=(lambda d: d['name']))
    return {"users": user_detail}


@app.get('/users')
def filter_users(name: str = ''):
    values = [x for x in response if name in x['name']]
    return {"users": values}
