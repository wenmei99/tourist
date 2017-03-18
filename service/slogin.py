# !/usr/bin/python
# -*- coding: utf-8 -*-
from db.db_opr import db_login
from util import PHONE,randomStr
from db.db_conn.db_redis import session_redis
import cfg

def login_check(type, user_name, user_pwd):
    res = db_login.login(type, user_name, user_pwd)
    if res == True:
        ssid = randomStr(128)
        session_redis.set(cfg.g_redis_pix + ssid, user_name)
        session_redis.set(user_name, cfg.g_redis_pix + ssid)
        session_redis.expire(cfg.g_redis_pix + ssid, cfg.g_ssid_timeout)
        return {"status": 0, "msg": "登录成功！", "ssid": ssid}
    else:
        return {"status": 1, "msg": "用户名或密码错误或权限不匹配！！"}

def edit_login_pwd(**data):
    if db_login.edit_pwd(**data):
        return {"status": 0, "msg": "密码修改成功！"}
    else:
        return {"status": 1, "msg": "密码修改失败！！"}

def forget_login_pwd(**data):
    if PHONE.match(data["_id"]) and PHONE.match(data["phone"]):
        if db_login.forget_login_pwd(**data):
            return {"status": 0, "msg": "重置登录密码成功！"}
        else:
            return {"status": 1, "msg": "信息核验不正确，请重试！！"}
    else:
        return {"status": 1, "msg": "请填入正确的商户ID或联系人手机号！"}


if __name__ == "__main__":
    print login_check("0","admin","admin")