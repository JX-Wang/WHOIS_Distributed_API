#! /usr/bin/env python
# coding:utf-8

import json


class Test:
    def __init__(self):
        info = {}
        info = self.start()
        print type(info), info['user']
        if info['mode']:
            print info['mode']
        print len(info)

    def start(self):
        return {'user': 'sdflsjflsf', 'mode': 'sock5'}


class dict:
    def __init__(self):
        self.str = "{'domain':'baidu.com','whois_server':'whois.crinic.com'}"
        print type(self.str)
        self.dit = eval(self.str)
        print self.dit, type(self.dit)
        print self.dit['domain']


if __name__ == '__main__':
    dict()
