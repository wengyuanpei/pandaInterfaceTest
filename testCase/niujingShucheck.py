import requests
from time import *

header={"Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNTYyNjI5MDYwMDc1MTAyMjA5Iiwic3ViIjoie1wiaWRcIjoxNTYyNjI5MDYwMDc1MTAyMjA5LFwibW9iaWxlXCI6XCIrODYxODM4NDI1MzUwNlwifSIsImV4cCI6MTcwMTY3NzU1M30.ByAdhAfbxwS5tTbkbSJIPJXN6bIrzoOjeWMwn6JA8pimm2v1fMTXVJfdXloqInXPY_FsTlc7ZPDwxlCGtFqQ5Q",
        "User-Uid":"1562629060075102209",
        "Kid-Uid":"1562629060075102209"}


dataList={"resource_id":24,"uid":1562629060075102209}

listUrl='https://hear-pre.abctime.com/v1/record/lesson/list'

listreq=requests.post(url=listUrl,json=dataList,headers=header)
level=1
errorlist = []
for lesson_list_num in range(len(listreq.json()['data']['lesson_list'])):

    # print(listreq.json()['data']['lesson_list'][lesson_list_num]['medias_obj']['audio'])

    for audioID in listreq.json()['data']['lesson_list'][lesson_list_num]['medias_obj']['audio']:

        getAudioInfoUrl='https://hear-pre.abctime.com/v1/media/audio/'+str(audioID)

        getAudioInfo=requests.get(headers=header,url=getAudioInfoUrl)
        # 歌词文件
        print(getAudioInfo.json()['data']['subtitleFileUrl'])
        #secondaryFileUrl
        print(getAudioInfo.json()['data']['secondaryFileUrl'])
        name=getAudioInfo.json()['data']['name']
        sleep(1)
        try:
            if getAudioInfo.json()['data']['subtitleText'] ==None or getAudioInfo.json()['data']['secondaryFileUrl'] ==None:
                errorlist.append([level,audioID,name])
                print('等级',level,'音频id：',audioID,'功能异常！！')
            else:
                print('等级', level, '音频id：', audioID, 'OK！！')
        except:
            print('等级', level, '音频id：', audioID, '音频异常！！')
    level += 1


print(errorlist)