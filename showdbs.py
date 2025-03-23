import pymongo

# Connect to MongoDB (default: localhost:27017)
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create the Database named "database1"
db = client["database1"]

# Create a Collection (Table)
collection = db["users"]

# Insert Sample Documents if Collection is Empty
if collection.count_documents({}) == 0:
    data_list = [
        {"name": "Alice", "age": 30, "city": "London"},
        {"name": "Charlie", "age": 35, "city": "Los Angeles"},
        {"name": "David", "age": 40, "city": "Chicago"},
        {"name": "Emma", "age": 22, "city": "San Francisco"}
    ]
    collection.insert_many(data_list)
    print("Inserted sample documents!")

# Function to display all documents
def display_all():
    print("\n--- All Users in database1 ---")
    for doc in collection.find():
        print(doc)

# Function to find a user by name
def find_by_name(name):
    print(f"\n--- Finding user with name '{name}' ---")
    doc = collection.find_one({"name": name})
    print(doc)

# Function to find users with age > 30
def find_age_gt_30():
    print("\n--- Users with age > 30 ---")
    query = {"age": {"$gt": 30}}  # $gt means "greater than"
    for doc in collection.find(query):
        print(doc)

# Function to display only name and age
def display_name_age():
    print("\n--- Displaying only Name and Age ---")
    query = {}  # Empty query means all documents
    projection = {"_id": 0, "name": 1, "age": 1}  # Show only 'name' and 'age'
    for doc in collection.find(query, projection):
        print(doc)

# Function to count total documents
def count_documents():
    count = collection.count_documents({})
    print("\nTotal Documents:", count)

# Execute functions
display_all()
find_by_name("Alice")
find_age_gt_30()
display_name_age()
count_documents()

#update a document
collection.update_one({"name":"Alice"},{"$set":{"city":"New York"}})
collection.update_many({"age":{"$gt":30}},{"$set":{"city":"delhi"}})
collection.update_one({"name": "David"}, {"$inc": {"age": 5}})
collection.update_many({"name":"david"}, {"$rename": {"delhi": "mumbai"}})

collection.delete_one({"name":"Alice"})
collection.delete_many({"age": {"$lt": 25}})

#sorting
a= collection.find().sort("name")
print(a)
data1= {"name":"Alices","age":30,"city":"London"}
collection.insert_one(data1)
for doc in collection.find().sort("age", 1):
    print(doc)

for doc in collection.find().limit(2):
    print(doc)
collection.create_index("name")

print(collection.index_information())

#avg age of doc list
pipeline = [
    {"$group": {"_id": None, "average_age": {"$avg": "$age"}}}
]

result = list(collection.aggregate(pipeline))  # Convert cursor to list
print(result)
pipeline = [
    {"$group": {"_id": "$city", "count": {"$sum": 1}}}
]
for doc in collection.aggregate(pipeline):
    print(doc)
pipeline = [
    {"$match": {"age": {"$gt": 30}}},
    {"$sort": {"age": 1}}
]
for doc in collection.aggregate(pipeline):
    print(doc)

requests = [
    pymongo.InsertOne({"name": "John", "age": 28}),
    pymongo.UpdateOne({"name": "Alice"}, {"$set": {"city": "Paris"}}),
    pymongo.DeleteOne({"name": "David"})
]
collection.bulk_write(requests)
for doc in collection.find():
    print(doc)

    #show all db
print(client.list_database_names())
#show all collections
print(db.list_collection_names())

col=client['database1']
print(col.list_collection_names())
