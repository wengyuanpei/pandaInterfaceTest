import requests
import time
from pandaInterfaceTest.common.make_num_random import random_num

url="https://pad-api-dev.xiongmaoboshi.com/s/drpanda/pad/pad/mqtt/auth/token"
header = {
            "Authorization": "tal173bzS7sPdIdmUJbe9NCcgBVxF4Lhvx4Fu_A9KTfttgyuABT_Kva9z8wUaCOeWYUKJlMDs-x5NqFVWv689Qz78VuxcR-4REnBfJe6sRk0lGE_4wStTs86U68VizJsGn3da_h0SXPZu0z1j6mL5Xo4kwlFLXTexciUtxtiOtGeH4N7Mey",
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


