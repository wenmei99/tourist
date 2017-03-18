# -*- coding: utf-8 -*-
from db.db_conn.db_mongo import MongoConn
from util import randomStr
from datetime import datetime
import json
import cfg
from util import randomStr

db = MongoConn().db


def login(type, user_name, user_pwd):
    # 商家管理员登录校验
    account = db["open_users"].find_one({"_id": user_name})
    if account and account["type"] == type and account["password"] == user_pwd:
        return True
    else:
        return False

def edit_pwd(**data):
    try:
        db["open_users"].update_one({"_id": data["_id"]}, {"$set": {"password": data["pwd"]}})
        db["business_info"].update_one({"_id": data["_id"]}, {"$set": {"password": data["pwd"]}})
        return True
    except:
        return False

def forget_login_pwd(**data):
    find = db["business_info"].find_one({"_id": data["_id"]})
    if find["contact"] == data["contact"] and find["phone"] == data["phone"]:
        db["open_users"].update_one({"_id": data["_id"]}, {"$set": {"password": data["pwd"]}})
        db["business_info"].update_one({"_id": data["_id"]}, {"$set": {"password": data["pwd"]}})
        return True
    else:
        return False

if __name__ == "__main__":
    print login("0","admin","admin")