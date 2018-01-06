import json
import urllib.request
import pymongo

# connect to mongo
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the jobs database
db = connection.jobs
jobs = db.jobs

# get the dice jobs
dice_jobs = urllib.request.urlopen("http://service.dice.com/api/rest/jobsearch/v1/simple.json?text=mongodb&city=07059")

parsed = json.loads(dice_jobs.read())

# check if nextURL exists
while parsed['count'] != parsed['lastDocument']:

    for item in parsed['resultItemList']:
        #print(item)
        jobs.insert_one(item)

    #get nextUrl
    nextURL = parsed['nextUrl']
    diceJobs = urllib.request.urlopen("http://service.dice.com" + nextURL)

    parsed = json.loads(diceJobs.read())
