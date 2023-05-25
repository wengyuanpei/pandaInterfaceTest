import  requests
from  time import  sleep

Uid='1640976882862985217'
Kid='1640976882862985217'
Uid_int=1640976882862985217
header={"Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjQwOTc2ODgyODYyOTg1MjE3Iiwic3ViIjoie1wiaWRcIjoxNjQwOTc2ODgyODYyOTg1MjE3LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTcwMDU2MTMxNX0.DVzMyDdL3LF3VH77JxuWHFp8bU1yOICMK8wTMYQF2OAlOzcXBaVonQi9eN74HyPBmeoyYy0yS8d3R8wQTMPL3g",
        "User-Uid":Uid,
        "Kid-Uid":Kid }

#请求汉字列表
data={"resource_id":19,"uid":Uid_int}

pre_url_info="https://hear-pre.abctime.com/v1/record/char-list"

pre_record_add=" https://hear-pre.abctime.com/v1/record/add"


#玩儿上报信息
data_play={"category_id":10,"content":"","content_id":3,"cost_time":0,"event_id":20,"extra":"","is_init":1,"play_place":0,"proportion":0,"score":0,"uid":1640976882862985217}

#学上报信息
data_study={"category_id":10,"content":"","content_id":3,"cost_time":0,"event_id":19,"extra":"","is_init":1,"play_place":0,"proportion":0,"score":0,"uid":1640976882862985217}


#读上报信息
data_read={"category_id":10,"content":"","content_id":3,"cost_time":0,"event_id":22,"extra":"","is_init":1,"play_place":0,"proportion":0,"score":0,"uid":1640976882862985217}

#上报写信息
data_write={"category_id":10,"content":"{\"video_urls\":[\"https://oaudios.abctime.com/tlj_oss_audio_1640976882862985217_1685010763502.wav\"]}","content_id":3,"cost_time":0,"event_id":21,"extra":"","is_init":1,"play_place":0,"proportion":0,"score":100,"uid":1640976882862985217}




charslist_req=requests.post(url=pre_url_info,headers=header,json=data)
# print(charslist_req.json()['data']['char_list'][0]['id'])
# for i in range(len(charslist_req.json()['data']['char_list'])):
for i in range(len(charslist_req.json()['data']['char_list'])):

        charid=charslist_req.json()['data']['char_list'][i]['id']
        print("汉字ID：",charid,'汉字：',charslist_req.json()['data']['char_list'][i]['chineseCharacter'])

        # 玩儿上报信息
        data_play = {"category_id": 10, "content": "", "content_id": charid, "cost_time": 0, "event_id": 20, "extra": "",
                     "is_init": 1, "play_place": 0, "proportion": 0, "score": 0, "uid": 1640976882862985217}

        # 学上报信息
        data_study = {"category_id": 10, "content": "", "content_id": charid, "cost_time": 0, "event_id": 19, "extra": "",
                      "is_init": 1, "play_place": 0, "proportion": 0, "score": 0, "uid": 1640976882862985217}

        # 读上报信息
        data_read = {"category_id": 10, "content": "", "content_id": charid, "cost_time": 0, "event_id": 22, "extra": "",
                     "is_init": 1, "play_place": 0, "proportion": 0, "score": 0, "uid": 1640976882862985217}

        # 上报写信息
        data_write = {"category_id": 10,
                      "content": "{\"video_urls\":[\"https://oaudios.abctime.com/tlj_oss_audio_1640976882862985217_1685010763502.wav\"]}",
                      "content_id": charid, "cost_time": 0, "event_id": 21, "extra": "", "is_init": 1, "play_place": 0,
                      "proportion": 0, "score": 100, "uid": 1640976882862985217}

        req1=requests.post(url=pre_record_add,headers=header,json=data_play)
        print(req1.json())
        sleep(1)
        req2 = requests.post(url=pre_record_add, headers=header, json=data_study)
        print(req2.json())
        sleep(1)
        req3 = requests.post(url=pre_record_add, headers=header, json=data_read)
        print(req3.json())
        sleep(1)
        req4 = requests.post(url=pre_record_add, headers=header, json=data_write)
        print(req4.json())
        sleep(1)