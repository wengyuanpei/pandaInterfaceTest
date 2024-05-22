#coding:utf-8
import os
import time
from datetime import datetime
from time import *


# adb截取手机屏幕
# adb shell screencap -p *.png
#
# 点击屏幕指定位置
# adb shell input tap <x> <y>
#
# 从屏幕的一点滑动到另一点
# adb shell input swipe x1 y1 x2 y2


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
    ip = '192.168.1.106'
    #连接adb
    tcpip_set='adb -s %s tcpip 9998' % ip
    get_ip='adb -s %s shell ifconfig|findstr Bcast' % ip
    connect_adb='adb -s %s connect 192.168.1.106:9999' % ip

    # execute(tcpip_set)
    # execute(get_ip)
    # execute(connect_adb)

    # 执行动作亮屏-解锁-锁定-解锁 循环

    a=1
    runadb=execute(get_ip)
    while len(runadb) ==1:
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

