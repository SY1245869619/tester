# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: runAll.py
@time: 2021/6/28 14:26
"""
# 开始执行接口自动化，项目工程 部署完毕后直接运行该文件即可
import os
import readConfig
import unittest
import getPathInfo
import common.HTMLTestRunner as HTMLTestRunner
from common.configEmail import SendEmail
import common.Log

log = common.Log.logger

send_mail = SendEmail(
    username='1245869619@qq.com',
    password='azugqhtyhalgifih',  # 这个填入的是授权码，不是密码！！！！
    recv=['sy17713146220@dingtalk.com', 'shenyuan@kachexiongdi.com'],  # 填入收件人
    # , '1438044262@qq.com'
    title='方向科技-自动化测试报告',
    content='本次测试需求包含\n”监管平台需求“\n*****请使用浏览器下载打开附件*****',
    file=r'D:\TestProject\result\report.html',
    ssl=False,
)
path = getPathInfo.get_path()
report_path = os.path.join(path, 'result')
on_off = readConfig.ReadConfig().get_email('on_off')


# log = common.Log.logger


class AllTest:  # 定义一个类AllTest
    def __init__(self):  # 初始化一些参数和数据
        global resultPath
        resultPath = os.path.join(report_path, "report.html")
        self.caseListFile = os.path.join(path, "caseList.txt")  # 配置执行哪些测试文件的配置文件路径
        self.caseFile = os.path.join(path, "testCase")  # 真正的测试断言文件路径
        self.caseList = []
        # log.info('resultPath', resultPath)
        # log.info('caseListFile', self.caseListFile)
        # log.info('caseList', self.caseList)

    def set_case_list(self):
        """
              读取caselist.txt文件中的用例名称，并添加到caselist元素组
        """
        fb = open(self.caseListFile)
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):  # 如果data非空且不以#开头
                self.caseList.append(data.replace("\n", ""))  # 读取每行数据会将换行转换为\n，去掉每行数据中的\n
        fb.close()

    def set_case_suite(self):
        self.set_case_list()  # 通过set_case_list()拿到caseList元素组
        test_suite = unittest.TestSuite()
        suite_module = []
        print("*********测试开始*********")
        for case in self.caseList:
            case_name = case.split("/")[-1]  # 通过split函数来将aaa/bbb分割字符串，-1取后面，0取前面
            print("执行用例为:" + case_name + '.py')  # 打印出取出来的名称
            # 批量加载用例，第一个参数为用例存放路径，第一个参数为路径文件名
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py', top_level_dir=None)
            suite_module.append(discover)  # 将discover存入suite_module元素组
            print('suite_module元素组:' + str(suite_module))
        if len(suite_module) > 0:  # 判断suite_module元素组是否存在元素
            for suite in suite_module:  # 如果存在，循环取出元素组内容，命名为suite
                for test_name in suite:  # 从discover中取出test_name，使用addTest添加到测试集
                    test_suite.addTest(test_name)
        else:
            print('else:')
            return None
        return test_suite  # 返回测试集

    def run(self):
        try:
            suit = self.set_case_suite()  # 调用set_case_suite获取test_suite
            print('尝试执行')
            print(str(suit))
            if suit is not None:  # 判断test_suite是否为空
                print('判断是否匹配断言')
                fp = open(resultPath, "wb")  # 打开result/report.html测试报告文件，如果不存在就创建
                # 调用HTMLTestRunner
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="方向科技-接口自动化测试报告", description="测试描述")
                runner.run(suit)
            else:
                print("没有测试用例需要执行")
        except Exception as ex:
            print(str(ex))
            # log.info(str(ex))

        finally:
            print("*********测试结束*********")
            # log.info("*********TEST END*********")
        # 判断邮件发送的开关
        if on_off == 'on':
            send_mail.send_email()
        else:
            print("邮件发送开关配置关闭，请打开开关后可正常自动发送测试报告")

    # pythoncom.CoInitialize()
    # scheduler = BlockingScheduler()
    # scheduler.add_job(AllTest().run, 'cron', day_of_week='1-5', hour=14, minute=59)
    # scheduler.start()


if __name__ == '__main__':
    AllTest().run()
