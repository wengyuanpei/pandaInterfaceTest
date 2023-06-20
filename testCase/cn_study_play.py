from time import sleep

import requests

url='https://hear.abctime.com/v1/study-cn/finish-plan'

data={"event_id":3,"user_plan_id":22715084,"uid":1640976882862985217}

header={'Authorization':"Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjQwOTc2ODgyODYyOTg1MjE3Iiwic3ViIjoie1wiaWRcIjoxNjQwOTc2ODgyODYyOTg1MjE3LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTcwMjI3NjU3MH0.e6CLa06064efURGTB9K0SmGdLMf1joGLrPhDGvUZt-SHBY9ZRTlWijLItbWrmrNP6TWovbAoXR8MW9Sfbk6VCA",
        'Sn':'S1DEV0051',
        'User-Uid':'1640976882862985217',
       'Kid-Uid':'1640976882862985217' }



def finishcnplan(id):
    url = 'https://hear.abctime.com/v1/study-cn/finish-plan'

    data = {"event_id": 3, "user_plan_id": id, "uid": 1640976882862985217}

    header = {
        'Authorization': "Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjQwOTc2ODgyODYyOTg1MjE3Iiwic3ViIjoie1wiaWRcIjoxNjQwOTc2ODgyODYyOTg1MjE3LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTcwMjI3NjU3MH0.e6CLa06064efURGTB9K0SmGdLMf1joGLrPhDGvUZt-SHBY9ZRTlWijLItbWrmrNP6TWovbAoXR8MW9Sfbk6VCA",
        'Sn': 'S1DEV0051',
        'User-Uid': '1640976882862985217',
        'Kid-Uid': '1640976882862985217'}
    finishresponse=requests.post(url=url,json=data,headers=header)
    print('完成第%s天语文计划' %(id))




def get_planid():
    url='https://hear.abctime.com/v1/study-cn/plan-info'
    data={"uid":1640976882862985217}
    header={'Authorization':"Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjQwOTc2ODgyODYyOTg1MjE3Iiwic3ViIjoie1wiaWRcIjoxNjQwOTc2ODgyODYyOTg1MjE3LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTcwMjI3NjU3MH0.e6CLa06064efURGTB9K0SmGdLMf1joGLrPhDGvUZt-SHBY9ZRTlWijLItbWrmrNP6TWovbAoXR8MW9Sfbk6VCA",
        'Sn':'S1DEV0051',
        'User-Uid':'1640976882862985217',
       'Kid-Uid':'1640976882862985217' }
    play_id=requests.post(url=url,json=data,headers=header)
    cnplanid=play_id.json()["data"]
    # plan_info=play_id.json()
    # print(cnplanid)
    return cnplanid


planid =int(get_planid()["user_plan_id"])
print('开始计划天数%s' % (planid))
errorlist=[]
for i in range(765):
    print('第%s天计划' %(i))

    finishcnplan(planid)

    planid = planid + 1

    try:
        print(get_planid())
    except:
        print('异常计划,计划id是%s！！！' % (get_planid()["user_plan_id"]))
        errorlist.append(get_planid()["user_plan_id"])



    sleep(2)


