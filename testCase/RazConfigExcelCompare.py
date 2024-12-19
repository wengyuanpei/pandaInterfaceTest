from common.excelreadwrite import *

def getwordexcelinfo(oldexcel,info):
     wordInfo=excel_read(oldexcel,info)
     return wordInfo


def diffWord(oldlist,newlist):
    listdif=set(oldlist)-set(newlist)
    return listdif


if __name__ == '__main__':
    # 老表数据处理
    oldexcel = r'C:\Users\zhang\Documents\pandaInterfaceTest\testCase\wordExcel\word.xlsx'
    oldWordlist=[]
    for num in range(260):
        numm=str(num+4)
        post="A"+numm+":"+"C"+numm
        infoOld=getwordexcelinfo(oldexcel,post)
        wordlistOld=list(infoOld[2].split(":"))  #处理数据列表
        levelOLd=infoOld[0]
        unitOld=infoOld[1]
        oldListInfo=[levelOLd,unitOld,wordlistOld]
        oldWordlist.append(oldListInfo)
    print('老版本单词表',oldWordlist)
    #新版本数据
    newexcel=r'C:\Users\zhang\Documents\pandaInterfaceTest\testCase\wordExcel\word1.xlsx'
    newWordlist=[]
    for num in range(260):
        numm=str(num+4)
        post="A"+numm+":"+"C"+numm
        infoNew=getwordexcelinfo(newexcel,post)
        wordlistNew=list(infoNew[2].split(":"))  #处理数据列表
        levelNew=infoNew[0]
        unitNew=infoNew[1]
        newListInfo=[levelNew,unitNew,wordlistNew]
        newWordlist.append(newListInfo)
    print('新版本单词表',newWordlist)


    for old,new in zip(oldWordlist,newWordlist):
        print(old,new)
        diffIdList=diffWord(old[2],new[2])


        for diffId in diffIdList:
            for oldunitlist in oldWordlist:
                for oldIdd in oldunitlist[2]:
                    if diffId==oldIdd:
                        print('单词id',diffId,'在老版本的 level：',oldunitlist[0],'unit:',oldunitlist[1])

            for newunitlist in newWordlist:
                for newidd in newunitlist[2]:
                    if diffId == newidd:
                        print('单词id', diffId, '在老版本的 level：', newunitlist[0], 'unit:', newunitlist[1])





