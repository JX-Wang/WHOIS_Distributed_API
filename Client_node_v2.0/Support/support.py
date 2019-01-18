#! /usr/bin/env python
# encoding:utf-8

"""
TLD以及对应的WHOIS服务器
====================
author @wud
date @2018.8.12

date @2019.1.17
    + 改写为接口，方便调用
"""

import pymysql
import json


class RefreshWhoisSrv:
    """Refresh Whois Server
    :param None
    :return new file -> support.json"""

    def __init__(self):
        pass

    def refresh(self):
        dict = {}
        try:
            db = pymysql.connect("xx.x.x.x",
                                 "xxxx",
                                 "xxxxx",
                                 "xxxxx",
                                 charset="utf8")
            cursor = db.cursor()
            sql = "select Punycode, whois_addr from whois_tld_addr_new"
            cursor.execute(sql)
            results = cursor.fetchall()
        except Exception as e:
            print "Get data from mysql Error ->", str(e)
        for result in results:
            dict[str(result[0])] = str(result[1])

        dict_unfin = {}
        dict_unfin["comment"] = "WHOIS_Support_Data"
        dict_unfin["TLD_WHOISSERVER"] = dict
        json_data = json.dumps(dict_unfin, indent=4)
        with open("support.json", 'w') as json_file:
            json_file.write(json_data)
        json_file.close()


if __name__ == '__main__':
    RefreshWhoisSrv().refresh()
