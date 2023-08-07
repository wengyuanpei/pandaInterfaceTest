
# encoding:utf-8

import requests
import base64

'''
植物识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/plant"
# 二进制方式打开图片文件
f = open(r'C:\Users\zhang\Desktop\VCG21gic20072684.jpg', 'rb')
img = base64.b64encode(f.read())
print(img)
params = {"image":img}
access_token = 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjg2NjM5NTA0NTgwMTkwMjEwIiwic3ViIjoie1wiaWRcIjoxNjg2NjM5NTA0NTgwMTkwMjEwLFwibW9iaWxlXCI6XCIrODYxODM4NDI1MzUwNlwifSIsImV4cCI6MTcwNjUxMzE2OX0.c8ch4WBbE6raEe8PKSkMcf5-GcO-TNis81sAcrE6RveVntoxUtVB076l8lhfA1IqshgF1u7msB9Q9uUlmIVhRw'

request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())