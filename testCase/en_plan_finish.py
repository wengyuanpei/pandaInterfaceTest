
#语文定级计划上报接口
import requests

# 英语部分

UID=1562629060075102209


#dev
dev_en_url=" https://hear-dev.abctime.com/v1/study/finish-plan"

header_dev={"Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxMTkxMzI1NzEwOTg3MzQ1OTIyIiwic3ViIjoie1wiaWRcIjoxMTkxMzI1NzEwOTg3MzQ1OTIyLFwibW9iaWxlXCI6XCIrODYxODg4ODg4ODg4OFwiLFwidXNlcm5hbWVcIjpcIkFha2FzaCDpmL_ljaHku4BcIn0iLCJleHAiOjE2OTc0NDU1ODl9.felcnqDtixPGVNaKNFDBGmOByUGGJI390GOYqsc_uwWzy0rq-ggf0XDB4-eIwoDbZXvibTENielLtM7kE7OJIQ"}

plan_info_list_erro=[]

day=1

user_plan_id=16770335
while day <= 1055:

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
    plan_info = "https://hear-dev.abctime.com/v1/study/plan-info"

    plan_info_data = {"next": 1, "uid": UID}
    requestt_plan_info = requests.post(url=plan_info, json=plan_info_data, headers=header_dev)
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
        #处理ID异常

    except:
        user_plan_id+=1


    day+=1
print(plan_info_list_erro)
