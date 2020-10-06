import os
import pandas as pd
from flask import Flask, request
from resources.predict_classifier import predict
from joblib import dump, load
import requests

app = Flask(__name__)

@app.route('/predict/<clf>', methods = ['POST'])
def predict_classifier(clf):
    #local solution
    #df = pd.read_json(r"test_data.json", orient="split") #PATHHHHH

    #clf = load("clf.joblib")

    #enviroment solution
    content = request.get_json()
    df = pd.read_json(json.dumps(content), orient='records')

    with open('column_names.json') as f:
        column_names = json.load(f)

    API_adress = request.remote_addr
    requests.post('http://' + API_adress + ':5000/data_container/test_data', json = column_names)
    requests.put('http://' + API_adress + ':5000/data_container/test_data', json= content)

    # Prediction with model
    prediction = predict(df, clf)

    return prediction

app.config["DEBUG"] = True
app.run(host='0.0.0.0', port=5000)
