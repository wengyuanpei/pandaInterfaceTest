import json

from common.excelreadwrite import excel_read

#读表方法

def getData():
    path=r'C:\Users\zhang\Documents\pandaInterfaceTest\testCase\studyFExcel\P025.xlsx'
    datalist=excel_read(path,"K2:K98")
    return datalist

def checkJson(jsondata):
    for data in jsondata:
        try:
            json.loads(data)
        except :
            pass
            #打印错误位置
