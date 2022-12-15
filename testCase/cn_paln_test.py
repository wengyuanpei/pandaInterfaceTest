

#语文定级计划上报接口
import requests
from time import sleep

S1_words=[4
,5
,8
,11
,12
,14
,15
,16
,17
,18
,19
,20
,22
,23
,26
,27
,29
,29
,31
,34
,38
,40
,41
,44
,46
,53
,60
,72
,74
,76
,77
,86
,88
,97
,108
,118
,140
,146
,152
,183
,204
,212
,254
]

S1_lesson=[31
,32
,33
,34
,35
,36
,37
,38
,39
,40
,41
,42
,43
,44
,45
]
S1_video=[2397
,2389
,2380
,2374
,2366
,2359
,2352
,2344
,2336
,2329
,2322
,2316
,2311
,2305
,2298
,2233
,2361
,2340
,2332
,2324
,2319
,2313
,2308
,2297
,2292
,2286
,2262
,2246
,2240
,2194
]

S2_words=[21
,37
,42
,43
,47
,51
,52
,54
,62
,63
,67
,80
,89
,95
,98
,107
,113
,116
,117
,119
,122
,133
,137
,143
,145
,164
,165
,170
,171
,199
,219
,255
,269
,279
,280
,284
,299
,336
,574
,590
,708
,774
,964
,1039
]
S2_lesson=[46
,47
,48
,49
,50
,51
,52
,53
,54
,55
,56
,57
,58
,59
,60
]
S2_video=[2291
,2285
,2280
,2273
,2267
,2261
,2254
,2247
,2239
,2218
,2275
,2158
,2196
,2171
,2177
,2942
,2888
,2882
,2876
,2894
,2930
,2936
,2783
,2779
,2774
,2769
,2607
,2603
,2600
,2599
]
S3_words=[25
,64
,65
,75
,82
,83
,106
,110
,114
,121
,125
,132
,134
,135
,139
,150
,161
,167
,169
,190
,215
,239
,241
,271
,278
,317
,346
,535
,586
,611
,614
,655
,724
,745
,751
,820
,902
,978
,1018
,1054
]

S3_lesson=[61
,62
,63
,64
,65
,66
,67
,68
,69
,70
,71
,72
,73
,74
,75
]
S3_video=[8277
,8276
,8278
,8279
,8281
,8280
,8282
,8283
,8285
,8286
,8287
,8284
,8288
,8291
,8290
,8289
,8292
,8295
,8293
,8294
,8296
,8299
,8297
,8298
,8304
,8307
,8305
,8306
,8310
,8309
,8308
,8311
,1679
,1757
,1721
,1686
,1743
,1750
,1734
,1728
,1713
,1700
,1771
,1672
,1642
,1663
,1649
]
S4_words=[73
,87
,102
,103
,120
,134
,141
,155
,161
,172
,213
,221
,225
,226
,229
,230
,231
,253
,261
,266
,266
,270
,281
,288
,295
,317
,321
,332
,367
,535
,548
,570
,580
,635
,740
,753
,816
,984
,1043
,1049
,1055
,1079
]
S4_lesson=[5
,7
,8
,9
,10
,11
,12
,13
,14
,16
,17
,18
,19
,20
,21
]
S4_video=[8315
,8312
,8314
,8313
,8317
,8319
,8318
,8316
,8322
,8321
,8320
,8323
,8330
,8329
,8328
,8331
,8334
,8332
,8333
,8335
,8339
,8338
,8336
,8337
,8343
,8340
,8341
,8342
,1698
,1689
,1681
,1670
,1659
,1650
,1644
,2038
,2044
,2031
,2021
,2014
,2006
,1998
,1991
]

S_plan_resorse=[1,2,3]

