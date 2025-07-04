import requests
from  common.excelreadwrite import excel_read

bookId=[1,2,3]
unitid =[1,2,3,4,5,6,7,89,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34]
dayId=['Day 1','Day 2','Day 3','Day 4','Day 5']
wordType=['学拼读','学句型','学单词']
#获取配置表的excel
def get_excel_date():
    daylist=[]

    for a in range(2,1783):
        station="A"+str(a)+":"+"G"+str(a)
        # print(station)
        print("正在获取第%d行数据" %a)
        planexceldate = excel_read('ttlstudydate.xlsx', station)
        daylist.append(planexceldate)
    print(daylist)
    #取出同一个unit、下的同一day 数据
    #同时处理三个列表list
    for bookIdNum,unitidNum,dayIdNum,wordTypeNum in zip(bookId,unitid,dayId,wordType):

        dataList1=[]
        for word in daylist:
            #book id unit id
            if word[0]==bookIdNum and word[6]==unitidNum and word[2]==dayIdNum and word[4]==wordTypeNum:
                pass
            elif  word[0]==bookIdNum and word[6]==unitidNum and word[2]==dayIdNum and word[4]==wordTypeNum:
                pass
            elif  word[0]==bookIdNum and word[6]==unitidNum and word[2]==dayIdNum and word[4]==wordTypeNum:
                pass



#获取接口返回的每日计划
def get_plan_interfacedate():
    pass


#对数据
if __name__ == '__main__':
    get_excel_date()
