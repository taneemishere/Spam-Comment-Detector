from flask import Flask, render_template, request
import pandas as pd
# import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pickle

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    load_data = pd.read_csv('final_dataframe.csv')
    data_df = load_data[["CONTENT", "CLASS"]]

    # Our features and label
    data_feature = data_df['CONTENT']
    data_label = data_df['CLASS']

    # Extracting features from text
    corpus = data_feature
    vectorizer = CountVectorizer()

    # Fit the data (feature) which is in corpus
    X = vectorizer.fit_transform(corpus)

    # Splitting the data into training and testing
    X_train, X_test, y_train, y_test = train_test_split(
        X, data_label, test_size=0.33, random_state=42
    )

    # Building the model
    clf = MultinomialNB()
    clf.fit(X_train, y_train)

    clf.score(X_test, y_test)

    print("Model Score is: ", clf.score(X_test, y_test))

    if request.method == "POST":
        predict_comment = request.form['predict_comment']
        data = [predict_comment]
        print("The received comment is: ", data)
        vectorizer_predict = vectorizer.transform(data).toarray()
        model_prediction = clf.predict(vectorizer_predict)

        if model_prediction == [1]:
            model_prediction = "Spam"

        elif model_prediction == [0]:
            model_prediction = "Not Spam/ Ham"

    return render_template('show.html', prediction=model_prediction)


if __name__ == '__main__':
    app.run(debug=True)
