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
    isitraining = 'yes'
    return render_template("index.html",lat=lat,log=log,isitraining=isitraining)
