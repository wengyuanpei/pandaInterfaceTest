import random
from time import sleep
import requests
from common.abcSign import *
from common.abcReqHeader import *

enverment='dev'
baseurl=abcBaseUrl(enverment)

#获取学习关卡数据重构
def GetChallengesList(uidd:int,uuid,token:str,cid:int)->list:
    url = baseurl + '/v5/challenges/getChallengeListByCid'
    data = {
        "ab_non_vip": 2,
        "cid": cid,
        "member_id": uidd
    }
    dataEND = getSignEnd(data, enverment)

    header = {'PANDA-TOKEN': token, 'PANDA-UID': uuid, 'versionCode': '360'}
    # header = {'PANDA-TOKEN': token, 'PANDA-UID': uuid}

    req = requests.post(url=url, json=dataEND, headers=header).json()

    print(req)


if __name__ == '__main__':
    uidd=60623
    uuid='60623'
    token='65eec45215682'
    cid=5

    GetChallengesList(uidd,uuid,token,cid)
