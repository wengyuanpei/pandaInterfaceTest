
#学习计划的计算翻译


booklist=[[  'aa',1,155,787],
        [  'A',2,93,595],
        [  'B',3,97,673],
        [  'C',4,95,777],
        [  'D',5,88,742],
        [  'E',6,86,504],
        [  'F',7,83,491],
        [  'G',8,83,478],
        [  'H',9,77,428],
        [  'I',10,70,381],
        [  'J',11,74,413],
        [  'K',12,69,102],
        [  'L',13,66,133],
        [  'M',14,52,129],
        [  'N',15,53,136],
        [  'O',16,49,134],
        [  'P',17,44,166],
        [  'Q',18,54,180],
        [  'R',19,54,206],
        [  'S',20,44,213],
        [  'T',21,43,221],
        [  'U',22,42,246],
        [  'V',23,32,201],
        [  'W',24,37,243],
        [  'X',25,41,261],
        [  'Y',26,45,257],
        [  'Z',27,112,496],]



def cuntnow(userInput):

    for nowlevel in booklist:

        if nowlevel[0]==userInput:
            nowbooknum = nowlevel[2]
            nowwordnum = nowlevel[3]
            return nowbooknum,nowwordnum

def cuntaim(userInputAim):

    for nowlevel in booklist:

        if nowlevel[0] == userInputAim:
            aimbooknum = nowlevel[2]
            aimwordnum = nowlevel[3]
            return aimbooknum, aimwordnum


if __name__ == '__main__':
    userInput = (input('输入用户的当前等级：'))

    userInputAim = (input('输入用户的目标等级：'))

    weekDay=input('输入每周学习的天数：')
    yeartoaim=input('输入多少年达到目标：')
    cuntnow= cuntnow(userInput)
    cuntaim= cuntaim(userInputAim)

    allbooknum=int(cuntnow[0]+cuntaim[0])
    allwordsnum=int(cuntaim[1]+cuntnow[1])
    print('共计学习绘本数%d,共计学习单词数%d' %(allbooknum,allwordsnum))
    #计算学习平均每天学习绘本数
    bookStudy=float(allbooknum/float(weekDay)/52/float(yeartoaim))

    bookStudy=round(bookStudy,1)

    wordsStudy=float(allwordsnum/float(weekDay)/52/float(yeartoaim))
    wordsStudy=round(wordsStudy,1)
    print('每天学习绘本数%s          每天学习单词数%s' %(str(bookStudy),str(wordsStudy)))


    words =round(allwordsnum /365/int(yeartoaim),1)
    print('按照365天进行单词数学习计算，每天学习单词为%s' %(str(words)))