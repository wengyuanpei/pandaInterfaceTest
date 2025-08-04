import openpyxl
import pymysql
file=openpyxl.load_workbook("P025.xlsx")
sheet=file.active
content=sheet["A1:C5"]

for i in content:
    for j in i:
        print(j.value)


# connt=pymysql.connect(
#     host="",
#     user="",
#     password="",
#     database=""
#
# )
# cur=connt.cursor()
# cur.execute("")

from locust import TaskSet,task,HttpUser,between

#任务类
class Mytaskset(TaskSet):
    @task
    def test(slef):
        print("测试任务")

#用户类
class Myuser(HttpUser):
    tasks = [Mytaskset]
    wait_time=between(5.0,8.0)

if __name__ == "__main__":
    import os
    os.system("locust -f sty_excel.py --host=http://hear-dev.abctime.com")
