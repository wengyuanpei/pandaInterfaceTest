from common.excelreadwrite import *


def studyFlowExcelInfo(path,excelposition):
    excel=excel_read(path,excelposition)
    del excel[1:4]
    return excel


if __name__ == '__main__':
    #处理每一列配置表数据


    excelpath=r"C:\Users\zhang\Documents\pandaInterfaceTest\testCase\iAbc\studyFlow\StudyFlow(20240627).xlsx"
    gameName=[
        ['I002','拼图'],
        ['P0004','记忆卡牌'],
        ['P002','赛跑比赛'],
        ['P003','拼字母游戏敲冰块'],
        ['P004','小汽车拼单词'],
        ['P005','火车拼句子'],
        ['P006','修桥拼句子'],
        ['P0061','字母描写'],
        ['P007','音阶拼单词'],
        ['P008','羊了个羊'],
        ['P009','传送带'],
        ['P0091','单词排队舞台拼单词'],
        ['P010','赛车游戏'],
        ['P011','过河游戏'],
        ['P012','赛车游戏·新'],
        ['P013','拼图·新'],
        ['P0251','朗读闪卡'],
        ['P5001','小怪兽拼装'],
        ['P5002','小怪兽洗澡'],
        ['P9001','泡泡.新'],
        ['P9002','土拨鼠'],
        ['P9003','涂抹照片'],
        ['P9004','兔子·新'],
        ['P9006','橱柜买东西'],
        ['P9007','看图拖字母'],
        ['P9009','绘本选图'],
        ['P9011','跳台子·新']]

    # 配置表id
    idposition = "A2:A2431"
    excelId=studyFlowExcelInfo(excelpath,idposition)
    print(excelId)

    # 配置表level
    levelposition = "B2:B2431"
    excelLevel = studyFlowExcelInfo(excelpath, levelposition)
    print(excelLevel)

    # 配置表unitId
    unitIdposition = "C2:C2431"
    excelUnitId = studyFlowExcelInfo(excelpath, unitIdposition)
    print(excelUnitId)

    # 配置表lessonId
    lessonIdposition = "D2:D2431"
    excelLessonId = studyFlowExcelInfo(excelpath, lessonIdposition)
    print(excelLessonId)

    # 配置表stepId
    stepIdposition = "F2:F2431"
    excelStepId = studyFlowExcelInfo(excelpath, stepIdposition)
    print(excelStepId)

    # 配置表gameCode
    gameCodeposition = "H2:H2431"
    excelGameCode = studyFlowExcelInfo(excelpath, gameCodeposition)
    print(excelGameCode)

    # 配置表gameCode
    wordslistposition = "I2:I2431"
    excelWords_list = studyFlowExcelInfo(excelpath, wordslistposition)
    print(excelWords_list)

    # 配置表复杂游戏的通用json数据结构 jsonData
    jsonDataposition = "Q2:Q2431"
    excelJsonData = studyFlowExcelInfo(excelpath, jsonDataposition)
    print(excelJsonData)
