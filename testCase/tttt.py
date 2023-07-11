from common.excelreadwrite import *
from common.finish_plan_urlenverment import *
import requests
from time import *
#
# filename=r'C:\Users\zhang\Desktop\新建 XLSX 工作表.xlsx'
# tion='A1:A923'
# read=excel_read(filename,tion)
#
#
#
#
# excel_write(read,1,'A',filename,'Sheet3')


baseurl=urlenverment(2)
a=1
while True:
    url=baseurl+'v1/study/my-plan'
    data={"uid":1640976882862985217}
    header={'Authorization':'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjQwOTc2ODgyODYyOTg1MjE3Iiwic3ViIjoie1wiaWRcIjoxNjQwOTc2ODgyODYyOTg1MjE3LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTcwNDUyNzc2OH0.FOW01pPijX0cRX6MDDBxX8OWdj72YUZF_tYxWYsbIupxJSpJd3z_HJwZpEsftQ08zPcL9Zubgg5Hk-UXr-P19w'}
    req=requests.post(url=url,json=data,headers=header)
    if req.status_code != 200:
        print("接口报错了！")

    else:
        print('第%d次请求' %a,req.status_code)
        sleep(5)
    a+=1
