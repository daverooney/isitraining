from app import app
from flask import Flask, render_template, request
import requests
import json

@app.route('/')
@app.route('/here')
def index():
	send_url = 'http://freegeoip.net/json/'
	user_ip = request.headers['X-Real-IP']
	print "Viewer's IP:\t", user_ip
	r = requests.get(send_url + str(user_ip))
	j = json.loads(r.text)
	lat = j['latitude']
	log = j['longitude']
	print "Viewer's lat/long:\t", lat, log
	url = "http://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(log)
	response = requests.get(url).json()
	weather = response['weather'][0]['main']

	if weather == "Rain":
		isitraining  = "yes."
	else:
		isitraining  = "no."
  
	return render_template("index.html",lat=lat,log=log,isitraining=isitraining)

@app.route('/japan')
def test():
#		These lines (and api calls) unneeded if we're just mocking with known Japan values.
#	send_url = 'http://freegeoip.net/json'
#	r = requests.get(send_url)
#	j = json.loads(r.text)
	lat = 45
	log = 139
	url = "http://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(log)
	response = requests.get(url).json()
	weather = response['weather'][0]['main']

	if weather == "Rain":
		isitraining  = "yes."
	else:
		isitraining  = "no."
  
	return render_template("index.html",lat=lat,log=log,isitraining=isitraining)
