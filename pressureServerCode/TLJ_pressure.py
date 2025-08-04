import json
import os
from locust import TaskSet, task, HttpUser,between,FastHttpUser,events
import random
import requests

from gevent._semaphore import Semaphore #集合点

@events.init.add_listener
def on_locust_init(environment, **_kwargs):
    environment.web_ui.host = "10.85.35.144"  # 强制绑定所有接口0.0.0.0
    environment.web_ui.port = 8099

# 创建任务类
class tlj_pressure(TaskSet):
    def on_start(self):
        # all_locusts_spawned = Semaphore
        # all_locusts_spawned.acquire(50)
        # 初始化方法on_start，相当于setup
        self.header={"Content-Type": "application/json;charset=UTF-8",
                     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35"}
        self.uuid=2719
        #绘本列表

    @task(1)
    def data_hb(self):
        # print('绘本列表')
        lower_level=random.randint(3,29)
        # raand=random.randint(1,100)
        data_hb = {
            "uid": self.uuid,
            "size": 100,
            "current": 1,
            "lower_level": lower_level
        }
        url_hb = '/v1/book/book-list'
        with self.client.post(url_hb, headers=self.header,json=data_hb , catch_response =True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure('Failed!')

        try:
            #返回bookid 作为其他接口的参数
            lenth = len(response.json()['data']['records'])
            # print('lenth:', lenth)
            raadom = random.randint(0, lenth-1)
            # print('raadom:', raadom)
            self.bookID = response.json()['data']['records'][raadom]['id']
            # print('bookID:', self.bookID)
            return  self.bookID
        except:
            return 2927

    # 绘本内容
    @task(3)
    def data_hbc(self):

        bookID=self.data_hb()
        # print('#绘本内容')
        url_hbx = '/v1/book/book-content'
        data_hbc = {
                      "book_id": bookID
                    }
        with  self.client.post(url_hbx,headers=self.header, json=data_hbc ,catch_response=True) as responsec:
            if responsec.status_code == 200:
                responsec.success()
            else:
                responsec.failure('Failed!')

    #绘本详情

    @task(4)
    def data_hbx(self):
        # print('绘本详情')
        bookID=self.data_hb()
        url_hbx = '/v1/book/book-detail'
        data_hbx = {
            "uid": self.uuid,
            "book_id": bookID
        }
        with  self.client.post(url_hbx, headers=self.header, json=data_hbx , catch_response=True) as responsex:
            if responsex.status_code == 200:
                responsex.success()
            else:
                responsex.failure('Failed!')


    #单词列表
    @task(2)
    def data_dc(self):
        # print('')
        current=random.randint(1,20)
        url_dc='/v1/book/words-list'
        data_dc={
              "uid": self.uuid,
              "status": 0,
              "size": 20,
              "current": 2
            }
        with self.client.post(url_dc,headers=self.header, json=data_dc) as responsecc:
            if responsecc.status_code == 200:
                responsecc.success()
            else:
                responsecc.failure('Failed!')


    def on_stop(self):
        # 清除方法，相当于teardown
        print('清除数据')


# 创建用户类
class TLJ(HttpUser):
    wait_time = between(1,10)   #设置运行过程中的间隔时间，需要在locust中引入between
    tasks = [tlj_pressure]
    min_wait = 1000
    max_wait = 2000

if __name__ == '__main__':
    os.system("locust -f TLJ_pressure.py --host=http://hear-dev.abctime.com  --run-time 60m")