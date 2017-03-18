# -*- coding: utf-8 -*-
from db.db_conn.db_mongo import MongoConn
import cfg
import json
db = MongoConn().db


def getAll(**data):
    order = db["order_info"].find()
    result = []
    a = order.count()
    if order.count() > cfg.pageSize:
        b_lists = order.skip((int(data["currentPage"]) - 1) * cfg.pageSize).limit(cfg.pageSize)
    else:
        b_lists = order
    for i in b_lists:
        data = {
            "_id": i["_id"],
            "b_name": i["b_name"],
            "createTime": i["createTime"],
            "goodsList": i["goodsList"],
            "goodsCount": i["goodsCount"],
            "orderMoney": i["orderMoney"],
            "state": i["state"]
        }
        result.append(data)
    res = {"status": 0, "currentPage": data["currentPage"], "pageSize": cfg.pageSize, "count": a, "data": result}
    return json.dumps(res)