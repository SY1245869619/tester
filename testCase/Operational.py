# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: AndroidDriver.py
@time: 2021/8/14 17:27
"""
# @@@@@@@@@@@@@@@@@@@@@@@@@运营后台的测试用例编写@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

import json

import requests

import getUrlParams
import unittest
import readExcel
import paramunittest
from common.configHttp import RunMain

url = getUrlParams.GetUrlParams().get_url_Operational()  # 调用我们的getURlParams获取拼接的url
read_xls = readExcel.ReadExcel().get_xls('Operational.xlsx', 'Page01')


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
            "Host": "test.data.kachexiongdi.com",
            "Connection": "keep-alive",
            "EagleEye-SessionID": "4Okj4s8mn9v2dvx9p7w1zz42830X",
            "EagleEye-TraceID": "f635b88f1629628861302100423008",
            "EagleEye-pAppName": "en91xqoenk@4a295060f323008",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
            "Web-User-Agent": "yyht-plateform/0.0.1,Web",
            "Accept": "*/*",
            "Referer": "http://test.data.kachexiongdi.com/rejectRecord",
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
        if self.case_name == '进入审核页':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '进入审核信息页':
            self.assertEqual(ss['warnType'], 1)
            print("》》》》》》》》》》测试通过，接口正常")


if __name__ == '__main__':
    print()
