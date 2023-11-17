import requests
from common.abcSign import getSignEnd

'''

curl --location 'http://api-dev.abctime.com/v5/book/all-words' \
--header 'PANDA-USE-NEW-VERSION: 2' \
--header 'PANDA-UID: 60623' \
--header 'PANDA-TOKEN: 655590d449b1d' \
--header 'channel: 2' \
--header 'versionCode: 351' \
--header 'versionName: 6.5.1' \
--header 'xh-debug: 1' \
--header 'Content-Type: application/json; charset=utf-8' \
--header 'Host: api-dev.abctime.com' \
--header 'User-Agent: okhttp/4.8.0' \
--data '{
    "collect": 0,
    "level": 0,
    "levels": [
        3
    ],
    "sort": 0,
    "status": 0,
    "type": 0,
    "uid": 60623,
    "word": "",
    "sign": "be49b7d676af632d88aaa604bf67bfec3f6c42d296b8ceb228d752f3c9e9139f"
}'


'''

def getAllWords(UID,TOKEN,uid):
    url='http://api-dev.abctime.com/v5/book/all-words'
    header={'PANDA-UID':UID,'PANDA-TOKEN':TOKEN}
    wordsList = []
    for level in range(3, 29):
        print(level)
        data_info = {
            "collect": 0,
            "level": 0,
            "levels": [
                level
            ],
            "sort": 0,
            "status": 0,
            "type": 0,
            "uid": uid,
            "word": ""}
        data=getSignEnd(data_info)
        req=requests.post(url=url,json=data,headers=header).json()['data']['wordScreenList']
        for i in req:
            wordId=i['wordId']
            word=i['word']
            wordsList.append([wordId,word])
    return wordsList



if __name__ == '__main__':

        info=getAllWords('60623','655590d449b1d',60623,)
        print(info)
        print(len(info))