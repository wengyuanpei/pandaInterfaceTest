import requests
from common.abcSign import *
from time import *
"""
获取单词接口

curl -H 'Host: api-dev.abctime.com' -H 'User-Agent: UnityPlayer/2021.3.16f1c1 (UnityWebRequest/1.0, libcurl/7.84.0-DEV)' 
-H 'Accept: */*' -H 'Content-Type: application/json' -H 'PANDA-TOKEN: 655ec9e44c453' -H 'PANDA-UID: 60642' -H 'versionCode: 353'
 -H 'xh-debug: 1' -H 'PANDA-USE-NEW-VERSION: 2' -H 'X-Unity-Version: 2021.3.16f1c1' --data-binary '{
  "uid": 60642,
  "sign": "024b2f18d5a8c422d5a67e002312610c27267351171bb09e5cd5005a5279b641"
}' --compressed 'http://api-dev.abctime.com/v5/words-remember-planet/get-words-sub-v2'

上报完成学习接口
curl -H 'Host: api-dev.abctime.com' -H 'User-Agent: UnityPlayer/2021.3.16f1c1 (UnityWebRequest/1.0, libcurl/7.84.0-DEV)' -H 'Accept: */*' -H 'Content-Type: application/json' -H 'PANDA-TOKEN: 655ec9e44c453' -H 'PANDA-UID: 60642' -H 'versionCode: 353' -H 'xh-debug: 1' -H 'PANDA-USE-NEW-VERSION: 2' -H 'X-Unity-Version: 2021.3.16f1c1' --data-binary '{
  "uid": 60642,
  "action": 2,
  "words_id": 45208,
  "sign": "f4246d64ca7dbecf9c466147415100723e9f5cfe4b89ff93c89a5ab5e4086c35"
}' --compressed 'http://api-dev.abctime.com/v5/words-remember-planet/report-words'

"""
headers = {'PANDA-TOKEN': '6568046886ee1', 'PANDA-UID': '136'}
uidd=136
def getWords():
    url='http://api-dev.abctime.com/v5/words-remember-planet/get-words-sub-v2'
    header=headers
    data1={"uid": uidd}
    data=getSignEnd(data1)

    wordidList=requests.post(url=url,json=data,headers=header).json()['data']['study_words_ids']
    # print(requests.post(url=url,json=data,headers=header).json()['data'])
    return wordidList

def reportStudyWords(words_id):
    url = 'http://api-dev.abctime.com/v5/words-remember-planet/report-words'
    header =headers
    data1 = {"uid":uidd,"action": 1,"words_id": words_id}
    data = getSignEnd(data1)
    req=requests.post(url=url,json=data,headers=header)
    return req.status_code

def coleectionWords(words_id):
    url='http://api-dev.abctime.com/v5/words-remember/collect-words'
    data1={"words_id": words_id,
        "action": 1,
        "uid":uidd}
    data=getSignEnd(data1)
    header = headers
    req = requests.post(url=url, json=data, headers=header)
    return req.status_code


if __name__ == '__main__':
    #上报多少个单词学习
    wordslisttt=[]

    reportNum=220


    rid=int(reportNum/5+1)

    for i in range(1,rid):
        print('第%d轮！' %i)
        wids=getWords()
        for wid in wids:

            sleep(0.5)
            code=reportStudyWords(wid)
            print(code,'上报单词id：',wid)
            if str(code) != '200':
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>error,上报失败！')
            #收藏单词
            coleectionWords(wid)

            if wid not in wordslisttt:
                wordslisttt.append(wid)
            else:
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>单词获取重复！，重复的id是：',str(wid))

            sleep(1.5)
    print(wordslisttt)