import pandas as pd
from pymongo import MongoClient
import pymongo
import json
from dateutil.parser import parse
from bson.objectid import ObjectId
from uuid import UUID
client = MongoClient(
    "mongodb+srv://tuandat1601:tuandat160117@cluster0.hm49c7t.mongodb.net/?retryWrites=true&w=majority")
db = client['Bicing']
collection = db['adresbook']
lis_adrbook = [{'name': 'startup_log',
                'type': 'collection',
                'options': {'capped': True, 'size': 10485760},
                'info': {'readOnly': False,
                         'uuid': '8dc84e3f-b0f7-4cd5-aa28-6d5aa9b2f3cc'},
                'idIndex': {'v': 2, 'key': {'_id': 1}, 'name': '_id_'}},
               {'name': 'adressbook',
                'type': 'collection',
                'options': {},
                'info': {'readOnly': False,
                         'uuid': 'b19b1f29-1648-438f-b7db-fb584f22c14e'},
                'idIndex': {'v': 2, 'key': {'_id': 1}, 'name': '_id_'}}]
# collection.insert_many(lis_adrbook)


Name = "Jordi "  # @param {type:"string"}
Age = 34  # @param {type:"slider", min:10, max:80, step:1}
Gender = "Male"  # @param ["Male", "Female"]
Likes_Python = "Yes"  # @param ["Yes", "No"]
if Likes_Python == "Yes":
    Likes_Python = True
else:
    Likes_Python = False


# @markdown Address
# Street = "Torrent de l'Olla"  # @param {type:"string"}
# Number = 70  # @param {type:"integer"}
# City = "Barcelona"  # @param {type:"string"}
# PostalCode = "08012"  # @param {type:"string"}
# data = {'name': Name,                                    # String
#         'age': Age,                                       # Integer
#         'gender': Gender,                                 # String
#         'likes_python': Likes_Python,                     # Boolean
#         'address': {
#             # String ( special character with escape \ )
#             'street': Street,
#             'number': Number,                             # Integer
#             'city': City,                                 # String
#             'floor': None,                                # Null
#             'postalcode': PostalCode,                     # String containing a number
#         },
#         'favouriteFruits': ['banana', 'pineapple', 'orange']  # Array
#         }
# contacts = None
# with open('contacts.json', "r+", encoding='utf-8') as f:
#     contacts = f.read()

# res = json.loads(contacts)
# for raw in res:
# 	raw["registered"]= parse(raw["registered"])
contact_db = db['contac ts']
# collection.update_many({"age":{"$gte":30}},{"$set":{"favouriteCar":"BMW"}})
# contact_db.insert_many(res)
# print(collection.count_documents({"age":{"$gte":20}}))
# print(max(collection.distinct("age")))
# documents = collection.find( {"_id": {"$exists": True}} , ['name','age']).limit(1)

# itemId = ""
# for item in documents:
#   print(item)
# print(collection.index_information()     )
# result = db.bicing.create_index([('user_id',pymongo.ASCENDING)],unique=True)
# user_profiles = [ {'user_id': 211, 'name': 'Luke'}, {'user_id': 212, 'name': 'Ziltoid'}]
# db.bicing.insert_many(user_profiles)
bi = db['bicing']
print(list(bi.find()))
