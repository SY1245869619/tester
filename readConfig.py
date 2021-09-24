# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: readConfig.py
@time: 2021/6/28 14:25
"""
# 读取配置文件的方法，返回文件中的内容
import configparser # 是用来读取配置文件的包
import os
import getPathInfo  # 引入自己写的获取路径的类

path = getPathInfo.get_path()  # 调用实例化
config_path = os.path.join(path, 'config.ini')  # 在path路径下再加一级
config = configparser.ConfigParser()  # 调用外部的读取配置文件的方法
config.read(config_path, encoding='utf-8')


class ReadConfig():
    def get_http(self, name):
        value = config.get('HTTP', name)
        return value

    def get_email(self, name):
        value = config.get('EMAIL', name)
        return value

    def get_mysql(self, name):  # 备用
        value = config.get('DATABASE', name)
        return value


if __name__ == '__main__':
    print('HTTP中的baseurl值为：', ReadConfig().get_http('baseurl'))
    print('EMAIL中的开关on_off值为：', ReadConfig().get_email('on_off'))
