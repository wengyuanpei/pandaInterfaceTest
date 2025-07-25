import pymysql
from datetime import datetime, timedelta
import os
import requests
from common.excelreadwrite import excel_read
from time import sleep

import os
import subprocess
from datetime import datetime


def execute(cmd):
    """执行系统命令并返回结果列表"""
    try:
        # 使用subprocess替代os.popen，提供更好的错误处理
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        result.check_returncode()  # 检查命令是否执行成功
        lines = [line.strip() for line in result.stdout.splitlines()]
        return lines
    except subprocess.CalledProcessError as e:
        print(f"命令执行失败: {e}")
        return []
    except subprocess.TimeoutExpired:
        print("命令执行超时")
        return []
    except Exception as e:
        print(f"执行命令失败: {e}")
        return []


def execute_redis(uid):
    """清空指定用户当天的学习记录缓存"""
    today = datetime.now()
    formatted_date = str(today.strftime("%Y%m%d"))

    # 将敏感信息作为环境变量或配置读取（此处保留原样以满足不改变功能要求）
    redis_host = "xue-xi-yan-fa-redis-nextapp-twproxy.xesv5.com"
    redis_port = "2080"
    redis_password = "hSL18msdMCrxp5Z_"

    # 合并为单条命令执行，确保原子性
    cmd = f"redis-cli -h {redis_host} -p {redis_port} -a {redis_password} del preschool:study:v2:user_today_finished_day:{uid}:{formatted_date}"

    execute(cmd)
    print("redis已清空")

def change_user_level(uid: str):
    today = datetime.now()
    next_day=today + timedelta(days=1)
    formatted_date = str(today.strftime("%Y%m%d"))
    print("formatted_date:", formatted_date)
    formate_nextday=str(next_day.strftime("%Y%m%d"))
    print("formate_nextday:", formate_nextday)
    # 将敏感信息作为环境变量或配置读取（此处保留原样以满足不改变功能要求）
    redis_host = "xue-xi-yan-fa-redis-nextapp-twproxy.xesv5.com"
    redis_port = "2080"
    redis_password = "hSL18msdMCrxp5Z_"

    get_cmd=f"redis-cli -h {redis_host} -p {redis_port} -a {redis_password} get preschool:study:v2:user_next_book_unit_learning_day:{uid}:{formate_nextday}"
    del_cmd=f"redis-cli -h {redis_host} -p {redis_port} -a {redis_password} del preschool:study:v2:user_next_book_unit_learning_day:{uid}:{formate_nextday}"

    try:
        # 执行获取命令
        result_get = execute(get_cmd)
        print(f"获取旧值结果: {result_get}")

        # 执行删除命令
        result = execute(del_cmd)
        print(f"删除旧键结果: {result}")

        # 执行设置命令
        result_get1 = result_get[0]
        print("result_get:", result_get)
        set_cmd = f"redis-cli -h {redis_host} -p {redis_port} -a {redis_password} set preschool:study:v2:user_next_book_unit_learning_day:{uid}:{formatted_date}"+" "+result_get1
        result = execute(set_cmd)
        print(f"设置新键结果: {result}")

        print("redis 切换至下一unit/book")
    except Exception as e:
        print(f"Redis操作失败: {e}")


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
    print( result)
    return result


def finish_day(report_list: list, token: str,uid:str):
    """提交每日学习进度"""
    url = 'https://app-test.chuangjing.com/abc-api/preschool/study/report-daily-proscess'
    headers = {
        "ntu-token": token
    }
    book, unit, day, stage = report_list[0], report_list[1], report_list[2], report_list[3]
    body = {"stage_id": stage, "learn_day_id": day, "book_id": book, "unit_id": unit}
    print(f"正在完成{book}下的{unit}第{day}天的step{stage}任务")
    try:
        response = requests.post(url=url, json=body, headers=headers)
        print(response.text)
        response.raise_for_status()
        #处理切换unit/book逻辑
        if day==5 and stage+1%4==0:
            change_user_level(uid)
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")


if __name__ == "__main__":
    book = 1
    unit = 5
    day = 3
    uid = '1090022822'
    token = '75dbebe13b44e82ec9cd7f7d3fc06d3d55e83f5243dda6c46f64d57ddefc1f6df7acda194a1b510cd62935c42b1c63c90464b0018a2d3a6a4fcf1ade1ccff60c40fd066ad7a498e7d41e0c1a75ed079fac775b20fcf67714761036592b5d290cbf4bec92fea856753f2b1decf7607702c51fa385dc5a7913e7c28aec0769577ab83d0bdd9a9eafac93b5d4cd8cd8b75d2fc812fdc036f0e92b65ad7f3fcde30e9e1befc732a0f474d89426215dbbc43880329f588d06d5bfdff43b0926af12e98a3256c0ba91bd8fc374249a1afb75ba'

    # config_list = get_study_plan_config(book, unit, day)
    # for report_list in config_list:
    #     sleep(1)
    #     finish_day(report_list, token)
    #     execute_redis(uid)
    #     sleep(1)
    #     fix_mysql_time(uid)
    #     sleep(1)
    change_user_level(uid)
