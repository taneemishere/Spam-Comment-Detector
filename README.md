# Spam-Comment-Detector
A Machine Learning Application that when you provide a comment and in return it predicts you whether it is spam or not.
This will going to be a full fledge application that will has a proper front and back end. 

## The Application Working
The appplication works as when user enters a comment in a HTML form, which is the ```index.html``` file, then that text captured by the "POST" method goes to the backend Python application based on 
Flask. Then there is Machine Learning model that is trained over to make prediction or more specifically to classify whether the entered comment or say text is 
spam or not spam (Ham). Now when everthing is completed and the model predicts it, then by the "GET" method the Flask application sends that prediction to the HTML form 
which is shown in the ```show.html``` file.\
The Ham word I first read in the book "Thoughtful Machine Learning with Python: A Test-Driven Approach" by Matthew Kirk in O'REILLY Series, while 
reading the Naive Bayes Classification chapter.

## The Model
The machine learning model working under the hood is the Nive Bayes Classifier which does really well in doing prediction about the spam classification.
The Naive Bayes Classifiers is supervised learning algorithms that are base on the Bayes Theorem. And these algorithms did really well on the data where every 
data point or say featrues are independent of each other. Some of the Naive Bayes Classifiers are:

-	#### Multinomial Naive Bayes: 
which we used in this project. And this classifier is typically used for the document classification
-	#### Bernoulli Naive Bayes:
This is used for binary classification in documents like a word occured or not in this document.
-	#### Gaussian Naive Bayes: 
This one is based on the conitinous distribution.

## The Data:
The data used in this project is taken from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/YouTube+Spam+Collection#:~:text=UCI%20Machine%20Learning%20Repository%3A%20YouTube%20Spam%20Collection%20Data%20Set&text=Abstract%3A%20It%20is%20a%20public,viewed%20on%20the%20collection%20period.).
It does contain 5 datasets from different artits' vidoes. The after analyzing all the datasets it 
we only come up with missing values in the ```Youtube04-Eminem.csv``` dataset, which was not that 
much important like it was in dates. And for this project we don't need to mess up with the dates. 
Then all the five datasets are concatenated into one. And then assign keys to everyone so that if 
we need to inspect specific, it would be easy for us to do so. And so finally we considered taking 
the data under ```CONTENT``` and ```CLASS``` columns. 

## The Code Flow
After describing the data into a single dataframe then extract the features from the comments into 
vector for our model. So we converted through vectorization our contents or say comments into crunching 
numbers so that it is awesome for our model.\
Then split the data into training and testing sets, 33% given to the testing. Then traing the 
classifier over the 66% of the data and yooooo we get 91.95% of total accuracy over testing sets.\
For the future prediction we've to use that pipelining as to first convert the text via the 
```CountVectorizer``` so that our model gets the same shaped data by which it is trained. 
