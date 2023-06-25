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

    print('RAZ数据：' + str(rep.json()['data']['read_book']))
    print('磨耳朵数据：'+str(rep.json()['data']['listen_info']))
    print('AI对话数据：' + str(rep.json()['data']['oral_training']))

    planid=rep.json()['data']['user_plan_id']
    lisen=rep.json()['data']['listen_info']['user_plan_id']

    return planid,lisen







if __name__ == '__main__':
    errorlist=[]
    uid=1607331624148455426
    initlisen=1192309
    info=getplaninfo(1)
    for i in range(180):
        if i==0:

            planid=info[0]

            print('listen_info %d' % info[1])

            req=finish_plan(planid,baseurl,header,uid,1)

            if planid=="":
                errorlist.append([planid,1])
        else:
            planid = info[0]
            print('listen_info %d' % info[1])
            if info[1]==initlisen:
                print('生成的磨耳朵正常！')

            else:
                print('生成的磨耳朵错误！')
                errorlist.append([planid, 2])

            req=finish_plan(planid, baseurl, header, uid, 1)

            if planid=="":
                errorlist.append([planid,1])
            sleep(1)
    print(errorlist)


