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

now = datetime.now()
newyear = datetime(year = 2026)

diff = newyear - now

print(diff)