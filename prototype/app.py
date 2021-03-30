######################################
# app for cs411 as3.
######################################

import flask
from flask import Flask, Response, request, render_template, redirect, url_for
from datetime import datetime
from getuserinfo import main1
from getusertweets import main2
import json

import os, base64

app = Flask(__name__)
app.secret_key = 'super secret'  # Changed


#default page
@app.route("/", methods=['GET', 'POST'])
def twitter():
	if flask.request.method == 'GET':
		return render_template('twitter.html', message='Welecome to twittersearch')
	else:
		if 'search' in request.form:
			user = request.form.get('username')
			if user == '':
				return render_template('twitter.html', message='Welecome to twittersearch - please enter valid username')
			f = main1(user)
			loaded = json.loads(f)
			uid = loaded['data'][0]['id']
			print(uid)
			tws = main2(uid)
			loaded2 = json.loads(tws)
			print(loaded2)
			return render_template('twitter.html', message='Welecome to twittersearch, search for '+user, tweets=loaded['data'][0], tweetlist=loaded2['data'])


if __name__ == "__main__":
	#this is invoked when in the shell you run
	#$ python app.py
	app.run(port=5000, debug=True)
