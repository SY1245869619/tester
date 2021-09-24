# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: demo.py
@time: 2021/8/28 18:01
"""
# c = "" > "2021-08-01 00:00:00"
# print(c)
time = "2021-07-01 06:00:00"
c = time > "2021-08-01 00:00:00"
print("是否大于筛选开始时间：", c)
a = time < "2021-08-25 23:59:59"
print("是否小于筛选结束时间：", a)
o = c and a
print(o)
