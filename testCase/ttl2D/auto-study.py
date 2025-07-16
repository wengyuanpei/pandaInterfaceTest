import pymysql
from datetime import datetime, timedelta
import os
import requests
from common.excelreadwrite import excel_read
from time import sleep


def execute(cmd):
    """执行系统命令并返回结果列表"""
    try:
        result = os.popen(cmd)
        context = result.read()
        lines = [line.strip() for line in context.splitlines()]
        result.close()
        return lines
    except Exception as e:
        print(f"执行命令失败: {e}")
        return []


def execute_redis(uid):
    """清空指定用户当天的学习记录缓存"""
    today = datetime.now()
    formatted_date = str(today.strftime("%Y%m%d"))

    cmd_connect = "redis-cli -h xue-xi-yan-fa-redis-nextapp-twproxy.xesv5.com -p 2080 -a hSL18msdMCrxp5Z_"
    cmd_del = f"del preschool:study:v2:user_today_finished_day:{uid}:{formatted_date}"

    execute(cmd_connect)  # 注意：原代码此处错误地递归调用 execute_redis
    execute(cmd_del)
    print("redis已清空")


def fix_mysql_time(uid: str):
    """更新用户的数据库学习时间字段"""
    try:
        conn = pymysql.connect(
            host=os.getenv('MYSQL_HOST', '10.176.5.167'),
            port=int(os.getenv('MYSQL_PORT', 2883)),
            user=os.getenv('MYSQL_USER', 'next_test_all_rw'),
            password=os.getenv('MYSQL_PASSWORD', 'USVkUu19XvrtGyb_'),
            database='preschool_study',
            charset='utf8mb4'
        )

        yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
        suffix = uid[-2:]

        # 防止非法表名注入
        if not suffix.isalnum():
            raise ValueError("Invalid UID suffix")

        table_name = f"abc_user_progress_{suffix}"

        sql = f"""
        UPDATE `{table_name}` 
        SET last_study_at = %s,
            first_finish_at = %s
        WHERE user_id = %s
        """

        with conn.cursor() as cursor:
            cursor.execute(sql, (yesterday, yesterday, uid))
            conn.commit()
            print(f"用户 {uid} 的学习记录数据库时间已更新为 {yesterday}")

    except pymysql.Error as e:
        print(f"MySQL操作失败: {e}")
    except Exception as e:
        print(f"未知错误: {e}")
    finally:
        if 'conn' in locals() and conn:
            conn.close()


def get_study_plan_config(book: int, unit: int, day: int):
    """获取学习计划配置数据"""
    offset_map = {1: 0, 2: 8, 3: 20}
    unit_offset = offset_map.get(book, 0)
    target_unit = unit + unit_offset

    reportlist = []

    for row_number in range(2, 172):
        row_data = excel_read("ttlstudydate.xlsx", f"A{row_number}:C{row_number}")
        if not row_data:
            continue
        b, u, d = row_data[0], row_data[1], row_data[2]
        reportlist.append([b, u, d])

        if b == book and u == target_unit and d == day:
            break

    # 构造 stage 列表
    stagelist1 = list(range(1, len(reportlist) * 4 + 1))
    stagelist3 = [stagelist1[i:i + 4] for i in range(0, len(stagelist1), 4)]

    result = []
    for i, item in enumerate(reportlist):
        for num in stagelist3[i]:
            if num % 4 != 0:
                new_item = item.copy()
                new_item.append(num)
                result.append(new_item)
    return result


def finish_day(report_list: list, token: str):
    """提交每日学习进度"""
    url = 'https://app-test.chuangjing.com/abc-api/preschool/study/report-daily-proscess'
    headers = {
        "ntu-token": token
    }
    book, unit, day, stage = report_list[0], report_list[1], report_list[2], report_list[3]
    body = {"stage_id": stage, "learn_day_id": day, "book_id": book, "unit_id": unit}

    try:
        response = requests.post(url=url, json=body, headers=headers)
        print(response.status_code)
        print(f"在完成{book}下的{unit}第{day}天的step{stage}任务")
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")


if __name__ == "__main__":
    book = 1
    unit = 2
    day = 2
    uid = '123'
    token = ''

    config_list = get_study_plan_config(book, unit, day)
    for report_list in config_list:
        sleep(1)
        finish_day(report_list, token)
        execute_redis(uid)
        sleep(2)
        fix_mysql_time(uid)
        sleep(2)
