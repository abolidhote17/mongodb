from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll=db["workers"]

id=input("Enter id: ")
nm=input("empnm: ")
dnm=input("dept: ")
pt=input("post: ")
ct=input("city: ")
sal=input("salary: ")
mob=input("mobile: ")
coll.insert_one({"_id":id,"empnm":nm,"dept":dnm,"post":pt,"city":ct,"salary":sal,"mobile":mob})

print("worker details inserted")