import requests
import time
from pymongo import MongoClient

#Connect to MongoDB
clientMongo=MongoClient("mongodb://dp-group8:jaskiran@dp-project-shard-00-00.2rlvr.mongodb.net:27017,dp-project-shard-00-01.2rlvr.mongodb.net:27017,dp-project-shard-00-02.2rlvr.mongodb.net:27017/?ssl=true&replicaSet=atlas-10913e-shard-0&authSource=admin&retryWrites=true&w=majority")
dataBase = clientMongo["DataProgCrypto"]
collTable = dataBase["CryptoPrice"]

while True:
    responseAPI = requests.get('https://api.wazirx.com/sapi/v1/tickers/24hr')
    if responseAPI.status_code==200:
        
        #Ingest in MongoDB Collection
        data=responseAPI.json()
        collTable.insert_many(data)

        #Ingest after 24 hours
        time.sleep(86400)
    else:
        exit()
