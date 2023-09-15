#coding:utf-8
import requests
from common.finish_plan_urlenverment import *


baseurl=urlenverment(1)
url=baseurl+'v1/book/level-map'
heder={'Authorization':"Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNzAxMTc2MTQ3NDcxMDI0MTMwIiwic3ViIjoie1wiaWRcIjoxNzAxMTc2MTQ3NDcxMDI0MTMwLFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTcxMDA2MzU3OX0.eujbdQmq5gL9DcWKijkKuFYaJLaPqm4NTX0ld7sVMBHdQPptqcV2v4IOl-zjzeOM1Voef4ItVh_dIasCFvS8Zw"}
data={"dict_type":2,"pid":1,"uid":1640976882862985217}
requestss=requests.post(url=url,json=data,headers=heder).json()['data']


for a in requestss:
    dictName=a['dictName']
    dictCode=a['dictCode']
    with open(r"C:\Users\zhang\Desktop\pandaInterfaceTest\testCase\api\raz_map.txt", "a") as f:
        f.write('\n' + str(dictName) +"---" + str(dictCode))  # 自带文件关闭功能，不需要再写
    f.close()
