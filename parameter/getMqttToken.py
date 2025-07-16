import requests
import time
from common.make_num_random import random_num
from common.get_tlj_auth import *
token=getauth(13800000001)[0]


url="https://pad-api-dev.xiongmaoboshi.com/s/drpanda/pad/pad/mqtt/auth/token"
header = {
            "Authorization": token,
            "Content-Type": "application/json;charset=UTF-8"
        }


def getmqtttoeken():
    sn ='TEST'+ random_num()
    datas = {"timestamp": "",
             "sign": "string",
             "body": {
                 "sn": sn
             }}
    requestss=requests.post(url=url,headers=header,json=datas)
    print(requestss.json()['data']['token'])
    time.sleep(1)
    return str(requestss.json()['data']['token']),sn

if __name__=="__main__":
    getmqtttoeken()


