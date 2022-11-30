import json
import os
from locust import TaskSet, task, HttpUser,between,FastHttpUser
import random
import requests
from gevent._semaphore import Semaphore #集合点



# 绘本相关任务类
class light_house_hb(TaskSet):
    def on_start(self):

        self.header={"Content-Type": "application/json;charset=UTF-8",
                     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35"}
        # self.baseurl='http://lighthouse-api-dev.xiongmaoboshi.com'


    #绘本分页查询

    @task(1)
    def data_hb_cx(self):
        #绘本内容
        url='/ns/dp/lighthouse/open-api/resource/picture/book/info/list'

        pictureBookType=random.randint(1,2)

        data_hb = {
                          "sign": "string",
                          "timestamp": 1,
                          "body": {
                            "current": 0 ,
                            "lowerLevel": 0,
                            "pictureBookType": pictureBookType,
                            "size": 100,
                            "stage": 1
                          }

                }

        req=self.client.post(url, headers=self.header,json=data_hb )
        respose=req.json()['data']['records']
        lent=len(respose)
        randomm=random.randint(1,lent-1)
        # print('列表随机绘本id：',randomm)
        pictureBookId=req.json()['data']['records'][randomm]['id']

        return pictureBookId

    @task(3)
    def data_hb_xq(self):
        #绘本内容
        url='/ns/dp/lighthouse/open-api/resource/picture/book/content/list'

        bookid=self.data_hb_cx()

        data_hb = {
                  "body": {
                    "pictureBookId":bookid
                  },
                  "sign": "string",
                  "timestamp": 0
                }

        self.client.post(url, headers=self.header,json=data_hb )


    @task(2)
    def data_hb_xx(self):
        #绘本基本信息详情接口
        url='/ns/dp/lighthouse/open-api/resource/picture/book/info/detail'

        bookid=self.data_hb_cx()

        data_hb = {
                  "body": {
                    "pictureBookId": bookid
                  },
                  "sign": "string",
                  "timestamp": 0
                }


        self.client.post(url, headers=self.header,json=data_hb )


    @task(2)
    def data_hb_words(self):

        # 绘本绑定的互动单词接口
        url = '/ns/dp/lighthouse/open-api/resource/picture/book/all/word/list'

        self.client.get(url, headers=self.header)



    @task(2)
    def data_hb_words(self):
        # 绘本绑定的互动单词接口
        url = '/ns/dp/lighthouse/open-api/resource/picture/book/interactive/word/list'

        id = [1877,1878,1882,1915,1964,1882,1964,1877,1878,1915]
        bookid=random.choice(id)

        data_hb = {
                  "body": {
                    "current": 1,
                    "pictureBookId": bookid,
                    "size": 10
                  },
                  "sign": "string",
                  "timestamp": 0
                }
        self.client.post(url, headers=self.header, json=data_hb)




    def on_stop(self):
        # 清除方法，相当于teardown
        print('清除数据')

# 视频任务类
class light_house_sp(TaskSet):
    def on_start(self):

        self.header={"Content-Type": "application/json;charset=UTF-8",
                     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35"}
        # self.baseurl='http://lighthouse-api-dev.xiongmaoboshi.com'


    #视频
    @task(2)
    def data_hb_cx(self):
        #绘本内容
        url='/ns/dp/lighthouse/open-api/resource/picture/book/info/list'

        pictureBookType=random.randint(1,2)

        data_hb = {
                          "sign": "string",
                          "timestamp": 1,
                          "body": {
                            "current": 0 ,
                            "lowerLevel": 0,
                            "pictureBookType": pictureBookType,
                            "size": 100,
                            "stage": 1
                          }

                }

        req=self.client.post(url, headers=self.header,json=data_hb )
        respose=req.json()['data']['records']
        lent=len(respose)
        randomm=random.randint(1,lent-1)
        # print('列表随机绘本id：',randomm)
        pictureBookId=req.json()['data']['records'][randomm]['id']

        return pictureBookId

    @task(8)
    def data_hb_xq(self):
        #绘本内容
        url='/ns/dp/lighthouse/open-api/resource/picture/book/content/list'

        bookid=self.data_hb_cx()

        data_hb = {
                  "body": {
                    "pictureBookId":bookid
                  },
                  "sign": "string",
                  "timestamp": 0
                }

        self.client.post(url, headers=self.header,json=data_hb )


    @task(8)
    def data_hb_xx(self):
        #绘本基本信息详情接口
        url='/ns/dp/lighthouse/open-api/resource/picture/book/info/detail'

        bookid=self.data_hb_cx()

        data_hb = {
                  "body": {
                    "pictureBookId": bookid
                  },
                  "sign": "string",
                  "timestamp": 0
                }


        self.client.post(url, headers=self.header,json=data_hb )


    @task(8)
    def data_hb_words(self):
        # 绘本绑定的互动单词接口
        url = '/ns/dp/lighthouse/open-api/resource/picture/book/interactive/word/list'

        id = [1877,1878,1882,1915,1964,1882,1964,1877,1878,1915]
        bookid=random.choice(id)

        data_hb = {
                  "body": {
                    "current": 1,
                    "pictureBookId": bookid,
                    "size": 10
                  },
                  "sign": "string",
                  "timestamp": 0
                }
        self.client.post(url, headers=self.header, json=data_hb)




    def on_stop(self):
        # 清除方法，相当于teardown
        print('清除数据')

# 创建用户类
class TLJ(FastHttpUser):
    wait_time = between(1,10)   #设置运行过程中的间隔时间，需要在locust中引入between
    tasks = [light_house_hb,]
    min_wait = 1000
    max_wait = 2000

if __name__ == '__main__':
    os.system("locust -f lighthouse_pressure.py --host=http://lighthouse-api-dev.xiongmaoboshi.com  --run-time 60m")