from flask import Flask, request
import os
import openml
import pandas as pd
import json
from sklearn.model_selection import train_test_split

def add_data(db):
    #get data
    data = request.get_json()
    df.append(array, ignore_index =  True)
    return data


def load_data(db):
    fmnist = openml.datasets.get_dataset(40996)
    X, y, _, _ = fmnist.get_data(target=fmnist.default_target_attribute)
    X, X_test, y, y_test = train_test_split(X, y, train_size=0.9)

    y = y.astype(int)
    df = X
    df["labels"] = y

    y_test = y.astype(int)
    df_test = X_test
    df_test["labels"] = y_test


    data = df.to_json( orient='split')
    parsed_data = json.loads(data)

    test_data = df_test.to_json(orient='split')
    parsed_test_data = json.loads(test_data)

    #save data to locataion (local solution)
    my_data_file = open('data.json', 'x')
    json.dump(parsed_data, my_data_file)

    my_test_data_file = open('test_data.json', 'x')
    json.dump(parsed_data, my_test_data_file)

    return json.dumps({'message': 'The data was saved locally.'},
                      sort_keys=False, indent=4), 200

    #save data to env location --- make exception if data is already loaded
    """""
    #data_repo = os.environ['DATA_REPRO']
    if data_repo:
        file_path = os.path.join(data, "data")
        data.save(file_path)
    else:
        data.save("data")
        return json.dumps({'message': 'The data was saved locally.'},
                          sort_keys=False, indent=4), 200
    pass
    """""

