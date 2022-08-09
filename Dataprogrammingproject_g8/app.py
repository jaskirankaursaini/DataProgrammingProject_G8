from flask import Flask, request, render_template
from pymongo import MongoClient
from flask import jsonify,json
from bson.json_util import dumps
import pandas as pd

app = Flask(__name__,)

clientMongo=MongoClient("mongodb+srv://dp-group8:jaskiran@dp-project.2rlvr.mongodb.net/?retryWrites=true&w=majority")
dataBase = clientMongo["DataProgCrypto"]
collTable = dataBase["CryptoPrice"]
MongoData = list(collTable.find())


@app.route("/")
def home():
    return render_template("index.html",variable="Currency")

@app.route("/chart")
def chart():
    dfData = pd.DataFrame(MongoData)
    dfCrypto=dfData[['baseAsset','bidPrice']]
    dfCrypto["baseAsset"] = dfCrypto["baseAsset"].astype(str)
    dfCrypto["bidPrice"] = dfCrypto["bidPrice"].astype(float).astype(int)
    dfCrypto=dfCrypto.sort_values(by='bidPrice',ascending=False).head(10)
    dfCryptoDict = dfCrypto.to_dict('index')
    return render_template("chart.html",data=dfCryptoDict)

@app.route("/data")
def data():
    dfData = pd.DataFrame(MongoData)
    data=dfData.to_dict('index')
    return render_template("data.html",data=data) 

@app.route("/api/distinct-base-Assets")
def baseassets():
    dataAsset = list(collTable.distinct("baseAsset"))
    return dumps(dataAsset)

@app.route("/api/all-data")
def alldata():
    return dumps(MongoData)

if __name__=='__main_':
    app.run(debug=True,host="0.0.0.0")
