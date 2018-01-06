import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.school
people = db.people
people.drop()


def insert(peopleList):
    print("insert reporting for duty")

    for item in peopleList:
        people.insert_one(item)


def main():
    peopleList = [
        {"name": "Smith", "age": 30, "profession": "hacker"},
        {"name": "Jones", "age": 35, "profession": "baker"},
        {"name": "Alice"},
        {"name": "Bob"},
        {"name": "Charlie"},
        {"name": "Dave"},
        {"name": "Edgar"},
        {"name": "Fred"},
        {"name": 42}
    ]

    insert(peopleList)

    for item in people.find():
        print(item)

if __name__ == "__main__":
    main()


