import requests
from  common.excelreadwrite import excel_read


#获取配置表的excel
def get_excel_date():
    day=[]

    for a in range(2,1783):
        station="A"+str(a)+":"+"G"+str(a)
        # print(station)
        print("正在获取第%d行数据" %a)
        planexceldate = excel_read('ttlstudydate.xlsx', station)
        day.append(planexceldate)
    print(day)
    #取出同一个unit、下的同一day 数据
    for word in day:
        pass

#获取接口返回的每日计划
def get_plan_interfacedate():
    pass


#对数据
if __name__ == '__main__':
    get_excel_date()
