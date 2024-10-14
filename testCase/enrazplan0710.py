from time import sleep

import requests
from common.finish_plan_urlenverment import *

headerpre={'Authorization':'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjQwOTc2ODgyODYyOTg1MjE3Iiwic3ViIjoie1wiaWRcIjoxNjQwOTc2ODgyODYyOTg1MjE3LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTcwNjk1NTI1NH0.nqZPvW2jPY3gdOoLmNDYseT8-SRp3UEsAq9btLqmVNku0VVwX7m1QRLtA4XOGG7Z2Rl1A6yEhRMegyKSobpfZg'}
header={'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjQwOTc2ODgyODYyOTg1MjE3Iiwic3ViIjoie1wiaWRcIjoxNjQwOTc2ODgyODYyOTg1MjE3LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTcwNzI5OTQwNH0.AVC4vgok2cQ8Ni9za3Najs-1mk9pOxuCUY6YYvgk5V5xlDlHRGPSOdbZECKS5HKV6vIwfpz-C5G6_-2iYsDLyg'}
baseurl=urlenverment(2)

#获取计划信息
def getplaninfo(uid):

    url=baseurl+'v1/study/plan-info-new'
    data={"next":1,"uid":uid}
    rep=requests.post(url=url,json=data,headers=headerpre)

    # print('RAZ数据：' + str(rep.json()['data']['read_book']))
    # print('磨耳朵数据：'+str(rep.json()['data']['listen_info']))
    # print('AI对话数据：' + str(rep.json()['data']['oral_training']))

    planid=rep.json()['data']['user_plan_id']
    lisen=rep.json()['data']['listen_info']['user_plan_id']

    return planid,lisen



if __name__ == '__main__':

    errorlist=[]
    ####################################填写UID########################################
    uid=1547790292942245889
    ######################################天数#########################################
    finishday=300

    for i in range(finishday):


        info = getplaninfo(uid)
        planid = info[0]


        req=finish_plan(planid, baseurl, header, uid, 1)


        if planid=="":
            errorlist.append([planid,1])
        sleep(1)
    print('异常计划数据：',errorlist)




