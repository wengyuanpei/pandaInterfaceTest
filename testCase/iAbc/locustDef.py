
from locust import HttpUser, task, between,TaskSet
import requests


class MyTaskCase(TaskSet):
    # 初始化方法，相当于 setup
    def on_start(self):
        pass
    #执行权重
    @task(2)
    def request1(self):
        url = '/erp/regist'  # 接口请求的URL地址
        self.headers = {"Content-Type": "application/json"}

        # 使用self.client发起请求，请求的方法根据接口实际选,
        # catch_response 值为True 允许为失败 ， name 设置任务标签名称   -----可选参数
        rsp = self.requests(url, json=data, headers=self.headers, catch_response=True, name='api_regist')
        if rsp.status_code == 200:
            rsp.success()
        else:
            rsp.failure('regist_ 接口失败！')

    @task  # 装饰器，说明下面是一个任务
    def request2(self):
        url = '/erp/loginIn'  # 接口请求的URL地址
        data = {"name": self.user, "pwd": self.pwd}
        rsp = self.client.post(url, json=data, headers=self.headers,
                               catch_response=True)  # 使用self.client发起请求，请求的方法 选择post
        self.token = rsp.json()['token']    # 提取响应json 中的信息，定义为 类变量
        if rsp.status_code == 200 and rsp.json()['code'] == "200":
            rsp.success()
        else:
            rsp.failure('login_ 接口失败！')

    @task  # 装饰器，说明下面是一个任务
    def request3(self):
        url = '/erp/user'  # 接口请求的URL地址
        headers = {"Token": self.token}  # 引用上一个任务的 类变量值   实现参数关联
        rsp = self.client.get(url, headers=headers, catch_response=True)  # 使用self.client发起请求，请求的方法 选择 get
        if rsp.status_code == 200:
            rsp.success()
        else:
            rsp.failure('getuser_ 接口失败！')

    # 结束方法， 相当于teardown
    def on_stop(self):
        pass


# 定义一个运行类 继承HttpLocust类， 所以要从locust中引入 HttpLocust类
class UserRun(HttpLocust):
    task_set = MyTaskCase  # 定义固定的 task_set  指定前面的任务类名称
    wait_time = between(0.1, 3)  # 设置运行过程中间隔时间 需要从locust中 引入 between


'''
运行：
    在终端中输入：locust -f 被执行的locust文件.py --host=http://被测服务器域名或ip端口地址
    也可以不指定host
命令执行成功，会提示服务端口，如：*：8089
此时，则可通过浏览器访问机器ip:8089,看到任务测试页面
'''

