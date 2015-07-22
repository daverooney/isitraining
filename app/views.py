from app import app
from flask import Flask, render_template
import requests
import json

@app.route('/')
@app.route('/index')
def index():
	send_url = 'http://freegeoip.net/json'
	r = requests.get(send_url)
	j = json.loads(r.text)
	lat = j['latitude']
	log = j['longitude']
	url = "http://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(log) + "&APPID=b1bf90077b688b5e1b3c75301de15520"
	response = requests.get(url).json()
	weather = response['weather'][0]['main']

	if weather == "Rain":
		isitraining  = "yes"
	else:
		isitraining  = "no"
  
	return render_template("index.html",lat=lat,log=log,isitraining=isitraining)
