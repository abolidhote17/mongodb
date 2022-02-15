from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll=db["workers"]

id=input("Enter id to update city and department: ")
data=coll.find_one({"_id":id})
if data:
    ncty=input("New city: ")
    ndept=input("New Deptartmet: ")

    coll.find_one_and_update({"_id":id},{"$set":{"city":ncty,"dept":ndept}})
    print("updated successfully")
    print(coll.find_one({"_id":id}))

if not data:
    print("worker not found")
    