#coding:utf-8
import os
from time import sleep

def execute(cmd):
    os.system(cmd)


if __name__ == '__main__':
    # 完整命令的
    a=1
    while True:
        sleep(1)
        print('第%d次执行锁屏命令！' % a)
        com="adb shell input keyevent 26"
        execute(com)
        a+=1
