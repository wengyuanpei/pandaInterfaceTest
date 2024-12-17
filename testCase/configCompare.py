from common.excelreadwrite import *

def getwordexcelinfo(oldexcel,info):
     wordInfo=excel_read(oldexcel,info)
     return wordInfo


def diffWord(oldlist,newlist):
    listdif=set(oldlist)-set(newlist)

    return listdif




if __name__ == '__main__':
    oldexcel = r'C:\Users\zhang\Documents\pandaInterfaceTest\testCase\wordExcel\word.xlsx'  #老表
    for num in range(260):
        numm=str(num+4)
        post="A"+numm+":"+"C"+numm
        infoOld=getwordexcelinfo(oldexcel,post)
        wordlistOld=list(infoOld[2].split(":"))  #代词列表
        levelOLd=infoOld[0]
        unitOld=infoOld[1]
        oldListInfo=[levelOLd,unitOld,wordlistOld]

        #新版本数据
        wordlistNew=[]



        #新版本数据

        difflist=diffWord(wordlistOld,wordlistNew)
        for diff in difflist:
            if diff in wordlistOld:
                print(diff,'单词在老表的位置是：level',str(levelOLd)+"  unit是：",str(unitOld))

        for diff in difflist:
            if diff in wordlistNew:
                print(diff,'单词在新表的位置是：level',str(levelNew)+"  unit是：",str(unitNew))


