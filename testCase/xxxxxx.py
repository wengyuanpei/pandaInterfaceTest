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


if __name__ == '__main__':
    aa= get_package_videoinfo(108)
    print(aa)