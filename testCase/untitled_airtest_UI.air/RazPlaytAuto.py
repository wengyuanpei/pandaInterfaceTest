# -*- encoding=utf8 -*-
__author__ = "zhang"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import requests
from time import sleep
import urllib3
http = urllib3.PoolManager()




# 循环执行绘本学习
user_plan_id=1190678

UID=1228221679737573378
header_live={"Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxMjI4MjIxNjc5NDAyMDI5MDU4Iiwic3ViIjoie1wiaWRcIjoxMjI4MjIxNjc5NDAyMDI5MDU4LFwibW9iaWxlXCI6XCIrODYxNjY2NjY2NjY2NlwifSIsImV4cCI6MTcwMTg1NjU4OH0.hQzQxeKM2jQegQNWo9Jn4K3dyQ2aIyLWFfkGMXJDtSzzugcZKrd9swFkGrtRxJGcoKVqqpe9_hG0e688nE9_ww"}


en_url="https://hear-dev.abctime/v1/study/finish-plan"

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
response =http.request('POST',en_url,body=data_2, headers=header_live)

# requests.post(url=en_url, headers=header_live, json=data_2)
print("计划id",user_plan_id,"上报音频完成")
finish_audio()
 
    
    

