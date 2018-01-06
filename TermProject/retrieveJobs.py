import requests

def retrieveJobs(url):

    r = requests.get(url)

    json_data = r.json()

    for item in json_data['resultItemList']:
        print("{} -> {}".format(item['jobTitle'], item['company']))


url = 'http://service.dice.com/api/rest/jobsearch/v1/simple.json?text=python&city=07059'
retrieveJobs(url)