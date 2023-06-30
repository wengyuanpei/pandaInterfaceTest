from time import sleep

import requests
from common.finish_plan import *


header={'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjA3MzMxNjI0MTQ4NDU1NDI2Iiwic3ViIjoie1wiaWRcIjoxNjA3MzMxNjI0MTQ4NDU1NDI2LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTcwMzIwOTg5NX0.yoClbSQIELdjNKqMHwMK4eGrV-Wyecl06vU8FqDgX0iKloSpdQpZrlUNfr6vPjDwHfogD3K0fu-GAPx45b1QLQ'}
baseurl=urlenverment(1)#dev环境

#获取计划信息
def getplaninfo(nextt,uid):

    url=baseurl+'v1/study/plan-info-new'
    data={"next":nextt,"uid":uid}
    rep=requests.post(url=url,json=data,headers=header)

    print('RAZ数据：' + str(rep.json()['data']['read_book']))
    print('磨耳朵数据：'+str(rep.json()['data']['listen_info']))
    print('AI对话数据：' + str(rep.json()['data']['oral_training']))

    planid=rep.json()['data']['user_plan_id']
    lisen=rep.json()['data']['listen_info']['user_plan_id']

    return planid,lisen








if __name__ == '__main__':
    errorlist=[]
    ####################################手动填写UID##############################################
    uid=1674375528984518657
    ######################################手动填写熏听ID#########################################
    # intlisen=1196900
    ############################################手动填写第一天计划iD##########################################
    firstday = 1197438
    ##############################################完成计划的天数###############################################
    for i in range(16):

        if i==0:
            info = getplaninfo(1,uid)
            planid = info[0]


            day = planid-firstday
            print('#####################################################计划的第%d天！#######################################################' % day)
            print('listen_info %d' % info[1])

            req=finish_plan(planid,baseurl,header,uid,1)


            if planid=="":
                errorlist.append([planid,1])
        else:
            info = getplaninfo(1,uid)

            planid = info[0]

            day = planid-firstday
            print('#####################################################计划的第%d天！#######################################################' % day)

            print('listen_info %d' % info[1])

            # if info[1]==intlisen:
            #     print('生成的磨耳朵正常！')
            #
            # else:
            #     print('生成的磨耳朵错误！')
            #     errorlist.append([planid, 2])

            req=finish_plan(planid, baseurl, header, uid, 1)


            if planid=="":
                errorlist.append([planid,1])
            sleep(0.5)
    print(errorlist)


