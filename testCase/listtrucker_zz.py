# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: AndroidDriver.py
@time: 2021/8/14 17:27
"""

import json

import requests

import getUrlParams
import unittest
import readExcel
import paramunittest
from common.configHttp import RunMain

url = getUrlParams.GetUrlParams().get_url_listtrucker()  # 调用我们的getURlParams获取拼接的url
read_xls = readExcel.ReadExcel().get_xls('listtrucker_zz.xlsx', 'Page01')


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
            "Connection": "keep-alive",
            "EagleEye-SessionID": "vbkemttn5hCi7zsnm0tRrnygsLy2",
            "EagleEye-TraceID": "f635b88f1629628861302100423008",
            "EagleEye-pAppName": "en91xqoenk@4a295060f323008",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
            "Web-User-Agent": "yyht-plateform/0.0.1,Web",
            "Accept": "*/*",
            "Referer": "https://data.kachexiongdi.com/truckerList",
            "Accept-Encoding": "gzip,deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,ko;q=0.6",
            "Cookie": "UM_distinctid=17ad319cb4972f-0d3f466d77dc29-6373264-1fa400-17ad319cb4a1062; "
                      "_bl_uid=28kj9s7nr4F5gmj4qykg0Rgw6s44; "
                      "34_admin_session=8782d934-61ef-4eca-b42d-18fd1ec230f6.iODNlAgFMqZAPkMV03i3pjd1Ae0; "
                      "CNZZDATA1279494848=40557228-1629875095-%7C1630737389",
        }
        print("接口为:" + self.path)
        print("传参为:" + self.query)
        new_url = url + self.path + '?' + self.query
        print("请求链接为⬇")
        print(new_url)
        info = RunMain().run_main(self.method, new_url, self.query,
                                  headers)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        ss = json.loads(info)  # 将响应转换为字典格式
        print("返回数据为⬇")
        print(ss)
        if self.case_name == '李玉岗':
            data_list = ss.get('result').get('data')
            for d in data_list:
                verified_status = d.get('verified_status')
                print("verified_status为：", verified_status)
                a = "SUCCESS" in verified_status
                trailerPlateNumber = d.get('trailerPlateNumber')
                print("trailerPlateNumber为：", trailerPlateNumber)
                phone = d.get('phone')
                b = "晋KS7481" in trailerPlateNumber
                c = a and b
                self.assertTrue(c)
            print("》》》》》》》》》》查询认证成功的司机，测试通过" + self.case_name)


if __name__ == '__main__':
    print()
