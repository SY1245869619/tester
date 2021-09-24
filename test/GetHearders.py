# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: GetHearders.py
@time: 2021/8/26 15:00
"""

import json
import requests

class GetHearders():

    # 定义一个方法，传入参数url和data
    def send_post(self, url, data, headers):
        # 参数按照url、data顺序传入,封装post方法，url和data不能写死
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