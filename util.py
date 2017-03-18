#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import os
# from db.db_conn.db_mongo import MongoConn
# import xlrd
import json

PHONE = re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}')
NUM = re.compile('^[0-9]*$')
RANDON_CHAR = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
# def saveGoodsPIN():
#     # 读取商品条形码表格
#     account = MongoConn().db["goods_PIN"]
#     data = xlrd.open_workbook('D:\PIN.xls')
#     table = data.sheets()[0]
#     # 读取excel第一行数据作为存入mongodb的字段名
#     # rowstag = table.row_values(0)
#     # print rowstag
#     rowstag = ["_id", "goodsName", "specification"]
#     nrows = table.nrows
#     # ncols=table.ncols
#     # print rows
#     returnData = {}
#     for i in range(1, nrows):
#         # 将字段名和excel数据存储为字典形式，并转换为json格式
#         returnData[i] = json.dumps(dict(zip(rowstag, table.row_values(i))))
#         # 通过编解码还原数据
#         returnData[i] = json.loads(returnData[i])
#         print returnData[i]
#         account.insert(returnData[i])

def randomStr(randomlength=128):
    str = ''
    chars = RANDON_CHAR
    length = len(chars) - 1
    for i in range(randomlength):
        str += chars[ord(os.urandom(1)) % length]
    return str




if __name__ == "__main__":
    # print randomStr(128)
    pass