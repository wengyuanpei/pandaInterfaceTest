# import openpyxl
#
# excel_dir='C:\Users\zhang\Desktop\无标题.xls'
import json
import os
import openpyxl

path = r"C:\Users\zhang\Desktop"
os.chdir(path)  # 修改工作路径

workbook = openpyxl.load_workbook('新计划绘本模板数据.xlsx')  # 返回一个workbook数据类型的值
sheet = workbook.active  # 获取活动表
# print('当前活动表是：')
# print(sheet)

cell = sheet['E2:E1056']  # 获取A1到A5的数据

# print(cell)

list_data=[]
day=0
# 打印A1到A5的数据
for i in cell:
    day+=1
    for j in i:
        json_data=json.loads(j.value)
        for ii in json_data["audio_book_ids"]:
            if ii>2956:
                print("第",day,"天，错误id",ii)






