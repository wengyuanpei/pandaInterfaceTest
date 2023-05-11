import requests
from time import sleep


dev_get_video_id_url=' https://hear-dev.abctime.com/v1/record/lesson/list'

dev_get_video_info='https://hear-dev.abctime.com/v1/media/audio/'

Uid="1547454324283875329"
Kid="1547454324283875329"
uid=1547454324283875329
header={"Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNTQ3NDU0MzI0MjgzODc1MzI5Iiwic3ViIjoie1wiaWRcIjoxNTQ3NDU0MzI0MjgzODc1MzI5LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NlwifSIsImV4cCI6MTY5OTMyNTc0OH0.E6hvhq2MCrptPgw6xX5zyuGqkbm4BQhVeHaUAMvbPCqlIwBEBpc0MQwqd94G3BURAiZQPw6MYvizssuP-EhmAQ",
        "User-Uid":Uid,
        "Kid-Uid":Kid }
post_data={"resource_id":24,"uid":uid}

#获取音频信息
requestss=requests.post(url=dev_get_video_id_url,json=post_data,headers=header)
print(requestss.json()["data"]['lesson_list'][0]['medias_obj']['audio'])
print(requestss.json()["data"]['lesson_list'][1]['medias_obj']['audio'])
print(requestss.json()["data"]['lesson_list'][2]['medias_obj']['audio'])
print(requestss.json()["data"]['lesson_list'][3]['medias_obj']['audio'])
print(requestss.json()["data"]['lesson_list'][4]['medias_obj']['audio'])
print(requestss.json()["data"]['lesson_list'][5]['medias_obj']['audio'])

