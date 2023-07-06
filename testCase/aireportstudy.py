

import requests

from common.finish_plan import *

baseurl=urlenverment(2)

header={'Authorization':'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjQwOTc2ODgyODYyOTg1MjE3Iiwic3ViIjoie1wiaWRcIjoxNjQwOTc2ODgyODYyOTg1MjE3LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTcwNDE4MTY4Nn0.lj0hwmWyy_h5F4PSoE8ldC6na6xkFIoz4YLEiaIEOuosJCcvKWcFrYXZU8oWh4wRF514sBFdV9eFCYi8ZuB06Q'}

uid=1640976882862985217
def getlevelinfo():

    levellisturl='v1/ai-oral-training/get-level-list'



    url=baseurl+levellisturl

    levellist=requests.get(url=url,headers=header)
    list_level=levellist.json()['data']['level_list']
    # print(levellist.json()['data']['level_list'])
    return list_level


def get_scene_id(levelid):
    list_info = 'v1/ai-oral-training/get-list'
    url=baseurl+list_info
    data={
    "level_id": levelid,
    "uid": uid
}
    get_scene_id_rp=requests.post(url=url,json=data,headers=header)
    scene_id_list=get_scene_id_rp.json()['data']['scene_list']

    return scene_id_list


def addinfo(content_id):
    url=baseurl+'v1/record/add'

    data1={"category_id":18,"content":"{\"0\":{\"list\":[{\"score\":100,\"trans\":\"\",\"word\":\"cold\"}],\"score\":100},\"1\":{\"list\":[{\"score\":100,\"trans\":\"\",\"word\":\"sweater\"}],\"score\":100},\"2\":{\"list\":[{\"score\":98,\"trans\":\"\",\"word\":\"cap\"}],\"score\":100},\"3\":{\"list\":[{\"score\":100,\"trans\":\"\",\"word\":\"scarf\"}],\"score\":100}}","content_id":content_id,"event_id":45,"extra":"1","is_init":0,"proportion":25,"score":100,"uid":uid}
    data2={"category_id":18,"content":"{\"0\":{\"list\":[{\"score\":69,\"trans\":\"\",\"word\":\"It\u0027s\"},{\"score\":15,\"trans\":\"\",\"word\":\"cold\"},{\"score\":100,\"trans\":\"\",\"word\":\"outside.\"}],\"score\":69},\"1\":{\"list\":[{\"score\":5,\"trans\":\"\",\"word\":\"Put\"},{\"score\":5,\"trans\":\"\",\"word\":\"on\"},{\"score\":5,\"trans\":\"\",\"word\":\"your\"},{\"score\":86,\"trans\":\"\",\"word\":\"sweater,\"},{\"score\":5,\"trans\":\"\",\"word\":\"please.\"}],\"score\":26},\"2\":{\"list\":[{\"score\":100,\"trans\":\"\",\"word\":\"OK.\"},{\"score\":5,\"trans\":\"\",\"word\":\"And\"},{\"score\":5,\"trans\":\"\",\"word\":\"I\u0027ll\"},{\"score\":5,\"trans\":\"\",\"word\":\"put\"},{\"score\":5,\"trans\":\"\",\"word\":\"on\"},{\"score\":5,\"trans\":\"\",\"word\":\"my\"},{\"score\":5,\"trans\":\"\",\"word\":\"cap\"},{\"score\":5,\"trans\":\"\",\"word\":\"and\"},{\"score\":5,\"trans\":\"\",\"word\":\"scarf.\"}],\"score\":21},\"3\":{\"list\":[{\"score\":85,\"trans\":\"\",\"word\":\"That\u0027\"},{\"score\":82,\"trans\":\"\",\"word\":\"right!\"},{\"score\":5,\"trans\":\"\",\"word\":\"You\"},{\"score\":5,\"trans\":\"\",\"word\":\"should\"},{\"score\":5,\"trans\":\"\",\"word\":\"keep\"},{\"score\":5,\"trans\":\"\",\"word\":\"warm.\"}],\"score\":37}}","content_id":content_id,"event_id":46,"extra":"1","is_init":0,"proportion":100,"score":37,"uid":uid}
    data3={"category_id":18,"content":"{\"0\":{\"list\":[],\"score\":0},\"1\":{\"list\":[],\"score\":0},\"2\":{\"list\":[{\"score\":17,\"trans\":\"\",\"word\":\"Put\"},{\"score\":6,\"trans\":\"\",\"word\":\"on\"},{\"score\":5,\"trans\":\"\",\"word\":\"your\"},{\"score\":5,\"trans\":\"\",\"word\":\"sweater,\"},{\"score\":5,\"trans\":\"\",\"word\":\"please.\"}],\"score\":0},\"3\":{\"list\":[],\"score\":0},\"4\":{\"list\":[{\"score\":99,\"trans\":\"\",\"word\":\"That\u0027\"},{\"score\":99,\"trans\":\"\",\"word\":\"right!\"},{\"score\":100,\"trans\":\"\",\"word\":\"You\"},{\"score\":100,\"trans\":\"\",\"word\":\"should\"},{\"score\":100,\"trans\":\"\",\"word\":\"keep\"},{\"score\":100,\"trans\":\"\",\"word\":\"warm.\"}],\"score\":100}}","content_id":content_id,"event_id":47,"extra":"1","is_init":0,"proportion":100,"score":100,"uid":uid}

    req1=requests.post(url=url,json=data1,headers=header)
    req2 = requests.post(url=url, json=data2, headers=header)
    req3 = requests.post(url=url, json=data3, headers=header)

    print(content_id,'上报完成')


if __name__ == '__main__':
    #需要学习的等级
    levelid=1
    scen=get_scene_id(levelid)
    # print(scen)
    langs=len(scen)
    print('当前等级下的数量',langs)
    #需要学习的数量减少多少本
    less=1
    for i in range(langs-less):

        scene_idget=scen[i]['scene_id']
        # print(scene_idget)
        addinfo(scene_idget)

