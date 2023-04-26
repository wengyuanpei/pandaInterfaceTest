

#语文定级计划上报接口
import requests
from time import sleep

# 英语部分
uid_173=1640976882862985217
xie=1584826171582775298

UID=1640976882862985217
header_live={"Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjQwOTc2ODgyODYyOTg1MjE3Iiwic3ViIjoie1wiaWRcIjoxNjQwOTc2ODgyODYyOTg1MjE3LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTY5Nzk3NjI1OH0.PHVbFL-xzc2os7DL9HpVK1c9gwECU55G7Dx6QJM4mE93h-SfqxzYmjIpUQKAW0tJeMSUklxW4ALRZT0h3i6yKA"}
en_url="https://hear.abctime.com/v1/study/finish-plan"



#dev
dev_en_url=" https://hear-dev.abctime.com/v1/study/finish-plan"

header_dev={"Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxMTkxMzI1NzEwOTg3MzQ1OTIyIiwic3ViIjoie1wiaWRcIjoxMTkxMzI1NzEwOTg3MzQ1OTIyLFwibW9iaWxlXCI6XCIrODYxODg4ODg4ODg4OFwiLFwidXNlcm5hbWVcIjpcIkFha2FzaCDpmL_ljaHku4BcIn0iLCJleHAiOjE2OTc0NDU1ODl9.felcnqDtixPGVNaKNFDBGmOByUGGJI390GOYqsc_uwWzy0rq-ggf0XDB4-eIwoDbZXvibTENielLtM7kE7OJIQ"}


plan_info_list_erro=[]
day=293

user_plan_id=17054705
while user_plan_id <= 17054710:
# while user_plan_id <= 15416864:


#获取计划信息
    plan_info="https://hear.abctime.com/v1/study/plan-info"
    plan_info_data={"next":0,"uid":UID}
    requestt_plan_info=requests.post(url=plan_info,json=plan_info_data,headers=header_live)
    if requestt_plan_info.json()['code']==str(300) or requestt_plan_info.json()['data']['user_plan_id']==0 or requestt_plan_info.json()['data']['user_plan_info']=="None":
        # print("ERRO异常计划id:",requestt_plan_info.json()['data']['user_plan_id'])
        print("ERRO，请求",requestt_plan_info.json())
        print('第',day,'天')
        plan_info_list_erro.append(user_plan_id)
    else:
        # print(requestt_plan_info.json())
        print("计划正常！code:",requestt_plan_info.json()['code'],'计划ID',"当前计划ID",requestt_plan_info.json()['data']['user_plan_id'],"执行计划ID",user_plan_id)
        print('第',day,'天')
        # print(requestt_plan_info.json())
    # sleep(0.5)

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

    reqsts1 = requests.post(url=en_url, headers=header_live, json=data_1)
    # print('英语学习完成上报1返回：', reqsts.text)
    sleep(2.5)
    reqsts2= requests.post(url=en_url, headers=header_live, json=data_2)
    # print('英语学习完成上报2返回：', reqsts.text)
    sleep(2.5)


    # plan_info = "https://hear.abctime.com/v1/study/plan-info"
    #
    # plan_info_data = {"next": 1, "uid": UID}
    # requestt_plan_info = requests.post(url=plan_info, json=plan_info_data, headers=header_live)
    # if requestt_plan_info.json()['code'] == str(300):
    #     print("ERRO异常计划id:", requestt_plan_info.json()['data']['user_plan_id'])
    #     print("ERRO，请求", requestt_plan_info.json())
    #     print('第', day, '天')
    #     plan_info_list_erro.append(user_plan_id)
    # else:
    #     print("计划正常！code:", requestt_plan_info.json()['code'], '计划ID', requestt_plan_info.json()['data']['user_plan_id'])
    #     print('第', day, '天')


    user_plan_id += 1
    day+=1
print(plan_info_list_erro)
