import requests
from time import sleep


dev_get_video_id_url='https://hear-dev.abctime.com/v1/record/lesson/list'

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
print(requestss.json())

# print(requestss.json()["data"]['lesson_list'][0]['medias_obj']['audio'])
l1_video_id_list=requestss.json()["data"]['lesson_list'][0]['medias_obj']['audio']
# print("l1_video_id_list",requestss.json()["data"]['lesson_list'][1]['medias_obj']['audio'])
l2_video_id_list=requestss.json()["data"]['lesson_list'][1]['medias_obj']['audio']
# print("l2_video_id_list",requestss.json()["data"]['lesson_list'][2]['medias_obj']['audio'])
l3_video_id_list=requestss.json()["data"]['lesson_list'][2]['medias_obj']['audio']
# print("l3_video_id_list",requestss.json()["data"]['lesson_list'][3]['medias_obj']['audio'])
l4_video_id_list=requestss.json()["data"]['lesson_list'][3]['medias_obj']['audio']
# print("l4_video_id_list",requestss.json()["data"]['lesson_list'][4]['medias_obj']['audio'])
l5_video_id_list=requestss.json()["data"]['lesson_list'][4]['medias_obj']['audio']
# print("l5_video_id_list",requestss.json()["data"]['lesson_list'][5]['medias_obj']['audio'])
l6_video_id_list=requestss.json()["data"]['lesson_list'][5]['medias_obj']['audio']
# print("l6_video_id_list",requestss.json()["data"]['lesson_list'][5]['medias_obj']['audio'])
list=[l1_video_id_list,l2_video_id_list,l3_video_id_list,l4_video_id_list,l5_video_id_list,l6_video_id_list]

def HS_methd(req_sub_2):
    #传入请求统计行数（去除空行）
    txt = req_sub_2.text.splitlines(True)
    HS = len([l for l in txt if l.strip(' \n') != ''])
    return HS

#id错误list
wrong_list=[]
#文件错误list
error_list=[]
#播放地址空
play_list_error=[]
#遍历音频
for list_id in list:
    for L1video_id in list_id:

        dev_get_video_info1=dev_get_video_info+str(L1video_id)

        req_get_video_info=requests.get(url=dev_get_video_info1,headers=header)

        # print("音频id:",L1video_id,'音频地址',req_get_video_info.json()['data']['urls']['playUrls'][0]['playUrl'])
        #音频地址
        try:
            play_url=req_get_video_info.json()['data']['urls']['playUrls'][0]['playUrl']
            if play_url=="":
                play_list_error.append(L1video_id)
                print('播放地址空',L1video_id)



            # 音频英文字幕
            subtitleFileUrl_video=req_get_video_info.json()['data']['subtitleFileUrl']
            req_sub_1=requests.get(subtitleFileUrl_video)
            # print('音频英文字幕',req_sub_1)
            #计算行数
            txt_hs1 = HS_methd(req_sub_1)
            print('音频英文字幕', req_sub_1.text,"行数：",txt_hs1)



            #音频中文字幕
            secondaryFileUrl_video=req_get_video_info.json()['data']['secondaryFileUrl']
            req_sub_2 = requests.get(secondaryFileUrl_video)
            # 计算行数
            txt_hs2=HS_methd(req_sub_2)
            print('音频中文字幕', req_sub_2.text, "行数：", txt_hs2)

            if txt_hs2==txt_hs1:
                print(L1video_id,"音频通过")
            else:
                error_list.append(L1video_id)
                print(L1video_id, "音频不通过")


        except:
            wrong_list.append(L1video_id)
            print(L1video_id,"id请求错误需要检查")
print('id错误list',wrong_list)
print('字幕错误错误list',error_list)
print('播放地址空',play_list_error)








