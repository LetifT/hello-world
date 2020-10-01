
# Train logistic regression model
from sklearn.linear_model import LogisticRegression
from joblib import dump, load
import os
import pandas as pd
import json

def train(clf):
    #data_repo = os.path.join('hello-world/Data preprocessing/' "data.json") #os.environ['DATA_REPO']
    #print(data_repo)
    #data_repo = "hello-world\Data preprocessing\resources\data.json"
    df = pd.read_json(r"Data preprocessing\data.json", orient="split")

    print(df)
    # Select features
    X = df.loc[:, df.columns != 'labels']

    # Select label
    y = df['labels']

    #train model
    clf = LogisticRegression().fit(X, y)
    dump(clf, 'clf.joblib')
    return json.dumps({'message': 'The model was saved locally.'},
                      sort_keys=False, indent=4), 200

    """
    clf_api = os.environ['CLF_API']
    if clf_api:
        clf.save(os.path.join(clf_api), "classifier")

    if type(classifier) == LogisticRegression:
        return 'Logistic regression model is trained'
        """

