

from flask import Flask, request
from resources.train_classifier import train
app = Flask(__name__)

@app.route('/train/<clf>', methods = ['POST'])
def train_classifier(clf):
    data_api = os.environ['DATA_API']
    data_json = request.get(data_api).json()
    df = pd.DataFrame.from_dict(data_json)

    message = train(df)

    return message

@app.route('/train/<clf>', methods = ['GET'])
def get_model(clf):
    model_repo = os.environ['MODEL_REPO']
    file_path = os.path.join(model_repo, "model.h5")
    model = load_model(file_path)
    return model


app.config["DEBUG"] = True
app.run(host='0.0.0.0', port=5000)