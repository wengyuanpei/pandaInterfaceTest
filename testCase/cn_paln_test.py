

#语文定级计划上报接口
import requests
from time import sleep

# 英语部分
uid_173=1640976882862985217
xie=1584826171582775298

header={"Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNTYxOTY5MDMyMzU1Njg4NDQ5Iiwic3ViIjoie1wiaWRcIjoxNTYxOTY5MDMyMzU1Njg4NDQ5LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTY4ODUyNTUyOH0.nxWVTxSikp_bAce2h_ywPQgqqtnY6qpLOqvGBTZ9qEyZfmQeb2K3nKIQt2Y94nA7N4DBjZLx_nXvY1VQ-TJ77A"}

en_url="https://hear.abctime.com/v1/study/finish-plan"



#dev
dev_eb_url=" https://hear-dev.abctime.com/v1/study/finish-plan"
dev_UID=1571801686167822338
dev_header={"Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjA3MzMxNjI0MTQ4NDU1NDI2Iiwic3ViIjoie1wiaWRcIjoxNjA3MzMxNjI0MTQ4NDU1NDI2LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTY5NjgxNzk3NH0.RaQ8Uw0Iz5e2iP7J7i_DM1jet2rzJOK2sRVQJWVvKFVmRGW0fdoxzXq2P_sHAermp2JgHPL5wPyrmfFex28VlA"}




user_plan_id=1181474
while user_plan_id <= 1181474:
# while user_plan_id <= 15416864:

    data_1 = {
                  "uid": dev_UID,
                  "user_plan_id": user_plan_id,
                  "event_id": 1
                }
    data_2 = {
                  "uid": dev_UID,
                  "user_plan_id": user_plan_id,
                  "event_id": 2
                }

    print('请求参数1：', data_1,'请求参数2：', data_2)

    reqsts = requests.post(url=dev_eb_url, headers=dev_header, json=data_1)
    print('英语学习完成上报1返回：', reqsts.text)
    sleep(0.5)
    reqsts = requests.post(url=dev_eb_url, headers=dev_header, json=data_2)
    print('英语学习完成上报2返回：', reqsts.text)
    sleep(0.5)
    user_plan_id += 1


