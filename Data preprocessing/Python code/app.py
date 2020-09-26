from flask import Flask, request

from pre_processing import read_json
app = Flask(__name__)

@app.route('/pre-processing/<db>', methods = ['POST'])
def select_sample(db):
    data = read_json(db)

    #Pre-processing steps ....

    return data

app.run(debug=True)
app.run(host='0.0.0.0', port=5000)