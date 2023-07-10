import json
from time import sleep
import requests
from common.finish_plan import *

#环境
baseurl=urlenverment(2)
header={'Authorization':'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjQwOTc2ODgyODYyOTg1MjE3Iiwic3ViIjoie1wiaWRcIjoxNjQwOTc2ODgyODYyOTg1MjE3LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTcwNDI3NTE1NH0.zg6KAmJHAbmu8Bf2xRSyYgxm5P3hnpYtzvnqAchQkaR9xiDTM1tTZu2-CubdpL3qWCrRMCGYzlw0E4IYJ1mHsQ'}


def getgushitext(vid):
    url=baseurl+'v1/media/video/'+str(vid)
    req=requests.get(url=url,headers=header)
    caption=req.json()['data']
    return caption




if __name__ == '__main__':
    errorlist=[]
    videolist=[2189]
    for vid in videolist:
        gushi=getgushitext(vid)['caption']
        gushi=json.loads(gushi)
        title=gushi['title']
        author=gushi['author']
        content=gushi['content']
        if gushi== "" or title=="" or author=="" or content=="":
            errorlist.append(vid)
            print('错误古诗配置',gushi)
        else:
            print('古诗正确！详细信息为：\n')
            print(str(gushi)+'\n')
            # print('title:',title)
            #
            # print('author:', author)
            #
            # print('content:\n',content)
        sleep(2)