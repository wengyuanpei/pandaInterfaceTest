# -*- coding:utf-8 -*-
import smtplib
#添加附件
from email.mime.text import MIMEText
#使用MIMEMUltipart添加附件
from email.mime.multipart import MIMEMultipart
import datetime
def sendemail():
    #1发送人账号
    sendAddress='wengyuanpei@163.com'
    #2发送人授权码，等同于密码
    passWord='TCDFPMVRILMVXVWM' #进入扣扣空间-设置-账户-开启服务(pop3/SMTP服务)-发送短信，获取授权码
    #3连接服务器，465端口就是发送邮件的端口
    server=smtplib.SMTP_SSL('smtp.163.com',465)
    #4登录
    LoginResult=server.login(sendAddress,passWord)
    #(235, b'Authentication successful')代表成功



    timenow=datetime.datetime.today()
    msg=MIMEMultipart()
    #构建发件人、收件人、邮件主题
    msg['From']='<wengyuanpei@163.com>'
    msg['To']='v_wengyuanpei@tal.com'
    msg['subject']='%s服务端接口测试报告' % timenow
    content="""
    服务端接口测试报告.
    """

    #添加正文

    #将附件使用二进制读取，在使用MIMEText方法进行规范化
    attachment_1=MIMEText(open(r'C:\Users\zhang\Desktop\pandaInterfaceTest\result\report.html', 'rb').read(), 'html', 'utf-8')
    attachment_1['content-Type']='application/octet-stream'
    attachment_1['content-Disposition']='attachment;filename="report.html"'
    msg.attach(attachment_1)




    #发送邮件
    To=['v_wengyuanpei@tal.com','v_chenqi5@tal.com']
    sd=server.sendmail(sendAddress,To,msg.as_string())

    print('发送成功')
