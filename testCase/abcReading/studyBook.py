
# 学习流上报绘本学习
import random
from time import sleep
import requests
from common.abcSign import *


def getBookIdChallengId(uidd:int,uuid,token:str,cid:int)->list:
    url='http://api-dev.abctime.com/v5/challenges/getChallengeListByCid'
    data={
        "ab_non_vip": 2,
        "cid": cid,
        "member_id": uidd
        }
    dataEND=getSignEnd(data)

    header = {'PANDA-TOKEN': token, 'PANDA-UID': uuid}

    req=requests.post(url=url,json=dataEND,headers=header).json()['data']['challenges']

    bookList=[]
    challengesList=[]
    # print(req)
    # print(type(req))
    for bookInfo in req:
        bookId=bookInfo['bookId']

        bookList.append(bookId)
        challengId=bookInfo['id']
        challengesList.append(challengId)

    return [bookList,challengesList]



def wordsRequestData(uidd:int,uuid:str,token:str,book_id)->list:

    header = {'PANDA-TOKEN': token, 'PANDA-UID': uuid}
    detailDat={
                "ab_non_vip": 2,
                "book_id": book_id,
                "scan": 0,
                "uid": uidd
            }
    detailData=getSignEnd(detailDat)
    url='http://api-dev.abctime.com/v5/book/detail'
    req=requests.post(url=url,headers=header,json=detailData).json()['data']['wordsList']
    # print(req)
    dictW=[]
    for widd in req:
        wid=widd['wordId']
        # print(wid)
        score=random.randint(50,100)
        dicttt={
                "score": score,
                "video_url": "",
                "words_id": 7727}
        dicttt['words_id']=wid
        # print(dicttt)
        dictW.append(dicttt)
    print('单词请求数据',dictW)
    return dictW




def reportBookLising(uidd:int,uuid,token:str,bookId):
    url = 'http://api-dev.abctime.com/v5/study/report_book'
    header = {'PANDA-TOKEN': token, 'PANDA-UID': uuid}
    data2={
        "coin_num": 0,
        "content_id": bookId,
        "cost_time": 0,
        "event_id": 9,
        "open_num": 0,
        "repair_date": 0,
        "score": 0,
        "true_num": 0,
        "uid": uidd,

            }
    dataEnd=getSignEnd(data2)

    code2 = requests.post(url=url, json=dataEnd, headers=header)
    print('上报听绘本：',code2.status_code)

def reportBookLisingDone(uidd:int,uuid:str,token:str,challenges_id):
    url = 'http://api-dev.abctime.com/v5/challenges/done'
    header = {'PANDA-TOKEN': token, 'PANDA-UID': uuid}
    data2 = {
            "again_coin": 5,
            "challenges_id": challenges_id,
            "content": "",
            "continue_true_num": 0,
            "cost_time": 16859,
            "extra": "{\"allCount\":0,\"correctCount\":0,\"currentCorrectCount\":0,\"maxCorrentCount\":0,\"maxScore\":0,\"openCount\":0}",
            "false_num": 0,
            "is_again": 'false',
            "proportion": 100,
            "repair_date": 0,
            "score": 0,
            "stage": -1,
            "stage_num": 1,
            "stage_type": 1,
            "true_num": 0,
            "true_proportion": 0,
            "uid": uidd,
            "video_urls": []}
    dataEnd = getSignEnd(data2)

    code2 = requests.post(url=url, json=dataEnd, headers=header)
    print('上报听绘本Done：',code2.status_code)


'''
单词学习上报
'''
def reportWords(uidd:int,uuid,token:str,bookId):
    wordData=wordsRequestData(uidd, uuid, token,bookId)
    url='http://api-dev.abctime.com/v5/study/report_words'
    data={
            "book_id": bookId,
            "cost_time": 1,
            "uid": uidd,
            "words_list": wordData}
    dataEnd=getSignEnd(data)
    header = {'PANDA-TOKEN': token, 'PANDA-UID': uuid}
    rep=requests.post(url=url,json=dataEnd,headers=header)
    print('单词上报',rep.status_code)


def reportBookread(uidd:int,uuid:str,token:str,bookId:int):
    url = 'http://api-dev.abctime.com/v5/study/report_book'
    header = {'PANDA-TOKEN': token, 'PANDA-UID': uuid}
    data2 = {

            "content_id": bookId,
            "cost_time": 28730,
            "event_id": 10,
            "open_num": 4,
            "score": 49,
            "score_list": [43, 54, 41, 57],
            "uid": uidd,
            "video_urls": ["oss_audio_135_1701767890776.wav", "oss_audio_135_1701767890784.wav", "oss_audio_135_1701767890785.wav", "oss_audio_135_1701767890786.wav"]
        }

    dataEnd = getSignEnd(data2)

    code2 = requests.post(url=url, json=dataEnd, headers=header)
    print('上报读绘本：',code2.status_code)


if __name__ == '__main__':

    uidd = 135
    uuid = '135'
    token = '656ee831ec8ef'
    cid = 8  #abc 绘本等级字段


    dataInfo=getBookIdChallengId(uidd,uuid,token,cid)
    bookId=dataInfo[0]
    challendid = dataInfo[1]
    times=1
    for bookId,challendid in zip(bookId,challendid):
        if bookId!=0:
            print('##################################上报第%d本绘本##############################' %times)
            print('上报绘本id:',bookId,'关卡id:',challendid)
            sleep(1)
            #上报绘本听
            reportBookLising(uidd, uuid, token, bookId)
            reportBookLisingDone(uidd,uuid,token,challendid)
            sleep(1)
            #上报单词读
            reportWords(uidd, uuid, token, bookId)
            sleep(1)
            #绘本跟读
            reportBookread(uidd, uuid, token, bookId)

            times+=1


    print('##########################用户%d等级%d,学习流完成学习！！！###############################' %(uidd,cid))
