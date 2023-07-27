import threading
from datetime import datetime
import requests


def demo1():
   url = "https://pad-api-dev.xiongmaoboshi.com/s/drpanda/pad/min-app/device/rights/vip/claim"
   header = {
      "x-miniapp-appid": "wx320c749fc17e90b9",
      "Authorization": "Tal tal173ECMc8OQmv1eZcl15ASR1-kqfIVHtxrRwgURXNbTYODN0v-yTZEpHa6BkKiCsh5spNWbsI64hwryuxTxL__vsqfUHEzmQaDV4_FGU9FR9pl64Y9U6MXb2gnHg8aU-j1d1nww250SNTn-o3yXSXr6hStXbLPf4o4V0l3Khj5GdNwAeyUY-EFSHmK4wStHPuzV-RCv86wQZTWKVbW5YjQw5slvURYiViPjV8zdv3Mmmi2iNW"
   }
   data = {
      "timestamp": 1677208972758,
      "sign": "",
      "body": {
         "sn": "S1TESTLY008",
         "phone": "17345043365",
         "applyType": "S1",
         "unionid": "oPDhI6IpAbhxosKQiuXLk2dZdcBE"
      }
   }
   reqeust = requests.post(url=url, json=data, headers=header)
   print("请求结果1》》》》》》", reqeust.text)


def demo2():
   url = "https://pad-api-dev.xiongmaoboshi.com/s/drpanda/pad/min-app/device/rights/vip/claim"
   header = {
      "x-miniapp-appid": "wx320c749fc17e90b9",
      "Authorization": "Tal tal173ECMc8OQmv1eZcl15ASR1-kqfIVHtxrRwgURXNbTYODN0v-yTZEpHa6BkKiCsh5spNWbsI64hwryuxTxL__vsqfUHEzmQaDV4_FGU9FR9pl64Y9U6MXb2gnHg8aU-j1d1nww250SNTn-o3yXSXr6hStXbLPf4o4V0l3Khj5GdNwAeyUY-EFSHmK4wStHPuzV-RCv86wQZTWKVbW5YjQw5slvURYiViPjV8zdv3Mmmi2iNW"
   }
   data1 = {
      "timestamp": 1677208972759,
      "sign": "",
      "body": {
         "sn": 'S01D1042320700479',
         "phone": "17345043365",
         "applyType": "S1",
         "unionid": "oPDhI6IpAbhxosKQiuXLk2dZdcBE"
      }
   }
   reqeust = requests.post(url=url, json=data1, headers=header)
   print("请求结果2》》》》》》", reqeust.text)

def many_thread():
    threads = []
    for _ in range(100):  # 循环创建1个线程
        t1 = threading.Thread(target=demo1)
        t2= threading.Thread(target=demo2)
        threads.append(t1)
        threads.append(t2)
    for t in threads:  # 循环启动线程
        t.start()


if __name__ == '__main__':
    many_thread()