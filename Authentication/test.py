from pymongo import MongoClient

client = MongoClient('localhost', 27017)

databases = client.list_database_names()
for db in databases:
    print(db)
