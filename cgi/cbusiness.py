#!/usr/bin/python
# -*- coding: utf-8 -*-
from cgibase import cgibase
from service.sbusiness import *

class Cbusiness(cgibase):
    def __init__(self):
        self.oprlist = {
            "getAll":self.getAllBusiness,   # 获取所有的商家列表
            "add": self.addBusiness,         # 添加商户
            "edit": self.editBusiness,         # 编辑商户信息
            "delete": self.delBusiness,          # 删除商户
            "find": self.findBusiness
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

    def getAllBusiness(self):
        """{
            "opr": "getAll",
            "data": {
                "currentPage": "1"
            }
        }"""
        req = self.input["input"]
        data = req["data"]
        currentPage = data["currentPage"]
        self.out = getAllBusiness(currentPage)

    def addBusiness(self):
        """{
                "opr": "add",
                "data": {
                    "_id": "18270884782",
                    "b_Name": "商家名称",
                    "b_address": "商家地址",
                    "password": "登录密码",
                    "contact": "联系人",
                    "phone": "联系电话"
                    }
            }"""
        req = self.input["input"]
        data = req["data"]
        self.out = addBusiness(**data)

    def editBusiness(self):
        """{
                "opr": "edit",
                "data": {
                    "_id": "18270884782",
                    "b_Name": "商家名称",
                    "password": "登录密码"
                    }
            }"""
        req = self.input["input"]
        data = req["data"]
        self.out = editBusiness(**data)

    def delBusiness(self):
        """{
                "opr": "delete",
                "data": {
                    "_id": "18270884782"
                    }
            }"""
        req = self.input["input"]
        data = req["data"]
        self.out = delBusiness(**data)

    def findBusiness(self):
        """{
                "opr": "find",
                "data": {
                    "search": "18270884782",
                    "currentPage": "1"      //从1开始
                    }
            }"""
        req = self.input["input"]
        data = req["data"]
        self.out = findBusiness(**data)


if __name__ == "__main__":
    business = Cbusiness()
    business.onInit()