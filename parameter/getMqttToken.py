import requests
import time


url="https://pad-api-dev.xiongmaoboshi.com/s/drpanda/pad/pad/mqtt/auth/token"
header = {
            "Authorization": "tal173bzS7sPdIdmUJbe9NCcgBVxF4Lhvx4Fu_A9KTfttgyuABT_Kva9z8wUaCOeWYUKJlMDs-x5NqFVWv689Qz78VuxcR-4REnBfJe6sRk0lGE_4wStTs86U68VizJsGn3da_h0SXPZu0z1j6mL5Xo4kwlFLXTexciUtxtiOtGeH4N7Mey",
            "Content-Type": "application/json;charset=UTF-8"
        }
datas={"timestamp": "",
      "sign": "string",
  "body": {
    "sn": "1123123"
         }}
def getmqtttoeken():
    requestss=requests.post(url=url,headers=header,json=datas)
    print(requestss.json()['data']['token'])
    time.sleep(1)
    return str(requestss.json()['data']['token'])
if __name__=="__main__":
    getmqtttoeken()
