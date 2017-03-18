# -*- coding: utf-8 -*-
from db.db_conn.db_mongo import MongoConn
import re
import cfg
import json
db = MongoConn().db


def add(**data):
    try:
        db["goods_PIN"].insert_one(data)
        return True
    except:
        return False

def find(**data):
    result = []
    find_list = db["goods_PIN"].find(
        {"$or": [{"_id": re.compile(data["search"])}, {"goodsName": re.compile(data["search"])}]})
    a = find_list.count()
    if find_list.count() > cfg.pageSize:
        P_lists = find_list.skip((int(data["currentPage"]) - 1) * cfg.pageSize).limit(cfg.pageSize)
    else:
        P_lists = find_list
    for i in P_lists:
        data = {
            "_id": i["_id"],
            "goodsName": i["goodsName"],
            "specification": i["specification"]
        }
        result.append(data)
    res = {"status": 0, "currentPage": data["currentPage"], "pageSize": cfg.pageSize, "count": a, "data": result}
    return json.dumps(res)


if __name__ == "__main__":
    data = {
    "_id" : "6901382023677",
    "goodsName" : "五粮液1618（52度）",
    "specification" : "500ml"
    }
    print add(**data)