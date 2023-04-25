
import json
import os
import openpyxl
import requests
from time import sleep


path = r"C:\Users\zhang\Desktop"
os.chdir(path)  # 修改工作路径

workbook = openpyxl.load_workbook('用户计划模板查询.xlsx')  # 返回一个workbook数据类型的值
sheet = workbook.active  # 获取活动表
# print('当前活动表是：')
# print(sheet)

cell = sheet['E2:E1056']  # 获取A1到A5的数据

# print(cell)

list_data=[]
day=0
url="https://hear.abctime.com/v1/book/book-detail"
header_dev={"Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNTk0ODcwNzg0NzA4NTAxNTA1Iiwic3ViIjoie1wiaWRcIjoxNTk0ODcwNzg0NzA4NTAxNTA1LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2OFwifSIsImV4cCI6MTY5Nzk1OTg1Nn0.wKCAumCwX_Ruhi9dmRhFcKYtUo1bvvgEsfvcgTJr_4i2RN_NvWcIENxooKZRcW8JW7b2a5go8076webN8On0qg"}
UID=1547454324283875329
book_id=1
data_en={
  "uid": UID,
  "book_id": book_id
}


for i in cell:
    day+=1
    for j in i:
        json_data=json.loads(j.value)
        for ii in json_data["audio_book_ids"]:
            book_id=ii
            sleep(0.5)
            requestss=requests.post(url=url,json=data_en,headers=header_dev)
            try:
                if requestss.json()['code'] == str(300) or requestss.json()['data']=="Null" or requestss.json()['message']=="无数据！"or requestss.json()['data']['id']<=1:
                    print("错误绘本，id：",ii)
                    list_data.append(ii)
            except:
                print("绘本正常，id",ii)
            if ii>2956:
            # if ii>2006:
                print("第",day,"天，错误id",ii)
print("异常绘本ID",list_data)





