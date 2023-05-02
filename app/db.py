from pymongo import MongoClient

client = MongoClient('localhost',27017)

# vamos a conectar a una db
db = client["character_bd_proy3"]