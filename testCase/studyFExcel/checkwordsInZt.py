import requests
from time import sleep
from common.excelreadwrite import *
def checkwords(id):

    url = 'https://cms-dev.xiongmaoboshi.com/s/dp/lighthouse/web/word/page?sf_request_type=fetch'
    headers = {
        'accept': 'application/json',
        'accept-language': 'zh-CN,zh;q=0.9',
        'authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ7XCJlbWFpbFwiOlwid2VuZ3l1YW5wZWlAZHJwYW5kYS5jb21cIixcImlkXCI6MjIzLFwibW9iaWxlXCI6XCIxNzM0NTA0MzM2NVwiLFwidXNlcm5hbWVcIjpcIndlbmd5dWFucGVpXCIsXCJ3b3JrY29kZVwiOlwiVjAwMTM3NTBcIixcInp5bE5hbWVcIjpcIjU3K0I2TCtjNlptcVwifSIsImV4cCI6MTczNTk3NTkyOX0.rh-eKzk8M28eGJIW_K46iOKvLB1wc2iwVKhgbvLIIKH-bY1QtEeun7gg2wotArAyfDenq1xWQ_gX3iR_1Jr_jw',
        'cache-control': 'no-cache',
        'content-type': 'application/json; charset=utf-8',
        'credentials': 'include',
        'domain': 'CMS',
        'mode': 'no-cors',
        'origin': 'https://cms-dev.xiongmaoboshi.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'roles': 'ivan',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }
    data = {
        "body": {
            "pageSize": 10,
            "current": 1,
            "total": 0,
            "showSizeChanger": True,
            "typeId": 5588,
            "path": "-1/5588/",
            "backupType": 0,
            "id": id
        }
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()

def getAllwords(station):
    path= r'/testCase/studyFExcel/checkWordsDG.xlsx'

    listID=excel_read(path,station)
    return listID

if __name__ == '__main__':
    errorlist = []
    for staion in range(1,445):
        stationE="P"+str(staion) +":"+ "P"+str(staion)
        listend=getAllwords(stationE)
        for i in listend:
            i=str(i)
            listend1 = i.split(":")
            # print(listend1)
            for ide in listend1:
                # print(ide)
                if ide != "":
                    sleep(1)
                    ide = str(ide)
                    try:
                        response=checkwords(ide)
                        # print(response)
                        if response["code"] ==0:
                            if response["data"]["total"] == "0" :
                                print("添加",ide,"到错误列表")
                                errorlist.append(ide)
                            else:
                                print(ide,'单词在灯塔数据正常！')
                        else:
                            continue
                    except:
                        response = checkwords(ide)
                        # print(response)
                        if response["code"] == 0:
                            if response["data"]["total"] == "0":
                                print("添加", ide, "到错误列表")
                                errorlist.append(ide)
                            else:
                                print(ide, '单词在灯塔数据正常！')

                else:
                    continue

        print('灯塔无数据id:   ',errorlist)



