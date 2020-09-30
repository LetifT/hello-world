from flask import Flask, request

from resources.pre_processing import read_json, load_data
app = Flask(__name__)




@app.route('/pre-processing/<db>', methods = ['POST'])
def select_sample(db):
    message = load_data(db)

    return message

app.run(debug=True)
app.run(host='0.0.0.0', port=5000)