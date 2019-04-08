#!/usr/local/bin/python3
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]


# 查询集合中第一条
# x = mycol.find_one()
# print(x)


# 查询集合中所有数据
# for x in mycol.find():
# print(x)


# 查询指定字段的数据
# for x in mycol.find({}, {"_id": 0, "name": 1, "alexa": 1}):
#     print(x)


# 指定条件查询
# myquery = {"name": "RUNOOB"}
# mydoc = mycol.find(myquery)

# for x in mydoc:
#     print(x)


# 高级查询
# name 字段中第一个字母 ASCII 值大于 "H" 的数据
# myquery = {"name": {"$gt": "H"}}
# mydoc = mycol.find(myquery)

# for x in mydoc:
#     print(x)


# 正则表达式查询
# 还是正则表达式好用
myquery = {"name": {"$regex": "^G"}}
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)


# 返回指定条数
# myresult = mycol.find().limit(3)
# for x in myresult:
#     print(x)
