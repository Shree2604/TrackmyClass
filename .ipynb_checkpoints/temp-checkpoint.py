import pymongo
from bson.objectid import ObjectId 
from bson.json_util import dumps
import os 
import json
from datetime import datetime
import hashlib

MONGODB_URI = 'mongodb+srv://Pubzeee1311:12345@30daysofpython.xpenqyh.mongodb.net/'
client = pymongo.MongoClient(MONGODB_URI)
db = client['TrackmyClass']

db.users.insert_one({"username":"cr","password":"password","role":"cr"})
db.users.insert_one({"username":"admin","password":"password","role":"admin"})
db.users.insert_one({"username":"student","password":"password","role":"student"})