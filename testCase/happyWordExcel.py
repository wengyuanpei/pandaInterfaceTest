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
    list1 = [42405,41995,42190,42574,42778,49663,49664,49665,49666,173908,173910,173907,173932,47035,42105,42021,42297,47036,42108,42530,42128


]
    listtt=getStudyFlowData(list1)
