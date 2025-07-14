import requests
from common.excelreadwrite import excel_group


def get_excel_date():
    groupp = ['book_id', 'unit_number', 'day', 'stage', 'unit_id']
    groupby = 'content'
    excelpath = 'ttlstudydate.xlsx'
    sheetname = 'Sheet1'
    result_data = excel_group(excelpath, sheetname, groupp, groupby)
    return result_data


# 获取接口返回的每日计划数据合并处理成列表的形式和配置表做对比
def get_plan_interfacedate():
    bookId = []
    unitId = []
    dayId = []
    studyType = []
    url = ''
    header = {}
    body = {}
    req = requests.post(url, header, body)
    jsondata = req.json()
    interfacedata = []
    interfacedata.append(1)
    return interfacedata


# 对数据
if __name__ == '__main__':
    exceldata = get_excel_date()
    interfacedata = get_plan_interfacedate()
    for day in exceldata:
        for dataw in interfacedata:
            if day[0] == dataw[0] and day[1] == dataw[1] and day[2] == dataw[2] and day[3] == dataw[3] and day[5] == \
                    day[5]:
                print("book" + str(day[0]) + "%d,%d,%d************数据一致" % day[1], day[2], day[3])
            else:
                print('excel:' + str(day) + "接口返回数据" + str(dataw))
