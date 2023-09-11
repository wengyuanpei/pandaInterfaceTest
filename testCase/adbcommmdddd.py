#coding:utf-8
import os
from time import sleep

def execute(cmd):
    os.system(cmd)


if __name__ == '__main__':
    # 执行动作亮屏-解锁-锁定-解锁 循环
    a=1
    b=1
    c=1
    while True:

        #设备3
        print('c第%d次执行！' % c)
        com = "adb -s 192.168.1.110 shell input keyevent 26"
        execute(com)
        # 解锁

        open = 'adb -s 192.168.1.110 shell input swipe 148 1015 563 1046'
        execute(open)
        sleep(0.5)

        execute(com)
        execute(com)
        execute(com)

        sleep(2)
        c += 1


