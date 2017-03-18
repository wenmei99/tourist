#!/usr/bin/env python
# coding=utf-8
import commands
import json
import logging
import logging.handlers
import sys
import urllib
import urlparse
import cfg
from db.db_conn.db_redis import session_redis


class cgibase:
    def __init__(self):
        self.myinit()

    def __del__(self):
        self.mydel()

    def myinit(self):
        self.out = {}
        self.input = {}
        self.out_ssid = None
        self.redirect_url = None
        self.log_handler = None
        self.__cookieFlag = True
        self.name = None
        self.log = None

    def mydel(self):
        if self.log_handler is not None:
            self.log.removeHandler(self.log_handler)
            self.log_handler = None

    def setenv(self, req_dict):
        self.input = req_dict

    def output(self):
        if type(self.out) is dict:
            self.out = json.dumps(self.out, ensure_ascii=False)
        return self.out

    def onInit(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        if self.input == {}:
            self.SetNoCheckCookie()
            if len(sys.argv) != 3:
                self.out = cfg.err["input_err"]
                return None
            self.input["self"] = {}
            self.input["self"]["fun"] = sys.argv[1]
            self.input["self"]["ip"] = "127.0.0.1"
            self.input["self"]["ssid"] = None
            self.input["self"]["m"] = "GET"
            arg = sys.argv[2]
            isjson = False
            if arg.find("file://") == 0:
                self.input["self"]["m"] = "POST"
                try:
                    file = open(arg[len("file://"):])
                except:
                    self.out = cfg.err["input_err"]
                    return None
                else:
                    data_in = file.read()
                    file.close()
                    try:
                        json.loads(data_in)
                    except:
                        isjson = False
                    else:
                        isjson = True
            else:
                data_in = arg
            jsondata = {}
            if isjson is False:
                data_in = urllib.unquote(data_in)
                data_in = urlparse.parse_qsl(data_in)
                for dat in data_in:
                    jsondata[dat[0]] = dat[1]
            else:
                jsondata = json.loads(data_in)
            self.input["input"] = jsondata

        opr = None
        if not self.input["input"].has_key("opr"):
            self.out = cfg.err["input_err"]
            return opr
        opr = self.input["input"]["opr"]

        return opr

    # def SetNoCheckCookie(self):
    #     self.__cookieFlag = False
    #     return

    def checkCookie(self):
        ssid = self.input["self"]["ssid"]
        if (ssid == '' or ssid is None):
            self.out = cfg.err["relogin"]
            return False
        r = session_redis.get(cfg.g_redis_pix + ssid)
        if r is None or r == "":
            self.out = cfg.err["relogin"]
            return False
        self.name = r
        check_sid = session_redis.get(r)
        if cfg.g_redis_pix + ssid == check_sid:
            session_redis.expire(cfg.g_redis_pix + ssid, cfg.g_ssid_timeout)
            return True
        else:
            session_redis.delete(cfg.g_redis_pix + ssid)
            self.out = cfg.err["relogin"]
            return False



if __name__ == "__main__":
    pass