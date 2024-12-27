#coding:utf-8

import random
from common.excelreadwrite import *

def getStudyFlowData(wordlist):


    while True:
        enddemo = []
        endlist=[]
        for i in wordlist:

            list3=random.sample(wordlist,2)

            if i in list3:
                continue
            else:
                list4=list3+[i]
                endlist.append(list4)
                damo = {"words_list": list4, "wordId": i}
                enddemo.append(damo)
        if len(endlist) == len(wordlist):

            enddd={"type":16,"questions":enddemo}
            return enddd
            break

def getData():
    path=r'C:\Users\zhang\Documents\pandaInterfaceTest\testCase\studyFExcel\P025.xlsx'
    datalist=excel_read(path,"K2:K98")
    return datalist

def writeExcel(readIn,hStaion,lStation,excelPath,sheetName):
    # print('写入文件名字', '行位置', '表格列位置', '文件绝对路径', 'sheet名字')

    excel_write(readIn,hStaion,lStation,excelPath,sheetName)

if __name__ == '__main__':
    excel=getData()
    # print(excel)

    listdamolist=[]
    for listdata in excel:
        #构造列表
        # print(listdata)
        lessonlist=listdata.split(',')
        listdamo = getStudyFlowData(lessonlist)
        print(listdamo)
        listdamolist.append(str(listdamo))




    hStaion = 2
    lStation='L'
    excelPath=r'C:\Users\zhang\Documents\pandaInterfaceTest\testCase\studyFExcel\P025.xlsx'
    writeExcel(listdamolist, hStaion, lStation, excelPath, 'Sheet1')