url="https://hear.abctime.com/v1/study-cn/finish-plan"
header={  "Content-Type": "application/json;charset=UTF-8"}
# data={"event_id":3,"user_plan_id":2335,"uid":1561969032355688449}
for i in range(3):
    print('这是S1学习')
    if i == 0:
        S1_words=S1_words
        for i_S1_w in  S1_words:
            for i_S1_w_event_id in (1,2,3):

                data = {"event_id": i_S1_w_event_id, "user_plan_id": i_S1_w, "uid": 1561969032355688449}
                sleep(2)
                print('请求参数：',data)
                reqsts=requests.post(url=url,headers=header,json=data)
                print('S1字卡学习完成上报：',reqsts.text)
                #获取当日推荐学习内容
                plan_url="https://hear.abctime.com/v1/study-cn/plan-info"
                data_plan={"uid": 1561969032355688449}
                plan_req=requests.post(url=plan_url,headers=header,json=data_plan)
                plan_next_day = plan_req.json()["data"]["user_plan_id"]
                if plan_next_day==str(i_S1_w):
                    print('当日推荐计划与预期一致')
    if i == 1:
        S1_lesson = S1_lesson
        for i_S1_w in S1_words:
            for i_S1_w_event_id in (1, 2, 3):
                data = {"event_id": i_S1_w_event_id, "user_plan_id": i_S1_w, "uid": 1561969032355688449}
                sleep(2)
                print('请求参数：',data)
                reqsts = requests.post(url=url, headers=header, json=data)
                print('S1古诗学习完成上报：', reqsts.text)
                plan_url="https://hear.abctime.com/v1/study-cn/plan-info"
                data_plan={"uid": 1561969032355688449}
                plan_req=requests.post(url=plan_url,headers=header,json=data_plan)
                plan_next_day = plan_req.json()["data"]["user_plan_id"]
                if plan_next_day==str(i_S1_w):
                    print('当日推荐计划与预期一致')
    if i == 2:
        S1_video = S1_video
        for i_S1_w in S1_words:
            for i_S1_w_event_id in (1, 2, 3):
                data = {"event_id": i_S1_w_event_id, "user_plan_id": i_S1_w, "uid": 1561969032355688449}
                sleep(2)
                print('请求参数：',data)
                reqsts = requests.post(url=url, headers=header, json=data)
                print('S1视频学习完成上报：', reqsts.text)
                plan_url="https://hear.abctime.com/v1/study-cn/plan-info"
                data_plan={"uid": 1561969032355688449}
                plan_req=requests.post(url=plan_url,headers=header,json=data_plan)
                plan_next_day = plan_req.json()["data"]["user_plan_id"]
                if plan_next_day==str(i_S1_w):
                    print('当日推荐计划与预期一致')


for i in range(3):
    print('这是S2学习')
    if i == 0:
        S2_words=S2_words
        for i_S1_w in  S1_words:
            for i_S1_w_event_id in (1,2,3):

                data = {"event_id": i_S1_w_event_id, "user_plan_id": i_S1_w, "uid": 1561969032355688449}
                sleep(2)
                print('请求参数：',data)
                reqsts=requests.post(url=url,headers=header,json=data)
                print('S2字卡学习完成上报：',reqsts.text)
                plan_url="https://hear.abctime.com/v1/study-cn/plan-info"
                data_plan={"uid": 1561969032355688449}
                plan_req=requests.post(url=plan_url,headers=header,json=data_plan)
                plan_next_day = plan_req.json()["data"]["user_plan_id"]
                if plan_next_day==str(i_S1_w):
                    print('当日推荐计划与预期一致')
    if i == 1:
        S2_lesson = S2_lesson
        for i_S1_w in S1_words:
            for i_S1_w_event_id in (1, 2, 3):
                data = {"event_id": i_S1_w_event_id, "user_plan_id": i_S1_w, "uid": 1561969032355688449}
                sleep(2)
                print('请求参数：',data)
                reqsts = requests.post(url=url, headers=header, json=data)
                print('S2古诗学习完成上报：', reqsts.text)
                plan_url="https://hear.abctime.com/v1/study-cn/plan-info"
                data_plan={"uid": 1561969032355688449}
                plan_req=requests.post(url=plan_url,headers=header,json=data_plan)
                plan_next_day = plan_req.json()["data"]["user_plan_id"]
                if plan_next_day==str(i_S1_w):
                    print('当日推荐计划与预期一致')
    if i == 2:
        S2_video = S2_video
        for i_S1_w in S1_words:
            for i_S1_w_event_id in (1, 2, 3):
                data = {"event_id": i_S1_w_event_id, "user_plan_id": i_S1_w, "uid": 1561969032355688449}
                sleep(2)
                print('请求参数：',data)
                reqsts = requests.post(url=url, headers=header, json=data)
                print('S2视频学习完成上报：', reqsts.text)
                plan_url="https://hear.abctime.com/v1/study-cn/plan-info"
                data_plan={"uid": 1561969032355688449}
                plan_req=requests.post(url=plan_url,headers=header,json=data_plan)
                plan_next_day = plan_req.json()["data"]["user_plan_id"]
                if plan_next_day==str(i_S1_w):
                    print('当日推荐计划与预期一致')
