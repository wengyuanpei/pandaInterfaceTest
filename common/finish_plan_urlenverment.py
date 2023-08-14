import requests


def urlenverment(inta):
    if inta == 1:
        print('dev环境！')
        return 'https://hear-dev.abctime.com/'
    elif inta == 2:
        print('pre环境！')
        return 'https://hear-pre.abctime.com/'
    elif inta == 3:
        print('prod环境！')
        return 'https://hear.abctime.com/'
    else:
        print('地址错误仅支持1（dev）/2（pre）/3(prod),请检查环境地址参数！')


def finish_plan(planid, urlbase, header, uid, event_id):
    data = {
        "uid": uid,
        "user_plan_id": planid,
        "event_id": event_id  # 1 RAZ,2 磨耳朵 710版本默认完成

    }
    url = urlbase + 'v1/study/finish-plan'

    response = requests.post(url=url, json=data, headers=header)

    print('ID：%s计划完成！' % (str(planid)))





if __name__ == '__main__':
    bse=urlenverment(3)
    heder={'Authorization':'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjQwOTc2ODgyODYyOTg1MjE3Iiwic3ViIjoie1wiaWRcIjoxNjQwOTc2ODgyODYyOTg1MjE3LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTcwNzI5OTQwNH0.AVC4vgok2cQ8Ni9za3Najs-1mk9pOxuCUY6YYvgk5V5xlDlHRGPSOdbZECKS5HKV6vIwfpz-C5G6_-2iYsDLyg'}
    finish_plan(24977310,bse,heder,1640976882862985217,1)
