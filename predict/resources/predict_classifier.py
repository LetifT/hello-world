from sklearn.linear_model import LogisticRegression
import os
import json
from joblib import load

def predict(df,clf):
    #clf_api = os.environ['CLF_API']
    model_api = os.environ("MODEL_API")
    clf = requests.get(model_api)

    X_test = df


    # predict and put it in the right format
    pred = list(clf.predict(X_test))
    pred_dict= {'labels_pred': pred}

    #pred_api = os.environ['PRED_API']
    json.dump(pred_dict, open('prediction.json', 'w'))
    return json.dumps({'message': 'The predictions were saved locally.',
                        'prediction': pred_dict['labels_pred'],
                        'real': y_test}, sort_keys=False, indent=4), 200


    pred_api = os.environ['PRED_REPO']
        if pred_api:
            pred.save(os.path.join(pred_api), "predictions")
            return 'Model predictions are created'

    else:

        return "Model can't be found"
        

