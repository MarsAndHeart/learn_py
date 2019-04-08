#!/usr/local/bin/python3
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]


# 更新找到的第一条
# myquery = {"alexa": "10000"}
# newvalues = {"$set": {"alexa": "12345"}}

# mycol.update_one(myquery, newvalues)


# 更新多条
# 如果该条记录以前没有alexa这个字段，会添加这个字段并赋值
myquery = {"name": {"$regex": "^F"}}
newvalues = {"$set": {"alexa": "123"}}

mycol.update_many(myquery, newvalues)
