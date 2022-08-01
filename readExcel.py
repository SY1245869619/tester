# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: readExcel.py
@time: 2021/6/29 10:51
"""
# @@@@@@@@@@@@@@@@@@@@@@@@@@读取Excel的方法@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
import os
# 需要安装包xlrd,因为2.0不支持xlsx格式，因此需要导入1.2.0的xlrd版本
from xlrd import open_workbook

import getPathInfo

# 获取项目的绝对路径
path = getPathInfo.get_path()


class ReadExcel():
    # xls_name填写用例的Excel名称 sheet_name是该Excel的sheet名称
    def get_xls(self, xls_name, sheet_name): # xls_name填写用例的Excel名称 sheet_name该Excel的sheet名称
        cls = []
        # 获取用例文件路径
        xlspath = os.path.join(path, "testFile", 'case', xls_name)
        # 打开用例Excel
        file = open_workbook(xlspath)
        # 获得打开Excel的sheet`
        sheet = file.sheet_by_name(sheet_name)
        # 获取sheet的内容行数
        nrows = sheet.nrows
        # 根据行数进行循环
        for i in range(nrows):
            # 如果这个 Excel的sheet的第i行的第i列不等于case_name,那么我们把这一行添加到cls[]中
            if sheet.row_values(i)[0] != u'case_name':
                cls.append(sheet.row_values(i))
        return cls


if __name__ == '__main__':  # 执行该文件测试是否可以正确获取Excel中的值
    print(ReadExcel().get_xls('userCase.xlsx', 'drivertrucker'))
    # print(ReadExcel().get_xls('userCase.xlsx', 'trucker')[0][1])
    # print(ReadExcel().get_xls('userCase.xlsx', 'trucker')[1][2])
