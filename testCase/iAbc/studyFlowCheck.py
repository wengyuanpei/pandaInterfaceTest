from common.excelreadwrite import *


def studyFlowExcelInfo(path,excelposition):
    excel=excel_read(path,excelposition)
    Excel_end=excel.remove(2)
    print(excel)


