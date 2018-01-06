import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.school
students = db.students

def getLowestHomeworkScore():

    cursor = students.find()

    minList = []
    for item in cursor:
        scores = item['scores']
        minScore = 100
        for type in scores:
            if type['type'] == "homework":
                if type['score'] <= minScore:
                    minScore = type['score']
        minList.append(minScore)
    return minList

def removeLowestHomework(id, score):

    query = {"_id":id}
    #updateArg = {"scores": {"$pull": {"type": "homework", "score": score}}}
    updateArg = {"$pull": {"scores": {"type": "homework", "score": score}}}

    result = students.update_one(query, updateArg)

    print(result.matched_count)

def updateInBulk():

    print("Update in bulk reporting for duty")







# This was previously main
def solution():
    minList = getLowestHomeworkScore()
    print(len(minList))
    id = 0
    for item in minList:
        removeLowestHomework(id, item)
        id += 1

def main():




if __name__ == "__main__":
    main()

