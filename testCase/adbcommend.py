#coding:utf-8
import os
import time
from datetime import datetime
from time import *

def execute(cmd):
    os.system(cmd)



if __name__ == '__main__':

    #连接adb
    tcpip_set='adb tcpip 9999'
    get_ip='adb shell ifconfig|findstr Bcast'
    connect_adb='adb connect 192.168.1.106:9999'

    # execute(tcpip_set)
    # execute(get_ip)
    # execute(connect_adb)

    # 执行动作亮屏-解锁-锁定-解锁 循环
    ip='192.168.1.106'
    a=1

    while True:
        #设备1
        print('a第%d次执行！' % a)
        print(datetime.now().strftime('%Y-%m-%d  %H:%M:%S'))
        com="adb -s %s shell input keyevent 26" % ip
        execute(com)
        #解锁
        open='adb -s %s shell input swipe 148 1015 563 1046' % ip
        execute(open)
        sleep(0.5)
        execute(com)
        execute(com)
        execute(com)

        sleep(2)
        a+=1

