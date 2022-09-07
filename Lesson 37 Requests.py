import json
from pprint import pprint
import requests

print('Task 1')

# Download and save to file robots.txt from wikipedia, twitter websites etc.

responce = requests.get('https://wikipedia.org/robots.txt')
test = responce.text
with open('robotswiki.json', 'w') as file:
    json.dump(test, file, indent=3)

print('Task 2')

# Download all comments from a subreddit of your choice using URL:
# https://api.pushshift.io/reddit/comment/search/ .
#
# As a result, store all comments in chronological order in JSON.

URL = ('https://api.pushshift.io/reddit/comment/search/')
r = requests.get(url=URL)
data = r.json()
cit = data['data']
#pprint(cit)
out = []
for i in cit:
    comment = i['body']
    #print(comment)
    com = {'comment':
               comment.replace('\n', '').replace('/r','').replace('/u','')}
    #pprint(com)
    out.append(com)

with open('comment.json', 'w') as file:
    json.dump(out, file, indent=3)


print('Task 3')

# Write a console application which takes as an input a city name and
# returns current weather in the format of your choice.
# For the current task, you can choose any weather API or website or use
# openweathermap.org


openwheatherkey = '46f1a6f55eed1b889c89e59ccb37af14'  #API key  keytok
city = 'London'  # city name
info = {}


def wheather(city, keytok):
    resp = requests.get(f'https://api.openweathermap.org/data/2.5/'
                        f'weather?q={city}&appid={keytok}')
    data = resp.json()
    far = data['main']['temp']
    KeltoCelt = round((far - 273), 2)
    info = {
        'Город: ': data['name'],
        'Температура: ': f'{KeltoCelt} град',
        'Облачность: ': f"{data['clouds']['all']} %",
        'Давление: ': f"{data['main']['temp']} hPa",
    }
    #pprint(data)
    return info

pprint(wheather(city, openwheatherkey))
