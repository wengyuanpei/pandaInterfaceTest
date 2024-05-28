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

# adb截取手机屏幕
# adb shell screencap -p *.png
#
# 点击屏幕指定位置
# adb shell input tap <x> <y>
#
# 从屏幕的一点滑动到另一点
# adb shell input swipe x1 y1 x2 y2




if __name__ == '__main__':

    #首页绘本坐标
    bookSetX=1480
    bookSetY=600
    #工具入口坐标
    toolSetX=66
    toolSetY=1011
    #完成分数坐标
    doneSetX=1300
    doneSetY=970
    #关闭工具坐标
    closeSetX=2270
    closeSetY=81
    #绘本返回坐标
    backSetX=100
    backSetY=100
    #绘本弹窗选择首页坐标
    homeSetX=920
    homeSetY=830

    ip = '94a3ad11'
    get_ip = 'adb -s %s shell ifconfig|findstr Bcast' % ip
    # 执行操作点击绘本-扉页双击左下角-三次点击分数-关闭窗口-返回-弹窗选择首页-循环
    a=1
    runadb=execute(get_ip)
    while len(runadb) ==1:
        #设备1
        print('a第%d次执行！' % a)
        print(datetime.now().strftime('%Y-%m-%d  %H:%M:%S'))

        print("手动打开工具！")
        #双击打开工具
        # adb shell input tap 600 1300; input tap 600 1300;  双击操作
        dbclicktool="adb -s %s shell input tap 66 1011 ;input tap 66 1011;" % ip
        execute(dbclicktool)
        sleep(0.5)
        #点击完成分数按钮


        sleep(1)
        a+=1
        if a==2:
            break

