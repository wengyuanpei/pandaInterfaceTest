from time import sleep

import requests

lecellist=[3,29]

def getbookidlist():


    url='https://hear-dev.abctime.com/v1/book/book-list'
    token='Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjA3MzMxNjI0MTQ4NDU1NDI2Iiwic3ViIjoie1wiaWRcIjoxNjA3MzMxNjI0MTQ4NDU1NDI2LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTcwMjg4MzQwM30.nT318ULonhQgcNA8kHuTiGrEKzbkj8ZPcSkc6atpFxKLgqs4dVjc73gh0apN-FN2R6Qph259uUnXraQtN_tSVg'
    header = {'Authorization':token}
    razbookidlist=[]
    for i in range(3,30):
        print('当前等级为%d,aa>>>z' % (i))
        data = {"current": 1, "lower_level": i, "size": 50, "uid": 1607331624148455426}
        req=requests.post(url=url,json=data,headers=header)
        for ii in range(len(req.json()["data"]["records"])):
            # print(req.json()["data"]["records"][ii]['id'])
            bookid=req.json()["data"]["records"][ii]['id']
            razbookidlist.append(bookid)
    return razbookidlist


def bookdetailmp3(id):
    errorlist=[]
    url='https://hear-dev.abctime.com/v1/book/book-detail'
    data={"book_id":id,"uid":1607331624148455426}
    token = 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjA3MzMxNjI0MTQ4NDU1NDI2Iiwic3ViIjoie1wiaWRcIjoxNjA3MzMxNjI0MTQ4NDU1NDI2LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTcwMjg4MzQwM30.nT318ULonhQgcNA8kHuTiGrEKzbkj8ZPcSkc6atpFxKLgqs4dVjc73gh0apN-FN2R6Qph259uUnXraQtN_tSVg'
    header = {'Authorization': token}
    reqbook=requests.post(url=url,json=data,headers=header)
    bookname=reqbook.json()['data']['pictureBookName']
    print('当前正在检查的绘本id为%d的绘本名称为%s' % (id,bookname))
    for i in range(len(reqbook.json()['data']['contentList'])):

        # print(reqbook.json()['data']['contentList'][i]['pageContentAudio'])
        mp3=reqbook.json()['data']['contentList'][i]['pageContentAudio']
        if len(mp3) <10:
            errorlist.append(id)
            continue

        else:
            print(reqbook.json()['data']['contentList'][i]['pageContentAudio'])
    return errorlist
    # print(errorlist)

if __name__ == '__main__':
    listid=getbookidlist()
    for id in listid:
        razerror=bookdetailmp3(id)
        print(razerror)
        sleep(2)



