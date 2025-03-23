print("hello world")
from pymongo import MongoClient

# Connect to MongoDB (Default: localhost:27017)
client = MongoClient("mongodb://localhost:27017/")

# Create/Get Database
db = client["test_database"]

# Create/Get Collection
collection = db["test_collection"]

# Insert Sample Document
test_doc = {"name": "John Doe", "age": 25, "city": "New York"}
insert_result = collection.insert_one(test_doc)

# Retrieve and Print Inserted Document
retrieved_doc = collection.find_one({"_id": insert_result.inserted_id})
print("Inserted Document:", retrieved_doc)

# Print all documents in the collection
print("All Documents in Collection:")
for doc in collection.find():
    print(doc)

# Close Connection
client.close()
