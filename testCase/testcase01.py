# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: testcase01.py
@time: 2021/6/28 14:23
"""
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@本地的接口测试@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# 读取userCase.xlsx中的用例，使用unittest进行断言校验
import json
import urllib.parse
import getUrlParams
import unittest
import readExcel
import paramunittest
from common.configHttp import RunMain

url = getUrlParams.GetUrlParams().get_url()  # 调用我们的getURlParams获取拼接的url
login_xls = readExcel.ReadExcel().get_xls('userCase.xlsx', 'login')


@paramunittest.parametrized(*login_xls)
class TestUrlLogin(unittest.TestCase):
    def setParameters(self, case_name, path, query, method):
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)

    def description(self):
        self.case_name

    def setUp(self):
        print(self.case_name + "测试开始前准备")

    def testcase01(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):  # 断言
        url1 = "http://127.0.0.1:8888/login?"
        new_url = url1 + self.query
        data1 = dict(urllib.parse.parse_qsl(
            urllib.parse.urlsplit(new_url).query))  # 将一个完整的URL中的name=&password=转换为{'name':'xxx','password':'bbb'}
        info = RunMain().run_main(self.method, url, data1)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        ss = json.loads(info)  # 将响应转换为字典格式
        if self.case_name == 'login':  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss['code'], 200)
        if self.case_name == 'login_error':
            self.assertEqual(ss['code'], -1)
        if self.case_name == 'login_null':
            self.assertEqual(ss['code'], 10001)
