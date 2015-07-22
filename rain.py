import requests
import json

url = "http://api.openweathermap.org/data/2.5/weather?lat=45&lon=139&APPID=b1bf90077b688b5e1b3c75301de15520"

response = requests.get(url).json()
weather = response['weather'][0]['main']

if weather == "Rain":
	print "yes"
else:
	print "no"