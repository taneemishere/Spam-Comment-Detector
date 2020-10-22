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
