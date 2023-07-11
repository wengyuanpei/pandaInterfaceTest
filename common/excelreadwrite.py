import openpyxl


def excel_read(excelname:str,getvaluestation:str)->list:

    print('文件绝对路径' ,'想要获取的数据位置如："A1：A2"','返回的是一个列表')
    print(excel_read.__annotations__)
    celllist =[]
    excelname =excelname
    workbook = openpyxl.load_workbook(excelname)  # 返回一个workbook数据类型的值
    sheet = workbook.active  # 获取活动表
    print('当前操作的表是：')
    print(sheet)
    cell1 = sheet[getvaluestation]  # 获取A1到A5的数据
    for i in cell1:
        for j in i:
            # print(j.value)
            celllist.append(j.value)
    print('文件读取成功！')
    return celllist

def excel_write(cell_list: list,start: int,station: str,excelname: str,sheetname:str):
    print('写入文件名字' ,'行位置' ,'表格列位置' ,'文件绝对路径','sheet名字')
    print(excel_write.__annotations__)
    workbook = openpyxl.load_workbook(excelname)
    start =start
    station =station
    wb=workbook[sheetname]
    for xin in cell_list:
        wb[station + str(start)] = xin
        start += 1
    workbook.save(excelname)
    print('文件写入成功！')