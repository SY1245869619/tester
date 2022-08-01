# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: testApi.py
@time: 2021/6/28 14:26
"""
# @@@@@@@@@@@@@@@@@@@@@@@@@@提供本地测试的接口服务，用于接口的测试@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

import json
import flask
from flask import request

"""
flask是一个web框架，通过flask提供的装饰器@server.route(),可以将普通的函数转换为服务
"""
# 创建一个服务，将当前python文件作为一个服务
server = flask.Flask(__name__)


# @server.route()可以将函数转变微服务。登录接口的路径、请求方式
@server.route('/login', methods=['get', 'post'])
def login():
    # 获取通过url请求传的用户名
    username = request.values.get('name')
    # 获取通过url请求传的明文密码
    password = request.values.get('password')
    # 判断用户名和密码都不为空
    if username and password:
        if username == 'shenyuan' and password == '123456':
            result = {'code': 200, 'message': '登录成功'}
            # 将字典转换为字符串
            return json.dumps(result, ensure_ascii=False)
        else:
            result = {'code': -1, 'message': '账号或密码错误'}
            return json.dumps(result, ensure_ascii=False)
    else:
        result = {'code': 1001, 'message': '参数不能为空！'}
        return json.dumps(result, ensure_ascii=False)


if __name__ == '__main__':
    server.run(debug=True, port=8888, host='127.0.0.1')
