from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll1=db["workers"]
coll2=db["exworkers"]

id=input("Enter id to delete: ")
data=coll1.find_one_and_delete({"_id":id})
if data:
    print(data)
    print("account deleted ")
    coll2.insert_one(data)
    print("inserted into exworkers")
else:
    print("id not found")