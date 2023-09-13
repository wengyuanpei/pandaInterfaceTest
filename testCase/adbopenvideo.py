#coding:utf-8
import os
import time
from datetime import datetime
from time import *

def execute(cmd):
    result = os.popen(cmd)
    context = result.read()
    infoooo=[]
    for line in context.splitlines():
        infoooo.append(line)
        print(infoooo)
    result.close()

    return infoooo

if __name__ == '__main__':
    ip = '192.168.1.119'
    #连接adb
    tcpip_set='adb -s %s tcpip 9997' % ip
    get_ip='adb -s %s shell ifconfig|findstr Bcast' % ip
    connect_adb='adb  -s %s connect 192.168.1.106:9997' % ip

    # execute(tcpip_set)
    # execute(get_ip)
    # execute(connect_adb)

    # 执行动作亮屏-解锁-锁定-解锁 循环

    a=1
    runadb=execute(get_ip)

    while len(runadb) ==1:

        print('a第%d次执行！' % a)

        print(datetime.now().strftime('%Y-%m-%d  %H:%M:%S'))
        #点击视频加载
        # click='adb -s %s shell input tap 316.5 544.5' % ip

        #￥点击全屏播放
        click_window = 'adb -s %s shell input tap 603 448' % ip

        sleep(0.5)

        click_open = 'adb -s %s shell input tap 603 448' % ip

        sleep(0.5)
        #返回
        back='adb  -s %s shell input keyevent 4' % ip

        #继续播放
        # cmmd = 'adb -s %s shell input tap 222 683' % ip

        execute(click_window)
        execute(click_open)
        # execute(cmmd)
        execute(back)
        a+=1




