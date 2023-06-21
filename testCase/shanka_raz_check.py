import requests
from time import sleep




#获取听力机绘本ID
def getrazid(razid):
    urlraz='https://hear.abctime.com/v1/book/book-detail'
    header_live={"Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNTYyNjI5MDYwMDc1MTAyMjA5Iiwic3ViIjoie1wiaWRcIjoxNTYyNjI5MDYwMDc1MTAyMjA5LFwibW9iaWxlXCI6XCIrODYxODM4NDI1MzUwNlwifSIsImV4cCI6MTcwMjcyNzY1M30.7xawiwUteBhZsvxa7tprATnAl7v2q-JLPxubqqpRoYdJcuGKzFgC-fKAhIw5DZRplBpJU3yvsU9mdO_38GiIhw"}
    data={
    "book_id": razid,
    "uid": 1610539670101397505
    }

    razrsponse=requests.post(url=urlraz,json=data,headers=header_live)
    print(razrsponse.json()["data"]['id'])
    return  razrsponse.json()["data"]['id']



def getshankarazid():
    pass










if __name__ == '__main__':
    getrazid(271)
