#单接口并发请求


import time
from threading import Thread, current_thread
import requests
import random
import time
from common.get_tlj_auth import *
from common.requestSimulationData import *


def demo1():
    url_reset_interface = "https://hear-dev.abctime.com/v1/study/reset-level"

    url_firstset_interface = "https://hear-dev.abctime.com/v1/study/set-level"

    a = 1
    while True:
        auth_end = getauth()[0]  # 令牌
        phone_end = getauth()[1]  # 手机号
        uid_end = getauth()[2]  # uid
        print("uid:", uid_end)
        print("auth_end:", auth_end)

        # print("uid:",uid_end)

        header = {"Authorization": auth_end}
        data_set_ch = {"level": "S2", "type": int(2), "week_plan": "1,2,3,4,5", "uid": int(uid_end)}

        # 首次定级
        req_set = requests.post(url=url_firstset_interface, json=data_set_ch, headers=header)
        print("req_set:", req_set.text)

        if req_set.json()["code"] == str(200):
            print("英语定级成功")
        else:
            print("英语定级失败,req_set.status_code:", req_set.text)
        # time.sleep(0.5)

        level_list = ["aa", "A", "B", "C", "D", "E", "F", "G"]
        le = random.choice(level_list)
        data_set_en = {"level": le, "type": int(1), "week_plan": "1,2,3,4,5", "uid": int(uid_end)}
        req_set_en = requests.post(url=url_firstset_interface, json=data_set_en, headers=header)
        print("req_set_en.text:", req_set_en.text)

        if req_set_en.json()["code"] == str(200):
            print("语文定级成功")
        else:
            print("语文定级失败,req_set.status_code:", req_set_en.text)
        # time.sleep(0.5)

        data_e = {
            "level": le,
            "study_time": "12:29",
            "week_plan": "3,4,5",
            "uid": int(uid_end)
        }

        data_c = {
            "uid": int(uid_end),
            "week_plan": "1,2,3,4,5",
            "study_time": "09:00",
            "type": int(2),
            "level": "S1"
        }

        datalist = [
            data_e, data_c
        ]

        req_e = requests.post(url=url_reset_interface, json=data_e, headers=header)
        print("req_e.text:", req_e.text)
        if req_e.json()["code"] == str(200):
            print("英语重定级成功")
        else:
            print("英语定级失败,req_set.status_code:", req_e.text)
        # time.sleep(0.5)

        req_c = requests.post(url=url_reset_interface, json=data_c, headers=header)
        print("req_c.text:", req_c.text)
        if req_c.json()["code"] == str(200):
            print("语文重定级成功")
        else:
            print("语文定级失败,req_set.status_code:", req_c.text)

        # time.sleep(0.5)
        a += 1

        # print(a)
        # if a==8000:
        #     break



if __name__ == '__main__':
    print('主线程开始...')
    threads = [Thread(target=demo1) for _ in range(500)]  # 这里是创建3个线程，放到一个列表里
    for t in threads:
        t.start()  # 启动线程
    for t in threads:
        t.join()  # 线程等待
    print('主线程结束...')