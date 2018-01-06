import pymongo

from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

db = connection.test

# handle to jobs collection
jobs = db.jobs

def insertIntoMongo():
    print("Insert into Mongo reporting for duty")
    print("Inserting a random job")

    job = {"title":"Software Engineer", "Company":"JPMC", "Salary":"100k", "Location":"NY"}

    jobs.insert_one(job)

    print(job)

def insertManyDocs():
    print("Inserting many documents")

# Is this file's default name main ? if so go ahead.
if __name__ == '__main__':
    insertIntoMongo()



