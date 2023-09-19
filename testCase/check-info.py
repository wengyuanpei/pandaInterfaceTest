#coding:utf-8
from common.finish_plan_urlenverment import *
from common.excelreadwrite import *
from time import *


def get_video_info(v_id):
    baseurl = urlenverment(3)
    url = baseurl + 'v1/media/video/' + str(v_id)
    heder = {'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjk5NzEwMDQ1OTY1MDcwMzM3Iiwic3ViIjoie1wiaWRcIjoxNjk5NzEwMDQ1OTY1MDcwMzM3LFwibW9iaWxlXCI6XCIrODYxODM4NDI1MzUwNlwifSIsImV4cCI6MTcwOTYyOTQyOH0.y39gNrr7xY3aA5PLxHYMV6Q2jnYYtJBeGlM5m7iJegjPV4wG8V-kj7cbL0B8IacqpiAzeXUY16CQpsc2JRHmmg'}
    v_info=requests.get(url=url,headers=heder)
    vinfocheck=v_info.json()['data']['urls']
    print('音频连接后缀检查~~~~~>',vinfocheck)
    return vinfocheck


def get_audio_info(a_id):
    baseurl = urlenverment(3)
    url = baseurl + 'v1/media/audio/' + str(a_id)
    heder = {'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjk5NzEwMDQ1OTY1MDcwMzM3Iiwic3ViIjoie1wiaWRcIjoxNjk5NzEwMDQ1OTY1MDcwMzM3LFwibW9iaWxlXCI6XCIrODYxODM4NDI1MzUwNlwifSIsImV4cCI6MTcwOTYyOTQyOH0.y39gNrr7xY3aA5PLxHYMV6Q2jnYYtJBeGlM5m7iJegjPV4wG8V-kj7cbL0B8IacqpiAzeXUY16CQpsc2JRHmmg'}
    v_info=requests.get(url=url,headers=heder)
    ainfocheck=v_info.json()['data']['urls']
    print('视频信息~~~~~>',ainfocheck)
    return ainfocheck


if __name__ == '__main__':
    vid_path=r'C:\Users\zhang\Desktop\vids.xlsx'

    aid_path=r'C:\Users\zhang\Desktop\aids.xlsx'
    listvids=excel_read(vid_path,'A2:A225')
    listaids = excel_read(aid_path, 'A2:A3173')
    print(listvids)
    print(listaids)
    v_error_list=[]
    #视频
    for vid in listvids:
        try:
            vinfo=get_video_info(vid)
            sleep(1)
        except:
            v_error_list.append(vid)

    #音频
    a_error_list = []
    # 视频
    for aid in listvids:
        try:
            vinfo = get_audio_info(aid)
            sleep(1)
        except:
            a_error_list.append(aid)

    print('视频error',v_error_list)
    print('音频error', a_error_list)
