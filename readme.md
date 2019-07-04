## Twitter API Dashboard

#### [Visit App](http://www.cork-ai.com/)


![1](https://user-images.githubusercontent.com/26208598/59977978-9578c680-95cf-11e9-83c2-13eec9e8e325.PNG)

## PROJECT OVERVIEW

Flask application hosting Twitter API. Main functionality allows user to find out what is currently trending and extract data sample to MongoDB.
Once data sample is extracted, next step is to pre-process it and load to SQL database. Final step is to apply Keras LSTM model on processed tweets to find out what's the dominating sentiment 
among conversation participants - positive, negative or neutral.



## APP STRUCTURE


### Main Dashboard View

Choose between app main functionalities:

<br>

![1](https://user-images.githubusercontent.com/26208598/59977978-9578c680-95cf-11e9-83c2-13eec9e8e325.PNG)

<br>

### Trend Search

Find out what is currently trending in US. Pick most interesting subject and guide your data sample through ETL pipeline to make it ready for sentiment analysis.

<br>

![2](https://user-images.githubusercontent.com/26208598/59977980-96115d00-95cf-11e9-8191-ae404f69d024.PNG)

<br>

### Manage Database

Get rid of obsolete collections from MongoDB or delete processed data from SQLite database:  

<br>

![3](https://user-images.githubusercontent.com/26208598/59977982-97428a00-95cf-11e9-9b22-bb09935d1fd6.PNG)

<br>

### Sentiment Analysis 

Apply Deep learning LSTM model on previously stored Twitter dataset. Find out what's the dominating sentiment among conversation participants - positive, negative or neutral:

<br>

![4](https://user-images.githubusercontent.com/26208598/59977983-9a3d7a80-95cf-11e9-83ae-5bc7d4427c9b.PNG)

<br>

### Tale of Two Cities

Find out what is currently trending in two chosen locations. Specify woe_id and find out common trends:

<br>

![5](https://user-images.githubusercontent.com/26208598/59977984-9b6ea780-95cf-11e9-87ef-7f704c2ad7bc.PNG)

<br>

### Popular Retweets


Choose a keyword and find out most popular tweets in a subject:

<br>

![6](https://user-images.githubusercontent.com/26208598/59977986-9d386b00-95cf-11e9-8a08-3814d86c39f5.PNG)

<br>

### Top 10 US Trends 

Find out what are the top Twitter trends in US at the moment. Trends are updated every 60 seconds. 

<br>

![2](https://user-images.githubusercontent.com/26208598/57719279-4dcd5980-7677-11e9-8647-9721da6eed9a.JPG)

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
