#coding:utf-8


# 先通过获取题目接口确认当前的题目的位置，再通过adb 去进行选择

import subprocess
import os
import time
from datetime import datetime
from time import *
import requests


def execute(cmd):
    result = os.popen(cmd)
    context = result.read()

def get_chose_info(uid,token):
    """
    curl --location 'https://api-dev.abctime.com/v5/words-remember-planet/get-words-sub' \
--header 'PANDA-TOKEN: 653f237e356f6' \
--header 'PANDA-UID: 61269' \
--header 'Content-Type: application/json' \
--data '{
  "uid": 51338
}'
    :return:
    """
    url='https://api-dev.abctime.com/v5/words-remember-planet/get-words-sub'
    header={'PANDA-TOKEN':token,'PANDA-UID': uid,'Content-Type': 'application/json'}
    data={
        "uid": uid
     }
    req=requests.post(url=url,json=data,headers=header)


def assert_page():
    ps = subprocess.Popen('adb logcat ', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

    answernum=0
    for line in ps.stdout:
        line = str(line)
        if "PK" in line:
            # 下面这个判断如果有值证明当前选择已经翻页
            if line != '':
                answernum=1
            else:
                answernum=answernum
    return answernum

if __name__ == '__main__':
    """
单词选项第一个位置：x:954 Y:756
单词选项第一个位置：1439 770
单词选项第一个位置：966 942
单词选项第一个位置：1465 940

图片1：826  868
图片2：1225 861
图片3：1576 850

"""

    ps = subprocess.Popen('adb logcat ', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

    answernum = 0
    for line in ps.stdout:
        line = str(line)
        while True:
            #adb 点击命令
            # adb shell input tap 500 1000
            ip = ' 94a3ad11'
            cmdwords1='adb -s %s shell  input tap 954 756' % ip
            cmdwords2 = 'adb -s %s shell  input tap 1439 770' % ip
            cmdwords3 = 'adb -s %s shell  input tap 966 942' % ip
            cmdwords4 = 'adb -s %s shell  input tap 1465 940' % ip
            condist=[cmdwords1,cmdwords2,cmdwords3,cmdwords4]
            for comd in condist:
                execute(cmdwords1)
                if "PK" in line:
                    continue
                else:
                    sleep(3)
                    execute(cmdwords2)
                    if "PK" in line:
                        continue
                    else:
                        sleep(3)
                        execute(cmdwords3)
                        if "PK" in line:
                            continue
                        else:
                            sleep(3)
                            execute(cmdwords4)

            comdpic1='adb -s %s shell  input tap 954 756' % ip
            comdpic2 = 'adb -s %s shell  input tap 954 756' % ip
            comdpic3 = 'adb -s %s shell  input tap 954 756' % ip
            execute(comdpic1)
            sleep(3)
            execute(comdpic2)
            sleep(3)
            execute(comdpic3)

