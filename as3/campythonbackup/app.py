######################################
# author ben lawson <balawson@bu.edu>
# Edited by: Craig Einstein <einstein@bu.edu>
# Edited by: Cameron Garrison <cgarriso@bu.edu>
######################################
# Some code adapted from
# CodeHandBook at http://codehandbook.org/python-web-application-development-using-flask-and-mysql/
# and MaxCountryMan at https://github.com/maxcountryman/flask-login/
# and Flask Offical Tutorial at  http://flask.pocoo.org/docs/0.10/patterns/fileuploads/
# see links for further understanding
###################################################

import flask
from flask import Flask, Response, request, render_template, redirect, url_for
from datetime import datetime

#for image uploading
import os, base64

app = Flask(__name__)
app.secret_key = 'super secret'  # Changed


#default page
@app.route("/", methods=['GET', 'POST'])
def twitter():
	if flask.request.method == 'GET':
		return render_template('twitter.html', message='Welecome to twittersearch')
	else:
		return render_template('twitter.html', message='Welecome to twittersearch')


if __name__ == "__main__":
	#this is invoked when in the shell  you run
	#$ python app.py
	app.run(port=5000, debug=True)
