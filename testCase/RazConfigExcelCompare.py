from common.excelreadwrite import *

def getwordexcelinfo(oldexcel,info):
     wordInfo=excel_read(oldexcel,info)
     return wordInfo


def diffWord(oldlist,newlist):
    listend=[]
    list=[]
    listdif=set(oldlist)-set(newlist)
    if len(listdif)>0:
        list.append(listdif)
        for i in list:
            for a in i:
                listend.append(a)


    return listend


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
    # print('老版本单词表',oldWordlist)
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
    # print('新版本单词表',newWordlist)

    diffIdList=[]
    for old,new in zip(oldWordlist,newWordlist):
        diffIdLists=diffWord(old[2],new[2])
        if len(diffIdLists)>0:
            diffIdList.append(diffIdLists)
    diffend=[]
    for diff in diffIdList:
        for i in diff:
            diffend.append(i)
    print('差异的列表：',diffend)

    for diffwordid in diffend:

        for widOld,widNew in zip(oldWordlist,newWordlist):

            nowlevel=widOld[0]
            nowunit=widOld[1]

            print('当前level：',nowlevel,'当前unit：',nowunit)
            if diffwordid in widOld[2]:
                print(diffwordid,"单词在老配置表的level：",widOld[0],'unit是：',widOld[1])

            if diffwordid in widNew[2]:
                print(diffwordid, "单词在新配置表的level：", widNew[0], 'unit是：', widNew[1])
