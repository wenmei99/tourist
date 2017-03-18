# !/usr/bin/python
# -*- coding: utf-8 -*-
from db.db_opr import db_goods


def showAllGoods(currentPage):
    return db_goods.showAll(currentPage)

def findGoods(**data):
    return db_goods.find(**data)

def addGoods(**data):
    return db_goods.addGoods(**data)

def editGoods(**data):
    return db_goods.editGoods(**data)

def delGoods(**data):
    return db_goods.delGoods(**data)