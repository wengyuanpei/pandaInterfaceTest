import requests

from common.abcSign import *
from common.abcReqHeader import *

envermen='pre'

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
    uid=11940857
    uids='11940857'
    token='657ab77776f68'
    coinnum=1000
    coincoin(uid,uids,token,coinnum)