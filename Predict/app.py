import os
import pandas as pd

from flask import Flask, request
from resources.predict_classifier import predict
from joblib import dump, load
app = Flask(__name__)

@app.route('/predict/<clf>', methods = ['POST'])
def predict_classifier(clf):
    data_json = pd.read_json(r"test_data.json", orient="split") #PATHHHHH
    clf = load("clf.joblib")
    # Prediction with model
    prediction = predict(data_json, clf)

    return prediction


app.run(debug=True)
app.run(host='0.0.0.0', port=5000)