#!/usr/bin/python
# -*- coding: utf-8 -*-
from cgibase import cgibase
from service.sgoods import *

class Cgoods(cgibase):
    def __init__(self):
        self.oprlist = {
            "show":self.showAllGoods,
            "find": self.findGoods,
            "add": self.addGoods,
            "edit": self.editGoods,
            "delete":self.delGoods
        }
        return cgibase.__init__(self)

    def onInit(self):
        if cgibase.checkCookie(self):
            opr = cgibase.onInit(self)
            if opr is None:
                return
            if opr not in self.oprlist:
                return
            self.oprlist[opr]()

    def showAllGoods(self):
        """{
            "opr": "show",
            "data": {
                "currentPage": "1"
            }
        }"""
        req = self.input["input"]
        data = req["data"]
        currentPage = data["currentPage"]
        self.out = showAllGoods(currentPage)

    def findGoods(self):
        """{
            "opr": "find",
            "data": {
                "search": "",
                "currentPage": "1"
                }
            }"""
        req = self.input["input"]
        data = req["data"]
        self.out = findGoods(**data)

    def addGoods(self):
        """{
            "opr": "add",
            "data": {
                "_id" : "商品条码",
                "b_id" : "商家id",
                "amount" : "进货数量",
                "pPrice" : "进价"}
            }"""
        req = self.input["input"]
        data = req["data"]
        self.out = addGoods(**data)

    def editGoods(self):
        """{
            "opr": "edit",
            "data": {
                "_id" : "商品条码",
                "b_id" : "商家id",
                "amount" : "进货数量"}
            }"""
        req = self.input["input"]
        data = req["data"]
        self.out = editGoods(**data)

    def delGoods(self):
        """{
            "opr": "delete",
            "data": {
                "_id" : "商品条码",
                "b_id" : "商家id"}
            }"""
        req = self.input["input"]
        data = req["data"]
        self.out = delGoods(**data)

if __name__ == "__main__":
    goods = Cgoods()
    goods.onInit()