for i in range(3):
    print('这是S3学习')
    if i == 0:
        S3_words=S3_words
        for i_S1_w in  S1_words:
            for i_S1_w_event_id in (1,2,3):

                data = {"event_id": i_S1_w_event_id, "user_plan_id": i_S1_w, "uid": 1561969032355688449}
                sleep(2)
                print('请求参数：',data)
                reqsts=requests.post(url=url,headers=header,json=data)
                print('S3字卡学习完成上报：',reqsts.text)
                plan_url="https://hear.abctime.com/v1/study-cn/plan-info"
                data_plan={"uid": 1561969032355688449}
                plan_req=requests.post(url=plan_url,headers=header,json=data_plan)
                plan_next_day = plan_req.json()["data"]["user_plan_id"]
                if plan_next_day==str(i_S1_w):
                    print('当日推荐计划与预期一致')
    if i == 1:
        S3_lesson = S3_lesson
        for i_S1_w in S1_words:
            for i_S1_w_event_id in (1, 2, 3):
                data = {"event_id": i_S1_w_event_id, "user_plan_id": i_S1_w, "uid": 1561969032355688449}
                sleep(2)
                print('请求参数：',data)
                reqsts = requests.post(url=url, headers=header, json=data)
                print('S3古诗学习完成上报：', reqsts.text)
                plan_url="https://hear.abctime.com/v1/study-cn/plan-info"
                data_plan={"uid": 1561969032355688449}
                plan_req=requests.post(url=plan_url,headers=header,json=data_plan)
                plan_next_day = plan_req.json()["data"]["user_plan_id"]
                if plan_next_day==str(i_S1_w):
                    print('当日推荐计划与预期一致')
    if i == 2:
        S3_video = S3_video
        for i_S1_w in S1_words:
            for i_S1_w_event_id in (1, 2, 3):
                data = {"event_id": i_S1_w_event_id, "user_plan_id": i_S1_w, "uid": 1561969032355688449}
                sleep(2)
                print('请求参数：',data)
                reqsts = requests.post(url=url, headers=header, json=data)
                print('S3视频学习完成上报：', reqsts.text)
                plan_url="https://hear.abctime.com/v1/study-cn/plan-info"
                data_plan={"uid": 1561969032355688449}
                plan_req=requests.post(url=plan_url,headers=header,json=data_plan)
                plan_next_day = plan_req.json()["data"]["user_plan_id"]
                if plan_next_day==str(i_S1_w):
                    print('当日推荐计划与预期一致')
for i in range(3):
    print('这是S4学习')
    if i == 0:
        S4_words=S4_words
        for i_S1_w in  S1_words:
            for i_S1_w_event_id in (1,2,3):

                data = {"event_id": i_S1_w_event_id, "user_plan_id": i_S1_w, "uid": 1561969032355688449}
                sleep(2)
                print('请求参数：',data)
                reqsts=requests.post(url=url,headers=header,json=data)
                print('S4字卡学习完成上报：',reqsts.text)
                plan_url="https://hear.abctime.com/v1/study-cn/plan-info"
                data_plan={"uid": 1561969032355688449}
                plan_req=requests.post(url=plan_url,headers=header,json=data_plan)
                plan_next_day = plan_req.json()["data"]["user_plan_id"]
                if plan_next_day==str(i_S1_w):
                    print('当日推荐计划与预期一致')
    if i == 1:
        S4_lesson = S4_lesson
        for i_S1_w in S1_words:
            for i_S1_w_event_id in (1, 2, 3):
                data = {"event_id": i_S1_w_event_id, "user_plan_id": i_S1_w, "uid": 1561969032355688449}
                sleep(2)
                print('请求参数：',data)
                reqsts = requests.post(url=url, headers=header, json=data)
                print('S4古诗学习完成上报：', reqsts.text)
                plan_url="https://hear.abctime.com/v1/study-cn/plan-info"
                data_plan={"uid": 1561969032355688449}
                plan_req=requests.post(url=plan_url,headers=header,json=data_plan)
                plan_next_day = plan_req.json()["data"]["user_plan_id"]
                if plan_next_day==str(i_S1_w):
                    print('当日推荐计划与预期一致')
    if i == 2:
        S4_video = S4_video
        for i_S1_w in S1_words:
            for i_S1_w_event_id in (1, 2, 3):
                data = {"event_id": i_S1_w_event_id, "user_plan_id": i_S1_w, "uid": 1561969032355688449}
                sleep(2)
                print('请求参数：',data)
                reqsts = requests.post(url=url, headers=header, json=data)
                print('S4视频学习完成上报：', reqsts.text)
                plan_url="https://hear.abctime.com/v1/study-cn/plan-info"
                data_plan={"uid": 1561969032355688449}
                plan_req=requests.post(url=plan_url,headers=header,json=data_plan)
                plan_next_day = plan_req.json()["data"]["user_plan_id"]
                if plan_next_day==str(i_S1_w):
                    print('当日推荐计划与预期一致')
                if plan_next_day!=str(i_S1_w):
                    print('当日推荐计划与预期不一致')
