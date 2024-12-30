#coding:utf-8

import random


def getStudyFlowData(wordlist):


    while True:
        enddemo = []
        endlist=[]
        for i in list1:

            list3=random.sample(list1,2)

            if i in list3:
                continue
            else:
                list4=list3+[i]
                endlist.append(list4)
                damo = {"words_list": list4, "wordId": i}
                enddemo.append(damo)
        if len(endlist) == len(list1):

            enddd={"type":16,"questions":enddemo}
            print(enddd)

            return enddd
            break


if __name__ == '__main__':
    list1 = [49645,49646,173893,173897,173924,173905



]
    listtt=getStudyFlowData(list1)
