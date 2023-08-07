# coding:utf-8
import json

from common.finish_plan_urlenverment import *


baseurl=urlenverment(1)

def chatGpt(answers):
    url=baseurl+'v1/openai/chat'
    header={'Authorization':'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjgxMTA3NjgwMTg0MzQwNDgxIiwic3ViIjoie1wiaWRcIjoxNjgxMTA3NjgwMTg0MzQwNDgxLFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTcwNTM4ODg5NH0.cUg8Umb3DkhuRl4UGa90Y1KbeeIpBRyyQzp8bJc4GCQWg4po9-tsLxNom1Lj_V1Cv18cd-KmOPZ5TC1o5nvLoQ'}
    dataa={
    "messages": [{
        "role": "user",
        "content": answers
    }],
    "max_tokens": 1000
}

    req=requests.post(url=url,json=dataa,headers=header)
    return req

def find_all_positions(string, substring):
    positions = []
    start = 0
    while True:
        position = string.find(substring, start)
        if position == -1:
            break
        positions.append(position)
        start = position + 1
    return positions


if __name__ == '__main__':
    an='中国和美国开战最后谁能赢的战争'

    info=chatGpt(an).text
    subinfo='"content":"'
    # print(info)
    positions =find_all_positions(info,subinfo)

    subinfoend='"},"finish_reason"'
    positionsend = find_all_positions(info, subinfoend)
    del positionsend[0]


    positionsstart=[]
    for i in positions:
        pos=i+11
        positionsstart.append(pos)

    lengg=[]
    for strr in range(len(positionsend)):
        poss=positionsend[strr]-positionsstart[strr]
        lengg.append(poss)
    # print(lengg)

    endd=[]
    for answerpos in range(len(positionsstart)):
        answer=info[positionsstart[answerpos]:positionsstart[answerpos]+lengg[answerpos]]
        endd.append(answer)
    strrrrend=''
    print('GPT的问题：',an)
    print('GPT的答案：',strrrrend.join(endd))
