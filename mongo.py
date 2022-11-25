import pymongo                            # Library to access MongoDB
from pymongo import MongoClient           # Imports MongoClient
import pandas as pd                       # Library to work with dataframes
import folium
import requests
import csv
from bson.objectid import ObjectId
# dataset = "https://raw.githubusercontent.com/Giffy/MongoDB_PyMongo_Tutorial/master/resources/bicing_data.csv"
# data = pd.read_csv(dataset)

# print(data.head())
client = MongoClient(
    "mongodb+srv://tuandat1601:tuandat160117@cluster0.hm49c7t.mongodb.net/?retryWrites=true&w=majority")
print(client.list_database_names())
# db = client['Bicing']
# collection = db['bicing']
# num_documents = collection.count_documents(
#     {'_id': {'$exists': 1}})     # Counts the documents in database
# print('Number of documents in database = ' + str(num_documents))
# bikes_list = list(collection.distinct('age'))
# for num in bikes_list:
# 	collection.update_many({'age':num},{'$set':{"age":num+1}})
# filters = {'age': {'$gte': 20}}
# filted = {"_id", "name", "age", "longitude"}
# query = list(collection.find(filters, filted))
# df = pd.DataFrame(query)
# print(df.iloc[0])

# post1 = {"_id":ObjectId(),"name":"tuong","age":20}
# collection.insert_one(post1)





# center_lat = 41.378
# center_lon = 2.139

# locationmap = folium.Map(
#     location=[center_lat, center_lon], zoom_start=16, width=800, height=600)
# longitud = len(data)

# for i in range(longitud):
#     lng = float(data.iloc[i]['longitude'])
#     lat = float(data.iloc[i]['latitude'])
#     description = 'Bikes: ' + \
#         str(data.iloc[i]['longitude']) + \
#         'Empty slots: ' + str(data.iloc[i]['latitude'])
#     folium.Marker([lat, lng],
#                   popup=description,
#                   icon=folium.Icon(color='red')).add_to(locationmap)
# locationmap.save("index2.html")

