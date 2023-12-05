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

    header  = {'PANDA-TOKEN': token, 'PANDA-UID': uuid}

    req=requests.post(url=url,json=dataEND,headers=header).json()['data']['challenges']

    bookList=[]
    challengesList=[]
    # print(req)
    # print(type(req))
    for bookInfo in req:
        bookId=bookInfo['bookId']
        # if bookId != 0:
        bookList.append(bookId)
        challengId=bookInfo['id']
        challengesList.append(challengId)

    return [bookList,challengesList]

def reportBookRead(uidd:int,uuid,token:str,bookId):
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

    code2 = requests.post(url=url, json=dataEnd, headers=header).json()['code']
    print(code2)

def reportBookReadDone(uidd:int,uuid:str,token:str,challenges_id):
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
	"video_urls": []
}
    dataEnd = getSignEnd(data2)

    code2 = requests.post(url=url, json=dataEnd, headers=header).json()['code']
    print(code2)


'''
单词学习上报
'''
def reportWords(uidd:int,uuid,token:str,bookId):
    url='http://api-dev.abctime.com/v5/study/report_words'
    data={
	"book_id": bookId,
	"cost_time": 1,
	"uid": uidd,
	"words_list": [{
		"score": 99,
		"video_url": "",
		"words_id": 7727
	}, {
		"score": 98,
		"video_url": "",
		"words_id": 7607
	}, {
		"score": 99,
		"video_url": "",
		"words_id": 7593
	}, {
		"score": 100,
		"video_url": "",
		"words_id": 7802
	}, {
		"score": 100,
		"video_url": "",
		"words_id": 7803
	}, {
		"score": 100,
		"video_url": "",
		"words_id": 7804
	}, {
		"score": 98,
		"video_url": "",
		"words_id": 7805
	}, {
		"score": 98,
		"video_url": "",
		"words_id": 7806
	}]}
    dataEnd=getSignEnd(data)
    header = {'PANDA-TOKEN': token, 'PANDA-UID': uuid}
    rep=requests.post(url=url,json=dataEnd,headers=header)
    print('单词上报',rep.status_code)

if __name__ == '__main__':
    uidd = 135
    uuid = '135'
    token = '656ee831ec8ef'
    cid = 3
    getBookIdChallengId(uidd,uuid,token,cid)
