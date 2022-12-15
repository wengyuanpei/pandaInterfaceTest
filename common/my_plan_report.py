from time import sleep
import requests

def myplanreport(S1_words,S1_lesson,S1_video,url,header,uid,event_id,s_time):
    for i in range(3):
        print('这是S1学习')
        if i == 0:
            S1_words = S1_words
            for i_S1_w in S1_words:
                for i_S1_w_event_id in event_id:
                    data = {"event_id": i_S1_w_event_id, "user_plan_id": i_S1_w, "uid": uid}
                    sleep(2)
                    print('请求参数：', data)
                    reqsts = requests.post(url=url, headers=header, json=data)
                    print(str(s_time)+'字卡学习完成上报：', reqsts.text)
        if i == 1:
            S1_lesson = S1_lesson
            for i_S1_w in S1_words:
                for i_S1_w_event_id in event_id:
                    data = {"event_id": i_S1_w_event_id, "user_plan_id": i_S1_w, "uid": uid}
                    sleep(2)
                    print('请求参数：', data)
                    reqsts = requests.post(url=url, headers=header, json=data)
                    print(str(s_time)+'古诗学习完成上报：', reqsts.text)
        if i == 2:
            S1_video = S1_video
            for i_S1_w in S1_words:
                for i_S1_w_event_id in event_id:
                    data = {"event_id": i_S1_w_event_id, "user_plan_id": i_S1_w, "uid": uid}
                    sleep(2)
                    print('请求参数：', data)
                    reqsts = requests.post(url=url, headers=header, json=data)
                    print(str(s_time)+'视频学习完成上报：', reqsts.text)