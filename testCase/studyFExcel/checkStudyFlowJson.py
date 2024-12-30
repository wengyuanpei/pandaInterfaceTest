import json

from common.excelreadwrite import excel_read

#读表方法

def getData():
    path= r'/testCase/studyFExcel/P025.xlsx'
    datalist=excel_read(path,"K2:K98")
    return datalist


def checkJson(jsonData):
    for data in jsonData:
        try:
            json.loads(data)
            return True
        except json.JSONDecodeError:
            return False


