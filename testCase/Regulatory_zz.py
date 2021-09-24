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

url = getUrlParams.GetUrlParams().get_url_Regulatory_zz()  # 调用我们的getURlParams获取拼接的url
read_xls = readExcel.ReadExcel().get_xls('Regulatory_zz.xlsx', 'Page01')
RegulatoryHeaders = {
    # "Host": "test.regulatory.kachexiongdi.com",
    "Connection": "keep-alive",
    "EagleEye-SessionID": "gLkaUtXX3Xdsvtmbdoym51sv0F3C",
    "EagleEye-TraceID": "1293c09b1630639473203100223008",
    "EagleEye-pAppName": "en91xqoenk@4a295060f323008",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/92.0.4515.159 Safari/537.36",
    "Web-User-Agent": "yyht-plateform/0.0.1,Web",
    "accept": "*/*",
    # "Referer": "http://test.regulatory.kachexiongdi.com/networkFreight",
    'content-type': 'application/json;charset=UTF-8',
    "accept-encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,ko;q=0.6",
    "Cookie": "UM_distinctid=17ad319cb4972f-0d3f466d77dc29-6373264-1fa400-17ad319cb4a1062; "
              "_bl_uid=Lhkpgthz31L2b2wbpx8IdqmqqqCw; "
              "14_admin_session=1b95d046-6653-476a-b8e9-fe6fa804c4bd.plry4kfE2T9T4qtTsoxtVfAmzQM; "
              "CNZZDATA1279494848=1450524110-1630540547-%7C1630633978",
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
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '货主信息查询认证时间':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '货主信息查询企业信息北京':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '货主信息查询姓名刘':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '货主信息查询手机号186':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '货主信息查询成功认证状态':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '货主信息查询失败认证状态':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '货主信息查询未认证认证状态':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '货主信息组合查询姓名和状态成功刘':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
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
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '货主详情页关联车队长授权中授权状态查询':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '货主详情页关联车队长未授权状态查询':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '货主详情页关联车队长姓名查询大大大':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '货主详情页关联车队长重置按钮':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '车队长信息查询注册时间':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '车队长信息查询认证时间':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '车队长信息查询姓名沈缘':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '车队长信息查询手机号17713146220':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '车队长信息查询成功认证状态':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '车队长信息查询失败认证状态':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '车队长信息查询未认证认证状态':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '车队长信息组合查询认证成功沈缘':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '车队长信息重置按钮':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '跳转进入车队长详情页':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '车队长详情页关联企业授权中状态查询':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '车队长详情页关联企业终止授权状态查询':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '车队长详情页关联企业未授权状态查询':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '车队长详情页关联企业名称查询北京':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '车队长详情页关联企业重置按钮':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '司机信息查询注册时间':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '司机信息查询认证时间':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '司机信息查询姓名沈缘':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '司机息查询手机号':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '司机信息查询成功认证状态':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '司机信息查询失败认证状态':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '司机信息查询未认证认证状态':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '司机信息组合查询认证成功沈缘':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '司机信息重置按钮':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '车辆信息查询注册时间':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '车辆信息查询认证时间':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '车辆信息查询姓名沈缘':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '车辆息查询手机号':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '车辆息查询车牌号京A12345':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '车辆信息查询成功认证状态':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '车辆信息查询失败认证状态':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '车辆信息查询未认证认证状态':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '车辆信息组合查询认证成功沈缘':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '车辆信息重置按钮':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '跳转进入车辆详情京A12345':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '运单信息页筛选运单开始时间':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '运单信息页筛选运单结束时间':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '运单信息页筛选运单编号':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '运单信息页筛选司机姓名沈缘':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '运单信息页筛选司机手机号':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '运单信息页筛选车牌号京A12345':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '运单信息页筛选所属企业北京测试公司':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '运单信息页筛选货主姓名沈缘':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '运单信息页筛选运单状态被驳回':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '运单信息页筛选运单状态待货主支付':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '运单信息页筛选运单状态已取消':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '运单信息页筛选专线类型车队单':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '运单信息页筛选专线类型个人单':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '运单信息页重置按钮':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '跳转进入运单详情页43877':
            self.assertEqual(ss['warnType'], 1)
            print("》》》》》》》》》》断言判断warnType为1，测试通过")
        if self.case_name == '运单详情页点击更多跳转专线页id7068':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '开票专线页筛选时间':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '开票专线页筛选发货企业北京':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '开票专线页筛选收货企业北京':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '开票专线页筛选专线编号7068':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '开票专线页筛选所属企业北京':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '开票专线页筛选货主姓名沈缘':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '开票专线页筛选车队长姓名沈缘':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '开票专线页筛选货品名称原料':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '开票专线页筛选专线状态已关闭':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '开票专线页筛选专线状态进行中':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '开票专线页筛选专线状态已过期':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '开票专线页筛选渠道方向物流':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '开票专线页组合筛选车队长沈货主沈':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
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
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '磅室专线页筛选发货企业北京':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '磅室专线页筛选收货企业北京':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '磅室专线页筛选专线编号6545':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '磅室专线页筛选所属企业北京':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '磅室专线页筛选货品名称煤':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
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
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '磅单信息页筛选所属企业':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '磅单信息页筛选发货磅单类型':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '磅单信息页筛选收货磅单类型':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '磅单信息页筛选车牌号京A12345':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '磅单信息页筛选货品名称煤':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '磅单信息页筛选发货企业北京':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '磅单信息页筛选收货企业北京':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
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
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '缴税进展筛选姓名沈':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
        if self.case_name == '网络货运平台搜索企业和顺':
            self.assertEqual(ss['status'], 0)
            print("》》》》》》》》》》断言判断status为0，测试通过")
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
