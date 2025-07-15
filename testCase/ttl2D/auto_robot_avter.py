import time

from common.excelreadwrite import excel_read
import requests
def get_aventer():
    url="https://app-test.chuangjing.com/abc-api/preschool/community/get-robot-avatar"
    header={"ntu-token":"75dbebe13b44e82ec9cd7f7d3fc06d3d55e83f5243dda6c46f64d57ddefc1f6d1e62d34076733259dbde08c41f2a59090464b0018a2d3a6a4fcf1ade1ccff60c40fd066ad7a498e7d41e0c1a75ed079fac775b20fcf67714761036592b5d290cbf4bec92fea856753f2b1decf7607702c51fa385dc5a7913e7c28aec0769577ab83d0bdd9a9eafac93b5d4cd8cd8b75d053b24f6458d834f19c2e2120b8a8bc99e1befc732a0f474d89426215dbbc43880329f588d06d5bfdff43b0926af12e9b773a2f6853de3438801dcf08668f2a7"}
    body={"robot_num":8}
    req= requests.post(url=url,json=body,headers=header)
    aventerlist=[]
    j=req.json()['data']['list']
    for i in j:
        for ii in i['props_list']:
            # print(ii['code'])
            aventerlist.append(ii['code'])
    return aventerlist
def get_avter_config():
    station="A2:A193"
    excel_config=excel_read("avter.xlsx",station)
    return excel_config

if __name__ == '__main__':
    config=get_avter_config()
    while True:
        time.sleep(1)
        avter=get_aventer()
        for i in avter:
            if i not in config:
                print("i")
                break


