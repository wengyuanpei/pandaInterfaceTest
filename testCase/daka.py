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
    #启动app包名  com.tal100.yach
    startapp="adb shell am start -n  com.tal100.yach/com.tal100.yach.main.activity.MainTabActivity"
    execute(startapp)
    sleep(5)
    #点击进入打卡界面的命令 （940,2500）   （1350,1180） 1370,2690
    check1="adb shell input tap 740 2700"
    execute(check1)
    sleep(5)
    check2="adb shell input tap 225 2000"
    execute(check2)
    sleep(5)
    #点击打卡 (800,1120)
    print("打卡点了")
    work="adb shell input tap 650 1260"
    # execute(work)
    #关闭app
    closeapp="adb shell am force-stop  com.tal100.yach"
    execute(closeapp)
