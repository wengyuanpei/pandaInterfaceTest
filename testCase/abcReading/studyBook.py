import requests
from common.abcSign import *

'''
curl -H 'PANDA-USE-NEW-VERSION: 2' -H 'PANDA-UID: 60667' -H 'PANDA-TOKEN: 656723167a39d' -H 'channel: 2' -H 'versionCode: 353' -H 'versionName: 6.5.3' -H 'xh-debug: 1' -H 'Content-Type: application/json; charset=utf-8' -H 'Host: api-dev.abctime.com' -H 'User-Agent: okhttp/4.8.0' --data-binary '{"uid":60667,"ab_non_vip":2,"sign":"0581a6ae7697c95b623ed485805358f7c549166bb6bf9571d02e3d152035bfa3"}' --compressed 'http://api-dev.abctime.com/v5/challenges/getNextChallengeInfo'
'''
headers = {'PANDA-TOKEN': '6568314eda122', 'PANDA-UID': '61359'}
uidd=61359

def getNextBook():
    url = 'http://api-dev.abctime.com/v5/challenges/getNextChallengeInfo'
    header = headers
    data1 = {"uid": uidd,"ab_non_vip": 2}
    data = getSignEnd(data1)
    NextInfo = requests.post(url=url, json=data, headers=header).json()['data']['id']
    challengeId = requests.post(url=url, json=data, headers=header).json()['data']['challengeId']
    return NextInfo,challengeId

def reportBookRead(uidd,bookId):
    url = 'http://api-dev.abctime.com/v5/challenges/getNextChallengeInfo'
    header = headers

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

def Done(uidd,challenges_id):
    url = 'http://api-dev.abctime.com/v5/challenges/getNextChallengeInfo'
    header = headers

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


if __name__ == '__main__':
    #需要完成多少本绘本

    for i in range(2):

        bookId=getNextBook()[0]
        challengeId = getNextBook()[1]
        print(bookId,challengeId)
        uidd = 60667
        Done(uidd, challengeId)
        reportBookRead(uidd, bookId)

