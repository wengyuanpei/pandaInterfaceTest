import requests
from time import sleep
from common.abcSign import *
from common.abcReqHeader import *




enverment='dev'
baseurl=abcBaseUrl("dev")

def get_bool_list(uuid:str,uid:int,token:str):
    url=baseurl+'/v5/book/list'
    header = {'PANDA-TOKEN': token, 'PANDA-UID': uuid}
    data={
            "ab_non_vip": 2,
            "book_name": "",
            "favourite": 0,
            "sort": 0,
            "status": 0,
            "uid": uid
        }
    dataend=getSignEnd(data,enverment)
    req=requests.post(url=url,json=dataend,headers=header).json()['data']['list']
    booklist=[]

    for bookjs in req:
        bookid=bookjs['id']
        booklist.append(bookid)
    return booklist

def get_book_detaile(uuid:str,uid:int,token:str,bookid:int):
    url = baseurl + '/v5/book/detail'
    header = {'PANDA-TOKEN': token, 'PANDA-UID': uuid}
    data = {
            "ab_non_vip": 2,
            "book_id": bookid,
            "scan": 0,
            "uid": uid
        }
    dataend = getSignEnd(data, enverment)
    req = requests.post(url=url, json=dataend, headers=header).json()

    return req


if __name__ == '__main__':
    uuid='60642'
    uid=60642
    token='6577cd6db48b7'
    listt=get_bool_list(uuid,uid,token)
    print(listt)
    errorlist=[]
    for bookid in listt:
        sleep(1)
        req=get_book_detaile(uuid, uid, token, bookid)
        if req['data']['id'] != "":
            print('详情获取成功！')
        else:
            print('详情获取失败！')
            errorlist.append(bookid)
    print(errorlist)