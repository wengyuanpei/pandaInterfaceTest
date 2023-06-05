import requests
from time import sleep

header = {
    "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjQwOTc2ODgyODYyOTg1MjE3Iiwic3ViIjoie1wiaWRcIjoxNjQwOTc2ODgyODYyOTg1MjE3LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTcwMTUwNjY5OH0.ymw2DKZATXWxGJ7h88T29A1vaMGPGbWu-eNl_9nuk4xoDkThu9Q0AR6KqE84gG0Hj22W6bK5uLXr54bRpvcDqw",
    "Sn": "S01D1042330600005",
    "User-Uid": "1640976882862985217",
    "Kid-Uid": "1640976882862985217"}

def getVideoInfo(lessonId):
#视频课包模块
    modeId=[]
    modeId.append(lessonId)

    # 获取视频id
    getVideoInfoUrl="https://hear.abctime.com/v1/lesson/"


    for modeId in modeId:
        getModeInfoUrl=getVideoInfoUrl+str(modeId)
        ModeInfo=requests.get(headers=header,url=getModeInfoUrl)
        # print(ModeInfo.json()['data']["medias_obj"]['video'])
        return ModeInfo.json()['data']["medias_obj"]['video']


def getPlayUrlRsposeTime(videoId):
    playInfo='https://hear.abctime.com/v1/media/video/'+str(videoId)
    playInfoUrl=requests.get(headers=header,url=playInfo)
    # print(playInfoUrl.json()['data'][ 'urls']['playUrls'][1]['playUrl'])

    end_url=str(playInfoUrl.json()['data'][ 'urls']['playUrls'][1]['playUrl'])
    resposeTime=requests.get(url=end_url)
    # 响应时间

    print("响应时间：",resposeTime.elapsed.total_seconds())
    return resposeTime.elapsed.total_seconds()


# getPlayUrlRsposeTime(11699)
lessonId=565
errorList=[]

for videoId in getVideoInfo(lessonId):
    sleep(0.5)
    timed=getPlayUrlRsposeTime(videoId)
    if timed>3:
        errorList.append(videoId)
    else:
        print("视频id:",videoId,"响应时间：",timed)

print("响应时间大于3秒，异常视频ID：",errorList)
