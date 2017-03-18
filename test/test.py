# -*- coding: utf-8 -*-
from db.db_conn.db_mongo import MongoConn
import json
# coding=utf-8
import xlrd
import sys
import json
import pymongo
from pymongo import MongoClient
# from db_conn.cont_redis import g_session_redis

def test(id):
    key = "bankcard"
    kwargs = {

            "card_holder": "xixin",
            "card_num": "62170020",
            "idcard": "412822"
    }

    MongoConn().db["ssid"].insert({"_id": id},json.dumps(kwargs))
    # MongoConn().db["ssid"].update({"_id": id}, {"$set": {"bankcard": kwargs}})


def test2():
    # 读取商品条形码表格
    account = MongoConn().db["goods_PIN"]
    data = xlrd.open_workbook('D:\PIN.xls')
    table = data.sheets()[0]
    # 读取excel第一行数据作为存入mongodb的字段名
    # rowstag = table.row_values(0)
    # print rowstag

    rowstag = ["_id", "goodsName", "specification"]
    nrows = table.nrows
    # ncols=table.ncols
    # print rows
    returnData = {}
    for i in range(1, nrows):
        # 将字段名和excel数据存储为字典形式，并转换为json格式
        returnData[i] = json.dumps(dict(zip(rowstag, table.row_values(i))))
        # 通过编解码还原数据
        returnData[i] = json.loads(returnData[i])
        print returnData[i]
        account.insert(returnData[i])

def testRedis():
    pass
    # g_session_redis.set("name", "xixin")
    # print g_session_redis.get("name")

if __name__ == "__main__":
    pass