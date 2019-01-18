#!/usr/bin/env python
# encoding:utf-8

"""
    主程序入口 - WHOIS api
=======================
WHOIS 查询api

version   :   0.1
author    :   @`13
time      :   2017.11.12

version   :   2.0
author    :   @WUD
time      :   2018.8.12

-history version 2.0-

    + 基于python官方的whois库进行的whois查询
    + 辅助数据全部迁移到程序中
    + 批量whois查询
    - 取消使用IP连接whois服务器
    - 所有的数据库相关操作
    ~ 速度以及资源占用的优化

"""


from flask import Flask

from gevent import monkey
from gevent.pywsgi import WSGIServer
monkey.patch_all()

import whois
import json

from Setting.static import Static
from get_domain_whois import whois_query, whois_list

Static.init()
app = Flask("WHOIS api")
app.config.update(DEBUG=False)


@app.route('/')
def index():
    """index page"""
    _start = "<h1>Whois API Service v1.1 </h1>"
    _start += "<h3>author - h-j-13(@`13)</h3>"
    _start += "<h3>author - WUD(@wangjunx)</h3><br><b4>"
    _start += "<h3>Harbin Institute of Technology at Weihai</h3>"
    _start += "system clk" + str(Static.get_local_time())
    return _start


@app.route('/whois/<domain>')
def whois(domain):
    """使用python自带whois库探测WHOIS"""
    try:
        whois_info = whois.whois(domain)
        print whois_info
        if whois_info:
            return str(whois_info)
    except Exception as e:
        print "whois query error: ", str(e)


@app.route('/WHOIS/<msg>')
def WHOIS(msg):
    """获取单一域名的WHOIS数据"""
    msg = "{" + str(msg) + "}"
    msg = eval(msg)
    if len(msg) == 2:
        try:
            domain = msg['domain']
            whois_server = msg['whois_server']
            domain, whois_server = str(domain), str(whois_server)
            print domain, whois_server
            data = whois_query(domain, whois_server, '')
            return json.dumps(data, indent=1)
        except:
            pass
    elif len(msg) >= 3:  # 主节点传有代理配置信息
        try:
            domain = msg['domain']
            whois_server = msg['whois_server']
            domain, whois_server = str(domain), str(whois_server)
            data = whois_query(domain, whois_server, msg)
            return json.dumps(data, indent=1)
        except:
            pass
    else:
        pass


if __name__ == '__main__':
    http_server = WSGIServer(('', Static.API_PORT), app)
    http_server.serve_forever()
    # 'domain':'baidu.com', 'whois_server':'whois.crsnic.net'
