import pymongo
import sys

from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

db = connection.school
scores = db.scores

def find_one():
    print "Find One reporting for duty"
    query = {'student_id':1}

    try:
        doc = scores.find_one(query)

    except:
        print "Unexpected error: ", type(e), e


    print doc


def find():
    print "Find reporting for duty"
    query = {'student_id': 1}

    try:
        cursor = scores.find(query)

    except:
        print "Unexpected error: ", type(e), e

    for doc in cursor:
        print doc



#find_one()
find()