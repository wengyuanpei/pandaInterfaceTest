import time
from locust import HttpUser, task, between, events

from locust.contrib.fasthttp import FastHttpLocust



@events.test_start.add_listener
def on_test_start(**kwargs):
    print('===测试最开始提示===')


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    print('===测试结束了提示===')


class TestTask(HttpUser):
    wait_time = between(1, 5)
    # host = 'https://www.baidu.com'

    def on_start(self):
        print('这是SETUP，每次实例化User前都会执行！')

    @task(1)
    def getBaidu(self):
        self.client.get(url="/", verify=False)

    def on_stop(self):
        print('这是TEARDOWN，每次销毁User实例时都会执行！')

class MyLocust(FastHttpLocust):

    task_set = TestTask
    min_wait = 1000
    max_wait = 60000

if __name__ == "__main__":

    import os

    os.system("locust -f locustDemo1.py --host=https://www.baidu.com")
#  locust -f dept_list.py --worker(从节点)/--master（主节点） --master-host=192.168.x.xx