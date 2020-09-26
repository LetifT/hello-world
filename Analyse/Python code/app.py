import os
import pandas as pd

from flask import Flask, request
app = Flask(__name__)

@app.route('/analyse/<clf>', methods = ['POST'])
def analyse_train(clf):
    pass

app.run(debug=True)
app.run(host='0.0.0.0', port=5000)