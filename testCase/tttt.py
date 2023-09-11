#coding:utf-8
import os
import time
from datetime import datetime
from time import *

def execute(cmd):
    info=os.system(cmd)
    return info



if __name__ == '__main__':

    get_ip = 'adb -s S1DEV005  shell ifconfig|findstr Bcast'

    a=execute(get_ip)
    print(11111,a.denominator)