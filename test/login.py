# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: login.py
@time: 2021/8/22 19:36
"""
import requests


def login():
    params = {
        "username": "17713146220", "password": "cs12345678",
    }
    # headers = {
    #     "Host": "test.data.kachexiongdi.com",
    #     "Connection": "keep-alive",
    #     "EagleEye-SessionID": "4Okj4s8mn9v2dvx9p7w1zz42830X",
    #     "EagleEye-TraceID": "f635b88f1629628861302100423008",
    #     "EagleEye-pAppName": "en91xqoenk@4a295060f323008",
    #     "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,"
    #                   "likeGecko)Chrome/92.0.4515.159Safari/537.36",
    #     "Web-User-Agent": "yyht-plateform/0.0.1,Web",
    #     "Accept": "*/*",
    #     "Referer": "http://test.data.kachexiongdi.com/login",
    #     "Accept-Encoding": "gzip,deflate",
    #     "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,ko;q=0.6",
    #     "Cookie": "UM_distinctid=7ad319cb4972f-0d3f466d77dc29-6373264-1fa400-17ad319cb4a1062",
    # }
    session = requests.session()
    url_login = "http://test.data.kachexiongdi.com/login"
    login = session.post(url_login, data=params, verify=False)
    cookie = login.cookies
    print(cookie)
if __name__ == '__main__':
    print(cookie)
    pass