# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: AndroidDriver.py
@time: 2021/8/14 17:27
"""
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@和顺监管平台的测试用例编写，已完成@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
import json
import getUrlParams
import unittest
import readExcel
import paramunittest
from common.configHttp import RunMain

url = getUrlParams.GetUrlParams().get_url_Regulatory()  # 调用我们的getURlParams获取拼接的url
read_xls = readExcel.ReadExcel().get_xls('Regulatory.xlsx', 'Page01')
print(read_xls)
RegulatoryHeaders = {
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


@paramunittest.parametrized(*read_xls)
class Test(unittest.TestCase):
    def setParameters(self, case_name, path, query, method):
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)
        self.headers = RegulatoryHeaders

    def description(self):
        self.case_name

    def setUp(self):
        print(self.case_name + "----测试开始前准备")

    def test_Regulatory(self):
        self.checkResult()

    def tearDown(self):
        print("----测试结束，输出log完结\n\n")

    def checkResult(self):  # 断言
        print("接口为:" + self.path)
        print("传参为:" + self.query)
        if self.method == 'post':
            new_url = url + self.path
        else:
            new_url = url + self.path + '?' + self.query
        print("请求链接为⬇")
        print(new_url)
        info = RunMain().run_main(self.method, new_url, self.query,
                                  self.headers)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        ss = json.loads(info)  # 将响应转换为字典格式
        print("返回数据为⬇")
        print(ss)
        # if self.case_name == '网络货运平台搜索企业':
        #     self.assertEqual(ss['status'], 0)
        #     print("》》》》》》》》》》断言判断status为0，测试通过")
        # if self.case_name == '网络货运平台重置':
        #     self.assertEqual(ss['status'], 0)
        #     print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '进入网络货运平台页':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '进入货主信息页':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '进入车队长信息页':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '进入司机信息页':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '进入车辆信息页':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '进入运单信息页':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '进入网络货运专线页':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '进入磅室专线页':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '进入磅单信息页':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '货主信息查询注册时间':
            data_list = ss.get('result').get('data')
            for d in data_list:
                time = d.get('register_time')
                c = time > "2021-08-26 00:00:00"
                print("是否大于筛选开始时间：", c)
                a = time < "2021-08-26 23:59:59"
                print("是否小于筛选结束时间：", a)
                o = c and a
                print(o)
                self.assertTrue(o)
            print("》》》》》》》》》》注册时间在查询范围内，测试通过")
        if self.case_name == '货主信息查询认证时间':
            data_list = ss.get('result').get('data')
            for d in data_list:
                time = d.get('verified_time')
                c = time > "2021-08-27 00:00:00"
                print("是否大于筛选开始时间：", c)
                a = time < "2021-08-27 23:59:59"
                print("是否小于筛选结束时间：", a)
                o = c and a
                print(o)
                self.assertTrue(o)
            print("》》》》》》》》》》认证时间在查询范围内，测试通过")
        if self.case_name == '货主信息查询企业信息北京':
            data_list = ss.get('result').get('data')
            for d in data_list:
                company = d.get('companyName')
                print("company为：", company)
                name = d.get('name')
                print("name为：", name)
                c = '北京' in company
                a = '北京' in name
                o = c or a
                self.assertTrue(o)
            print("》》》》》》》》》》company和name中包含“北京”，测试通过")
        if self.case_name == '货主信息查询姓名刘':
            data_list = ss.get('result').get('data')
            for d in data_list:
                name = d.get('name')
                print("name为：", name)
                self.assertIn('刘', name)
            print("》》》》》》》》》》查询姓名中包含“刘”，测试通过")
        if self.case_name == '货主信息查询手机号186':
            data_list = ss.get('result').get('data')
            for d in data_list:
                phone = d.get('phone')
                print("phone为：", phone)
                self.assertIn('186', phone)
            print("》》》》》》》》》》查询手机号中包含“186”，测试通过")
        if self.case_name == '货主信息查询成功认证状态':
            data_list = ss.get('result').get('data')
            for d in data_list:
                verified_status = d.get('verified_status')
                print("verified_status为：", verified_status)
                self.assertEqual(verified_status, 'SUCCESS')
            print("》》》》》》》》》》查询认证成功的货主，测试通过")
        if self.case_name == '货主信息查询失败认证状态':
            data_list = ss.get('result').get('data')
            for d in data_list:
                verified_status = d.get('verified_status')
                print("verified_status为：", verified_status)
                self.assertEqual(verified_status, 'FAIL')
            print("》》》》》》》》》》查询认证失败的货主，测试通过")
        if self.case_name == '货主信息查询未认证认证状态':
            data_list = ss.get('result').get('data')
            for d in data_list:
                verified_status = d.get('verified_status')
                c = '' in verified_status
                a = 'APPROVE' in verified_status
                o = c or a
                print("verified_status为：", verified_status)
                self.assertTrue(o)
            print("》》》》》》》》》》查询未认证(审核中)的货主，测试通过")
        if self.case_name == '货主信息组合查询姓名和状态成功刘':
            data_list = ss.get('result').get('data')
            for d in data_list:
                verified_status = d.get('verified_status')
                print("verified_status为：", verified_status)
                name = d.get('name')
                print("name为：", name)
                c = 'SUCCESS' == verified_status
                print(c)
                a = '刘' in name
                print(a)
                o = c and a
                self.assertTrue(o)
            print("》》》》》》》》》》货主信息组合查询认证成功的刘，测试通过")
        if self.case_name == '货主信息重置按钮':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '跳转进入货主详情页':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '货主详情页关联车队长显示':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '货主详情页关联车队长终止授权状态查询':
            data_list = ss.get('result').get('data')
            for d in data_list:
                status = d.get('status')
                print("status为：", status)
                self.assertEqual(status, 'CLOSED')
            print("》》》》》》》》》》查询货主详情页关联车队长终止授权状态，测试通过")
        if self.case_name == '货主详情页关联车队长授权中授权状态查询':
            data_list = ss.get('result').get('data')
            for d in data_list:
                status = d.get('status')
                print("status为：", status)
                self.assertEqual(status, 'OPEN')
            print("》》》》》》》》》》查询货主详情页关联车队长授权中状态，测试通过")
        if self.case_name == '货主详情页关联车队长未授权状态查询':
            data_list = ss.get('result').get('data')
            for d in data_list:
                status = d.get('status')
                print("status为：", status)
                self.assertEqual(status, 'WAIT')
            print("》》》》》》》》》》查询货主详情页关联车队长未授权状态，测试通过")
        if self.case_name == '货主详情页关联车队长姓名查询大大大':
            data_list = ss.get('result').get('data')
            for d in data_list:
                middleman = d.get('middleman')
                name = middleman.get('name')
                print("name为：", name)
                self.assertIn('大大大', name)
            print("》》》》》》》》》》查询货主详情页关联车队长姓名包含大大大，测试通过")
        if self.case_name == '货主详情页关联车队长重置按钮':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '车队长信息查询注册时间':
            data_list = ss.get('result').get('data')
            for d in data_list:
                time = d.get('createdAt')
                c = time > "2021-08-01 00:00:00"
                print("是否大于筛选开始时间：", c)
                a = time < "2021-08-26 23:59:59"
                print("是否小于筛选结束时间：", a)
                o = c and a
                print(o)
                self.assertTrue(o)
        if self.case_name == '车队长信息查询认证时间':
            data_list = ss.get('result').get('data')
            for d in data_list:
                time = d.get('verified_time')
                c = time > "2021-08-01 00:00:00"
                print("是否大于筛选开始时间：", c)
                a = time < "2021-08-26 23:59:59"
                print("是否小于筛选结束时间：", a)
                o = c and a
                print(o)
                self.assertTrue(o)
        if self.case_name == '车队长信息查询姓名沈缘':
            data_list = ss.get('result').get('data')
            for d in data_list:
                name = d.get('name')
                print("name为：", name)
                self.assertIn('沈缘', name)
            print("》》》》》》》》》》查询姓名中包含“沈缘”，测试通过")
        if self.case_name == '车队长信息查询手机号17713146220':
            data_list = ss.get('result').get('data')
            for d in data_list:
                phone = d.get('phone')
                print("phone为：", phone)
                self.assertIn('17713146220', phone)
            print("》》》》》》》》》》查询手机号中包含“17713146220”，测试通过")
        if self.case_name == '车队长信息查询成功认证状态':
            data_list = ss.get('result').get('data')
            for d in data_list:
                verified_status = d.get('verified_status')
                print("verified_status为：", verified_status)
                self.assertEqual(verified_status, 'SUCCESS')
            print("》》》》》》》》》》查询认证成功的车队长，测试通过")
        if self.case_name == '车队长信息查询失败认证状态':
            data_list = ss.get('result').get('data')
            for d in data_list:
                verified_status = d.get('verified_status')
                print("verified_status为：", verified_status)
                self.assertEqual(verified_status, 'FAIL')
            print("》》》》》》》》》》查询认证失败的车队长，测试通过")
        if self.case_name == '车队长信息查询未认证认证状态':
            data_list = ss.get('result').get('data')
            for d in data_list:
                verified_status = d.get('verified_status')
                a = 'APPROVE' in verified_status
                print("verified_status为：", verified_status)
                self.assertTrue(a)
            print("》》》》》》》》》》查询未认证(审核中)的车队长，测试通过")
        if self.case_name == '车队长信息组合查询认证成功沈缘':
            data_list = ss.get('result').get('data')
            for d in data_list:
                verified_status = d.get('verified_status')
                print("verified_status为：", verified_status)
                name = d.get('name')
                print("name为：", name)
                c = 'SUCCESS' == verified_status
                print(c)
                a = '沈缘' in name
                print(a)
                o = c and a
                self.assertTrue(o)
            print("》》》》》》》》》》车队长信息组合查询认证成功的沈缘，测试通过")
        if self.case_name == '车队长信息重置按钮':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '跳转进入车队长详情页':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '车队长详情页关联企业授权中状态查询':
            data_list = ss.get('result').get('data')
            for d in data_list:
                status = d.get('status')
                print("status为：", status)
                self.assertEqual(status, 'OPEN')
            print("》》》》》》》》》》车队长详情页关联企业查询授权中状态企业，测试通过")
        if self.case_name == '车队长详情页关联企业终止授权状态查询':
            data_list = ss.get('result').get('data')
            for d in data_list:
                status = d.get('status')
                print("status为：", status)
                self.assertEqual(status, 'CLOSED')
            print("》》》》》》》》》》车队长详情页关联企业查询终止授权状态企业，测试通过")
        if self.case_name == '车队长详情页关联企业未授权状态查询':
            data_list = ss.get('result').get('data')
            for d in data_list:
                status = d.get('status')
                print("status为：", status)
                self.assertEqual(status, 0)
            print("》》》》》》》》》》车队长详情页关联企业查询终止授权状态企业，测试通过")
        if self.case_name == '车队长详情页关联企业名称查询北京':
            data_list = ss.get('result').get('data')
            for d in data_list:
                ownerCompanyName = d.get('ownerCompanyName')
                print('ownerCompanyName为：', ownerCompanyName)
                self.assertIn('北京', ownerCompanyName)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '车队长详情页关联企业重置按钮':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '司机信息查询注册时间':
            data_list = ss.get('result').get('data')
            for d in data_list:
                time = d.get('register_time')
                print(time)
                c = time > "2021-08-01 00:00:00"
                print("是否大于筛选开始时间：", c)
                a = time < "2021-08-26 23:59:59"
                print(time)
                print("是否小于筛选结束时间：", a)
                o = c and a
                print(o)
                self.assertTrue(o)
            print("》》》》》》》》》》注册时间在查询范围内，测试通过")
        if self.case_name == '司机信息查询认证时间':
            data_list = ss.get('result').get('data')
            for d in data_list:
                time = d.get('verified_time')
                c = time > "2021-08-01 00:00:00"
                print("是否大于筛选开始时间：", c)
                a = time < "2021-08-26 23:59:59"
                print("是否小于筛选结束时间：", a)
                o = c and a
                print(o)
                self.assertTrue(o)
            print("》》》》》》》》》》认证时间在查询范围内，测试通过")
        if self.case_name == '司机信息查询姓名沈缘':
            data_list = ss.get('result').get('data')
            for d in data_list:
                name = d.get('name')
                print("name为：", name)
                self.assertIn('沈缘', name)
            print("》》》》》》》》》》查询姓名中包含“沈缘”，测试通过")
        if self.case_name == '司机息查询手机号':
            data_list = ss.get('result').get('data')
            for d in data_list:
                phone = d.get('phone')
                print("phone为：", phone)
                self.assertIn('13171521557', phone)
            print("》》》》》》》》》》查询手机号中包含“13171521557”，测试通过")
        if self.case_name == '司机信息查询成功认证状态':
            data_list = ss.get('result').get('data')
            for d in data_list:
                verified_status = d.get('verified_status')
                print("verified_status为：", verified_status)
                self.assertEqual(verified_status, 'SUCCESS')
            print("》》》》》》》》》》查询认证成功的司机，测试通过")
        if self.case_name == '司机信息查询失败认证状态':
            data_list = ss.get('result').get('data')
            for d in data_list:
                verified_status = d.get('verified_status')
                print("verified_status为：", verified_status)
                self.assertEqual(verified_status, 'FAIL')
            print("》》》》》》》》》》查询认证成功的司机，测试通过")
        if self.case_name == '司机信息查询未认证认证状态':
            data_list = ss.get('result').get('data')
            for d in data_list:
                verified_status = d.get('verified_status')
                c = '' in verified_status
                a = 'APPROVE' in verified_status
                o = c or a
                print("verified_status为：", verified_status)
                self.assertTrue(o)
            print("》》》》》》》》》》查询未认证(审核中)的司机，测试通过")
        if self.case_name == '司机信息组合查询认证成功沈缘':
            data_list = ss.get('result').get('data')
            for d in data_list:
                verified_status = d.get('verified_status')
                print("verified_status为：", verified_status)
                name = d.get('name')
                print("name为：", name)
                c = 'SUCCESS' == verified_status
                print(c)
                a = '沈缘' in name
                print(a)
                o = c and a
                self.assertTrue(o)
            print("》》》》》》》》》》司机信息组合查询认证成功的沈缘，测试通过")
        if self.case_name == '司机信息重置按钮':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '车辆信息查询注册时间':
            data_list = ss.get('result').get('data')
            for d in data_list:
                time = d.get('createdAt')
                c = time > "2021-08-01 00:00:00"
                print("是否大于筛选开始时间：", c)
                a = time < "2021-08-27 23:59:59"
                print("是否小于筛选结束时间：", a)
                o = c and a
                print(o)
                self.assertTrue(o)
            print("》》》》》》》》》》注册时间在查询范围内，测试通过")
        if self.case_name == '车辆信息查询认证时间':
            data_list = ss.get('result').get('data')
            for d in data_list:
                time = d.get('check_time')
                c = time > "2021-08-01 00:00:00"
                print("是否大于筛选开始时间：", c)
                a = time < "2021-08-27 23:59:59"
                print("是否小于筛选结束时间：", a)
                o = c and a
                print(o)
                self.assertTrue(o)
            print("》》》》》》》》》》认证时间在查询范围内，测试通过")
        if self.case_name == '车辆信息查询姓名沈缘':
            data_list = ss.get('result').get('data')
            for d in data_list:
                name = d.get('name')
                print("name为：", name)
                self.assertIn('沈缘', name)
            print("》》》》》》》》》》查询姓名中包含“沈缘”，测试通过")
        if self.case_name == '车辆息查询手机号':
            data_list = ss.get('result').get('data')
            for d in data_list:
                phone = d.get('phone')
                print("phone为：", phone)
                self.assertIn('13171521557', phone)
            print("》》》》》》》》》》查询手机号中包含“13171521557”，测试通过")
        if self.case_name == '车辆息查询车牌号京A12345':
            data_list = ss.get('result').get('data')
            for d in data_list:
                trailerPlateNumber = d.get('trailerPlateNumber')
                print("trailerPlateNumber为：", trailerPlateNumber)
                self.assertIn('京A12345', trailerPlateNumber)
            print("》》》》》》》》》》查询车牌号中包含“京A12345”，测试通过")
        if self.case_name == '车辆信息查询成功认证状态':
            data_list = ss.get('result').get('data')
            for d in data_list:
                verified_status = d.get('verified_status')
                print("verified_status为：", verified_status)
                self.assertEqual(verified_status, 'SUCCESS')
            print("》》》》》》》》》》查询认证成功的车辆，测试通过")
        if self.case_name == '车辆信息查询失败认证状态':
            data_list = ss.get('result').get('data')
            for d in data_list:
                verified_status = d.get('verified_status')
                print("verified_status为：", verified_status)
                self.assertEqual(verified_status, 'FAIL')
            print("》》》》》》》》》》查询认证失败的车辆，测试通过")
        if self.case_name == '车辆信息查询未认证认证状态':
            data_list = ss.get('result').get('data')
            for d in data_list:
                verified_status = d.get('verified_status')
                c = '' in verified_status
                a = 'APPROVE' in verified_status
                o = c or a
                print("verified_status为：", verified_status)
                self.assertTrue(o)
            print("》》》》》》》》》》查询未认证(审核中)的车辆，测试通过")
        if self.case_name == '车辆信息组合查询认证成功沈缘':
            data_list = ss.get('result').get('data')
            for d in data_list:
                verified_status = d.get('verified_status')
                print("verified_status为：", verified_status)
                name = d.get('name')
                print("name为：", name)
                c = 'SUCCESS' == verified_status
                print(c)
                a = '沈缘' in name
                print(a)
                o = c and a
                self.assertTrue(o)
            print("》》》》》》》》》》车辆信息组合查询认证成功的沈缘，测试通过")
        if self.case_name == '车辆信息重置按钮':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '跳转进入车辆详情京A12345':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '运单信息页筛选运单开始时间':
            data_list = ss.get('result').get('data')
            for d in data_list:
                createdAt = d.get('createdAt')
                c = createdAt > "2021-08-01 00:00:00"
                print("是否大于筛选开始时间：", c)
                a = createdAt < "2021-08-27 23:59:59"
                print("是否小于筛选结束时间：", a)
                o = c and a
                print(o)
                self.assertTrue(o)
            print("》》》》》》》》》》运单开始时间在查询范围内，测试通过")
        if self.case_name == '运单信息页筛选运单结束时间':
            data_list = ss.get('result').get('data')
            for d in data_list:
                payTime = d.get('payTime')
                c = payTime > "2021-08-01 00:00:00"
                print("是否大于筛选开始时间：", c)
                a = payTime < "2021-08-27 23:59:59"
                print("是否小于筛选结束时间：", a)
                o = c and a
                print(o)
                self.assertTrue(o)
            print("》》》》》》》》》》运单结束时间在查询范围内，测试通过")
        if self.case_name == '运单信息页筛选运单编号':
            data_list = ss.get('result').get('data')
            for d in data_list:
                orderNo = d.get('orderNo')
                print("orderNo为：", orderNo)
                self.assertEqual('2021081601010106312730148257', orderNo)
            print("》》》》》》》》》》查询运单编号2021081601010106312730148257，测试通过")
        if self.case_name == '运单信息页筛选司机姓名沈缘':
            data_list = ss.get('result').get('data')
            for d in data_list:
                truckerName = d.get('truckerName')
                print("truckerName为：", truckerName)
                self.assertIn('沈缘', truckerName)
            print("》》》》》》》》》》查询司机姓名中包含“沈缘”，测试通过")
        if self.case_name == '运单信息页筛选司机手机号':
            data_list = ss.get('result').get('data')
            for d in data_list:
                phone = d.get('phone')
                print("phone为：", phone)
                self.assertIn('13171521557', phone)
            print("》》》》》》》》》》查询手机号中包含“13171521557”，测试通过")
        if self.case_name == '运单信息页筛选车牌号京A12345':
            data_list = ss.get('result').get('data')
            for d in data_list:
                trailerPlateNumber = d.get('trailerPlateNumber')
                print("trailerPlateNumber为：", trailerPlateNumber)
                self.assertIn('京A12345', trailerPlateNumber)
            print("》》》》》》》》》》查询车牌号中包含“京A12345”，测试通过")
        if self.case_name == '运单信息页筛选所属企业北京测试公司':
            data_list = ss.get('result').get('data')
            for d in data_list:
                companyName = d.get('companyName')
                print("companyName为：", companyName)
                self.assertIn('北京测试公司', companyName)
            print("》》》》》》》》》》查询所属企业北京测试公司，测试通过")
        if self.case_name == '运单信息页筛选货主姓名沈缘':
            data_list = ss.get('result').get('data')
            for d in data_list:
                ownerName = d.get('ownerName')
                print("ownerName为：", ownerName)
                self.assertIn('沈', ownerName)
            print("》》》》》》》》》》查询货主姓名中包含“沈缘”，测试通过")
        if self.case_name == '运单信息页筛选运单状态被驳回':
            data_list = ss.get('result').get('data')
            for d in data_list:
                status = d.get('status')
                print("status为：", status)
                self.assertEqual(status, 'REJECT')
            print("》》》》》》》》》》查询运单信息页筛选运单状态被驳回，测试通过")
        if self.case_name == '运单信息页筛选运单状态待货主支付':
            data_list = ss.get('result').get('data')
            for d in data_list:
                status = d.get('status')
                c = "GO_WAIT_PAY_FC_WAIT_PAY" in status
                a = "WAIT_PAY" in status
                o = c or a
                print(o)
                self.assertTrue(o)
            print("》》》》》》》》》》查询运单信息页筛选运单状态待货主支付，测试通过")
        if self.case_name == '运单信息页筛选运单状态已取消':
            data_list = ss.get('result').get('data')
            for d in data_list:
                status = d.get('status')
                print("status为：", status)
                self.assertEqual(status, 'CANCEL')
            print("》》》》》》》》》》查询运单信息页筛选运单状态待货主支付，测试通过")
        if self.case_name == '运单信息页筛选专线类型车队单':
            data_list = ss.get('result').get('data')
            for d in data_list:
                leader = d.get('leader')
                print("leader为：", leader)
                self.assertIsNotNone(leader)
            print("》》》》》》》》》》查询运单信息页筛选专线类型车队单，测试通过")
        if self.case_name == '运单信息页筛选专线类型个人单':
            data_list = ss.get('result').get('data')
            for d in data_list:
                leader = d.get('leader')
                print("leader为：", leader)
                self.assertEqual("", leader)
            print("》》》》》》》》》》查询运单信息页筛选专线类型个人单，测试通过")
        if self.case_name == '运单信息页重置按钮':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '跳转进入运单详情页43877':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '运单详情页点击更多跳转专线页id7068':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '开票专线页筛选时间':
            data_list = ss.get('result').get('data')
            for d in data_list:
                createdAt = d.get('createdAt')
                c = createdAt > "2021-08-01 00:00:00"
                print("是否大于筛选开始时间：", c)
                a = createdAt < "2021-08-28 23:59:59"
                print("是否小于筛选结束时间：", a)
                o = c and a
                print(o)
                self.assertTrue(o)
            print("》》》》》》》》》》创建时间在查询范围内，测试通过")
        if self.case_name == '开票专线页筛选发货企业北京':
            data_list = ss.get('result').get('data')
            for d in data_list:
                fromCompany = d.get('fromCompany')
                print("fromCompany为：", fromCompany)
                self.assertIn('北京', fromCompany)
            print("》》》》》》》》》》查询发货企业中包含“北京”，测试通过")
        if self.case_name == '开票专线页筛选收货企业北京':
            data_list = ss.get('result').get('data')
            for d in data_list:
                toCompany = d.get('toCompany')
                print("toCompany为：", toCompany)
                self.assertIn('北京', toCompany)
            print("》》》》》》》》》》查询收货企业中包含“北京”，测试通过")
        if self.case_name == '开票专线页筛选专线编号7068':
            data_list = ss.get('result').get('data')
            for d in data_list:
                id = d.get('id')
                print("id为：", id)
                self.assertEqual(7068, id)
            print("》》》》》》》》》》查询专线编号6521，测试通过")
        if self.case_name == '开票专线页筛选所属企业北京':
            data_list = ss.get('result').get('data')
            for d in data_list:
                company = d.get('company')
                print("company为：", company)
                self.assertIn('北京', company)
            print("》》》》》》》》》》查询所属企业中包含“北京”，测试通过")
        if self.case_name == '开票专线页筛选货主姓名沈缘':
            data_list = ss.get('result').get('data')
            for d in data_list:
                goodsOwnerName = d.get('goodsOwnerName')
                print("goodsOwnerName：", goodsOwnerName)
                self.assertIn('沈缘', goodsOwnerName)
            print("》》》》》》》》》》查询开票专线页筛选货主姓名沈缘，测试通过")
        if self.case_name == '开票专线页筛选车队长姓名沈缘':
            data_list = ss.get('result').get('data')
            for d in data_list:
                fleetCaption = d.get('fleetCaption')
                name = fleetCaption.get('name')
                print("name为：", name)
                self.assertIn('沈缘', name)
            print("》》》》》》》》》》查询开票专线页筛选车队长姓名沈缘，测试通过")
        if self.case_name == '开票专线页筛选货品名称原料':
            data_list = ss.get('result').get('data')
            for d in data_list:
                goodsType = d.get('goodsType')
                print("goodsType为：", goodsType)
                self.assertIn('原料', goodsType)
            print("》》》》》》》》》》查询开票专线页筛选货品名称原料，测试通过")
        if self.case_name == '开票专线页筛选专线状态已关闭':
            data_list = ss.get('result').get('data')
            for d in data_list:
                status = d.get('status')
                print("status为：", status)
                self.assertEqual('CLOSE', status)
            print("》》》》》》》》》》查询开票专线页筛选专线状态已关闭，测试通过")
        if self.case_name == '开票专线页筛选专线状态进行中':
            data_list = ss.get('result').get('data')
            for d in data_list:
                status = d.get('status')
                print("status为：", status)
                self.assertEqual('PROCESS', status)
            print("》》》》》》》》》》查询开票专线页筛选专线状态进行中，测试通过")
        if self.case_name == '开票专线页筛选专线状态已过期':
            data_list = ss.get('result').get('data')
            for d in data_list:
                status = d.get('status')
                print("status为：", status)
                self.assertEqual('EXPIRED', status)
            print("》》》》》》》》》》查询开票专线页筛选专线状态已过期，测试通过")
        if self.case_name == '开票专线页筛选渠道方向物流':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '开票专线页组合筛选车队长沈货主沈':
            data_list = ss.get('result').get('data')
            for d in data_list:
                goodsOwnerName = d.get('goodsOwnerName')
                print("goodsOwnerName为：", goodsOwnerName)
                name = d.get('fleetCaption').get('name')
                print("name为：", name)
                c = '沈' in goodsOwnerName
                print(c)
                a = '沈' in name
                print(a)
                o = c and a
                self.assertTrue(o)
            print("》》》》》》》》》》车队长信息组合查询车队长沈货主沈，测试通过")
        if self.case_name == '开票专线页重置按钮':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '跳转进入开票专线详情的专线基本信息tab页id7068':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '跳转进入开票专线详情的专线关联运单tab':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '跳转进入开票专线详情的专线变更记录tab':
            self.assertEqual(ss['warnType'], 1)
            print("》》》》》》》》》》断言判断warnType为1，测试通过")
        if self.case_name == '磅室专线页筛选时间':
            data_list = ss.get('result').get('data')
            for d in data_list:
                createdAt = d.get('createdAt')
                c = createdAt > "2021-08-01 00:00:00"
                print("是否大于筛选开始时间：", c)
                a = createdAt < "2021-08-28 23:59:59"
                print("是否小于筛选结束时间：", a)
                o = c and a
                print(o)
                self.assertTrue(o)
            print("》》》》》》》》》》查询时间在磅室专线页筛选时间内，测试通过")
        if self.case_name == '磅室专线页筛选发货企业北京':
            data_list = ss.get('result').get('data')
            for d in data_list:
                fromCompany = d.get('fromCompany')
                print("fromCompany为：", fromCompany)
                self.assertIn('北京', fromCompany)
            print("》》》》》》》》》》查询磅室专线页筛选发货企业北京，测试通过")
        if self.case_name == '磅室专线页筛选收货企业北京':
            data_list = ss.get('result').get('data')
            for d in data_list:
                toCompany = d.get('toCompany')
                print("toCompany为：", toCompany)
                self.assertIn('北京', toCompany)
            print("》》》》》》》》》》查询磅室专线页筛选收货企业北京，测试通过")
        if self.case_name == '磅室专线页筛选专线编号6545':
            data_list = ss.get('result').get('data')
            for d in data_list:
                id = d.get('id')
                print("toCompany为：", id)
                self.assertEqual(6545, id)
            print("》》》》》》》》》》查询磅室专线页筛选专线编号6545，测试通过")
        if self.case_name == '磅室专线页筛选所属企业北京':
            data_list = ss.get('result').get('data')
            for d in data_list:
                company = d.get('company')
                print("company为：", company)
                self.assertIn('北京', company)
            print("》》》》》》》》》》查询磅室专线页筛选所属企业北京，测试通过")
        if self.case_name == '磅室专线页筛选货品名称煤':
            data_list = ss.get('result').get('data')
            for d in data_list:
                goodsType = d.get('goodsType')
                print("goodsType为：", goodsType)
                self.assertIn('煤', goodsType)
            print("》》》》》》》》》》查询磅室专线页筛选货品名称煤，测试通过")
        if self.case_name == '磅室专线页筛选渠道方向物流':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '磅室专线页重置按钮':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '跳转进入磅室专线详情的专线基本信息tab':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '跳转进入磅室专线详情的专线变更记录tab':
            self.assertEqual(ss['warnType'], 1)
            print("》》》》》》》》》》断言判断warnType为1，测试通过")
        if self.case_name == '磅单信息页筛选出站时间':
            data_list = ss.get('result').get('data')
            for d in data_list:
                outTime = d.get('outTime')
                c = outTime > "2021-08-01 00:00:00"
                print("是否大于筛选开始时间：", c)
                a = outTime < "2021-08-28 23:59:59"
                print("是否小于筛选结束时间：", a)
                o = c and a
                print(o)
                self.assertTrue(o)
            print("》》》》》》》》》》查询时间在磅单信息页筛选出站时间内，测试通过")
        if self.case_name == '磅单信息页筛选所属企业':
            data_list = ss.get('result').get('data')
            for d in data_list:
                companyName = d.get('companyName')
                print("companyName为：", companyName)
                self.assertIn('北京', companyName)
            print("》》》》》》》》》》查询磅单信息页筛选所属企业北京，测试通过")
        if self.case_name == '磅单信息页筛选发货磅单类型':
            data_list = ss.get('result').get('data')
            for d in data_list:
                receiveOrSend = d.get('receiveOrSend')
                print("receiveOrSend为：", receiveOrSend)
                self.assertEqual(False, receiveOrSend)
            print("》》》》》》》》》》查询磅单信息页筛选发货磅单类型，测试通过")
        if self.case_name == '磅单信息页筛选收货磅单类型':
            data_list = ss.get('result').get('data')
            for d in data_list:
                receiveOrSend = d.get('receiveOrSend')
                print("receiveOrSend为：", receiveOrSend)
                self.assertEqual(True, receiveOrSend)
            print("》》》》》》》》》》查询磅单信息页筛选收货磅单类型，测试通过")
        if self.case_name == '磅单信息页筛选车牌号京A12345':
            data_list = ss.get('result').get('data')
            for d in data_list:
                trailerPlateNumber = d.get('trailerPlateNumber')
                print("trailerPlateNumber为：", trailerPlateNumber)
                self.assertIn('京A12345', trailerPlateNumber)
            print("》》》》》》》》》》查询磅单信息页筛选车牌号京A12345，测试通过")
        if self.case_name == '磅单信息页筛选货品名称煤':
            data_list = ss.get('result').get('data')
            for d in data_list:
                goodsType = d.get('goodsType')
                print("goodsType为：", goodsType)
                self.assertIn('煤', goodsType)
            print("》》》》》》》》》》查询磅单信息页筛选货品名称煤，测试通过")
        if self.case_name == '磅单信息页筛选发货企业北京':
            data_list = ss.get('result').get('data')
            for d in data_list:
                fromCompany = d.get('fromCompany')
                print("fromCompany为：", fromCompany)
                self.assertIn('北京', fromCompany)
            print("》》》》》》》》》》查询磅单信息页筛选发货企业北京，测试通过")
        if self.case_name == '磅单信息页筛选收货企业北京':
            data_list = ss.get('result').get('data')
            for d in data_list:
                toCompany = d.get('toCompany')
                print("toCompany为：", toCompany)
                self.assertIn('北京', toCompany)
            print("》》》》》》》》》》查询磅单信息页筛选收货企业北京，测试通过")
        if self.case_name == '磅单信息页重置按钮':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '跳转进入电子磅单页':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '缴税进展筛选交易时间':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '缴税进展筛选企业名称北京':
            data_list = ss.get('result').get('data')
            for d in data_list:
                companyName = d.get('companyName')
                print("companyName为：", companyName)
                self.assertIn('北京', companyName)
            print("》》》》》》》》》》查询缴税进展筛选企业名称北京，测试通过")
        if self.case_name == '缴税进展筛选姓名沈':
            data_list = ss.get('result').get('data')
            for d in data_list:
                name = d.get('name')
                print("name为：", name)
                self.assertIn('沈', name)
            print("》》》》》》》》》》查询缴税进展筛选姓名沈，测试通过")
        if self.case_name == '网络货运平台搜索企业和顺':
            data_list = ss.get('result').get('data')
            for d in data_list:
                companyName = d.get('companyName')
                print("companyName为：", companyName)
                self.assertIn('和顺', companyName)
            print("》》》》》》》》》》查询网络货运平台搜索企业和顺，测试通过")
        if self.case_name == '网络货运平台重置':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '切换至返税进展tab':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '返税进展页填入备注信息':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '跳转进入司机详情页':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")



if __name__ == '__main__':
    print()
