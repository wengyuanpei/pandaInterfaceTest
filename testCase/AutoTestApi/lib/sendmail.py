import sys,os
import yagmail
import configparser
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import setting
from lib.newReport import new_report


def send_mail(file_new):
    #读取配置表

    con=configparser.ConfigParser()
    con.read(setting.TEST_CONFIG, encoding='UTF-8')



    host=con["maild"]['HOST_SERVER']
    send=con["maild"]['user']
    pwd=con["maild"]['password']
    sendTo1=con["maild"]['TO1']
    email_title = con["maild"]['SUBJECT']

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
    send_mail(r'C:\Users\zhang\Desktop\interfaceTest\report\2025-02-07 14_14_25result.html')
