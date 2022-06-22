# !/usr/bin python3
# encoding: utf-8 -*-
# @file : testLogin.py
# @author : hanks7
# @Time : 2022/6/23 1:05
# @Copyright: 日赢集团
import json

import requests


def method_name():
    url = 'http://82.156.74.26:9099/login'
    d = {
        "username": "18866668888",
        "password": "123456"
    }
    r = requests.post(url, data=d)
    print(r.text)


def method_name2():
    url = 'http://82.156.74.26:9099/CrmCustomer/addOrUpdate'

    d = {
        "entity": {
            "customer_name": "沙陌001",
            "mobile": "18729399607",
            "telephone": "01028375678",
            "website": "http://mtongxue.com/",
            "next_time": "2022-05-12 00:00:00",
            "remark": "这是备注",
            "address": "北京市,北京城区,昌平区",
            "detailAddress": "霍营地铁口",
            "location": "",
            "lng": "",
            "lat": ""
        },
        "headers": {'Admin-Token': '2fde6f8d8fcc4e949470fd72a8a6a25a'}
    }
    r = requests.post(url, data=d)
    print(r.text)


method_name2()
