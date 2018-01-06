class DiceDAO:
    def __init__(self, db, collection):
        self._db = db
        self._collection = collection

    def retreiveJobs(self):
        print("Retrieving jobs")
        #print(self._url)
        #TODO: Retrieve jobs from the url and store them into mongodb
        #TODO: Handle pagination and store all of the docs in one collection

    def countJobs(self):

        print("Count the jobs for a jobTitle and location")
        print(self._collection)

        return (self._collection.count())


    def filterJobsByCity(self, city):

        #TODO: Print the jobs here one by one

        print("Filtering jobs by city")
        query = {"location": city}
        projection = {"_id":0, "detailUrl": 0}

        cursor = self._collection.find(query, projection)

        for item in cursor:
            print(item)

    def groupByLocation(self):

        print("Grouping by city and counting the number of jobs")

        query = [{"$group": {
            "_id": "$location",
            "totalJobs": {"$sum": 1}
        }}]

        cursor = self._collection.aggregate(query)

        for item in cursor:
            print(item)

    def groupJobsByCompany(self):

        print("Grouping jobs by company")

