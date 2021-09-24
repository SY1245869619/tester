# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: configHttp.py
@time: 2021/6/28 14:20
"""
# 通过get、post、put、delete等方法进行http请求，拿到请求的响应
import json
import urllib

import requests


class RunMain():

    # 定义一个方法，传入参数url和data
    def send_post(self, url, data, headers):
        # 参数按照url、data顺序传入,封装post方法，url和data不能写死
        data1 = data.encode('utf-8')
        data = data1
        result = requests.post(url=url, data=data, headers=headers).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def send_get(self, url, data, headers):
        result = requests.get(url=url, params=data, headers=headers).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    # 定义一个run_main函数，通过传过来的method来判断进行不同的get或者post请求
    def run_main(self, method, url=None, data=None, headers=None):
        result = None
        if method == 'post':
            result = self.send_post(url, data, headers)
        elif method == 'get':
            result = self.send_get(url, data, headers)
        else:
            print("method值错误！！！")
        return result


if __name__ == '__main__':
    data = '{"remark": "测试", "id": 1}'
    data1 = data.encode('utf-8')
    headers = {
        "Host": "test.regulatory.kachexiongdi.com",
        "Connection": "keep-alive",
        "EagleEye-SessionID": "69k52sLwspUkjCoU4fXyb4k3nXm1",
        "EagleEye-TraceID": "80364a401629961312831100523008",
        "EagleEye-pAppName": "en91xqoenk@4a295060f323008",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/92.0.4515.159 Safari/537.36",
        "Web-User-Agent": "yyht-plateform/0.0.1,Web",
        "Accept": "*/*",
        "Referer": "http://test.regulatory.kachexiongdi.com/networkFreight",
        'content-type': 'application/json;charset=UTF-8',
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,ko;q=0.6",
        "Cookie": "36_admin_session=db062b6b-4d05-4911-a48a-a513c0320cd2.Me447HJjvGbj_T0H3yoNCkYkeWo; "
                  "Expires=Sun, 26-Sep-2021 06:07:06 GMT; HttpOnly; Path=/",
    }
    result1 = requests.post('http://test.regulatory.kachexiongdi.com/api/invoice/network_freight_platform_remark',
                            data1,
                            headers=headers)
    # result2 = RunMain().run_main('get', 'http://127.0.0.1:8888/login', 'name=shenyuan&password=12345')
    print(result1.json())
    # print(result2)
