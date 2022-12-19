

#语文定级计划上报接口
import requests
from time import sleep





S_plan_resorse=[1,2,3]
url="https://hear.abctime.com/v1/study-cn/finish-plan"
header={  "Content-Type": "application/json;charset=UTF-8"}
# data={"event_id":3,"user_plan_id":2335,"uid":1561969032355688449}
uid_18384243506=1562629060075102209
uid_173=1585185031592185857
uid_zl=1547790292942245889


user_plan_id=15654


while user_plan_id <= 15699:

    data = {"event_id": 5, "user_plan_id": user_plan_id, "uid": uid_zl}
    sleep(1)
    print('请求参数：', data)
    reqsts = requests.post(url=url, headers=header, json=data)
    print('S1字卡学习完成上报：', reqsts.text)
    user_plan_id+=1

    plan_info="https://hear.abctime.com/v1/study-cn/plan-info"
    data_info={"uid":uid_zl}
    reqsts_plan_info=requests.post(url=plan_info, headers=header, json=data)
    # print(reqsts_plan_info.json()['data']['user_plan_info']['poetry']['lesson']['lesson_id'])
    print(reqsts_plan_info.text)

# 英语部分

