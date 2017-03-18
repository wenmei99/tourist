# !/usr/bin/python
# -*- coding: utf-8 -*-
from db.db_opr import db_PIN
import cfg


def addPIN(**data):
    if db_PIN.add(**data):
        return {"status": 0, "msg": "添加PIN成功！"}
    else:
        return {"status": 1, "msg": "添加PIN失败，请检查该PIN是否已存在！"}

def findPIN(**data):
    return db_PIN.find(**data)