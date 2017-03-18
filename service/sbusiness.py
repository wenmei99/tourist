# !/usr/bin/python
# -*- coding: utf-8 -*-
from db.db_opr import db_business
from util import PHONE

def getAllBusiness(currentPage):
    return db_business.getall(currentPage)

def addBusiness(**data):
    if PHONE.match(data["_id"]) and PHONE.match(data["phone"]):
        if db_business.check_business(data["_id"]):
            return {"status": 1, "msg": "该商户已经录入！！"}
        else:
            if db_business.addBusiness(**data):
                return {"status": 0, "msg": "商户录入成功！"}
            else:
                return {"status": 1, "msg": "商户录入失败！！"}
    else:
        return {"status": 1, "msg": "请填入正确的手机号格式！！"}

def editBusiness(**data):
    if db_business.editBusiness(**data):
        return {"status": 0, "msg": "编辑商户信息成功！"}
    else:
        return {"status": 1, "msg": "编辑商户信息成功！！"}

def delBusiness(**data):
    if db_business.delBusiness(**data):
        return {"status": 0, "msg": "成功删除商户！"}
    else:
        return {"status": 1, "msg": "删除商户信息失败！！"}

def findBusiness(**data):
    return db_business.findBusiness(**data)