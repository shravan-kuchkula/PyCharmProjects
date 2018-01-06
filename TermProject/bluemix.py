import pymongo

# connect to mongo
#connection = pymongo.MongoClient("mongodb://admin:XKHWOTZGLJTCHADJ@sl-us-south-1-portal.5.dblayer.com:18885,sl-us-south-1-portal.3.dblayer.com:18885/compose?ssl=false&authSource=admin")
#connection = pymongo.MongoClient("mongodb://admin:XKHWOTZGLJTCHADJ@sl-us-south-1-portal.5.dblayer.com:18885/compose")
connection = pymongo.MongoClient("mongodb://admin:XKHWOTZGLJTCHADJ@sl-us-south-1-portal.5.dblayer.com:18885/test")

# get a handle to jobs db
db = connection.myinfo

# get a handle to dice collection
empinfo = db.empinfo

empinfo.find_one()
