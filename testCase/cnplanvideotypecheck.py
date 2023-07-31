# coding:utf-8
import requests
from common.finish_plan_urlenverment import *
from common.get_tlj_auth import *
from time import sleep
basurl=urlenverment(1)
authdev=getauth()[0]
# print(authdev)

def getvideoinfo(vid):
    url=basurl+'v1/media/video/'+str(vid)
    header={'Authorization':authdev}
    req=requests.get(url=url,headers=header)
    return req.json()


if __name__ == '__main__':
    listvideo=[15679]
    listplay=['FD','LD','SD','HD','OD','HQ',]
    videoinfolist=[]
    for vid in listvideo:
        info=getvideoinfo(vid)
        sleep(0.2)
        play_url=info['data']['urls']['playUrls']
        for i in range(len(play_url)):
            info_play=play_url[i]['definition']
            videoinfolist.append([vid,info_play])
            if info_play not in listplay:
                print('%d视频资源清晰异常，清晰度为：%s' %(vid,info_play))
            if info_play == 'OD':
                print('检查 OD 原画视频视频id为：%s' % vid)


    print(videoinfolist)
    path=r'C:\Users\zhang\Desktop\pandaInterfaceTest\result\responsetime.txt'
    with open(path, "a") as file:
        for iii in videoinfolist:
            file.write(str(iii))
            file.write('\n')

        file.close()

