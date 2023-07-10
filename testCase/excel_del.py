import json
import os
import openpyxl
import requests
from time import sleep
import xlwt


path = r"C:\Users\zhang\Desktop"
os.chdir(path)  # 修改工作路径

workbook = openpyxl.load_workbook('SN汇总统计.xlsx')  # 返回一个workbook数据类型的值
sheet = workbook.active  # 获取活动表
# print('当前活动表是：')
print(sheet)

cell1 = sheet['A2:A52904']  # 获取A1到A5的数据

cell2 = sheet['B2:B13816']  # 获取A1到A5的数据



cell1list=[]
cell2list=[]
for i in cell1:
    for j in i:
        print(j.value)
        cell1list.append(j.value)

for ii in cell2:
    for jj in ii:
        print(jj.value)
        cell2list.append(jj.value)
print(len(cell1list))
errorlist=[]
for sm in cell2list:
    if sm in cell1list:
        print('售卖SN统计正确！')
        cell1list.remove(sm)
    else:
        errorlist.append(sm)
wb=workbook['1.26新用户SN']
start=2
print(len(cell1list))
print()
for xin in cell1list:
    wb['C'+str(start)]=xin
    start+=1
workbook.save("SN汇总统计.xlsx")

