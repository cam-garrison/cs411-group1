# cs411-group1 | Tweet Store

Tweet Store is an app that pulls tweets from a friend and recommends stores perfect for gift shopping.

## Video Link

https://www.youtube.com/watch?v=q4ozKM1QuSc

## Note for Graders

The code can all be found in the prototype folder - the main backend file is oauth.py - which uses functions from other python files to perform most API calls. 

## Inspiration

The idea for Tweet Store arose from several initial ideas that had come together. Narrowing our brainstorming session into two ideas (Hum Guessing similar to Shazam and a Gift Matching App), we proceeded with the latter given the feasibility of the project both in terms of APIs to use and scope of the class. In an age where getting gift cards are just a sign of laziness and not knowing where to start comes as a result of wanting get something "more", Tweet Store is the place to start!

## What It Does

Tweet Store is a simple, straightforward web app that pulls a public user's tweets and will display a selection of stores in your area (based on what you input into the "City" parameter) to start your gift shopping process for the Twitter User entered. In a simple three-step application, all a user needs to do is login via Twitter OAuth, click on the "Start The Search" button to enter the search page, and then enter a public Twitter handle with enough tweets as well as the city where you will shop. In a few clicks, any user will have be able to see a list of stores displayed on cards that show where a user can start shopping for gifts.

## How We Built It

Tweet Store was built via a Flask back-end and HTML/(S)CSS/JS front-end. We used the Twitter API for both OAuth and pulling tweets from users as well as the Google Places API to list locations of shops of a certain category that was produced by the back-end.

## Future Directions

As a result of the many challenges encountered along the way, the future of Tweet Store would be to implement additional pages regarding Tweet Store's use and practicality (on a marketing standpoint) as well as the implementation of the Google Places/Maps API on an autocomplete feature when typing in a city name. Unfortunately, Google recently made it so that any search queries or sessions would generate tokens that cost money to integrate.

## Members

### Back-End Team

- Cameron Garrison
- Angela Castronuovo
- Caitlin Trout

### Front-End Team

- Andy Vo
- Brian Amusat
- Anastasiia Sviridenko


