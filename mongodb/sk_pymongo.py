import pymongo
import sys

from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

db = connection.test
zips = db.zips

def find_with_projections():
    print "Find with projections reporting to duty"

    query = {"state": "NJ"}
    projection = {"state":1, "city":1, "_id":0}

    cursor = zips.find(query, projection)

    for doc in cursor:
        print doc

find_with_projections()
