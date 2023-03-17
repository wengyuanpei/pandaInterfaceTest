import  requests
import  time,random

url="https://hear-pre.abctime.com/v1/book/book-list"
data={"current":1,"lower_level":3,"size":50,"uid":1562629060075102209}

headerrs={"Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNTYyNjI5MDYwMDc1MTAyMjA5Iiwic3ViIjoie1wiaWRcIjoxNTYyNjI5MDYwMDc1MTAyMjA5LFwibW9iaWxlXCI6XCIrODYxODM4NDI1MzUwNlwifSIsImV4cCI6MTY5NDU4Njc1OX0.lISnSvFcTrKPwME6-MyAqS7QYOKBSuIX1YztCMUq7rEwVx9BwmUx2KDXp0Kz2_ZiHxkK6xIZ-R5meaw0x_G7CQ"}




while True:
    list=[3,4,5,6,7,8,9,10,11,12,13,14,15,16]


    reeqq = requests.post(url=url, json=data, headers=headerrs)
    if reeqq.status_code==200:
        print("ok")

    else:
        print(reeqq.json())
        break

    time.sleep(2)
