import xlrd
from testCase import translate
import xlsxwriter as xw


def getexcellieinfo(col_value):
    if col_value==0:
        print('英文原文！')
    if col_value==1:
        print('英文译文！')
    if col_value not in (0,1):
        print('输入错误请输入0或1获取内容！')

    worksheet = xlrd.open_workbook(r'C:\Users\zhang\Desktop\pandaInterfaceTest\testCase\log\ai.xls')
    sheet_names= worksheet.sheet_names()
    print(sheet_names)
    sheet1 = worksheet.sheet_by_name(sheet_names[0])
    cols1 = sheet1.col_values(col_value) # 获取第二列内容， 数据格式为此数据的原有格式（原：字符串，读取：字符串；  原：浮点数， 读取：浮点数）
    print(cols1)

    return cols1
 #查看数据类型


def xw_toExcel(data, fileName):  # xlsxwriter库储存数据到excel
    workbook = xw.Workbook(fileName)  # 创建工作簿
    worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    worksheet1.activate()  # 激活表
    title = ['序号', '酒店', '价格']  # 设置表头
    worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
    i = 2  # 从第二行开始写入数据
    for j in range(len(data)):
        insertData = [data[j]["id"], data[j]["name"], data[j]["price"]]
        row = 'A' + str(i)
        worksheet1.write_row(row, insertData)
        i += 1
    workbook.close()



if __name__ == '__main__':
    list=getexcellieinfo(0)
    list1 = getexcellieinfo(1)
    for i in list:
        trans=i

        Obj = translate.trans()
        text = " "+trans+" "
        res = Obj.tran(text)
        print('英语',trans,'译文',res)


