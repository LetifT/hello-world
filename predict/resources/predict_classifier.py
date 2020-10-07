from sklearn.linear_model import LogisticRegression
import os
import json
from joblib import load

def predict(df,clf):
    model_repo = os.environ['MODEL_REPO']
    file_path = os.path.join(model_repo, "clf.joblib")
    clf = load(file_path, 'clf.joblib')
    X_test = df

    # predict and put it in the right format
    pred = list(clf.predict(X_test))
    pred_dict= {'labels_pred': pred}

    #pred_api = os.environ['PRED_API']
    #json.dump(pred_dict, open('prediction.json', 'w'))
    return pred, json.dumps({'message': 'The predictions were saved locally.',
                        'prediction': pred_dict['labels_pred']}, sort_keys=False, indent=4), 200



