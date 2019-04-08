#!/usr/local/bin/python3
import pymongo

# 连接
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]


# 插入
# mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
# x = mycol.insert_one(mydict)
# print(x)

# 返回id
# mydict = {"name": "Google", "alexa": "1", "url": "https://www.google.com"}
# x = mycol.insert_one(mydict)
# print(x.inserted_id)

# 插入多条
# mylist = [
#     {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
#     {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
#     {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
#     {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
#     {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
# ]
# x = mycol.insert_many(mylist)
# print(x.inserted_ids)


# 插入多条并指定_id
mylist = [
    {"_id": 1, "name": "RUNOOB", "cn_name": "菜鸟教程"},
    {"_id": 2, "name": "Google", "address": "Google 搜索"},
    {"_id": 3, "name": "Facebook", "address": "脸书"},
    {"_id": 4, "name": "Taobao", "address": "淘宝"},
    {"_id": 5, "name": "Zhihu", "address": "知乎"}
]

x = mycol.insert_many(mylist)

# 输出插入的所有文档对应的 _id 值
print(x.inserted_ids)
