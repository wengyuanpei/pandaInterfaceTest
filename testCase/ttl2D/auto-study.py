import redis
import pymysql
from datetime import datetime, timedelta
import os
import subprocess
import re

import requests

from common.excelreadwrite import excel_read


def execute_redis_command(command_type, key, value=None):

    REDIS_HOST = "10.176.5.171"
    REDIS_PORT = 2080
    REDIS_PASSWORD = "hSL18msdMCrxp5Z_"
    REDIS_CLI_PATH = r"G:/redis-cli.exe"  # 指定客户端软件安装位置

    try:
        # 构造基础命令
        base_cmd = [
            REDIS_CLI_PATH,
            "-h", REDIS_HOST,
            "-p", str(REDIS_PORT),
            "-a", REDIS_PASSWORD
        ]

        # 根据命令类型构建完整命令
        if command_type.lower() == "delunit":  #删除unit的key
            full_cmd = base_cmd + ["del", key]
            print(full_cmd)
        elif command_type.lower() == "setunit":    #设置新的unit day
            # 先执行get命令获取当前值
            get_cmd = base_cmd + ["get", key]
            get_result = subprocess.run(
                get_cmd,
                capture_output=True,
                text=True,
                encoding='utf-8',
                check=True
            )
            today = datetime.now().strftime('%Y%m%d')
            # 使用正则替换最后8位数字（日期部分）
            updated_str = re.sub(r'\d{8}$', today, key)
            current_value = get_result.stdout.strip() if get_result.stdout else ""
            new_value = f"{current_value}{value}" if value else current_value
            # 构建set命令
            # full_cmd = base_cmd + ["set", updated_str, " ",new_value]
            full_cmd = base_cmd + [
                "set",
                updated_str,  # key部分
                new_value  # value部分（自动用一个空格分隔）
            ]
            print(full_cmd)
        elif command_type.lower() == "delday":
            full_cmd = base_cmd + ["del", key]
            print(full_cmd)
        else:
            print("不支持的命令类型或缺少必要参数")
            return None

        # 执行最终命令
        result = subprocess.run(
            full_cmd,
            capture_output=True,
            text=True,
            encoding='utf-8',
            check=True
        )

        # 处理错误输出
        if result.stderr:
            print("Redis错误:", result.stderr.strip())
            return None

        # 返回处理后的结果
        return result.stdout.strip() if result.stdout else None

    except subprocess.CalledProcessError as e:
        print(f"命令执行失败: {e}\n错误输出: {e.stderr}")
        return None
    except Exception as e:
        print(f"未知错误: {e}")
        return None
def fix_mysql_time(uid):
    try:
        conn = pymysql.connect(
            host='10.176.5.167',
            port=2883,
            user='next_test_all_rw',
            password='USVkUu19XvrtGyb_',
            database='preschool_study',
            charset='utf8mb4'
        )

        yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y%m%d %H:%M:%S')
        suffix = str(uid)[-2:]
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
            print(f"用户 {uid} 的时间已更新为 {yesterday}")

    except pymysql.Error as e:
        print(f"MySQL操作失败: {e}")
    finally:
        if conn:
            conn.close()
def generate_stage_ids(day_number):

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
def finish_day(book,unit,day,uid):

    finish_book=[]
    for book_num in range(1,book+1):
        finish_book.append(book_num)
    finish_unit1=[]
    if book==1:
        for unit_num  in range(1,unit+1) :
            finish_unit1.append(unit_num)
    elif book==2:
        for unit_num  in range(1,unit+1+8) :
            finish_unit1.append(unit_num)
    elif book==3:
        for unit_num  in range(1,unit+1+20) :
            finish_unit1.append(unit_num)
    all_day = 1
    for finish_book_num in finish_book:
        for finish_unit1_num in finish_unit1:

            for dayy in range(1,6):
                # stage_id_start = 1
                current_stage_ids = generate_stage_ids(all_day)
                for current_stage in current_stage_ids:
                    url = 'https://app-test.chuangjing.com/abc-api/preschool/study/report-daily-proscess'
                    header = {
                        "ntu-token": uid
                    }
                    body = {"stage_id": 1, "learn_day_id": dayy, "book_id": finish_book_num, "unit_id": finish_unit1_num}
                    # req = requests.post(url=url, json=body, headers=header)
                    print(f"在完成{finish_book_num}下的{finish_unit1_num}第{dayy}天的step{current_stage}任务")
                all_day += 1
                if book==finish_book_num and unit==finish_unit1_num and day==dayy:
                    break



def redis_cmd(type,uid):
    current_time_day = datetime.now().strftime('%Y%m%d')
    tomorrow = (datetime.now() + timedelta(days=1)).strftime('%Y%m%d')
    if type=="delday":
        cmd_delday=f"preschool:study:v2:user_today_finished_day:{uid}:{current_time_day}"
        return cmd_delday

    elif type=="delunit" or "setunit": #删除的日期是+1的
        cmd_unit=f"preschool:study:v2:user_next_book_unit_learning_day:{uid}:{tomorrow}"
        return cmd_unit


if __name__ == "__main__":


    type="delday"       #需要操作的类型
    uid='123'
    redis_cmd=redis_cmd(type,uid)
    execute_redis_command(type,redis_cmd)

