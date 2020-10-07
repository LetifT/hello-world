import os
import pandas as pd
from flask import Flask, request
from resources.predict_classifier import predict
from joblib import dump, load
import requests

app = Flask(__name__)


@app.route('/predict/<clf>', methods=['POST'])
def predict_classifier(clf):
    # local solution
    # df = pd.read_json(r"test_data.json", orient="split") #PATHHHHH

    # clf = load("clf.joblib")

    # enviroment solution
    content = request.get_json()
    df = pd.read_json(json.dumps(content), orient='records')

    with open('resources/column_names.json') as f:
        column_names = json.load(f)

    X_test = df.loc[:, df.columns != 'labels']

    # Select label
    # Prediction with model
    pred, message = predict(X_test, clf)
    df = X_test
    df['labels'] = pred
    API_adress = os.environ['DATA_API']
    content = df.to_json(orient='records')

    requests.post(API_adress, json=column_names)
    requests.put(API_adress, json=content)

    return message


app.config["DEBUG"] = True
app.run(host='0.0.0.0', port=5000)
