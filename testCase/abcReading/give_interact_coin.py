import requests
from common.abcSign import *
from common.abcReqHeader import *

envermen='dev'

baseurl=abcBaseUrl(envermen)

def coincoin(uid:int,uids:str,token:str,coinnum:int):
    url=baseurl+'/v5/clock/give_interact_coin'
    header={'PANDA-UID': uids,'PANDA-TOKEN':token}

    data={
            "uid": uid,
            "interact_type": 2,
            "coin": coinnum
           }
    dataend=getSignEnd(data,envermen)
    req=requests.post(url=url,json=dataend,headers=header)
    print(req.status_code)


if __name__ == '__main__':
    uid=64361
    uids='64361'
    token='65a8ddced2cb8'
    #发放金币数量
    coinnum=100000
    coincoin(uid,uids,token,coinnum)
