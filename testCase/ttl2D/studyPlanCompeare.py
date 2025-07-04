import requests
from common.excelreadwrite import excel_group
def get_excel_date():
    groupp=['book_id', 'unit_number', 'day', 'stage', 'unit_id']
    groupby='content'
    excelpath='ttlstudydate.xlsx'
    sheetname='Sheet1'
    result_data=excel_group(excelpath,sheetname,groupp,groupby)
    return result_data
#获取接口返回的每日计划
def get_plan_interfacedate():
    pass


#对数据
if __name__ == '__main__':
    dateaaa=get_excel_date()
    print(dateaaa)
