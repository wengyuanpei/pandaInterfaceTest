import requests
import time
from pandaInterfaceTest.common.make_num_random import random_num



token="tal173bFwMOBHWX8nyh0ewjtFyWW9PhnOvfrDZ2BcnyRNWuqYy6-WAn1Dg0z1eA3wsRN2j1ZRWBDsJQO1f7xPODAvM4R4UNLvikgBk7Qfw1zt9UQJeYDgVmUu5juAHWjM5zGutbRHFCOruDbDudi6A-_cBhg5K8J_IcaH6Ew3hdD_UVfUey"

url="https://pad-api-dev.xiongmaoboshi.com/s/drpanda/pad/pad/mqtt/auth/token"
header = {
            "Authorization": token,
            "Content-Type": "application/json;charset=UTF-8"
        }


def getmqtttoeken():
    sn = random_num() + 'test'
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


