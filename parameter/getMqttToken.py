import requests
import time
from pandaInterfaceTest.common.make_num_random import random_num



token="tal173UaFSsPwBw2IHBAFoCKcQd2zcLM_90E4t_bHVa7UjTmScoD4bblbOdLghDfRBk1vx-SzynsBL1-rV3GIFORelxxFVIZZ1Sz9D55KTYyOIwkn-mD2B2Zp5BsFsV4wJMvYUfHfrETylSWBtpBTu4361eyy3HalNjdtQF36qgBX969Qey"

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


