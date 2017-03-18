#!/usr/bin/python
# -*- coding: utf-8 -*-
pageSize = 5
g_redis_pix = "ssid_"
g_ssid_timeout = 15*60
debug_mode = False #False
url_pre = "/xixin/goods/"
rSyslog = ('127.0.0.1',514)
err = {
    "refused":'{"status":1, "msg":"拒绝访问！"}',
    "input_err":'{"status":2, "msg":"输入错误！"}',
    "relogin":'{"status":3, "msg":"会话超时，需要重新登录！", "need_login":1}',
    "ext_error":'{"status":4, "msg":"上传文件的扩展名不支持。"}'
}