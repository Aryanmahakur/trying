import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
db=client["database1"]
collection=db["users"]

dataenter={"name2":"John Doe","age":25,
 "city":"New York"
  }
collection.insert_one(dataenter)
print(client.list_database_names())

print(db.list_collection_names())
dataenter2 = [
    {"name3": "John Doe", "age": 25, "city": "New York"},
    {"name3": "Jane Doe", "age": 30, "city": "Los Angeles"},
    {"name3": "Mike Smith", "age": 28, "city": "Chicago"}
]

collection.insert_many(dataenter2)


# # for doc in collection.find():
# #     print(doc)
# doc =collection.find_one({"name3":"John Doe"})
# print(doc)
# query = {"age": {"$gt": 25}}
# for doc in collection.find(query):
#     print(doc)
print(collection.count_documents({}))
print(collection.find().sort("name3",1))