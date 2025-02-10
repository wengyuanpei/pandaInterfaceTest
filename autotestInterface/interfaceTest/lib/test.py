import sys,os
import yagmail
import configparser

from config import setting
from lib.newReport import new_report


def send_mail(file_new):
    #读取配置表

    con=configparser.ConfigParser()

    current_dir = os.path.dirname(__file__)
    cinfig = 'database'
    file_path = os.path.abspath(cinfig)
    full_path=os.path.join(file_path,'config.ini')
    # print(full_path)
    con.read(full_path, encoding='utf-8')


    host=con["maild"]['HOST_SERVER']
    send=con["maild"]['user']
    pwd=con["maild"]['password']
    sendTo1=con["maild"]['TO1']
    email_title = con["maild"]['SUBJECT']
    print(host,send,pwd,sendTo1)
    # 连接服务器
    # 用户名、授权码、服务器地址
    yag_server = yagmail.SMTP(user=send, password=pwd, host=host)

    # 发送对象列表
    email_to = [sendTo1 ]


    f = open(file_new,'r',encoding='utf-8')
    mail_body = f.read()
    f.close()
    email_content = mail_body

    # 附件列表
    report = new_report(setting.TEST_REPORT)
    # print(report)
    email_attachments = [report,]

    # 发送邮件
    try:
        yag_server.send(email_to, email_title,email_content,email_attachments)
        yag_server.close()
        print('Email send OK')
    # 关闭连接
    except Exception as e:
        print('Email send fail',e)


if __name__ == '__main__':

    cinfig = 'database'
    file_path = os.path.abspath(cinfig)
    data_path1=os.path.dirname(file_path)
    data_path=os.path.dirname(data_path1)
    full_path = os.path.join(data_path,'database','config.ini')

    # send_mail(r'/report/2025-02-06 17_11_09result.html')
