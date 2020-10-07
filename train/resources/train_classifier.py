
# train logistic regression model
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from joblib import dump
from flask import json
import os
import pandas as pd
import json

def train(df):

    # local solution

    """
    data_repo = os.path.join('hello-world/data_container/' "data.json") #os.environ['DATA_REPO']
    print(data_repo)
    data_repo = "hello-world\data_container\resources\data.json"
"""

    # Select features
    X = df.loc[:, df.columns != 'labels']
    X = X.loc[:, X.columns != 'id']
    # Select label
    y = df['labels']
    X_train, X_validate, y_train, y_validate = train_test_split(X, y, train_size= 0.9)

    #train model
    clf = LogisticRegression().fit(X_train, y_train)
    y_pred_test = clf.predict(X_validate)
    y_pred_train = clf.predict(X_train)
    accuracy_test = accuracy_score(y_pred_test, y_validate)
    accuracy_train = accuracy_score(y_pred_train, y_train)



    clf_REPO = os.environ['MODEL_REPO']
    file_path = os.path.join(clf_REPO, "clf.joblib")
    dump(clf, file_path)
    return json.dumps({'message': 'The model was saved locally at ' + file_path,
                       'accuracy test':  accuracy_test,
                       'accuracy train': accuracy_train}, sort_keys=False, indent=4), 200



