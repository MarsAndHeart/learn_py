#!/usr/local/bin/python3
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]


# 升序排序
# 没有该字段的记录会排在最前面，对库里面的数据没有影响，只是取出来的数据被排序了
# mydoc = mycol.find().sort("alexa")
# for x in mydoc:
#     print(x)


# 降序排序
# 没有该字段的记录会被排在最后
mydoc = mycol.find().sort("alexa", -1)
for x in mydoc:
    print(x)
