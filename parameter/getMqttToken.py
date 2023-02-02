import requests
import time
from common.make_num_random import random_num



token="tal173Dzsr-o9wxNEo5WQk-IdSlY5cN-FhNSw-KaENAYTGOmZZUxaCCxRz-YPLMfQ2qVo7NfL1_eFyH4dg2SgrLT1one7C-7cclTWPqEWnvl3ugBjJOvW8nDX_v_0fvfJczWBt6pnlE5zAiYn9GIvY9pqM-G09xDOpejMelLh5-ZMVa-cey"

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


