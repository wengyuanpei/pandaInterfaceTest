import requests
from common.abcSign import getSignEnd

'''

curl --location 'http://api-dev.abctime.com/v5/book/all-words' \
--header 'PANDA-USE-NEW-VERSION: 2' \
--header 'PANDA-UID: 60623' \
--header 'PANDA-TOKEN: 655d66b7c4815' \
--header 'channel: 2' \
--header 'versionCode: 352' \
--header 'versionName: 6.5.2' \
--header 'xh-debug: 1' \
--header 'Content-Type: application/json; charset=utf-8' \
--header 'Host: api-dev.abctime.com' \
--header 'User-Agent: okhttp/4.8.0' \
--data '{"collect":0,"level":0,"levels":[3],"sort":0,"status":0,"type":0,"uid":60623,"word":"","sign":"be49b7d676af632d88aaa604bf67bfec3f6c42d296b8ceb228d752f3c9e9139f"}'

'''

def getAllWords(UID,TOKEN,uid):
    url='http://api-dev.abctime.com/v5/book/all-words'
    header={'PANDA-UID':UID,'PANDA-TOKEN':TOKEN}
    wordsList = []
    for level in range(3, 30):
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
            wordlenth=len(word)
            wordsList.append([wordId,word,wordlenth])
    return wordsList



if __name__ == '__main__':
        checkWordsList=['ame',
                'ake',
                'ate',
                'ade',
                'abe',
                'ape',
                'afe',
                'ale',
                'ave',
                'ime',
                'ine',
                'ipe',
                'ike',
                'ome',
                'one',
                'ope',
                'ube',
                'ule',
                'une',
                'ute',
                'ai',
                'ay',
                'ee',
                'ea',
                'y',
                'ey',
                'igh',
                'ie',
                'oa',
                'ow',
                'ue',
                'ui',
                'ew',
                'oo',
                'bl',
                'cl',
                'br',
                'cr',
                'fl',
                'gl',
                'fr',
                'gr',
                'pl',
                'sl',
                'dr',
                'tr',
                'sm',
                'sn',
                'sp',
                'sw',
                'st',
                'sh',
                'ch',
                'tch',
                'ph',
                'wh',
                'th',
                'ck',
                'qu',
                'ng',
                'nk',
                'nd',
                'nt',
                'it',
                'mp',
                'sk',
                'sc',
                'spr',
                'str',
                'spl',
                'squ',
                'ar',
                'ir',
                'ur',
                'er',
                'or',
                'ou',
                'ow',
                'oi',
                'oy',
                'u',
                'au',
                'aw',
                'all',
                'wa',
                'or',
                'oar',
                'are',
                'air',
                'ea',
                'ear',
                'eer',
                'a',
                'e',
                'i',
                'o',
                'u',
                'kn',
                'wr',
                'ture',
                'sure',
                'tion',
                'sion',
                'ous',
                'ful']
        info=getAllWords('60623','655590d449b1d',60623,)
        #去重
        new_info=[]
        for i in info:
            if i not in new_info:
                new_info.append(i)

        lenth4=[]
        lenth46=[]
        lenth7=[]

        for lenth in new_info:
            if lenth[2] <4:
                lenth4.append(lenth)
            if 4<=lenth[2]<=6:
                lenth46.append(lenth)
            if lenth[2]>7:
                lenth7.append(lenth)

        print('小于4的单词有%d个' %len(lenth4))
        print(lenth4)

        print('4-6长度的单词有%d个' % len(lenth46))
        print(lenth46)

        print('大于7的单词有%d个' % len(lenth7))
        print(lenth7)

