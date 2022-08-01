# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: Invoice.py
@time: 2021/9/1 16:48
"""
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@和顺开票平台测试用例@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

import json

import requests

import getUrlParams
import unittest
import readExcel
import paramunittest
from common.configHttp import RunMain

url = getUrlParams.GetUrlParams().get_url_Invoice()  # 调用我们的getURlParams获取拼接的url
read_xls = readExcel.ReadExcel().get_xls('Invoice.xlsx', 'Page01')


@paramunittest.parametrized(*read_xls)
class Test(unittest.TestCase):
    def setParameters(self, case_name, path, query, method):
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)

    def description(self):
        self.case_name

    def setUp(self):
        print(self.case_name + "----测试开始前准备")

    def test_Operational(self):
        self.checkResult()

    def tearDown(self):
        print("----测试结束，输出log完结\n\n")

    def checkResult(self):  # 断言
        headers = {
            "Host": "test.invoice.kachexiongdi.com",
            "Connection": "keep-alive",
            "EagleEye-SessionID": "tzkCst541IO9veggq43Uxtw54tvy",
            "EagleEye-TraceID": "d2aa95081630486706524102823008",
            "EagleEye-pAppName": "en91xqoenk@4a295060f323008",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
            "Web-User-Agent": "yyht-plateform/0.0.1,Web",
            "Accept": "*/*",
            "Referer": "http://test.invoice.kachexiongdi.com/financialAudit",
            "Accept-Encoding": "gzip,deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,ko;q=0.6",
            "Cookie": "UM_distinctid=17ad319cb4972f-0d3f466d77dc29-6373264-1fa400-17ad319cb4a1062; 36_admin_session=152a465a-f9c0-48a0-9e06-d717d37648a6.rNVIZTajC2KnixdpXoU_8NXbfEg",
        }
        print("接口为:"+self.path)
        print("传参为:"+self.query)
        new_url = url + self.path + '?' + self.query
        print("请求链接为⬇")
        print(new_url)
        info = RunMain().run_main(self.method, new_url, self.query,
                                  headers)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        ss = json.loads(info)  # 将响应转换为字典格式
        print("返回数据为⬇")
        print(ss)
