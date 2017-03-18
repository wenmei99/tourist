#!/usr/bin/python
# -*- coding: utf-8 -*-
from cgibase import cgibase
from service.sorder import *

class Corder(cgibase):
    def __init__(self):
        self.oprlist = {
            "getAll":self.getAllOrder,
            "add": self.addOrder,
            "edit": self.editOrder,
            "delete": self.delOrder,
            "find": self.findOrder
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

    def getAllOrder(self):
        """{
            "opr": "getAll",
            "data": {
                "currentPage" : "1"
            }
        }"""
        req = self.input["input"]
        data = req["data"]
        self.out = getAllOrder(**data)

    def addOrder(self):
        """{
            "opr": "add",
            "data": {
                "b_name" : "商家名称",
                "goodsList" : [
                    {
                        "goodsName" : "商品名称",
                        "goodsNum" : "商品数量",
                        "goodsMoney" : "该商品总金额"
                    }
                ],
                "goodsCount" : "总商品数",
                "orderMoney" : "订单总价",
                "state" : "订单状态（未付款 失效 付款成功 付款失败）"
            }
        }"""

if __name__ == "__main__":
    order = Corder()
    order.onInit()