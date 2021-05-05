
#####################################
# WITH FLASK_DANCE

# Source video tutorial: https://www.youtube.com/watch?v=MiHVTHzIgyE
# Source video 2        https://www.youtube.com/watch?v=G44Tpi58dcc

######################################
# app for cs411 as3.
######################################

######
# TO RUN SERVER do these
# export OAUTHLIB_INSECURE_TRANSPORT=1
# export FLASK_APP=oauth.py
# export FLASK_ENV=development
# python3 -m flask run
######

import flask
from flask import Flask, Response, request, render_template, redirect, url_for
from datetime import datetime
from text_taker import get_category
from get_stores import find_stores
import json
import twitter
import os
import base64

# Needed for OAUTH
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
from settings import CONSUMER_KEY1, CONSUMER_SECRET1, API_SECRET1
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, current_user, LoginManager, login_required, login_user, logout_user
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin, SQLAlchemyStorage
from flask_dance.consumer import oauth_authorized
from sqlalchemy.orm.exc import NoResultFound

app = Flask(__name__)
app.secret_key = API_SECRET1  # Added from settings doc

# TO USE TWITTER OAUTH
twitter_blueprint = make_twitter_blueprint(
    api_key=CONSUMER_KEY1, api_secret=CONSUMER_SECRET1)
# MAKE /twitter_login from /authorized
app.register_blueprint(
    twitter_blueprint, url_prefix='/login')

#FOR DATABASE:#######################################
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://{user}:{password}@{host}:3306/sqlalch".format(
    user='camgarrison', password='tamtam13', host='127.0.0.1')


db = SQLAlchemy(app)


login_manager = LoginManager(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True)


class OAuth(OAuthConsumerMixin, db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


twitter_blueprint.backend = SQLAlchemyStorage(
    OAuth, db.session, user=current_user)
####################################################


# default page for searching users
# MIGHT NEED TO CHANGE !!!!!!!!!!!!!!!!
@login_required
@app.route("/twitter", methods=['GET', 'POST'])
def twitter():
    if flask.request.method == 'GET':
        return render_template('twitter.html')
    else:
        if 'search' in request.form:
            user = request.form.get('username')
            if user == '':
                return render_template('twitter.html', message='Welecome to Gift Search - please enter valid username')
            city = request.form.get('city')
            if city == '':
                return render_template('twitter.html', message='Welecome to Gift Search - please enter valid city')

            category = get_category(user)
            print(category)
            if category == "NoTweets":
                return render_template('twitter.html', message='We cannot access the tweets of this user - or they have no tweets. Try another username')
            if category == "NoCat":
                return render_template('twitter.html', message='This user does not have enough tweets for us to determine a gift category. Sorry')

            searchstring = category + " stores in " + city
            print(searchstring)
            storeslist = find_stores(searchstring)
            print(' ')
            print(' ')
            storeslist = storeslist[:9]

            return render_template('stores.html', message='Here are some stores you could shop at', stores=storeslist, category=category, user=user)


@app.route('/login')  # MAKE /twitter from /twitter_login
def login():
    # if we are not logged in--> go to login page

    return redirect(url_for('twitter.login'))
    # SOME INDENTATION ERROR
    account_info = twitter.get('account/settings.json')
    account_info_json = account_info.json()

    return '<h1> Your Twitter Name is @{}'.format(account_info_json['screen_name'])


# Signal for already being logged in to twitter
@oauth_authorized.connect_via(twitter_blueprint)
def twitter_logged_in(blueprint, token):
    # once we are logged in
    account_info = blueprint.session.get('account/settings.json')

    if account_info.ok:
        account_info_json = account_info.json()
        username = account_info_json['screen_name']
        # Check if user exists in db, if no--> add to db

        query = User.query.filter_by(username=username)

        try:
            user = query.one()
        except NoResultFound:
            user = User(username=username)
            db.session.add(user)
            db.session.commit()

        login_user(user)


@app.route('/')
def index():

    return render_template('home.html')


@app.route('/logout')
def logout():
    logout_user()
    return render_template('home.html', message='Logged out')


if __name__ == "__main__":
    # this is invoked when in the shell you run
    # $ python app.py
    app.run(port=5000, debug=True)
