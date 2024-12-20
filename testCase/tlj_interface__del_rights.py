'''
听力机删除权益的接口
'''


import  requests
from common.get_tlj_auth import *

url="https://pad-dev.xiongmaoboshi.com/s/device/hearing/rights/manufacturer/data/clear/"


#需要删除权益的SN
list=['{S1TESTLY015}','{S01D1042320702478}']

#听力机的令牌
phone=phone_num()
auth_b=getauth(phone)[1]
# print(auth)

#ola 鉴权
auth_ht='Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ7XCJlbWFpbFwiOlwid2VuZ3l1YW5wZWlAZHJwYW5kYS5jb21cIixcImlkXCI6MjIzLFwibW9iaWxlXCI6XCIxNzM0NTA0MzM2NVwiLFwidXNlcm5hbWVcIjpcIndlbmd5dWFucGVpXCJ9IiwiZXhwIjoxNjc4MzU4NDIzfQ.QuCZd_AEXaONUu9jOVoDMSmNuIekU-K6rKIbpFzMBj5V1GdW0UYNVE3Kx35iq8jcW2-bMz7BQ-TbpTUKA1oPqg'
header={
            "Authorization": auth_b,
            "Content-Type": "application/json;charset=UTF-8"
        }
for sn in list:
    url_end=url+sn
    print("请求地址：",url_end)
    requstss=requests.post(url=url_end,headers=header)
    print(requstss.text)
