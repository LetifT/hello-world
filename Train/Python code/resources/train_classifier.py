import os

# Train logistic regression model
def train(df):

    # Select features
    x = df.loc[:, X.columns != 'labels']

    # Select label
    y = df['labels']

    #train model
    clf = LogisticRegression().fit(x, y)

    clf_api = os.environ['CLF_API']
    if repo_clf:
        clf.save(os.path.join(clf_api), "classifier")