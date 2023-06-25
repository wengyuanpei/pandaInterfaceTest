from time import sleep

import requests
from common.finish_plan import *


header={'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjA3MzMxNjI0MTQ4NDU1NDI2Iiwic3ViIjoie1wiaWRcIjoxNjA3MzMxNjI0MTQ4NDU1NDI2LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTcwMzIwOTg5NX0.yoClbSQIELdjNKqMHwMK4eGrV-Wyecl06vU8FqDgX0iKloSpdQpZrlUNfr6vPjDwHfogD3K0fu-GAPx45b1QLQ'}
baseurl=urlenverment(1)#dev环境

#获取计划信息
def getplaninfo(nextt):

    url=baseurl+'v1/study/plan-info-new'
    data={"next":nextt,"uid":1607331624148455426}
    rep=requests.post(url=url,json=data,headers=header)
    print(rep.json())
    planid=rep.json()['data']['user_plan_id']
    if nextt==0:
        print('当前计划ID为：%d' % planid)
    if nextt==1:
        print('下个计划ID为：%d' % planid)
    return rep.json()['data']['user_plan_id']










if __name__ == '__main__':
    uid=1607331624148455426
    for i in range(1200):
        if i==0:

            planid=getplaninfo(0)

            finish_plan(planid,baseurl,header,uid,1)
        else:
            planid = getplaninfo(1)

            finish_plan(planid, baseurl, header, uid, 1)

            sleep(1)