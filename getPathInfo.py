# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: getPathInfo.py
@time: 2021/6/28 14:25
"""
# 获取项目的绝对路径
import os


def get_path():
    path = os.path.split(os.path.realpath(__file__))[0]
    return path


if __name__ == '__main__':
    print('测试路径是否OK,路径为：', get_path())
