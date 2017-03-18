# -*- coding: utf-8 -*-
from db.db_conn.db_mongo import MongoConn
from datetime import datetime
import cfg
import re
import json
db =MongoConn().db

def getall(currentPage):
    # 获取所有商家
    account = db["business_info"].find()
    result = []
    a = account.count()
    if account.count() > cfg.pageSize:
        b_lists = account.skip((int(currentPage) - 1) * cfg.pageSize).limit(cfg.pageSize)
    else:
        b_lists = account
    for i in b_lists:
        data = {
            "_id": i["_id"],
            "b_Name": i["b_Name"],
            "b_address": i["b_address"],
            "password": i["password"],
            "contact": i["contact"],
            "phone": i["phone"],
            "input_time": i["input_time"]
        }
        result.append(data)
    res = {"status": 0, "currentPage": currentPage, "pageSize": cfg.pageSize, "count": a, "data": result}
    return json.dumps(res)

def check_business(_id):
    if db["business_info"].find_one({"_id": _id}) and db["open_users"].find_one({"_id": _id}):
        return True
    else:
        return False

def addBusiness(**data):
    data["input_time"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    open_data = {
        "_id": data["_id"],
        "type": "1",
        "password": data["password"]
    }
    try:
        db["open_users"].insert_one(open_data)
        db["business_info"].insert_one(data)
        return True
    except Exception,e:
        try:
            db["open_users"].delete_one(open_data)
            db["business_info"].delete_one(data)
        except:
            pass
        return False

def editBusiness(**data):
    try:
        db["business_info"].update_one({"_id": data["_id"]},{"$set": {"b_Name": data["b_Name"], "password": data["password"]}})
        db["open_users"].update_one({"_id": data["_id"]},{"$set": {"password": data["password"]}})
        return True
    except Exception,e:
        print e.message
        return False

def delBusiness(**data):
    try:
        db["business_info"].remove({"_id": data["_id"]})
        db["open_users"].remove({"_id": data["_id"]})
        return True
    except Exception,e:
        print e.message
        return False

def findBusiness(**data):
    result = []
    find_list = db["business_info"].find({"$or": [{"_id": re.compile(data["search"])}, {"b_Name": re.compile(data["search"])}]})
    print find_list.count()
    a = find_list.count()
    if find_list.count() > cfg.pageSize:
        c_lists = find_list.skip((int(data["currentPage"])-1) * cfg.pageSize).limit(cfg.pageSize)
    else:
        c_lists = find_list
    print c_lists.count()
    for i in c_lists:
        data = {
            "_id": i["_id"],
            "b_Name": i["b_Name"],
            "b_address": i["b_address"],
            "password": i["password"],
            "contact": i["contact"],
            "phone": i["phone"],
            "input_time": i["input_time"]
        }
        result.append(data)
    res = {"status": 0, "currentPage": data["currentPage"], "pageSize": cfg.pageSize, "count": a, "data": result}
    return json.dumps(res)




if __name__ == "__main__":
    getall()