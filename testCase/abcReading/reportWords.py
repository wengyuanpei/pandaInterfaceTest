import requests

from common.abcReqHeader import abcBaseUrl
from common.abcSign import *
from time import *


'''
curl -H 'PANDA-USE-NEW-VERSION': 2' -H 'PANDA-UID': '11940857' -H 'PANDA-TOKEN': '65728ba9eda34' -H 'channel: 2' -H 'versionCode: 353' -H 'versionName: 6.5.3' -H 'Host: pre-api.abctime.com' -H 'User-Agent: okhttp/4.8.0' --data-binary "" --compressed 'https://pre-api.abctime.com/v5/task/get_reward_num'

'''


headers_dev = {'PANDA-TOKEN': '6568046886ee1', 'PANDA-UID': '136'}
baseurl_dev='http://api-dev.abctime.com'





uidd=18324628
UID='18324628'
token='657815137fddb'
enverment='pre'
baseurl=abcBaseUrl("pre")


headers_pre={'PANDA-UID': UID,'PANDA-TOKEN': token,
             'Content-Type':'application/json; charset=utf-8',
             'PANDA-USE-NEW-VERSION':'2',
             'versionCode':'653'
             }




def getWords():
    url=baseurl + '/v5/words-remember-planet/get-words-sub-v2'
    header=headers_pre
    data1={"uid": uidd}
    data=getSignEnd(data1,enverment)

    wordidList=requests.post(url=url,json=data,headers=header).json()['data']['study_words_ids']
    # print(requests.post(url=url,json=data,headers=header).json()['data'])
    return wordidList

def reportStudyWords(words_id):
    url = baseurl+'/v5/words-remember-planet/report-words'
    header =headers_pre
    data1 = {"uid":uidd,"action": 1,"words_id": words_id}
    data = getSignEnd(data1,enverment)
    req=requests.post(url=url,json=data,headers=header,verify=False)
    return req.status_code

def coleectionWords(words_id):
    url=baseurl+'/v5/words-remember/collect-words'
    data1={"words_id": words_id,
        "action": 1,
        "uid":uidd}
    data=getSignEnd(data1,enverment)
    header = headers_pre
    req = requests.post(url=url, json=data, headers=header,verify=False)
    return req.status_code


if __name__ == '__main__':
    #上报多少个单词学习
    wordslisttt=[]

    reportNum=400


    rid=int(reportNum/5+1)

    for i in range(1,rid):
        print('第%d轮！' %i)
        wids=getWords()
        for wid in wids:

            sleep(1.5)
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

            sleep(3.5)
    print(wordslisttt)