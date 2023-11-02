#coding:utf-8


# 先通过获取题目接口确认当前的题目的位置，再通过adb 去进行选择


import os
import time
from datetime import datetime
from time import *
import requests


def execute(cmd):
    result = os.popen(cmd)
    context = result.read()
    print(context)
def get_chose_info(uid,token,uid_data):
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
        "uid": uid_data
     }
    req=requests.post(url=url,json=data,headers=header)
    print(req.json()['data']['study_sub_list'])
    list_word=req.json()['data']['study_sub_list']
    for i in range(len(list_word)):
        print(list_word[i]['itemRespList'])



if __name__ == '__main__':
    # uid_data=53634
    # uid='53634'
    # token='65430b11cf1d6'
    # get_chose_info(uid,token,uid_data)
    ip = ' 94a3ad11'
    cmdwords1 = 'adb -s %s shell logcat ' % ip


    # cmdwords2 = 'logcat  |grep -E "PK"'

    execute(cmdwords1)
    # sleep(1)
    # execute(cmdwords2)
    print('运行到这！')