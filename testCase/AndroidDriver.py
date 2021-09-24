# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: AndroidDriver.py
@time: 2021/8/14 17:27
"""

import json
import getUrlParams
import unittest
import readExcel
import paramunittest
from common.configHttp import RunMain

url = getUrlParams.GetUrlParams().get_url_AndroidDriver()  # 调用我们的getURlParams获取拼接的url
read_xls = readExcel.ReadExcel().get_xls('AndroidDriver.xlsx', 'MyPage')


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

    def test_AndroidDriver(self):
        self.checkResult()

    def tearDown(self):
        print( "----测试结束，输出log完结\n\n")

    def checkResult(self):  # 断言
        new_url = url + self.path + '?' + self.query
        print(new_url)
        info = RunMain().run_main(self.method, new_url, self.query)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        ss = json.loads(info)  # 将响应转换为字典格式
        print(ss)
        if self.case_name == '进入我的页':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》测试通过，status为0")
        if self.case_name == '获取消息':
            self.assertEqual(ss['warnType'], 1)
            print("》》》》》》》》》》测试通过，接口正常")


if __name__ == '__main__':
    print()
