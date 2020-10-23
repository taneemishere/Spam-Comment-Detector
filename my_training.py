import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pickle

if __name__ == '__main__':
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

    # Saving the model
    file = open("NBC_Model_final.pkl", "wb")
    pickle.dump(obj=clf, file=file)
    file.close()
