

#语文定级计划上报接口
import requests
from time import sleep

# 英语部分
uid_173=1640976882862985217
xie=1584826171582775298

header={"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNTYxOTY5MDMyMzU1Njg4NDQ5Iiwic3ViIjoie1wiaWRcIjoxNTYxOTY5MDMyMzU1Njg4NDQ5LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTY4ODUyNTUyOH0.nxWVTxSikp_bAce2h_ywPQgqqtnY6qpLOqvGBTZ9qEyZfmQeb2K3nKIQt2Y94nA7N4DBjZLx_nXvY1VQ-TJ77A"}

en_url="https://hear.abctime.com/v1/study/finish-plan"



#dev
dev_en_url=" https://hear-dev.abctime.com/v1/study/finish-plan"
UID=1562629060075102209
dev_header={"Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNTYyNjI5MDYwMDc1MTAyMjA5Iiwic3ViIjoie1wiaWRcIjoxNTYyNjI5MDYwMDc1MTAyMjA5LFwibW9iaWxlXCI6XCIrODYxODM4NDI1MzUwNlwifSIsImV4cCI6MTY5NzU5MjQyNn0.cxJqNLvfFPOpaMtnb7t7VLCLxshttK1-biTWQpiYPpLF1gi-GA-M6ekvMrsMLnLguEcouBfZlWCKUU1d5m4GyQ"}


plan_info_list_erro=[]

user_plan_id=16576879
while user_plan_id <= 16576987+1184:
# while user_plan_id <= 15416864:


#获取计划信息
    plan_info="https://hear.abctime.com/v1/study/plan-info"
    plan_info_data={"next":0,"uid":UID}
    requestt_plan_info=requests.post(url=plan_info,json=plan_info_data,headers=dev_header)
    if requestt_plan_info.json()['code']==str(300):
        print("ERRO异常计划id:",user_plan_id)
        plan_info_list_erro.append(user_plan_id)
    else:
        print("计划正常！",requestt_plan_info.json())

    sleep(0.5)

    data_1 = {
                  "uid": UID,
                  "user_plan_id": user_plan_id,
                  "event_id": 1
                }
    data_2 = {
                  "uid": UID,
                  "user_plan_id": user_plan_id,
                  "event_id": 2
                }

    print('请求参数1：', data_1,'请求参数2：', data_2)

    reqsts = requests.post(url=en_url, headers=dev_header, json=data_1)
    print('英语学习完成上报1返回：', reqsts.text)
    sleep(0.5)
    reqsts = requests.post(url=en_url, headers=dev_header, json=data_2)
    print('英语学习完成上报2返回：', reqsts.text)
    sleep(0.5)



    user_plan_id += 1

print(plan_info_list_erro)
