from common.excelreadwrite import *


filename=r'C:\Users\zhang\Desktop\新建 XLSX 工作表.xlsx'
tion='A1:A923'
read=excel_read(filename,tion)




excel_write(read,1,'A',filename,'Sheet3')