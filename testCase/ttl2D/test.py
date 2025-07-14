from common.excelreadwrite import *
def generate_stage_ids(day_number):
    """根据天数生成对应的stage_id列表"""
    if day_number < 1:
        return []
    start_num = (day_number - 1) * 4 + 1
    return [start_num, start_num + 1, start_num + 2]


def get_study_plan_config(book, unit, day):
    study_day_list = []
    for staion in range(2, 172):
        station = f"A{staion}:C{staion}"
        liststudy = excel_read("ttlstudylist.xlsx", station)
        study_day_list.append(liststudy)
        print(liststudy)
        # print(type(liststudy[0]))
        # print(type(book))
        print(liststudy[0],liststudy[1],liststudy[2])
        if liststudy[0]==book and liststudy[1]==unit and liststudy[2]==day:
            break


    return study_day_list

def finish_day(uthtoken):


    url = 'https://app-test.chuangjing.com/abc-api/preschool/study/report-daily-proscess'
    header = {"ntu-token": "uid"}
    body = {
        "stage_id": "current_stage",  # 使用生成的stage_id
        "learn_day_id": "dayy",
        "book_id": "finish_book_num",
        "unit_id": "finish_unit_num"
    }
    # req = requests.post(url=url, json=body, headers=header)
    print(f"在完成{1}下的{1}第{1}天的step{1}任务")



# 使用示例
b=2
unit=7
day=2
a=get_study_plan_config(b,unit,day)
print(a)