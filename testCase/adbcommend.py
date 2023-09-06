#coding:utf-8
import os
from time import sleep

def execute(cmd):
    os.system(cmd)


if __name__ == '__main__':
    # 执行动作亮屏-解锁-锁定-解锁 循环
    a=1
    while True:

        print('第%d次执行锁屏命令！' % a)
        com="adb shell input keyevent 26"
        execute(com)
        #解锁

        open='adb shell input swipe 148 1015 563 1046'
        execute(open)
        sleep(0.5)

        execute(com)
        execute(com)

        sleep(2)
        a+=1
