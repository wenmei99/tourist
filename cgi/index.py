#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import cfg
from cbusiness import Cbusiness
from cgoods import Cgoods
from clogin import Clogin
from corder import Corder
from cPIN import CPIN
from flask import Flask, request, make_response, redirect
app = Flask(__name__)
app.debug = cfg.debug_mode

def pre_do(c, fun):
    req_dict = {}
    if request.method == "GET":
        req_dict["input"] = request.args
    elif request.method == "POST":
        try:
            req_dict["input"] = json.loads(request.get_data())
        except:
            return cfg.err["refused"]
    ip = request.headers.get('X-Real-IP')
    if ip is None or ip == "":
        ip = "127.0.0.1"
    ssid = request.headers.get('ssid')
    if ssid is None:
        ssid = ''
    req_dict["self"] = {}
    req_dict["self"]["ip"] = ip
    req_dict["self"]["ssid"] = ssid
    req_dict["self"]["m"] = request.method
    req_dict["self"]["fun"] = fun

    c.setenv(req_dict)
    try:
        c.myinit()
        c.setenv(req_dict)
        c.onInit()
    except:
        c.mydel()
        raise
    out = c.output()
    redirect_url = c.redirect_url
    c.mydel()

    if redirect_url is not None:
        return redirect(redirect_url)
    resp = make_response(out)
    return resp


@app.route(cfg.url_pre + "login.do", methods=['GET', 'POST', 'OPTIONS'])
def login_func():
    return pre_do(Clogin(), "login")


@app.route(cfg.url_pre + "business.do", methods=['GET', 'POST', 'OPTIONS'])
def business_func():
    return pre_do(Cbusiness(), "business")


@app.route(cfg.url_pre + "PIN.do", methods=['GET', 'POST', 'OPTIONS'])
def PIN_func():
    return pre_do(CPIN(), "PIN")


@app.route(cfg.url_pre + "goods.do", methods=['GET', 'POST', 'OPTIONS'])
def goods_func():
    return pre_do(Cgoods(), "goods")


@app.route(cfg.url_pre + "order.do", methods=['GET', 'POST', 'OPTIONS'])
def order_func():
    return pre_do(Corder(), "order")

if __name__ == '__main__':
    app.debug = True
    app.run()
