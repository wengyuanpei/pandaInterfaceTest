
# 学习流上报绘本学习
import random
from time import sleep
import requests
from common.abcSign import *
from  common.abcReqHeader import *

enverment='dev'
baseurl=abcBaseUrl(enverment)



def getBookIdChallengId(uidd:int,uuid,token:str,cid:int)->list:
    url=baseurl+'/v5/challenges/getChallengeListByCid'
    data={
        "ab_non_vip": 2,
        "cid": cid,
        "member_id": uidd
        }
    dataEND=getSignEnd(data,enverment)

    # header = {'PANDA-TOKEN': token, 'PANDA-UID': uuid,'versionCode':'360'}
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
    ###################################################################################
    # header = {'PANDA-TOKEN': token, 'PANDA-UID': uuid,'versionCode':'360'}
    header = {'PANDA-TOKEN': token, 'PANDA-UID': uuid}
    ####################################################################################
    detailDat={
                "ab_non_vip": 2,
                "book_id": book_id,
                "scan": 0,
                "uid": uidd
            }
    detailData=getSignEnd(detailDat,enverment)
    url=baseurl+'/v5/book/detail'
    req=requests.post(url=url,headers=header,json=detailData).json()['data']['wordsList']
    # print(req)
    dictW=[]
    for widd in req:
        wid=widd['wordId']
        # print(wid)
        score=random.randint(50,100)
        dicttt= {"score": score,"video_url": "","words_id": 7727}
        dicttt['words_id']=wid
        # print(dicttt)
        dictW.append(dicttt)
    # print('单词请求数据',dictW)
    return dictW




def reportBookLising(uidd:int,uuid,token:str,bookId):
    url =baseurl+ '/v5/study/report_book'
    ###################################################################################
    # header = {'PANDA-TOKEN': token, 'PANDA-UID': uuid,'versionCode':'360'}
    header = {'PANDA-TOKEN': token, 'PANDA-UID': uuid}
    ###################################################################################
    data2={
            "content_id": bookId,
            "cost_time": 10513,
            "event_id": 9,
            "uid": uidd

        }
    dataEnd=getSignEnd(data2,enverment)

    code2 = requests.post(url=url, json=dataEnd, headers=header)
    print('上报听绘本：',code2.status_code)

def reportBookLisingDone(uidd:int,uuid:str,token:str,challenges_id):
    url = baseurl+'/v5/challenges/done'
    ###################################################################################
    # header = {'PANDA-TOKEN': token, 'PANDA-UID': uuid,'versionCode':'360'}
    header = {'PANDA-TOKEN': token, 'PANDA-UID': uuid}
    ###################################################################################
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
    dataEnd = getSignEnd(data2,enverment)

    code2 = requests.post(url=url, json=dataEnd, headers=header)
    print('上报听绘本Done：',code2.status_code)


'''
单词学习上报
'''
def giveChallegeAad(uidd:int,uuid:str,token:str,challenges_id):
    url=baseurl+'/v5/challenges/give_challenges_award'
    ###################################################################################
    # header = {'PANDA-TOKEN': token, 'PANDA-UID': uuid,'versionCode':'360'}
    header = {'PANDA-TOKEN': token, 'PANDA-UID': uuid}
    ###################################################################################
    data={
            "uid": uidd,
            "challenge_id": challenges_id,
            "score": 5
        }
    dataend=getSignEnd(data,enverment)
    req=requests.post(url=url,json=dataend,headers=header)
    print('单词上报', req.status_code)
def reportWords(uidd:int,uuid,token:str,bookId):
    wordData=wordsRequestData(uidd, uuid, token,bookId)
    ###################################################################################
    # header = {'PANDA-TOKEN': token, 'PANDA-UID': uuid,'versionCode':'360'}
    header = {'PANDA-TOKEN': token, 'PANDA-UID': uuid}
    ###################################################################################
    url=baseurl+'/v5/study/report_words'
    data={
            "book_id": bookId,
            "cost_time": 1,
            "uid": uidd,
            "words_list": wordData}
    dataEnd=getSignEnd(data,enverment)




    rep=requests.post(url=url,json=dataEnd,headers=header)
    print('单词上报',rep.status_code)

def reportBookreadDone(uidd:int,uuid:str,token:str,challenges_id):
    url = baseurl + '/v5/challenges/done'
    ###################################################################################
    # header = {'PANDA-TOKEN': token, 'PANDA-UID': uuid,'versionCode':'360'}
    header = {'PANDA-TOKEN': token, 'PANDA-UID': uuid}
    ###################################################################################
    data={
            "again_coin": 5,
            "challenges_id": challenges_id,
            "content": "",
            "continue_true_num": 7,
            "cost_time": 271031,
            "extra": "{\"allCount\":0,\"correctCount\":0,\"currentCorrectCount\":2,\"maxCorrentCount\":7,\"maxScore\":100,\"openCount\":19}",
            "false_num": 3,
            "is_again": 'false',
            "proportion": 66,
            "repair_date": 0,
            "score": 93,
            "stage": 2,
            "stage_num": 3,
            "stage_type": 2,
            "total_num": 16,
            "true_num": 13,
            "true_proportion": 81,
            "uid": uidd,
            "video_urls": ["oss_audio_136_1702887655049.wav", "oss_audio_136_1702887655056.wav", "oss_audio_136_1702887655057.wav", "oss_audio_136_1702887655058.wav", "oss_audio_136_1702887655059.wav", "oss_audio_136_1702887655060.wav", "oss_audio_136_1702887655061.wav", "oss_audio_136_1702887655062.wav"],
            "sign": "519f8d0f308b7dd2f8f45e3c645d75768d4866b1710a66ba8939bcf9405caa4a"
        }
    dataend=getSignEnd(data,enverment)
    req=requests.post(url=url,json=dataend,headers=header)
    print('上报读绘本：',req.status_code)

def reportBookread(uidd:int,uuid:str,token:str,bookId:int):
    url = baseurl+'/v5/study/report_book'
    ###################################################################################
    # header = {'PANDA-TOKEN': token, 'PANDA-UID': uuid,'versionCode':'360'}
    header = {'PANDA-TOKEN': token, 'PANDA-UID': uuid}
    ###################################################################################
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

    dataEnd = getSignEnd(data2,enverment)

    code2 = requests.post(url=url, json=dataEnd, headers=header)
    print('上报读绘本：',code2.status_code)


if __name__ == '__main__':

    uidd = 63330
    uuid = '63330 '
    token = '658544bfa4fb3'
    # abc 绘本等级字段
    cid = 4


    dataInfo=getBookIdChallengId(uidd,uuid,token,cid)
    bookId=dataInfo[0]
    challendid = dataInfo[1]
    times=1
    for bookId,challendid in zip(bookId,challendid):
        if bookId!=0:
            print('##################################上报第%d本绘本##############################' %times)
            print('上报绘本id:',bookId,'关卡id:',challendid)
            sleep(0.1)
            #上报绘本听
            reportBookLising(uidd, uuid, token, bookId)
            sleep(0.1)
            reportBookLisingDone(uidd,uuid,token,challendid)
            sleep(0.1)
            #上报单词读
            giveChallegeAad(uidd, uuid, token, challendid)
            sleep(0.1)
            reportWords(uidd, uuid, token, bookId)
            sleep(0.1)
            #绘本跟读
            reportBookread(uidd, uuid, token, bookId)
            sleep(0.1)
            reportBookreadDone(uidd, uuid, token, challendid)
            sleep(0.1)
            times+=1


    print('##########################用户%d等级%d,学习流完成学习！！！###############################' %(uidd,cid))
