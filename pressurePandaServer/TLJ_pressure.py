import json
import os
from locust import TaskSet, task, HttpUser,between
import random
import requests

# 创建任务类
class tlj_pressure(TaskSet):
    def on_start(self):
        # 初始化方法on_start，相当于setup

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
        req1 = self.client.post(url_hb,json=data_hb)


        #返回bookid 作为其他接口的参数
        lenth = len(req1.json()['data']['records'])
        # print('lenth:', lenth)
        raadom = random.randint(1, lenth)
        # print('raadom:', raadom)
        self.bookID = req1.json()['data']['records'][raadom]['id']
        # print('bookID:', self.bookID)
        return  self.bookID

    # 绘本内容
    @task(3)
    def data_hbc(self):
        bookID=self.data_hb()
        print('#绘本内容')
        url_hbx = '/v1/book/book-content'
        data_hbc = {
                      "book_id": bookID
                    }
        req2 = self.client.post(url_hbx, json=data_hbc)
        # print(req2.text)

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
        req3 = self.client.post(url_hbx, json=data_hbx)
        # print(req3.text)

    #单词列表
    @task(2)
    def data_dc(self):
        # print('')
        url_dc='/v1/book/words-list'
        data_dc={
              "uid": self.uuid,
              "status": 2,
              "size": 100,
              "current": 1
            }
        req4=self.client.post(url_dc,json=data_dc)





    def on_stop(self):
        # 清除方法，相当于teardown
        print('清除数据')


# 创建用户类
class TLJ(HttpUser):
    wait_time = between(1,5)   #设置运行过程中的间隔时间，需要在locust中引入between
    tasks = [tlj_pressure]
    min_wait = 1000
    max_wait = 2000



if __name__ == '__main__':
    os.system("locust -f test_locust_tlj.py --host=http://hear-dev.abctime.com")