from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi
import pymongo
import pandas as pd

def connect():
    uri = "<uri>"

    # Create a new client and connect to the server
    client = MongoClient(uri)

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    mydb = client["iot_database"]
    mycol = mydb["capteur"]

    result = []
    for x in mycol.find({},{ "_id": 0, "created":1, "temperature": 1, "humidity": 1 }).sort("created"):
        result.append(x)
    return result
