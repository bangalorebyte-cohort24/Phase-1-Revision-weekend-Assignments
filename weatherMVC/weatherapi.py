# weatherapi.py

import json
import requests
import datetime

# url='http://api.openweathermap.org/data/2.5/forecast?q=London&APPID=1960401d79b51d8c3be286b9463a081b'
# weather=requests.get(url)

# string=NewYork,London
# print(weather)


with open("city.list.json","r") as cityJSON:
	data=json.load(cityJSON)

cityName='Bangalore'

for item in data:
	if item['name']==cityName:
		print(item['country'])

url='http://api.openweathermap.org/data/2.5/forecast?q='+cityName+'&APPID=1960401d79b51d8c3be286b9463a081b'
source=requests.get(url)
weather=json.loads(source.text)


def WeatherTime(dt):
	dtItem=datetime.datetime.fromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S')
	dtList=dtItem.split(' ')
	return dtList

# time of data forecasted.

weatherCity=weather['city']['name']

weatherList=[]
for weatherItem in weather['list']:

	weatherList.append([WeatherTime(weatherItem['dt'])[0],WeatherTime(weatherItem['dt'])[1],weatherCity,weatherItem['main']['temp'],weatherItem['main']['temp_min'],weatherItem['main']['temp_max'],weatherItem['wind']['speed'],weatherItem['clouds']['all'],weatherItem['main']['humidity']])

print(len(weatherList))
dateList=list(set([item[0] for item in weatherList]))
print(dateList)