# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: configEmail.py
@time: 2021/6/28 14:20
"""
# @@@@@@@@@@@@@@@@@@@@@@配置发送邮件的主题、正文等，将测试报告发送并抄送到相关人邮箱的逻辑@@@@@@@@@@@@@@@@@@@@@@

import os
import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendEmail(object):
    def __init__(self, username, password, recv, title, content,
                 file=None, ssl=False,
                 email_host='smtp.qq.com', port=25, ssl_port=445):
        self.username = username  # 用户名
        self.password = password  # 授权码
        self.recv = recv  # 收件人，多个要传list ['1245869619@qq.com','17713146220@163.com]
        self.title = title  # 邮件标题
        self.content = content  # 邮件正文
        self.file = file  # 附件路径，如果不在当前目录下，要写绝对路径
        self.email_host = email_host  # smtp服务器地址
        self.port = port  # 普通端口
        self.ssl = ssl  # 是否安全链接
        self.ssl_port = ssl_port  # 安全链接端口

    def send_email(self):
        msg = MIMEMultipart()
        # 发送内容的对象
        if self.file:  # 处理附件的
            file_name = os.path.split(self.file)[-1]  # 只取文件名，不取路径
            try:
                f = open(self.file, 'rb').read()
            except Exception as e:
                raise Exception('附件打不开！！！！')
            else:
                att = MIMEText(f, "base64", "utf-8")
                att["Content-Type"] = 'application/octet-stream'
                # base64.b64encode(file_name.encode()).decode()
                new_file_name = '=?utf-8?b?' + base64.b64encode(file_name.encode()).decode() + '?='
                # 这里是处理文件名为中文名的，必须这么写
                att["Content-Disposition"] = 'attachment; filename="%s"' % new_file_name
                msg.attach(att)
        msg.attach(MIMEText(self.content))  # 邮件正文的内容
        msg['Subject'] = self.title  # 邮件主题
        msg['From'] = self.username  # 发送者账号
        msg['To'] = ','.join(self.recv)  # 接收者账号列表
        if self.ssl:
            self.smtp = smtplib.SMTP_SSL(self.email_host, port=self.ssl_port)
        else:
            self.smtp = smtplib.SMTP(self.email_host, port=self.port)
        # 发送邮件服务器的对象
        self.smtp.login(self.username, self.password)
        try:
            self.smtp.sendmail(self.username, self.recv, msg.as_string())
            pass
        except Exception as e:
            print('出错了，测试报告发不出去。。', e)
        else:
            print('自动化测试报告发送成功！')
        self.smtp.quit()


if __name__ == '__main__':
    m = SendEmail(
        username='1245869619@qq.com',
        password='azugqhtyhalgifih',  # 这个填入的是授权码，不是密码！！！！
        recv=['sy17713146220@dingtalk.com'],  # 填入收件人
        title='自动化测试报告',
        content='测试发送邮件',
        file=r'C:\Resources\InterFaceTest\result\report.html',
        ssl=False,
    )
    m.send_email()
