# coding:utf-8
import  requests
from common.finish_plan_urlenverment import *

def aicheck(infoo):
    baseurl=urlenverment(1)
    url=baseurl+'v1/aigc/chat'

    header={'Authorization':'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjgxMTA3NjgwMTg0MzQwNDgxIiwic3ViIjoie1wiaWRcIjoxNjgxMTA3NjgwMTg0MzQwNDgxLFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTcwODg0OTcwMn0.65WwfziNOw89Cfr3fcjmkT-5w-95WHhN_VuhyaKBBOtV6I7dCSbEFtez2vhKSQhTCdlwM033PapBerLOikRQ2g',
            'Sn':'S1DEV003'}

    data={"content":infoo,"time":1693300995813,"type":6,"uid":1681107680184340481}

    requestss=requests.post(url=url,json=data,headers=header)
    return requestss.json()


if __name__ == '__main__':
    from common.excelreadwrite import *
    from time import sleep
    errorlist=[]
    mgckpath=r'C:\Users\zhang\Desktop\敏感词库\mgck.xlsx'
    mgcklist=excel_read(mgckpath,'A8853:A19339')
    a=8853
    for mgc in mgcklist:
        print('敏感词>>',mgc)

        print('第%d个敏感词！' %a)
        try:
            inff= aicheck(str(mgc))
            print(inff)
            sleep(0.5)
            if inff['code']=="4666" or '托托不太明白你在说什么' in inff['message'] :
                print('过滤成功')
            else:
                print('过滤失败')
                errorlist.append(mgc)
        except:
            sleep(30)
            inff = aicheck(mgc)
            print(inff)
            sleep(1)
            if inff['code'] == "4666" or '托托不太明白你在说什么' in inff['message']:
                print('过滤成功')
            else:
                print('过滤失败')
                errorlist.append(mgc)
        a += 1
    print('过滤失败列表',errorlist)