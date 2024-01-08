import requests

from common.abcSign import *
from common.abcReqHeader import abcBaseUrl


baseurl=abcBaseUrl('live')
enverment='live'
headerr={'PANDA-TOKEN':'658157e4934c0','PANDA-UID':'61050'}
def getOldReport(uid):
    url=baseurl+'/v5/study/get_report'
    header=headerr
    data={
        "uid": uid,
        "member_id": str(uid)}
    dataend=getSignEnd(data,enverment)
    req=requests.post(url=url,json=dataend,headers=header)

    return req.json()['data']['listen_book_num']


def getNueReport(uid):
    url = baseurl + '/v5/study/total_report?uid='+str(uid)
    header = headerr
    req = requests.get(url=url,  headers=header)
    return req.json()['data']['base']['book_num']


if __name__ == '__main__':
    uidlist=[16290218]
    errorlist=[]
    for uid in uidlist:
        oldNUm=getOldReport(uid)
        newNUM=getNueReport(uid)
        print('老版本阅读绘本数据%d,新版本阅读绘本数%d'%(oldNUm,newNUM))
        if oldNUm >newNUM:
            print('异常账号'+str(uid))
            errorlist.append(uid)
    print(errorlist)