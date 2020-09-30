from flask import Flask, request
import os
import openml
import pandas as pd
import json

def read_json(db):
    data = request.get_json()
    return data

def load_data(db):
    fmnist = openml.datasets.get_dataset(40996)
    X, y, _, _ = fmnist.get_data(target=fmnist.default_target_attribute)
    y = y.astype(int)
    df = X
    df["labels"] = y
    data = df.to_json(orient="split")
    parsed_data = json.loads(data)


    #save data to locataion (local solution)
    my_data_file = open('data.json', 'x')
    json.dump(parsed_data, my_data_file)
    return json.dumps({'message': 'The data was saved locally.'},
                      sort_keys=False, indent=4), 200

    #save data to env location
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

