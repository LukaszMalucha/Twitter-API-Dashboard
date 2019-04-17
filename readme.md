## Twitter API Dashboard

#### [Visit App](https://twitter-rest-api-dashboard.herokuapp.com/)


## PROJECT OVERVIEW

Flask application hosting Twitter API. Main functionality allows user to find out what is currently trending and extract data sample to MongoDB.
Once data sample is extracted, next step is to pre-process it and load to SQL database. Final step is to apply Keras LSTM model on processed tweets to find out what's the dominating sentiment 
among conversation participants - positive, negative or neutral.



## APP STRUCTURE


### Main Dashboard View

Choose between app main functionalities:

<br>

![1](https://user-images.githubusercontent.com/26208598/52292307-57ef0600-296c-11e9-872b-f8ccdf31c024.JPG)

<br>

### Trend Search

Find out what is currently trending in US. Pick most interesting subject and guide your data sample through ETL pipeline to make it ready for sentiment analysis.

<br>

![2](https://user-images.githubusercontent.com/26208598/52292311-59b8c980-296c-11e9-9f31-d6eeb323c1c3.JPG)

<br>

### Manage Database

Get rid of obsolete collections from MongoDB or delete processed data from SQLite database:  

<br>

![3](https://user-images.githubusercontent.com/26208598/52292313-59b8c980-296c-11e9-9169-45209ee43dec.JPG)

<br>

### Sentiment Analysis 

Apply Deep learning LSTM model on previously stored Twitter dataset. Find out what's the dominating sentiment among conversation participants - positive, negative or neutral:

<br>

![4](https://user-images.githubusercontent.com/26208598/52292314-59b8c980-296c-11e9-83ea-ca378f0ffd97.JPG)

<br>

### Tale of Two Cities

Find out what is currently trending in two chosen locations. Specify woe_id and find out common trends:

<br>

![5](https://user-images.githubusercontent.com/26208598/52292315-5a516000-296c-11e9-87f2-979aabbfc221.JPG)

<br>

### Popular Retweets


Choose a keyword and find out most popular tweets in a subject:

<br>

![6](https://user-images.githubusercontent.com/26208598/52292319-5c1b2380-296c-11e9-92da-f5d8c7672f59.JPG)

<br>

### Travis CI:

[![Build Status](https://travis-ci.com/LukaszMalucha/Twitter-API-Dashboard.svg?branch=master)](https://travis-ci.com/LukaszMalucha/Twitter-API-Dashboard)

### Test Files:

##### /tests

## TOOLS, MODULES & TECHNIQUES

##### Python – app development:
Flask | REST | Tweepy | Oauthlib | Pickle

##### Databases
MongoDB | Sqlite 

##### Python – Text Processing
nltk | re 

##### Python – LSTM:
keras | tensorflow | numpy | scikit-learn | h5py

##### Web Development:
HTML | CSS | Bootstrap | Materialize | Conda | Heroku | Docker

##### Testing
selenium | unittest

<br>

Thank you,

Lukasz Malucha
