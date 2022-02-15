from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll=db["workers"]

id=input("Enter worker's id: ")

ser=coll.find_one({'_id': id})
print(ser)