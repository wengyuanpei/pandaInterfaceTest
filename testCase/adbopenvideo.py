#coding:utf-8
import os
from time import sleep

def execute(cmd):
    os.system(cmd)

if __name__ == '__main__':

    #模拟打开加载视频后返回
    a=1
    while True:

        print('a第%d次执行！' % a)
        #点击
        click='adb -s 192.168.1.131 shell input tap 316.5 544.5'

        #返回
        back='adb  -s 192.168.1.131 shell input keyevent 4'

        #继续播放
        cmmd = 'adb -s 192.168.1.131 shell input tap 222 683'

        execute(click)


        execute(cmmd)

        execute(back)
        a+=1




