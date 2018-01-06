import json
import urllib.request

# get the dice jobs
dice_jobs = urllib.request.urlopen("http://service.dice.com/api/rest/jobsearch/v1/simple.json?text=mongodb&city=07059")
parsed = json.loads(dice_jobs.read())
count = 0

for item in parsed['resultItemList']:
    count += 1

# check if nextURL exists
while parsed['count'] != parsed['lastDocument']:

    print("Count = {}".format(parsed['count']))
    print("LastDocument = {}".format(parsed['lastDocument']))

    #get nextUrl
    nextURL = parsed['nextUrl']
    diceJobs = urllib.request.urlopen("http://service.dice.com" + nextURL)

    parsed = json.loads(diceJobs.read())
    for item in parsed['resultItemList']:
        count += 1

print("Final Count = {}".format(count))