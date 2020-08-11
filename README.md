# umatter-mental-health-prediction
Machine Learning for Mental Health Prediction

This is a Web Application that uses a Twitter username to access most recent public tweets of a given user, and analyzes the sentiment of those tweets using a custom-built NLP model using [this](http://help.sentiment140.com/for-students) dataset from Stanford University
to predict the mental health of the user

## The Problem

According to the National Association of Mental Illnesses (NAMI) one in 5 college students experience a mental health condition. While there are resources put out by universities to help them, they are often overwhelmed by the sheer number of students to support.

Increasing the staffing of mental heatlh support staff members is one way to mitigate the problem, but that has a lot of administrative decisions to be made that may not be impacted by one individual. So, this project proposes the solution of instead increasing the amount of impact each support staff member can have.

## The Solution

We use the recent social media history (currently, only Twitter) to predict the sentiment of each tweet and create a weighted score (where most recent tweets weigh the most and older tweets weigh lesser) that can be correlated to the user's mental health.

## Solution Architecture

### Machine Learning (ML):
- We create a support vector machine (SVM) model using the scikit-learn library that is trained on 1.6+ million labelled (positive, negative, or neutral) tweets from the Sentiment140 dataset (linked above) from Stanford University.
- Accuracy of said model: **77.125%**

### Web Technology:
#### Backend
- We run the ML training job as soon as the application is started
- We expose the API endpoint that the front-end hits with the username and number of tweets to process
- When this API endpoint is triggered, we pull tweets from Twitter's API and run them against the ML model previously mentioned, and the processed data is sent as a response to the front-end

#### Frontend
- Allows user to enter the Twitter username and number of tweets to process, and hit 'Search' to query the backend
- Displays reports and aggregations, including a donut chart and our weighted mental health score
- Chronologically displays recent tweets and shows the sentiment expressed in each

