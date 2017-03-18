# -*- coding: utf-8 -*-
from db.db_conn.db_mongo import MongoConn
import json
import cfg
import re
from datetime import datetime
db = MongoConn().db


def showAll(currentPage):
    find_goods = db["goods_info"].find()
    result = []
    a = find_goods.count()
    if find_goods.count() > cfg.pageSize:
        g_lists = find_goods.skip((int(currentPage) - 1) * cfg.pageSize).limit(cfg.pageSize)
    else:
        g_lists = find_goods
    for i in g_lists:
        data = {
            "_id": i["_id"],
            "b_id": i["b_id"],
            "b_name": i["b_name"],
            "goodsName": i["goodsName"],
            "specification": i["specification"],
            "amount": i["amount"],
            "pPrice": i["pPrice"],
            "lastPurchase": i["lastPurchase"]
        }
        result.append(data)
    res = {"status": 0, "currentPage": currentPage, "pageSize": cfg.pageSize, "count": a, "data": result}
    return json.dumps(res)

def find(**data):
    result = []
    find_list = db["goods_info"].find(
        {"$or": [{"_id": re.compile(data["search"])}, {"b_Name": re.compile(data["search"])}]})
    print find_list.count()
    a = find_list.count()
    if find_list.count() > cfg.pageSize:
        c_lists = find_list.skip((int(data["currentPage"]) - 1) * cfg.pageSize).limit(cfg.pageSize)
    else:
        c_lists = find_list
    print c_lists.count()
    for i in c_lists:
        data = {
            "_id": i["_id"],
            "b_id": i["b_id"],
            "b_name": i["b_name"],
            "goodsName": i["goodsName"],
            "specification": i["specification"],
            "amount": i["amount"],
            "pPrice": i["pPrice"],
            "lastPurchase": i["lastPurchase"]
        }
        result.append(data)
    res = {"status": 0, "currentPage": data["currentPage"], "pageSize": cfg.pageSize, "count": a, "data": result}
    return json.dumps(res)

def addGoods(**data):
    """         "_id" : "商品条码",
                "b_id" : "商家id",
                "amount" : "进货数量",
                "pPrice" : "进价"
    """
    # 通过_id查找goods_info表是否存在，若存在，将amount累加，更新 进价 最新进货时间  同时增加一条进货记录
        # 若不存在该商品，从goods_PIN表中读取 goodsName specification,
        # 通过商家id查找商品名称  组json
        # insert 进  goods_info中  同时增加一条进货记录
            # 如果goods_PIN表中不存在该PIN，返回提示
    g_find = db["goods_info"].find_one({"_id": data["_id"]})
    lastPurchase = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    purchase_id = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
    a = int(data["amount"])+int(g_find["amount"])
    if g_find:
        db["goods_info"].update_one({'_id':data["_id"]},{"$set": {'amount': a, 'pPrice': int(data["pPrice"]), 'lastPurchase': lastPurchase}})
        data2 = {
            "_id": purchase_id,
            "b_id": "b_id",
            "goods_id": data["_id"],
            "amount": int(data["amount"]),
            "pPrice": int(data["pPrice"]),
            "p_time": lastPurchase
        }
        db["purchase_info"].insert_one(data2)
        return {"status": 0, "msg": "商品入库成功！"}
    else:
        pin_find = db["goods_PIN"].find_one({"_id": data["_id"]})
        if pin_find:
            b_name = db["business_info"].find_one({"_id": data["b_id"]},{"_id": 0, "b_Name": 1})
            data = {
                "_id": data["_id"],
                "b_id": data["_id"],
                "b_name": b_name["b_Name"],
                "goodsName": pin_find["goodsName"],
                "specification": pin_find["specification"],
                "amount": data["amount"],
                "pPrice": data["pPrice"],
                "lastPurchase": lastPurchase
            }
            try:
                db["goods_info"].insert_one(data)
                data2 = {
                    "_id": purchase_id,
                    "b_id": "b_id",
                    "goods_id": data["_id"],
                    "amount": int(data["amount"]),
                    "pPrice": int(data["pPrice"]),
                    "p_time": lastPurchase
                }
                db["purchase_info"].insert_one(data2)
                return {"status": 0, "msg": "新商品入库成功！"}
            except:
                return {"status": 1, "msg": "商品入库失败！"}
        else:
            return {"status": 1, "msg": "请输入正确的商品PIN或联系系统管理员！"}

def editGoods(**data):
    try:
        db["goods_info"].update_one({"_id": data["_id"]},{"$set": {"amount": data["amount"]}})
        return {"status": 0, "msg": "修改商品信息成功！"}
    except:
        return {"status": 1, "msg": "修改商品信息失败！！"}

def delGoods(**data):
    try:
        db["goods_info"].delete_one({"_id": data["_id"]})
        return {"status": 0, "msg": "删除商品信息成功！"}
    except:
        return {"status": 1, "msg": "删除商品信息失败！！"}

if __name__ == "__main__":
    pass





