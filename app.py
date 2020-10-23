import my_training
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# Opening the file
file = open("NBC_Model_final.pkl", "rb")
clf = pickle.load(file=file)
file.close()


@app.route('/', methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        comment = request.form['predict_comment']
        data = [comment]
        vectorizer_predict = my_training.vectorizer.transform(data).toarray()

        # TODO:
        #  this has to be checked after implementing the front whether is working not
        # model_predict = my_training.clf.predict(vectorizer_predict)

        model_predict = clf.predict(vectorizer_predict)
        print(model_predict)

        if model_predict == 1:
            prediction = "Spam"
            return render_template('show.html', prediction=prediction)
        elif model_predict == 0:
            prediction = "Not Spam/ Ham"
            return render_template('show.html', prediction=prediction)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
