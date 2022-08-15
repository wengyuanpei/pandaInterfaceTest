from locust import HttpLocust
from locust import HttpUser
from locust import task
from locust import TaskSet


# 指定一个任务集
class My_task_set(TaskSet):

    # 这是某个任务,30是比例，比如这里是30/50
    @task(30)
    def getindex1(self):
        # client就是个requests对象
        # catch_response，告诉locust如何判断请求失败还是成功
        res = self.client.get("/bainianminguo/p/10952586.html")

    @task(20)
    def getindex2(self):
        # client就是个requests对象
        res = self.client.get("/bainianminguo/p/7253930.html")


class WebSite(HttpUser):
    # 指定要执行哪个任务集
    tasks = [My_task_set, ]
    # 请求和请求之间最小的间隔时间
    min_wait = 1000
    # 请求和请求之间最大的间隔时间
    max_waif = 2000

# 启动命令  >locust -f locustForPanda.py --host=https://www.cnblogs.com