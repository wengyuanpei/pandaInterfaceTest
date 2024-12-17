from common.excelreadwrite import *

def getwordexcelinfo(oldexcel,info):

     wordInfo=excel_read(oldexcel,info)

     return  wordInfo

if __name__ == '__main__':
    oldexcel = r'C:\Users\zhang\Documents\pandaInterfaceTest\testCase\wordExcel\word.xlsx'
    for num in range(260):
        numm=str(num+4)
        post="A"+numm+":"+"C"+numm
        infoOld=getwordexcelinfo(oldexcel,post)
        print('等级: '+str(infoOld[0])+'  unit:  '+str(infoOld[1])+'  单词: '+str(infoOld[2]))


