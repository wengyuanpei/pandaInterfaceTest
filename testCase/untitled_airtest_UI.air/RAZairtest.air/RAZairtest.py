# -*- encoding=utf8 -*-
__author__ = "zhang"

from airtest.core.api import *
import requests
from time import sleep

auto_setup(__file__)
import requests
from time import sleep


UID=1640976882862985217
header_live={"Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjQwOTc2ODgyODYyOTg1MjE3Iiwic3ViIjoie1wiaWRcIjoxNjQwOTc2ODgyODYyOTg1MjE3LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTcwMjA5MTkwNn0.t6DT-7Rs7JfOStzggSVDIyw5vz7lVgHwNcP9H9AdrvI5ogwPSudMu8YuWFR20xEg1NTi0lWjAiqwLZpaBEygZg"}


en_url="https://hear-pre.abctime.com/v1/study/finish-plan"

errorlist=[]
    
# 异常绘本学习
 
def errorback():
    touch(Template(r"tpl1686302178695.png", record_pos=(-0.412, -0.727), resolution=(640, 1136)))
    
    sleep(1.0)
    touch(Template(r"tpl1686302195518.png", record_pos=(-0.177, 0.305), resolution=(640, 1136)))
    
    finish_RAZ()
    finish_audio()
    
    touch(Template(r"tpl1686302178695.png", record_pos=(-0.412, -0.727), resolution=(640, 1136)))
    touch(Template(r"tpl1686304862421.png", record_pos=(0.302, -0.441), resolution=(640, 1136)))

    
    
    
    wait(Template(r"tpl1686302568119.png", record_pos=(0.323, -0.594), resolution=(640, 1136)))
    
    touch(Template(r"tpl1686302576303.png", record_pos=(0.323, -0.588), resolution=(640, 1136)))
    
    
def get_playInfo():
    data={"next":0,"uid":1640976882862985217}
    url_playInfo='https://hear-pre.abctime.com/v1/study/plan-info'
    info=requests.post(url=url_playInfo,headers=header_live,json=data)
    return  info.json()['data']["user_plan_id"]
        

#获取计划ID信息
user_plan_id=get_playInfo()
print('获取计划ID成功>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'+str(user_plan_id))
# 循环执行绘本学习
RazNum=1

errorList=[]
while RazNum<1200:
    
        

    # RAZ
    data_1 = {
                      "uid": UID,
                      "user_plan_id": user_plan_id,
                      "event_id": 1
                    }


    #音频完成
    data_2 = {
                      "uid": UID,
                      "user_plan_id": user_plan_id,
                      "event_id": 2
                    }


    def finish_RAZ():
        reqsts1 = requests.post(url=en_url, headers=header_live, json=data_1)
        print("计划id",user_plan_id,"上报音频完成")



    def finish_audio():
        reqsts2= requests.post(url=en_url, headers=header_live, json=data_2)
        print("计划id",user_plan_id,"上报音频完成")

    
    
    
    print("第"+str(RazNum)+"本绘本开始学习")
    snapshot(msg="第"+str(RazNum)+"本绘本")
    wait(Template(r"tpl1686620238815.png", record_pos=(0.003, -0.742), resolution=(640, 1136)))
    sleep(2)
    
    touch(Template(r"tpl1686298775912.png", record_pos=(0.314, -0.42), resolution=(640, 1136)))
    sleep(2)

    #听绘本环节
    sleep(10.0)
    wait(Template(r"tpl1686620338502.png", record_pos=(-0.009, -0.728), resolution=(640, 1136)))


    touch(Template(r"tpl1686298800555.png", record_pos=(0.383, 0.786), resolution=(640, 1136)))
    for aa in range(15):
        swipe([500,555],[160,555])
        print('第'+str(aa)+'次滑动')
        sleep(1)
        
    sleep(5)
    wait(Template(r"tpl1686540387817.png", record_pos=(0.0, 0.22), resolution=(640, 1136)))

    touch(Template(r"tpl1686540387817.png", record_pos=(0.0, 0.22), resolution=(640, 1136)))
    print("听绘本环节正常，计划ID："+str(user_plan_id))
      
    
    touch(Template(r"tpl1686540401605.png", record_pos=(0.013, 0.286), resolution=(640, 1136)))

    #学单词环节
    for ii in range(15):
        swipe([500,555],[160,555])
        print('第'+str(ii)+'次滑动')
    
    
    
    touch(Template(r"tpl1686540581327.png", record_pos=(-0.002, 0.752), resolution=(640, 1136)))
    sleep(2)
    touch(Template(r"tpl1686540581327.png", record_pos=(-0.002, 0.752), resolution=(640, 1136)))
    
    wait(Template(r"tpl1686540624381.png", record_pos=(-0.003, 0.222), resolution=(640, 1136)))
    print("读单词环节正常，计划ID："+str(user_plan_id))
    
    touch(Template(r"tpl1686540634956.png", record_pos=(0.0, 0.291), resolution=(640, 1136)))
    #读绘本环节
    
    try:
        for i in range(20):
            swipe([500,555],[160,555])
            print('第'+str(i)+'次滑动')
            sleep(1)

        

        touch(Template(r"tpl1686540880654.png", record_pos=(0.002, 0.744), resolution=(640, 1136)))
        sleep(2)
        touch(Template(r"tpl1686540880654.png", record_pos=(0.002, 0.744), resolution=(640, 1136)))
        
        
        wait(Template(r"tpl1686540974726.png", record_pos=(0.017, 0.772), resolution=(640, 1136)))
        
        finish_audio()
        print("读绘本环节正常，计划ID："+str(user_plan_id))
        
        touch(Template(r"tpl1686540980411.png", record_pos=(0.017, 0.781), resolution=(640, 1136)))
        
        
        wait(Template(r"tpl1686541126637.png", record_pos=(0.327, -0.584), resolution=(640, 1136)))
        
        touch(Template(r"tpl1686541138124.png", record_pos=(0.334, -0.584), resolution=(640, 1136)))
        sleep(1)
        user_plan_id+=1
        RazNum+=1

    except:
        errorlist.append(user_plan_id)
        errorback()
    
         
        user_plan_id+=1
        RazNum+=1
    

#     user_plan_id+=1
#     RazNum+=1
       
                


        
    
        
        

      


