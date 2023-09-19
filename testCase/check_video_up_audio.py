#coding:utf-8
from common.finish_plan_urlenverment import *
import json
from common.excelreadwrite import *
from time import *
baseurl=urlenverment(3)

def get_package_videoinfo(package_id):
    baseurl = urlenverment(3)
    url=baseurl+'v1/lesson/'+str(package_id)
    heder={'Authorization':'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjk5NzEwMDQ1OTY1MDcwMzM3Iiwic3ViIjoie1wiaWRcIjoxNjk5NzEwMDQ1OTY1MDcwMzM3LFwibW9iaWxlXCI6XCIrODYxODM4NDI1MzUwNlwifSIsImV4cCI6MTcwOTYyOTQyOH0.y39gNrr7xY3aA5PLxHYMV6Q2jnYYtJBeGlM5m7iJegjPV4wG8V-kj7cbL0B8IacqpiAzeXUY16CQpsc2JRHmmg'}
    get_video=requests.get(url=url,headers=heder)
    # print(get_video.json()['data'])
    get_video_info=get_video.json()['data']['medias']
    get_video_info1=eval(get_video_info)
    #判断音视频
    check=get_video_info1.keys()
    # print(check)
    if 'video' in check:

        get_video_info=json.loads(get_video_info)

        return get_video_info['video']
    else:
        print(package_id,'音频课包！')
        return 'audio'

def get_video_info(v_id):
    baseurl = urlenverment(3)
    url = baseurl + 'v1/media/video/' + str(v_id)
    heder = {'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjk5NzEwMDQ1OTY1MDcwMzM3Iiwic3ViIjoie1wiaWRcIjoxNjk5NzEwMDQ1OTY1MDcwMzM3LFwibW9iaWxlXCI6XCIrODYxODM4NDI1MzUwNlwifSIsImV4cCI6MTcwOTYyOTQyOH0.y39gNrr7xY3aA5PLxHYMV6Q2jnYYtJBeGlM5m7iJegjPV4wG8V-kj7cbL0B8IacqpiAzeXUY16CQpsc2JRHmmg'}
    v_info=requests.get(url=url,headers=heder)
    mp3check=v_info.json()['data']['urls']['playUrls'][-1]['playUrl'][-3:]
    print('音频连接后缀检查~~~~~>',mp3check)
    return mp3check


if __name__ == '__main__':
    excel=r'C:\Users\zhang\Desktop\id.xlsx'
    idlist=excel_read(excel,'A1:A388')
    print(idlist)
    # idlist=[108]
    errorlist=[]
    audio_package=[]
    xxx=[]
    for id in idlist:
            vids=get_package_videoinfo(id)
            try:
                if vids !='audio':
                    sleep(1)
                    for vid in vids:

                            mp3check=get_video_info(vid)
                            sleep(1)
                            print('正在检查课包id为%d，视频id为%d！' %(id,vid))
                            if mp3check!='mp3' or mp3check!='MP3' or mp3check!='Mp3' or mp3check!='mP3':
                                 errorlist.append([id,vid])


                else:
                    audio_package.append(id)
            except:
                xxx.append(id)

    print('视频无法转音频',errorlist)
    print('音频课包',audio_package)
    print(xxx)