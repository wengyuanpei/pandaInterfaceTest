import openpyxl
import pandas as pd


def excel_read(excelname:str,getvaluestation:str)->list:

    # print('文件绝对路径' ,'想要获取的数据位置如："A1：A2"','返回的是一个列表')
    celllist =[]
    workbook = openpyxl.load_workbook(excelname)
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
    # print('写入数据列表' ,'起始行位置（自动递增）' ,'起始表格列位置' ,'文件绝对路径','sheet名字')
    workbook = openpyxl.load_workbook(excelname)
    start =start
    station =station
    wb=workbook[sheetname]
    for xin in cell_list:
        wb[station + str(start)] = xin
        start += 1
    workbook.save(excelname)
    print('文件写入成功！')

def excel_group(excelname: str,sheet_name: str,listdata:list,groupdata:str):
    print('excel地址，sheet名字，需要合并的字段，需要被合并的值')
    print("将excel中的多个相同属性的值合并到一起输出为一个列表形式例如：[1, 'Unit 1', 'Day 1', '学单词', 1, ['apple', 'banana', 'pear']]")
    print("输出为列表的形式")
    df = pd.read_excel(excelname, sheet_name=sheet_name)
    # 合并数据
    grouped = df.groupby(listdata)[groupdata].apply(list).reset_index()
    # 将结果转换为所需的格式
    result_data = grouped.values.tolist()
    return result_data
