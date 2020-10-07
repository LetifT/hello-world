from flask import Flask, request
import os
import openml
import pandas as pd
import json
from sklearn.model_selection import train_test_split
import sqlalchemy as db
from sqlalchemy import Column, Float, Table, Integer
from sqlalchemy.ext.declarative import declarative_base

engine = db.create_engine('sqlite:///trainingdata.db', echo=True)
Base = declarative_base()
Base.metadata.reflect(engine)


def create_tb(table_name, column_names):
    conn = engine.connect()
    trans = conn.begin()
    columns = (Column(name, Float, quote=False) for name in column_names)
    v_table = Table(table_name, Base.metadata, Column('id', Integer, primary_key=True, autoincrement=True),
                    extend_existing=True, *columns)
    v_table.create(engine, checkfirst=True)
    trans.commit()

def drop_tb(table_name):
    conn = engine.connect()
    trans = conn.begin()
    v_table = Base.metadata.tables[table_name]
    v_table.drop(engine, checkfirst=True)
    trans.commit()


def add_data_records(table_name, records):
    v_table = Base.metadata.tables[table_name]
    query = db.insert(v_table)
    connection = engine.connect()
    trans = connection.begin()
    connection.execute(query, records)
    trans.commit()


def read_data_records(table_name):
    v_table = Base.metadata.tables[table_name]
    connection = engine.connect()
    trans = connection.begin()
    query = db.select([v_table]).limit(100)
    df = pd.read_sql_query(query, con=connection)
    trans.commit()
    return df


def load_data(table_name):
    #This does not work in the kubernetes
    #download data and transform in DF
    fmnist = openml.datasets.get_dataset(40996)
    X, y, _, _ = fmnist.get_data(target=fmnist.default_target_attribute)
    X, _, y, _ = train_test_split(X, y, train_size=0.1)
    y = y.astype(int)
    df = X
    df["labels"] = y
    #create new table and store data in table
    column_names = list(df.columns)
    conn = engine.connect()
    trans = conn.begin()
    columns = (Column(name, Float, quote=False) for name in column_names)
    v_table = Table(table_name, Base.metadata, Column('id', Integer, primary_key=True, autoincrement=True),
                    extend_existing=True, *columns)
    v_table.create(engine, checkfirst=True)
    return json.dumps({'message': 'The data was saved locally.'}, #hoort hier niet
                      sort_keys=False, indent=4), 200



    #save data to locataion (local solution)

    data = df.to_json(orient='records')

    """"
    parsed_data = json.loads(data)
    my_data_file = open('data.json', 'x')
    json.dump(parsed_data, my_data_file)

    return json.dumps({'message': 'The data was saved locally.'},
                      sort_keys=False, indent=4), 200 """

    #save data to env location --- make exception if data is already loaded
    v_table = Base.metadata.tables[table_name]
    query = db.insert(v_table)
    connection = engine.connect()
    records = json.loads(data)
    trans = connection.begin()
    connection.execute(query, records)
    trans.commit()
  #  return json.dumps({'message': 'The data was saved locally.'},
  #                    sort_keys=False, indent=4), 200