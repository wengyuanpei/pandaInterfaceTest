
#codeing:utf-8
"""
curl -H 'PANDA-USE-NEW-VERSION: 2' -H 'PANDA-UID: 136' -H 'PANDA-TOKEN: 6549d610e5151' -H 'channel: 2' -H 'versionCode: 350' -H 'versionName: 6.5.0' -H 'xh-debug: 1' -H 'Content-Type: application/json; charset=utf-8' -H 'Host: api-dev.abctime.com' -H 'User-Agent: okhttp/4.8.0' --data-binary '{"action":1,"uid":136,"words_id":7574,"sign":"c8216e99df4a7c26c0815c89260c261ae9c2b9036d662c89b62df70cf83a1a90"}' --compressed 'http://api-dev.abctime.com/v5/words-remember/collect-words'


curl -H 'PANDA-USE-NEW-VERSION: 2' -H 'PANDA-UID: 136' -H 'PANDA-TOKEN: 6549d610e5151' -H 'channel: 2' -H 'versionCode: 350' -H 'versionName: 6.5.0' -H 'xh-debug: 1' -H 'Content-Type: application/json; charset=utf-8' -H 'Host: api-dev.abctime.com' -H 'User-Agent: okhttp/4.8.0' --data-binary '{"collect":0,"level":0,"levels":[29],"sort":0,"status":0,"type":0,"uid":136,"word":"","sign":"9b80d8a048cc96ca3d7972fc81be7413a34a7e75849f9bc3cb8222026d756a4c"}' --compressed 'http://api-dev.abctime.com/v5/book/all-words'
"""

import requests
def getWordList():
    header={'PANDA-UID': '136','PANDA-TOKEN':'6549d610e5151'}
    data={"collect":0,"level":0,"levels":[29],"sort":0,"status":0,"type":0,"uid":136,"word":"","sign":"9b80d8a048cc96ca3d7972fc81be7413a34a7e75849f9bc3cb8222026d756a4c"}
    url='http://api-dev.abctime.com/v5/book/all-words'
    req=requests.post(url=url,json=data,headers=header)
    return req.json()['data']
    # print(req.json())


def colectWords(wid):
    header={'PANDA-UID':'',
            'PANDA-TOKEN':'',
           'versionCode':350}
    data={}


if __name__ == '__main__':
    listWord=[]
    info=getWordList()['wordScreenList']

    # print(info)
    for i in range(len(info)):
        # print(info[i])
        wordid=info[i]['wordId']
        word=info[i]['word']
        listWord.append([word,wordid])
    print(listWord)