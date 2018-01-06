import pymongo

from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

db = connection.test

# handle to names collection
names = db.zips

item = names.find_one()

print item['state']