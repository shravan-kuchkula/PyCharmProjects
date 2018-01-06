import json
import urllib.request
import pymongo

# connect to mongo
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to jobs db
db = connection.jobs

# get a handle to dice collection
pythonJobsWarren = db.pythonJobsWarren

# drop existing collection
pythonJobsWarren.drop()

# get the dice jobs
dice_jobs = urllib.request.urlopen("http://service.dice.com/api/rest/jobsearch/v1/simple.json?text=python&city=07059")
parsed = json.loads(dice_jobs.read())

# iterate and insert jobs
for item in parsed['resultItemList']:
    pythonJobsWarren.insert_one(item)

# for paginated results
while parsed['count'] != parsed['lastDocument']:

    # get nextUrl for paginated results
    nextURL = parsed['nextUrl']
    dice_jobs = urllib.request.urlopen("http://service.dice.com" + nextURL)

    parsed = json.loads(dice_jobs.read())
    for item in parsed['resultItemList']:
        pythonJobsWarren.insert_one(item)