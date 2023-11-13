#coding:utf-8
import requests
'''




绘本数据对比

'''
#灯塔数据获取
'''
更改绘本里面的数据，更新绘本后去灯塔取改绘本和去ABC去取改绘本的数据查看数据是否一致
'''

UID = '136'
TOKEN = '654a074f405d9'

uidreq=136

def getLighitBookData(BookId):
    url='http://lighthouse-api-dev.xiongmaoboshi.com/ns/dp/lighthouse/open-api/resource/picture/book/all/info/list/cache'
    data={
              "body": {
                "level": 0,
                "pictureBookId": [
                  BookId
                ]
              },
              "sign": "string",
              "timestamp": 0
            }
    bookInfo=requests.post(url=url,json=data).json()['data'][0]
    return bookInfo

def getLightWordsinfo(wordId):
    url='http://lighthouse-api-dev.xiongmaoboshi.com/ns/dp/lighthouse/open-api/resource/word/cache/all'
    data = {
              "body": {
                "wordId": [
                  wordId
                ]
              },
              "sign": "string",
              "timestamp": 0
            }
    lifgtWord=requests.post(url=url,json=data).json()['data'][0]
    return lifgtWord
'''
获取ABC数据
curl -H 'PANDA-USE-NEW-VERSION: 2' -H 'PANDA-UID: 136' -H 'PANDA-TOKEN: 654a074f405d9' -H 'channel: 2' -H 'versionCode: 351' -H 'versionName: 6.5.1' -H 'xh-debug: 1' -H 'Content-Type: application/json; charset=utf-8' -H 'Host: api-dev.abctime.com' -H 'User-Agent: okhttp/4.8.0' --data-binary '{"ab_non_vip":2,"book_name":"","favourite":0,"sort":0,"status":0,"uid":136,"sign":"ed244994728af729e4a32aa7417c07bbf4d640fd0d610eca017b1e68db35fc03"}' --compressed 'http://api-dev.abctime.com/v5/book/list'


获取到单词数量和绘本信息
'''
def getAbcBookInfo():

    url='http://api-dev.abctime.com/v5/book/list'
    data={"ab_non_vip":2,
          "book_name":"",
          "favourite":0,
          "sort":0,
          "status":0,
          "uid":136,
          "sign":"ed244994728af729e4a32aa7417c07bbf4d640fd0d610eca017b1e68db35fc03"}
    header={'PANDA-UID':UID,
           'PANDA-TOKEN':TOKEN}

    BookInfo=requests.post(url=url,json=data,headers=header)
    BookInfo.encoding='utf-8'
    return BookInfo

def getAbcWordInfo():
    """
    curl -H 'PANDA-USE-NEW-VERSION: 2' -H 'PANDA-UID: 136' -H 'PANDA-TOKEN: 654a074f405d9' -H 'channel: 2' -H 'versionCode: 351' -H 'versionName: 6.5.1' -H 'xh-debug: 1' -H 'Content-Type: application/json; charset=utf-8' -H 'Host: api-dev.abctime.com' -H 'User-Agent: okhttp/4.8.0' --data-binary '{"collect":0,"level":0,"levels":[18],"sort":0,"status":0,"type":0,"uid":136,"word":"","sign":"cb6d86de239a4a5f2975aca044ce097d7c7dc8b7e2698eefec57dc7729156c5e"}' --compressed 'http://api-dev.abctime.com/v5/book/all-words'
    """
    url='http://api-dev.abctime.com/v5/book/all-words'
    header={'PANDA-UID':UID,
           'PANDA-TOKEN':TOKEN}
    data={
            "collect": 0,
            "level": 0,
            "sort": 0,
            "status": 0,
            "type": 0,
            "uid": 136,
            "word": "",
            "sign": "67fcf882a01499c26627631c74a262ea1a10182e9337b56bc3475b175af0d826"
        }

    abcWordreq=requests.post(url=url,json=data,headers=header).json()['data']['wordScreenList']

    return abcWordreq


if __name__ == '__main__':
    '''
    1、验证灯塔修改资源后同步至abc缓存
    
    2、验证修改绘本资源同步
    
    3、验证修改单词资源同步
    
    4、增量同步
    
    5、全量同步
    
    6、删除redis某个key，预缓存请求不到时请求灯塔
    
    '''
