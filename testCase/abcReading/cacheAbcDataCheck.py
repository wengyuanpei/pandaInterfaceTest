#coding:utf-8
import requests
'''




绘本数据对比

'''
#灯塔数据获取
'''
更改绘本里面的数据，更新绘本后去灯塔取改绘本和去ABC去取改绘本的数据查看数据是否一致
'''

UID = '61445'
TOKEN = '6557215a9463e'

uidreq=61445

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
          "sign":"821a7a8a885a98d9ff75e70f4f24cccc64bc8b7cd098dc7b8d87b663ad3ca0df"}
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

    #绘本判断

    #step1 获取ABC绘本数据
    booklist=[]
    print(getAbcBookInfo().json())
    book=getAbcBookInfo().json()['data']['list']
    print('绘本数量%d本' % len(book))
    for i in book:
        booklist.append(i['id'])
    print(booklist)
    # step2 获取对比的绘本&单词数量对比
    errodlist=[]
    for bookid in booklist:
        for abc in book:
            if abc['id'] == bookid:
                idbook=abc['id']
                level=abc['level']
                pictureBookName=abc['pictureBookName']
                wordNum=abc['wordNum']
                print('ABC数据：id：%d  level：%s pictureBookName:%s wordNum:%s' %(idbook,level,pictureBookName,wordNum))

                lightdata=getLighitBookData(bookid)
                idbookL = lightdata['id']
                levelL = lightdata['level']
                pictureBookNameL = lightdata['pictureBookName']
                wordNumL = lightdata['wordNum']

                print('灯塔数据：idbookL：%d  levelL：%s pictureBookNameL:%s wordNumL:%s' %(idbookL,levelL,pictureBookNameL,wordNumL))
                if idbook==idbookL and level==levelL and pictureBookName==pictureBookNameL and  wordNum ==wordNumL:
                    print('绘本%d对比灯塔数据正常！' %bookid )
                else:
                    errodlist.append(bookid)
                    print('绘本%d数据对比异常' %bookid)
    # print('数据对比异常的绘本id>>>',errodlist)

    #单词判断
    errodlistwords=[]
    wordslist = []
    words = getAbcWordInfo()
    # print(words)
    print('单词数量%d个' % len(words))
    for wods in words:
        # print(wods)
        wds=wods['wordId']
        wordslist.append(wds)
    print(wordslist)
    for wordslistid in wordslist:
        for abcWods in words:
            # print(abcWods)
            if abcWods['wordId'] == int(wordslistid):
                abcwordId=abcWods['wordId']
                abcword=abcWods['word']
                abcwordLabelId=abcWods['wordLabelId']
                abclowerLevelList=abcWods['lowerLevelList']
                print('ABC数据：abcwordId：%s  abcword：%s abcwordLabelId:%s abclowerLevelList:%s' % (abcwordId, abcword, abcwordLabelId, abclowerLevelList))

                lightwordddd=getLightWordsinfo(wordslistid)
                lightwordId=lightwordddd['wordId']
                lightword=lightwordddd['word']
                lightwordLabelId=lightwordddd['wordLabelId']
                lightlowerLevelList=lightwordddd['lowerLevelList']
                print('灯塔数据：lightword：%d  lightword：%s lightwordLabelId:%s lightlowerLevelList:%s' % (lightwordId, lightword, lightwordLabelId, lightlowerLevelList))
                if abcwordId==lightwordId and abcword==lightword and abcwordLabelId == lightwordLabelId and abclowerLevelList==lightlowerLevelList:
                    print('绘本%d对比灯塔数据正常！' %wordslistid )
                else:
                            errodlistwords.append(wordslistid)
                            print('绘本%d数据对比异常' %wordslistid)
    print('数据对比异常的单词id>>>', errodlistwords)
    print('数据对比异常的绘本id>>>', errodlist)