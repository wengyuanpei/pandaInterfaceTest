#coding:utf-8

from common.excelreadwrite import *
import json
base=r'C:\Users\zhang\Desktop\听力机资源'

dateill=r'\plan_detail.xlsx'

idss=r'\plan_ids.xlsx'

dateail_ids=base+dateill
#计划表
detail1=excel_read(dateail_ids,'A2:A1056')
# print(detail1)

#配置excel
plan_idss=base+idss
detail2=excel_read(plan_idss,'A1:A1055')

for detailstr,idsss in zip(detail1,detail2):
    # print(type(detailstr))
    # detailstr=detailstr['audio_book_ids']+detailstr['audio_ids']
    print(detailstr,"####",idsss)