import requests
import time
from pymongo import MongoClient
from flask import Flask, request, render_template
from pymongo import MongoClient
from flask import jsonify,json
from bson.json_util import dumps

app = Flask(__name__,)


@app.route("/api/Base-Assets")
def baseassets():

    connectSrting="mongodb://dp-group8:jaskiran@dp-project-shard-00-00.2rlvr.mongodb.net:27017,dp-project-shard-00-01.2rlvr.mongodb.net:27017,dp-project-shard-00-02.2rlvr.mongodb.net:27017/?ssl=true&replicaSet=atlas-10913e-shard-0&authSource=admin&retryWrites=true&w=majority"

    clientMongo = MongoClient(connectSrting)

    dataBase = clientMongo["DataProgCrypto"]

    collTable = dataBase["CryptoPrice"]

    dataAsset = list(collTable.distinct("baseAsset"))

    return dumps(dataAsset)



@app.route("/api/alldata")

def alldata():

    connectSrting="mongodb://dp-group8:jaskiran@dp-project-shard-00-00.2rlvr.mongodb.net:27017,dp-project-shard-00-01.2rlvr.mongodb.net:27017,dp-project-shard-00-02.2rlvr.mongodb.net:27017/?ssl=true&replicaSet=atlas-10913e-shard-0&authSource=admin&retryWrites=true&w=majority"

    clientMongo = MongoClient(connectSrting)

    dataBase = clientMongo["DataProgCrypto"]

    collTable = dataBase["CryptoPrice"]

    datacrypto = list(collTable.find())

    return dumps(datacrypto)