import os
import pandas as pd

from flask import Flask, request
from predict_classifier import predict

app = Flask(__name__)

@app.route('/predict/<clf>', methods = ['POST'])
def predict_classifier(clf):
    data_json = request.get_json()

    # Prediction with model
    message = predict(pd.DataFrame.from_dict(data_json))

    return message


app.run(debug=True)
app.run(host='0.0.0.0', port=5000)