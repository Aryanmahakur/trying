import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db=client["database2"]
collection=db["db2collection"]

if collection.count_documents({}) == 0:
   
  dataenters=[
    {"name":"John Doe","age":25,"city":"New York"},
    {"name":"Jane Doe","age":30,"city":"Los Angeles"},
    {"name":"Mike Smith","age":28,"city":"Chicago"}
 ]
  collection.insert_many(dataenters)

for doc in collection.find({"age":{ "$gt":25}}):
    print(doc)
doc=collection.find_one({"name":"John Doe"})
print(doc)
query=({"age":{"$gt":25}})
for doc in collection.find(query):
    print(doc)
    
query={"name":"John Doe"}
newage=collection.update_one(query,{"$set":{"age":26}})
print(newage)

query={"name":"John Doe"}
newvalue= ({"$set":{"city":"Chicago"}})
newcity= collection.update_one(query,newvalue)
print(newcity)
collection.delete_one({"name":"John Doe"})

totalstudent = collection.count_documents({})
print("Total students:", totalstudent)

for doc in collection.find().sort("age",1):
    print(doc)

for doc in collection.find({"city":{"$in":["New York","Los Angeles"]}}):
    print(doc)

pipeline = [{"$group":{"_id":"$city","count":{"$sum":1}}}]
result= list(collection.aggregate(pipeline))
print(result)


pipeline = [
    {"$sort": {"age": 1}},  # Sort in ascending order
    {"$limit": 1}  # Take only the first document
]
youngest_student = list(collection.aggregate(pipeline))[0]
print("Youngest Student:", youngest_student)

#find student whose name starts with J
query = {"name": {"$regex": "^J"}}
for doc in collection.find(query):
    print(doc)

dataentry2 = [
    {
    "name": "Alice",
    "age": 21,
    "city": "Chicago",
    "courses": [
        {"name": "Math", "grade": "A"},
        {"name": "Physics", "grade": "B"}
    ]
}

    ]
collection.insert_many(dataentry2)
for doc in collection.find():
    print(doc)
for doc in collection.find({"courses.name":"Math"}):
    print("mydata",doc)  

collection.create_index("name")
print(collection.index_information())


bulk=[
    pymongo.InsertOne({"name":"John","age":28}),
    pymongo.InsertOne({"name":"Jane","age":25}),
    pymongo.InsertOne({"name":"Mike","age":30})
]
collection.bulk_write(bulk)
a