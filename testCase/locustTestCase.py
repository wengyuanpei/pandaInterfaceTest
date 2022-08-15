from locust import HttpUser, TaskSet, task,events
from pandaInterfaceTest.parameter.locustParameter import *
import json


@events.test_start.add_listener
def on_test_start():
    print('===测试最开始提示===')


@events.test_stop.add_listener
def on_test_stop():
    print('===测试结束了提示===')

# 定义每个用户的任务集合
class DeptList(TaskSet):


    # 任务A--GET示例
    @task(7)        # 权重 7/ 10
    def t_login(self):
        url = url_001()
        h = headerForRequests()

        #get接口数据包
        data = dataForGet()

        # catch_response =True：允许该请求被标记为失败
        with self.client.get(url, headers=h, params=data, catch_response=True) as response:
            if response.status_code == 200:
                response.success()

    # 任务B--POST示例
    @task(3)        # 权重 3/ 10
    def t_query_dept(self):
        url = url_001()
        h =headerForRequests()

        entity = dataForPost()

        body = {'entityInfo': json.dumps(entity)}

        with self.client.post(url, headers=h, data=body, catch_response=True) as response:
            if response.status_code == 200:
                response.success()


# 继承Locust类
# 生成的每一个虚拟的HTTP用户
# 用来发送请求到进行负载测试的系统
class Login(HttpUser):
    tasks = [DeptList]
    # 权重
    weight = 1
    # 执行事务之间用户最小等待时间
    min_wait = 1000
    # 执行事务之间用户最大等待时间
    max_wait = 3000
    # 超时时间
    stop_timeout = 5
    #定义测试host
    host = "10.227.253.226:7000"


if __name__ == "__main__":

    import os
    os.system("locust -f locustForPanda.py --host=https://www.baidu.com")