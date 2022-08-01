# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: login.py
@time: 2021/8/22 19:36
"""
import requests
from requests import utils
import json


def login():
    url_login = "http://test.data.kachexiongdi.com/api/v_admin/admin_user/login"
    data = {
        "username": "17713146220", "password": "cs12345678"
    }
    # headers = {

    #     "Host": "test.data.kachexiongdi.com",
    #     "Connection": "keep-alive",
    #     "EagleEye-SessionID": "4Okj4s8mn9v2dvx9p7w1zz42830X",
    #     "EagleEye-TraceID": "f635b88f1629628861302100423008",
    #     "EagleEye-pAppName": "en91xqoenk@4a295060f323008",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    #                   "Chrome/94.0.4606.54 Safari/537.36",
    #     "Web-User-Agent": "yyht-plateform/0.0.1,Web",
    #     "Accept": "*/*",
    #     "Referer": "http://test.data.kachexiongdi.com/login",
    #     "Accept-Encoding": "gzip,deflate",
    #     "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,ko;q=0.6",
    #     "Cookie": "UM_distinctid=7ad319cb4972f-0d3f466d77dc29-6373264-1fa400-17ad319cb4a1062",
    # }
    login = requests.get(url_login, params=data)
    print(login.json())
    cookie = login.cookies
    cookie_jar = requests.utils.dict_from_cookiejar(cookie)
    print("响应参数返回cookie为")
    print(cookie_jar)


def login1():
    url_login1 = "https://test.kuangda.kachexiongdi.com/user/login"
    data = {
        "username": "17713146220",
        "password": "17713146220",
        "weChatOpenId": "ouWOS5SY4hLrb3r-heylPtcBDpI4"
    }
    # headers = {

    #     "Host": "test.data.kachexiongdi.com",
    #     "Connection": "keep-alive",
    #     "EagleEye-SessionID": "4Okj4s8mn9v2dvx9p7w1zz42830X",
    #     "EagleEye-TraceID": "f635b88f1629628861302100423008",
    #     "EagleEye-pAppName": "en91xqoenk@4a295060f323008",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    #                   "Chrome/94.0.4606.54 Safari/537.36",
    #     "Web-User-Agent": "yyht-plateform/0.0.1,Web",
    #     "Accept": "*/*",
    #     "Referer": "http://test.data.kachexiongdi.com/login",
    #     "Accept-Encoding": "gzip,deflate",
    #     "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,ko;q=0.6",
    #     "Cookie": "UM_distinctid=7ad319cb4972f-0d3f466d77dc29-6373264-1fa400-17ad319cb4a1062",
    # }
    login1 = requests.get(url_login1, params=data)
    print(login1.json())
    cookie = login1.cookies
    cookie_jar = requests.utils.dict_from_cookiejar(cookie)
    print("响应参数返回cookie为")
    print(cookie_jar)


if __name__ == '__main__':
    # sy = requests.get("http://test.data.kachexiongdi.com/api/v_admin/admin_user/login",
    # "username=17713146220&password=cs12345678") print(sy.json()) cookie = sy.cookies print(cookie) cookie_jar =
    # requests.utils.dict_from_cookiejar(cookie) print(cookie_jar)
    login1()
