

import requests
from time import sleep


url='https://hear-dev.abctime.com/hear-admin/v1/plan/finish-plan'

header={"Authorization":"eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ7XCJlbWFpbFwiOlwid2VuZ3l1YW5wZWlAZHJwYW5kYS5jb21cIixcImlkXCI6MjIzLFwibW9iaWxlXCI6XCIxNzM0NTA0MzM2NVwiLFwidXNlcm5hbWVcIjpcIndlbmd5dWFucGVpXCIsXCJ3b3JrY29kZVwiOlwiVjAwMTM3NTBcIixcInp5bE5hbWVcIjpcIjU3K0I2TCtjNlptcVwifSIsImV4cCI6MTY4NjExOTQ2M30.xaRUvC3OlcNGM29Lt_b48buQRWUyeANuQx48FRuO6PLPmZG3epFn0Qb2qr2yMF41S7ijQSPMMr8idGjtjNG9VA"}


day=2

while day<3:

    data1 = {"uid_string": "1607331624148455426", "subject": 1, "day": day, "event_id": 1}  # 绘本
    data2 = {"uid_string": "1607331624148455426", "subject": 1, "day": day, "event_id": 2}  # 音频
    req1 = requests.post(headers=header, json=data1, url=url)
    sleep(0.5)
    print("第"+str(day)+"天绘本请求：",req1.json())
    req2 = requests.post(headers=header, json=data2, url=url)
    print("第" + str(day) + "天音频请求：", req2.json())
    sleep(0.5)
    day+=1

