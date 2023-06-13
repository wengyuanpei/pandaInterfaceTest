import requests
from time import *

header={"Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNTYyNjI5MDYwMDc1MTAyMjA5Iiwic3ViIjoie1wiaWRcIjoxNTYyNjI5MDYwMDc1MTAyMjA5LFwibW9iaWxlXCI6XCIrODYxODM4NDI1MzUwNlwifSIsImV4cCI6MTcwMTY3NzU1M30.ByAdhAfbxwS5tTbkbSJIPJXN6bIrzoOjeWMwn6JA8pimm2v1fMTXVJfdXloqInXPY_FsTlc7ZPDwxlCGtFqQ5Q",
        "User-Uid":"1562629060075102209",
        "Kid-Uid":"1562629060075102209"}


dataList={"resource_id":24,"uid":1562629060075102209}

listUrl='https://hear-pre.abctime.com/v1/record/lesson/list'

listreq=requests.post(url=listUrl,json=dataList,headers=header)
print(listreq.json())
level=1
#没有返回字幕地址
errorlist = []
#字幕地址包含特殊字符无法解析
wronglist=[]
for lesson_list_num in range(len(listreq.json()['data']['lesson_list'])):

    # print(listreq.json()['data']['lesson_list'][lesson_list_num]['medias_obj']['audio'])
    print(lesson_list_num)

    for audioID in listreq.json()['data']['lesson_list'][lesson_list_num]['medias_obj']['audio']:
        print(audioID)
        getAudioInfoUrl='https://hear-pre.abctime.com/v1/media/audio/'+str(audioID)
        # print(getAudioInfoUrl)
        getAudioInfo=requests.get(headers=header,url=getAudioInfoUrl)
        # 歌词文件
        lrcEN=getAudioInfo.json()['data']['subtitleFileUrl']
        # print(getAudioInfo.json()['data']['subtitleFileUrl'])
        #secondaryFileUrl
        lrcCN=getAudioInfo.json()['data']['secondaryFileUrl']
        # print(getAudioInfo.json()['data']['secondaryFileUrl'])
        name=getAudioInfo.json()['data']['name']
        sleep(1)
        listStr=['!','@','#','&','%']

        for i in listStr:

            lrcCNfind1=str(lrcCN).find(i)
            lrcCNfind11 = str(lrcEN).find(i)
            if lrcCNfind1==0 or lrcCNfind11==0:
                wronglist.append([level,audioID,name])
                print('字幕地址包含特殊字符无法解析',lrcCNfind1)
                print('字幕地址包含特殊字符无法解析',lrcCNfind11)

        try:
            if str(lrcCN) == "" or str(lrcEN) == "" :
                errorlist.append([level,audioID,name])
                print('等级',level,'音频id：',audioID,'缺失链接字幕异常！！')
            else:
                print('等级', level, '音频id：', audioID, '链接OK！！')
        except:
            print('等级', level, '音频id：', audioID, '音频链接地址返回异常！！')
    level += 1


print('没有返回字幕地址',errorlist)
print('字幕地址包含特殊字符无法解析',wronglist)