

#语文定级计划上报接口
import requests
from time import sleep

# 英语部分
uid_173=1640976882862985217

header={  "Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNTYxOTY5MDMyMzU1Njg4NDQ5Iiwic3ViIjoie1wiaWRcIjoxNTYxOTY5MDMyMzU1Njg4NDQ5LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTY4ODUyNTUyOH0.nxWVTxSikp_bAce2h_ywPQgqqtnY6qpLOqvGBTZ9qEyZfmQeb2K3nKIQt2Y94nA7N4DBjZLx_nXvY1VQ-TJ77A"}

en_url="https://hear.abctime.com/v1/study/finish-plan"




user_plan_id=15416863
while user_plan_id <= 15416975:
# while user_plan_id <= 15416864:

    data_1 = {
                  "uid": uid_173,
                  "user_plan_id": user_plan_id,
                  "event_id": 1
                }
    data_2 = {
                  "uid": uid_173,
                  "user_plan_id": user_plan_id,
                  "event_id": 2
                }

    print('请求参数：', data_1,data_2)

    reqsts = requests.post(url=en_url, headers=header, json=data_1)
    print('英语学习完成上报1返回：', reqsts.text)
    sleep(1)
    reqsts = requests.post(url=en_url, headers=header, json=data_2)
    print('英语学习完成上报2返回：', reqsts.text)
    sleep(1)
    user_plan_id += 1


