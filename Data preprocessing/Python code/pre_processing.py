from flask import Flask, request

def read_json(db):
    data = request.get_json()
    return data

def pre_processing(db):

    # CONVERT LABELS TO NUMERIC!!
    pass