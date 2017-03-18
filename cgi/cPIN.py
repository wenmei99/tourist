#!/usr/bin/python
# -*- coding: utf-8 -*-
from cgibase import cgibase
from service.sPIN import *

class CPIN(cgibase):
    def __init__(self):
        self.oprlist = {
            # "getAll":self.getAllBusiness,
            "add": self.addPIN,
            # "edit": self.editPIN,
            # "delete": self.delBusiness,
            "find": self.findPIN
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

    def addPIN(self):
        """{
            "opr": "add",
            "data": {
                "_id" : "6902018995528",
                "goodsName" : "古井金纯粮白酒（39度）",
                "specification" : "500ml"
            }
        }"""
        req = self.input["input"]
        data = req["data"]
        self.out = addPIN(**data)

    def findPIN(self):
        """{
            "opr": "find",
            "data": {
                "search": "",
                "currentPage": ""
            }
        }"""
        req = self.input["input"]
        data = req["data"]
        self.out = findPIN(**data)