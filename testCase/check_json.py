from common.excelreadwrite import *
import json
def is_json():
    errorlist=[]
    namepath=r'C:\Users\zhang\Desktop\plan_detail.xlsx'
    postion='A2:A1056'
    jsondata=excel_read(namepath,postion)
    print(jsondata)
    for myjson in jsondata:
        try:
            json_object = json.loads(myjson)
        except:
            errorlist.append(myjson)
            print('False')
        print('True')
    print(errorlist)

if __name__ == '__main__':
    is_json()

