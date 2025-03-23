import pymongo

# Connect to MongoDB (Default: localhost:27017)
if __name__ == "__main__":
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db=client["db_test"]
    collection=db["collection_test"]
    # dictio={"name":"John Doe","age":25,"city":"New York"}
    # collection.insert_one(dictio)
    # insertthese=[
    #     {"name":"John Doe","age":25,"city":"New York"},
    #     {"name":"Jane Doe","age":24,"city":"New York"},
    #     {"name":"John Smith","age":30,"city":"Los Angeles"}
    # ]
    # collection.insert_many(insertthese)
   
    #find
    one=collection.find_one({"name":"John Doe"},{'name':1,'_id':0})
    # many=collection.find({"city":"New York"},{'name':1,'_id':0}) 
    print(one)
    # print(many)
#  for item in many:
# #     print(item)
