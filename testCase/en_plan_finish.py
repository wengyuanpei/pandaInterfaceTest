

import requests
from common.finish_plan_urlenverment import *
baseurl=urlenverment(2)
#dev
dev_en_url=baseurl+"v1/study/finish-plan"
plan_info =baseurl+ "v1/study/plan-info"
header_dev={"Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjQwOTc2ODgyODYyOTg1MjE3Iiwic3ViIjoie1wiaWRcIjoxNjQwOTc2ODgyODYyOTg1MjE3LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTcwNDU0MTE3OH0.mDacHgK7aBKkWpMKejwx9w2Mdg31CqVXz7wnPDQQ7cQ-2aAUKRsTpt50h271Z_DSQOonCEUsWmZrDFvTwEE42g"}

plan_info_list_erro=[]
# 英语部分
#####################################手动添加###########
UID=1640976882862985217

#####################################手动添加###########
day=1
#####################################手动添加###########
user_plan_id=1197344
#####################################手动添加###########
while day <= 200:
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

    # print('请求参数1：', data_1,'请求参数2：', data_2)

    reqsts1 = requests.post(url=dev_en_url, headers=header_dev, json=data_1)
    # print('英语学习完成上报1返回：', reqsts.text)
    # sleep(0.5)
    reqsts2= requests.post(url=dev_en_url, headers=header_dev, json=data_2)
    # print('英语学习完成上报2返回：', reqsts.text)
    # sleep(0.5)

#获取下一个计划接口


    plan_info_data = {"next": 1, "uid": UID}
    requestt_plan_info = requests.post(url=plan_info, json=plan_info_data, headers=header_dev)
    print(requestt_plan_info.json())
    try:
        user_plan_id = requestt_plan_info.json()['data']['user_plan_id']
        if requestt_plan_info.json()['code'] == str(300) or requestt_plan_info.json()['data']['user_plan_id']==0 or requestt_plan_info.json()['data']['user_plan_info']=="None":

            print("ERRO异常计划id:", requestt_plan_info.json()['data']['user_plan_id'])
            print("ERRO，请求", requestt_plan_info.json())
            print('第', day, '天')


            plan_info_list_erro.append(user_plan_id)

        else:

            print("计划正常！code:", requestt_plan_info.json()['code'], '计划ID', requestt_plan_info.json()['data']['user_plan_id'])
            print('第', day, '天')
            print( requestt_plan_info.json())
        #处理ID异常

    except:
        user_plan_id+=1


    day+=1
print("异常英语计划ID列表：",plan_info_list_erro)

