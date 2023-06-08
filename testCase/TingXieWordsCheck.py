import requests
from time import  sleep

#听写单词扣词验证PRE环境


header={"Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNTYyNjI5MDYwMDc1MTAyMjA5Iiwic3ViIjoie1wiaWRcIjoxNTYyNjI5MDYwMDc1MTAyMjA5LFwibW9iaWxlXCI6XCIrODYxODM4NDI1MzUwNlwifSIsImV4cCI6MTcwMTY3NzU1M30.ByAdhAfbxwS5tTbkbSJIPJXN6bIrzoOjeWMwn6JA8pimm2v1fMTXVJfdXloqInXPY_FsTlc7ZPDwxlCGtFqQ5Q",
        "User-Uid":"1562629060075102209",
        "Kid-Uid":"1562629060075102209"}

DataGetTcheBox={"uid":1562629060075102209}

#获取教材版本接口

GetTeacherBoxUrl="https://hear-pre.abctime.com/v1/dictation/textbook"


#获取年级信息
GetTcheBoxInfo=requests.post(url=GetTeacherBoxUrl,json=DataGetTcheBox,headers=header)

# print(GetTcheBoxInfo.json()["data"]['grade_list'][0])
# print(GetTcheBoxInfo.json()["data"]['grade_list'][0]['textbook_list'])
bookErrorList=[]
worderror=[]

for grade_id in range(19):
    # print(textbook_id)
    sleep(1)
    for textbook_id in range(1,len(GetTcheBoxInfo.json()["data"]['grade_list'][grade_id]['textbook_list'])+1):
        grade_name = GetTcheBoxInfo.json()["data"]['grade_list'][grade_id]['grade_name']
        # print(grade_name)
        JX = GetTcheBoxInfo.json()["data"]['grade_list'][grade_id]['textbook_list'][textbook_id-1]['textbook_name']

        sleep(1)
        # 获取每本教材的单元
        GetRescourseUrl = "https://hear-pre.abctime.com/v1/dictation/rescourse"
        DataGetRescourse = {"grade_id": grade_id+1, "publisher_id": textbook_id, "uid": 1562629060075102209}
        GetDataGetRescourse = requests.post(headers=header, json=DataGetRescourse, url=GetRescourseUrl)
        # print("年级教材版本：",GetDataGetRescourse.json()['data'])


        try:
            for i in range(len(GetDataGetRescourse.json()['data']['resource_list'])):
                # print(GetDataGetRescourse.json()['data']['resource_list'][i])

                    book_id=GetDataGetRescourse.json()['data']['resource_list'][i]['unit_id']

                    DY=book_id
                    publisher_idd=GetDataGetRescourse.json()['data']['resource_list'][i]['unit_id']
                    sleep(1)
                    # print('book_id',book_id)

                    # 选择单词
                    selectUrl = "https://hear-pre.abctime.com/v1/dictation/select"
                    selectData = {"book_id": book_id, "type": 1, "uid": 1562629060075102209}
                    selctreq = requests.post(json=selectData, url=selectUrl, headers=header)
                    sleep(1)
                    # print("选择单词：",selctreq.json()['data']['words_list'])

                    #遍历保存出单词和单词ids
                    wordss=[]
                    wordIdss =[]
                    for words in range(len(selctreq.json()['data']['words_list'])):
                        wordsEnd=selctreq.json()['data']['words_list'][words]['word']
                        # print("单词:",wordsEnd)
                        wordss.append(wordsEnd)
                        wordidEnd = selctreq.json()['data']['words_list'][words]['word_id']
                        # print("单词id:", wordidEnd)
                        wordIdss.append(wordidEnd)

                    sleep(1)
                    # 扣词接口
                    value=len(wordss)
                    deductionUrl = 'https://hear-pre.abctime.com/v1/dictation/deduction'
                    dataDeduction = {"pictureBookIds": [book_id], "value": value,
                            "word": wordss,
                            "wordIds": wordIdss, "uid": 1562629060075102209}

                    deductionReq=requests.post(url=deductionUrl,json=dataDeduction,headers=header)
                    # print("扣词请求：",deductionReq.json())
                    # Errorlist=[]
                    if deductionReq.json()['code']=="200" :
                        print('年级：',grade_name, '教材：',JX, '单元：',book_id, '正常!')
                        # print(deductionReq.json())
                    else:
                        print('年级：',grade_name, '教材：',JX, '单元：',book_id, '扣词异常!')
                        print("选择单词",selctreq.json())
                        worderror.append([grade_name,JX,book_id,[selctreq.json()]])

        except:
            print("异常请求",GetDataGetRescourse.json())
            print('年级：', grade_name, '教材：', JX)
            print("请求参数：",DataGetRescourse)
            bookErrorList.append([grade_name,JX])
            continue
print('教材无单词数据',bookErrorList)
print("扣词异常",worderror)

