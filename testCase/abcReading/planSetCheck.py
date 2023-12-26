import requests
from common.abcSign import getSignEnd
from common.abcReqHeader import abcBaseUrl

enverment='dev'
abcBaseUrl=abcBaseUrl(enverment)

def setPlan(uid:int,uuid:str,token:str,cid:int):
    header = {'PANDA-TOKEN': token, 'PANDA-UID': uuid}
    url=abcBaseUrl+'/v5/study/set-read-plan'
    data={
            "book_nums": 2,
            "cid": cid,
            "uid": uid,
            "year": 1
        }
    dataend=getSignEnd(data,enverment)
    req=requests.post(url=url,json=dataend,headers=header)
    return req.json()['code']


if __name__ == '__main__':
    errorlist=[]

    uid=63439
    uuid='63439'
    token='658a76f1ed3ca'


    for cid in range(3,30):
        code=setPlan(uid,uuid,token,cid)
        print(code)
        if code=='200':
            print('等级%d定级成功！' %cid)
        else:
            print('等级%d定级失败！' %cid)
            errorlist.append(cid)
    print(errorlist)