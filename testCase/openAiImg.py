import json
encoding='utf-8'
from common.get_tlj_auth import *



def creatImg():
    url='https://hear-dev.abctime.com/v1/aigc/chat'
    auth=getauth(13800000001)[1]
    print(auth)
    header={'Authorization':auth,'Sn':"S1DEV003",'Content-Type':'application/json'}


    date={'content':"动物",'type':"3","uid":"1681107680184340481",'time':"1693300995813"}
    req=requests.post(url,headers=header,json=date)

    return req


if __name__ == '__main__':
    back=creatImg()
    print(back.json())
