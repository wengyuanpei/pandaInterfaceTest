from time import sleep

import requests
from common.finish_plan_urlenverment import *

header={'Authorization':'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjQwOTc2ODgyODYyOTg1MjE3Iiwic3ViIjoie1wiaWRcIjoxNjQwOTc2ODgyODYyOTg1MjE3LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTcwNTQ1NjUxMn0.D5DSiRlELtggp1etr_0h4uBHpMvOZeNw9llo2s1_2AZKvSMsFEvcmtfvIZXiAxHwebprodmQMojDg5GCujzjOw'}
baseurl=urlenverment(3)
def cnplan(uid):

    url=baseurl+'v1/study-cn/plan-info-new'
    data={"uid":uid}
    req=requests.post(url=url,json=data,headers=header)
    return req.json()

def finishplan(user_plan_id,week_day,uid):
    url=baseurl+'v1/study-cn/report-plan-new'
    data={"user_plan_id":user_plan_id,"week_day":week_day,"uid":uid}

    req=requests.post(url=url,json=data,headers=header)




if __name__ == '__main__':
    #################################################################输入执行完成的计划信息############################################################
    uid=1640976882862985217
    day=3
    #############################################################################################################################

    user_plan_id=cnplan(uid)['data']['user_plan_id']
    day_info=cnplan(uid)['data']['plan_list'][day-1]
    print('想要完成的任务信息：',day_info)
    sleep(2)
    print('\n','开始执行完成周%d的计划！' %day)
    finishplan(user_plan_id,day,uid)
    sleep(2)
    print('\n', '周%d的计划执行完成！' %day)