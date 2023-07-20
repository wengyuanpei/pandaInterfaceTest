import requests

from common.excelreadwrite import *
from common.finish_plan_urlenverment import *





def check_video(char_id):
    baseurl=urlenverment(3)
    url=baseurl+'v1/record/char-info'
    header={'Authorization':'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjQwOTc2ODgyODYyOTg1MjE3Iiwic3ViIjoie1wiaWRcIjoxNjQwOTc2ODgyODYyOTg1MjE3LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTcwNTI4OTMyMH0.hGicZajQBFUEyNyS0dqgTYFRUSr0YcALP6xQCdeLijLWmB7Xbj2aXVgUM3ngWAEoG8A_UGg9LC0wiVnZbytOlQ'}
    data={"char_id":char_id,"uid":1640976882862985217}

    req=requests.post(url=url,headers=header,json=data)
    return req.json()


if __name__ == '__main__':
    # errorlist=[]
    # file = r'C:\Users\zhang\Desktop\汉字ID.xlsx'
    # list = excel_read(file, 'A1:A120')
    # for char_id in list:
    #     req=check_video(char_id)['data']['chineseCharacterVideoRelationDtoList']
    #
    #     # print(req)
    #     if req == {} or req ==[] or req =='':
    #         errorlist.append(char_id)
    #         print('添加至错误名单！')
    #     else:
    #         print(char_id,'\n',req)
    #
    # print(errorlist)

    list=[13, 3, 85, 158, 246, 149, 129, 147, 352, 154, 166, 368, 71, 192, 217, 1, 99, 153, 59, 327, 297, 68, 985, 224, 351, 453, 387, 162, 49, 218, 222, 396, 682, 55, 28, 322, 115, 78, 277, 331, 79, 91, 238, 455, 148, 263]
    errorlist=[]

    for char_id in list:
        req=check_video(char_id)['data']['videoUrl']
        print(req)

        if req=='':
            errorlist.append(char_id)
            print('添加至错误名单！')
        else:
            print(req)
    print(errorlist)
    list1=[985, 682, 55]