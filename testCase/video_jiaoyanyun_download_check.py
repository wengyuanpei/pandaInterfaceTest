# -*- coding: gbk -*-
import requests
from common.finish_plan_urlenverment import *

baseurl=urlenverment(3)
header={'Authorization':'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjQwOTc2ODgyODYyOTg1MjE3Iiwic3ViIjoie1wiaWRcIjoxNjQwOTc2ODgyODYyOTg1MjE3LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTcwNTQ1NjUxMn0.D5DSiRlELtggp1etr_0h4uBHpMvOZeNw9llo2s1_2AZKvSMsFEvcmtfvIZXiAxHwebprodmQMojDg5GCujzjOw'}

def get_video_url(video_id):
    url=baseurl+'v1/media/video/'+str(video_id)
    req=requests.get(url=url,headers=header)
    video_url=req.json()["data"]['urls']['playUrls'][0]['playUrl']
    return video_url


def download_video(download_url):
    req=requests.get(download_url)
    # print(req.content)
    return req


def check_video(vid):

    urll=get_video_url(vid)
    dataa=str(download_video(urll).content)

    if 'IV=0x000000000000000000000000000' in dataa[131:277]:
        print(dataa[132:277])
        print('OK视频')
        oklist=[]
        oklist.append(vid)
        return oklist
    else:
        end_1=dataa[130:]
        end_2=end_1.split('"\\n')[0]
        print(end_2)
        errorlist=[]
        errorlist.append(vid)
        print('错误视频')
        return errorlist

        # print(end_2[5:9])
        #
        # if end_2[5:9] != 'http':
        #     end_3=end_2[:5]+'http:'+end_2[5:]
        #     print(end_3)
        #     end_4=end_3[5:]
        #     print(end_4)
        #     end_doen=download_video(end_4)
        #     print(end_doen)
        #
        #     if str(type(end_doen)) != 'str':
        #         print('不能播放')
        # if end_2[5:9] == 'http':
        #     end_doen = download_video(end_2[5:])
        #     print(end_doen)
        #
        #     if str(type(end_doen.content)) != 'str':
        #         print('不能播放')
        #
        # if end_2[5:9] == 'http':
        #     end_doen = download_video(end_2[5:])
        #     print(end_doen.content)
        #
        #     if str(type(end_doen)) == 'str':
        #         print('能播放')


if __name__ == '__main__':

    list=[10138,2158]
    for id in list:
        erlist=check_video(id)
        print(erlist)