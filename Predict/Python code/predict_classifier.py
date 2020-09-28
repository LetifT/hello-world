from sklearn.linear_model import LogisticRegression

def predict(df):
    clf_api = os.environ['CLF_API']
    if clf_api:

        #Load model from envir var
        clf = load.model(os.path.join(clf_api))

        # Predict and put it in the right format
        pred = list(clf.predict(x))
        pred_dict= {'labels_pred': pred}

        pred_api = os.environ['PRED_API']
        if pred_api:
            pred.save(os.path.join(pred_api), "predictions")
            return 'Model predictions are created'

    else:
        return "Model can't be found"