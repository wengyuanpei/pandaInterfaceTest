
import requests
from common.abcSign import *
from common.abcReqHeader import *
from random import randint

envermen='dev'

baseurl=abcBaseUrl(envermen)

def check_reqeustiom(uid:int,uids:str,token:str):
    url=baseurl+'/toto/v3/get_toto_question'
    header={'PANDA-UID': uids,'PANDA-TOKEN':token}
    data={
            "uid": uid,
            "num": 8,
            "question_type": 2
           }
    dataend=getSignEnd(data,envermen)
    req=requests.post(url=url,json=dataend,headers=header)
    # print(req.json()['data']['item_list'])
    req=req.json()['data']['item_list']
    return req

if __name__ == '__main__':
    uid=65819
    uids="65819"
    token="6620e5c49028e"
    listw=[]
    for i in range(11):
        print('第%d次请求题目！' %i)
        req=check_reqeustiom(uid,uids,token)
        for a in range(len(req)):

            wordid=req[a]['data'][0]['word_id']
            word = req[a]['data'][0]['word']
            listw.append([wordid,word])

    print(listw)
    #处理检查重复
    c = [n for n in listw if listw.count(n) > 1]

    print(c)



