# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: getUrlParams.py
@time: 2021/6/28 14:25
"""
# 获取接口的URL、参数、和method等
import readConfig as readConfig

readConfig = readConfig.ReadConfig()


class GetUrlParams():
    def get_url(self):
        new_url = readConfig.get_http('scheme') + '://' + readConfig.get_http('baseurl') + ':8888' + '/login' + '?'
        # logger.info('new_url' + new_url)
        return new_url
    #Android司机端
    def get_url_AndroidDriver(self):
        new_url = 'http://test.api.kachexiongdi.com'
        return new_url
    #运营后台
    def get_url_Operational(self):
        new_url = 'http://test.data.kachexiongdi.com'
        return new_url
    #监管平台
    def get_url_Regulatory(self):
        new_url = 'http://test.regulatory.kachexiongdi.com'
        return new_url
    #开票平台
    def get_url_Invoice(self):
        new_url = 'http://test.invoice.kachexiongdi.com'
        return new_url
    #监管平台正式
    def get_url_Regulatory_zz(self):
        new_url = 'https://regulatory.kachexiongdi.com'
        return new_url
    #运营后台正式
    def get_url_listtrucker(self):
        new_url = 'https://data.kachexiongdi.com'
        return new_url

if __name__ == '__main__':
    print(GetUrlParams().get_url())
