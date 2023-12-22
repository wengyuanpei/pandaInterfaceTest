from common.abcSign import *
from common.abcReqHeader import *

import requests

from common.abcReqHeader import abcBaseUrl
from common.abcSign import *
from time import sleep


uidd=60642
UID='60642'
token='658417a363f0f'
enverment='dev'
baseurl=abcBaseUrl("dev")
version='660'

headers={'PANDA-UID': UID,'PANDA-TOKEN': token,
             'Content-Type':'application/json; charset=utf-8',
             'PANDA-USE-NEW-VERSION':'2',
             'versionCode':version
             }

def getfuxiwords(uid):
    url=baseurl+'/v5/words-remember-planet/get-words-sub-v2'
    header=headers
    data={
            "uid": uid
        }
    dataend=getSignEnd(data,enverment)
    req=requests.post(url=url,json=dataend,headers=header).json()['data']['review_words_ids']
    return req

def reportViweWords(uid,wordid):
    url=baseurl+'/v5/words-remember-planet/report-words'
    header=headers
    data={
            "uid": uid,
            "action": 2,
            "words_id": wordid
        }
    dataend=getSignEnd(data,enverment)
    req=requests.post(url=url,json=dataend,headers=header)
    print('上报结果：',req.status_code)

if __name__ == '__main__':

    #复习单词个数输入
    allword=[]


    uid=60642
    viewNum=800

    num=viewNum/8+1
    for i in range(1,int(num)):
        wordlist = getfuxiwords(uid)
        allword.append(wordlist)
        print('第',str(i),'轮复习的单词是',wordlist)
        for wid in wordlist:
            reportViweWords(uid, wid)
            sleep(1)
    print('全部复习单词：',allword)