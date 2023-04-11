

#语文定级计划上报接口
import requests
from time import sleep






# url="https://hear.abctime.com/v1/study-cn/finish-plan"
# header={  "Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNTYxOTY5MDMyMzU1Njg4NDQ5Iiwic3ViIjoie1wiaWRcIjoxNTYxOTY5MDMyMzU1Njg4NDQ5LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTY4ODUyNTUyOH0.nxWVTxSikp_bAce2h_ywPQgqqtnY6qpLOqvGBTZ9qEyZfmQeb2K3nKIQt2Y94nA7N4DBjZLx_nXvY1VQ-TJ77A"}
# data={"event_id":3,"user_plan_id":2335,"uid":1561969032355688449}
# uid_18384243506=1562629060075102209
#
# uid_173=1640976882862985217

# uid_zl=1547790292942245889
#
#
# user_plan_id=15654
#
#
# while user_plan_id <= 15699:
#
#     data = {"event_id": 5, "user_plan_id": user_plan_id, "uid": uid_zl}
#     sleep(1)
#     print('请求参数：', data)
#     reqsts = requests.post(url=url, headers=header, json=data)
#     print('S1字卡学习完成上报：', reqsts.text)
#     user_plan_id+=1
#
#     plan_info="https://hear.abctime.com/v1/study-cn/plan-info"
#     data_info={"uid":uid_zl}
#     reqsts_plan_info=requests.post(url=plan_info, headers=header, json=data)
#     # print(reqsts_plan_info.json()['data']['user_plan_info']['poetry']['lesson']['lesson_id'])
#     print(reqsts_plan_info.text)

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
    print('英语学习完成上报：', reqsts.text)
    reqsts = requests.post(url=en_url, headers=header, json=data_2)
    print('英语学习完成上报：', reqsts.text)

    user_plan_id += 1


