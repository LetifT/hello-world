from flask import Flask, request

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/pre-processing/<db>', methods = ['POST'])
def read_json(db):
    data = request.get_json()

    return 'Hello'

if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)