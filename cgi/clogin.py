#!/usr/bin/python
# -*- coding: utf-8 -*-
from cgibase import cgibase
from service.slogin import *

class Clogin(cgibase):
    def __init__(self):
        self.oprlist = {
            "login":self.login,
            "edit":self.edit_login_pwd,
            "forget":self.forget_login_pwd,
            "logout":self.logout
        }
        return cgibase.__init__(self)

    def onInit(self):
        opr = cgibase.onInit(self)
        if opr is None:
            return
        if opr not in self.oprlist:
            return
        self.oprlist[opr]()

    def login(self):
        """{
            "opr": "login",
            "data":{
            "type" : "0",    // 0 管理员  1 商户
            "user_name": "admin",
            "pwd":"123456"}
        }"""
        req = self.input["input"]
        data = req["data"]
        type = data["type"]
        user_name = data["user_name"]
        user_pwd = data["pwd"]
        self.out = login_check(type, user_name, user_pwd)

    def edit_login_pwd(self):
        """{
            "opr": "edit",
            "data":{
                "_id" : "18270884782",
                "pwd":"123456"}
            }"""
        req = self.input["input"]
        data = req["data"]
        self.out = edit_login_pwd(**data)

    def forget_login_pwd(self):
        """{
            "opr": "forget",
            "data":{
                "_id" : "18270884782",
                "contact": "",
                "phone": "",
                "pwd": ""}
            }"""
        req = self.input["input"]
        data = req["data"]
        self.out = forget_login_pwd(**data)

    def logout(self):
        """{
                "opr": "logout"
            }"""
        ssid = self.input["self"]["ssid"]
        session_redis.delete(cfg.g_redis_pix + ssid)
        self.out = {"status":0, "msg": "退出登录成功！！"}


if __name__ == "__main__":
    login = Clogin()
    login.onInit()