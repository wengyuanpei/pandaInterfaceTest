#coding:utf-8
import os
import time
from datetime import datetime
from time import *


def execute(cmd):
    result = os.popen(cmd)
    # 返回的结果是一个<class 'os._wrap_close'>对象，需要读取后才能处理
    context = result.read()
    infoooo=[]
    for line in context.splitlines():
        infoooo.append(line)
        print(infoooo)
    result.close()

    return infoooo

if __name__ == '__main__':
    tcpip_set = 'adb tcpip 9999'
    get_ip = 'adb -s ddd shell ifconfig|findstr Bcast'
    connect_adb = 'adb connect 192.168.1.106:9999'

    runadb=execute(get_ip)
    while len(runadb) ==1 :
        print('run')