import openpyxl


def excel_read(excelname ,getvaluestation):

    print('文件绝对路径' ,'想要获取的数据位置如："A1：A2"','返回的是一个列表')
    celllist =[]
    excelname =excelname
    workbook = openpyxl.load_workbook(excelname)  # 返回一个workbook数据类型的值
    sheet = workbook.active  # 获取活动表
    print('当前操作的表是：')
    print(sheet)
    cell1 = sheet[getvaluestation]  # 获取A1到A5的数据
    for i in cell1:
        for j in i:
            print(j.value)
            celllist.append(j.value)
    return celllist

def excel_write(celllist ,start ,station ,excelname,sheetname):
    print('写入文件名字' ,'数字开始位置' ,'表格字母开始位置' ,'文件绝对路径','sheet名字')
    workbook = openpyxl.load_workbook(excelname)
    start =start
    station =station
    wb=workbook[sheetname]
    for xin in celllist:
        wb[station + str(start)] = xin
        start += 1
    workbook.save(excelname)
