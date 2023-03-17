import  requests
import time

headerss={"Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNTYxOTY5MDMyMzU1Njg4NDQ5Iiwic3ViIjoie1wiaWRcIjoxNTYxOTY5MDMyMzU1Njg4NDQ5LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTY5NDQzMTUwNH0.9ToNPthEBzk602y4XeCSxQdzo7csBunc-nqFCHZExaVoS0XJia75q7Zf5kvLele85mOcDyUDv5H4rGN777V06A"}


url='https://hear-pre.abctime.com/v1/page/index/3'

while True:
    reqq=requests.get(url=url,headers=headerss)
    # print(reqq.json()['data']['module_list'][1]["module_resource_list"][0])
    if reqq.json()['data']['module_list'][1]["module_resource_list"][0]["id"] != 85:
        print("ERRO!!!!")
        print(reqq.json()['data']['module_list'][1]["module_resource_list"][0])
        break
    else:
        print("正确")
    time.sleep(2)

