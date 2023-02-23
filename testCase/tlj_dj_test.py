import requests
import random
import time
from common.get_tlj_auth import *
from common.requestSimulationData import *



url_reset_interface="https://hear-dev.abctime.com/v1/study/reset-level"

url_firstset_interface="https://hear-dev.abctime.com/v1/study/set-level"


a=1
while True:
    auth_end = getauth()[0]   #令牌
    phone_end = getauth()[1]  #手机号
    uid_end=getauth()[2]      #uid
    print("uid:",uid_end)
    print("auth_end:",auth_end)
    # print("uid:",uid_end)

    header = {"Authorization":auth_end}
    data_set_ch={"level":"S4","type":2,"week_plan":"1,2,3,4,5,6,7","uid":uid_end}

    #首次定级
    req_set=requests.post(url=url_firstset_interface,json=data_set_ch,headers=header)
    print("req_set:",req_set.text)

    if req_set.json()["code"]==0:
        print("英语定级成功")
    else:
        print("英语定级失败,req_set.status_code:",req_set.text)
    time.sleep(1)




    level_list = ["aa", "A", "B", "C", "D", "E", "F", "G"]
    le = random.choice(level_list)
    data_set_en={"level": le, "type": 1, "week_plan": "1,2,3,4,5,6,7", "uid": uid_end}
    req_set_en=requests.post(url=url_firstset_interface,json=data_set_en,headers=header)
    print("req_set_en.text:",req_set_en.text)

    if req_set_en.json()["code"]==0:
        print("语文定级成功")
    else:
        print("语文定级失败,req_set.status_code:",req_set_en.text)
    time.sleep(1)

    data_e = {
        "level": le,
        "study_time": "12:29",
        "week_plan": "3,4,5",
        "uid": uid_end
    }

    data_c = {
        "uid": uid_end,
        "week_plan": "1,2,3,4,5",
        "study_time": "09:00",
        "type": 2,
        "level": "S1"
    }

    datalist = [
        data_e, data_c
    ]



    req_e=requests.post(url=url_reset_interface,json=data_e,headers=header)
    print("req_e.text:",req_e.text)
    time.sleep(1)
    if req_e.json()["code"]==0:
        print("英语重定级成功")
    else:
        print("英语定级失败,req_set.status_code:",req_e.text)
    time.sleep(1)




    req_c=requests.post(url=url_reset_interface,json=data_c,headers=header)
    print("req_c.text:", req_c.text)
    if req_c.json()["code"]==0:
        print("语文重定级成功")
    else:
        print("语文定级失败,req_set.status_code:",req_c.text)

    time.sleep(1)
    a+=1

    print(a)
    if a==2:
        break
