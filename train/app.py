from joblib import load
import requests
from flask import Flask, request, json
from resources.train_classifier import train
import pandas as pd
import json

app = Flask(__name__)
import os
@app.route('/train/<clf>', methods = ['POST'])
def train_classifier(clf):
    data_api = os.environ['DATA_API']
    data_json = requests.get(data_api).json()
    df = pd.DataFrame.from_dict(data_json)

    message = train(df)

    return message

@app.route('/train/<clf>', methods = ['GET'])
def get_model(clf):
    model_repo = os.environ['MODEL_REPO']
    file_path = os.path.join(model_repo, "clf.joblib")
    clf = load(file_path)
    return clf


app.config["DEBUG"] = True
app.run(host='0.0.0.0', port=5000)