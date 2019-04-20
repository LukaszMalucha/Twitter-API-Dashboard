## Twitter API Dashboard

#### [Visit App](https://twitter-rest-api-dashboard1.herokuapp.com/)


![1](https://user-images.githubusercontent.com/26208598/56461857-839d5c00-63b1-11e9-9c8a-4d1b5a4d0884.JPG)


## PROJECT OVERVIEW

Flask application hosting Twitter API. Main functionality allows user to find out what is currently trending and extract data sample to MongoDB.
Once data sample is extracted, next step is to pre-process it and load to SQL database. Final step is to apply Keras LSTM model on processed tweets to find out what's the dominating sentiment 
among conversation participants - positive, negative or neutral.



## APP STRUCTURE


### Main Dashboard View

Choose between app main functionalities:

<br>

![1](https://user-images.githubusercontent.com/26208598/56461857-839d5c00-63b1-11e9-9c8a-4d1b5a4d0884.JPG)

<br>

### Trend Search

Find out what is currently trending in US. Pick most interesting subject and guide your data sample through ETL pipeline to make it ready for sentiment analysis.

<br>

![2](https://user-images.githubusercontent.com/26208598/56461858-839d5c00-63b1-11e9-88b9-a4c4e0bd0221.JPG)

<br>

### Manage Database

Get rid of obsolete collections from MongoDB or delete processed data from SQLite database:  

<br>

![3](https://user-images.githubusercontent.com/26208598/56461859-8435f280-63b1-11e9-82ca-2fdd7f27be71.JPG)

<br>

### Sentiment Analysis 

Apply Deep learning LSTM model on previously stored Twitter dataset. Find out what's the dominating sentiment among conversation participants - positive, negative or neutral:

<br>

![4](https://user-images.githubusercontent.com/26208598/56461860-8435f280-63b1-11e9-816d-46d989e0f853.JPG)

<br>

### Tale of Two Cities

Find out what is currently trending in two chosen locations. Specify woe_id and find out common trends:

<br>

![6](https://user-images.githubusercontent.com/26208598/56461861-8435f280-63b1-11e9-9b28-0ce89dca1a18.JPG)

<br>

### Popular Retweets


Choose a keyword and find out most popular tweets in a subject:

<br>

![7](https://user-images.githubusercontent.com/26208598/56461862-8435f280-63b1-11e9-9557-db3468aa9de3.JPG)

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

##### Images:

[Ractapopulous - Pixabay ](https://pixabay.com/users/ractapopulous-24766/?tab=popular&pagi=5)

<br>

Thank you,

Lukasz Malucha
