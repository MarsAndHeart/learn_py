#!/usr/local/bin/python3
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]


# 删除一条
# myquery = {"name": "Taobao"}
# mycol.delete_one(myquery)


# 删除多条
# myquery = {"name": {"$regex": "^Z"}}
# x = mycol.delete_many(myquery)
# print(x.deleted_count, "条记录已删除")


# 删除集合中所有文档
# mycol.delete_many({})


# 删除一个集合
mycol.drop()
