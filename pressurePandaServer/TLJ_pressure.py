import os
from locust import TaskSet, task, HttpUser,between


# 创建任务类
class Test1(TaskSet):
    def on_start(self):
        # 初始化方法on_start，相当于setup
        print('获取令牌')

    #
    @task(1)
    def data_hb(self):
        print('绘本列表')
        data_hb = {
            "uid": 2927,
            "size": 100,
            "current": 1,
            "lower_level": 3
        }
        url_hb = '/v1/book/book-list'
        req1 = self.client.post(url_hb,json=data_hb)

    @task(1)
    def data_dc(self):
        print('单词列表')
        url_dc='/v1/book/words-list'
        data_dc={
              "uid": 2927,
              "status": 2,
              "size": 100,
              "current": 1
            }
        req2=self.client.post(url_dc,json=data_dc)
    #绘本详情
    @task(5)
    def data_hbx(self):
        print('绘本详情')
        url_hbx = '/v1/book/book-detail'
        data_hbx = {
            "uid": 2729,
            "book_id": 2927
        }
        req2 = self.client.post(url_hbx, json=data_hbx)

    @task(5)
    def data_hbx(self):
        print('单词详情')
        url_dcx='/v1/book/words-list'
        data_dcx = {
            "uid": 2927,
            "status": 3,
            "size": 100,
            "current": 1
        }
        req2 = self.client.post(url_dcx, json=data_dcx)

    def on_stop(self):
        # 清除方法，相当于teardown
        print('清除数据')


# 创建用户类
class BI(HttpUser):
    wait_time = between(1,5)   #设置运行过程中的间隔时间，需要在locust中引入between
    tasks = [Test1]
    min_wait = 1000
    max_wait = 2000



if __name__ == '__main__':
    os.system("locust -f test_locust_tlj.py --host=http://hear-dev.abctime.com")