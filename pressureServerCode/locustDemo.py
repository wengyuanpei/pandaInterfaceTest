import os
from locust import TaskSet, task, HttpUser,between,stats
import random

# 创建任务类
class tlj_pressure(TaskSet):
    def on_start(self):

        # 初始化方法on_start，相当于setup，创建一些请求的头信息参数或者token

        self.header={"Content-Type": "application/json;charset=UTF-8",
                     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35"}

        self.uuid=2719

    #执行权重
    #创建压测请求
    @task(1)
    def data_hb(self):
        lower_level=random.randint(3,29)
        data_hb = {
            "uid": self.uuid,
            "size": 100,
            "current": 1,
            "lower_level": lower_level
        }
        #请求是否成功的判断处理
        url_hb = '/v1/book/book-list'
        with self.client.post(url_hb, headers=self.header,json=data_hb, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure('Failed!')
        try:
            #返回bookid 作为其他接口的参数
            lenth = len(response.json()['data']['records'])
            raadom = random.randint(0, lenth-1)
            self.bookID=response.json()['data']['records'][raadom]['id']
            return self.bookID
        except:
            return 2927




    @task(3)
    def data_hbc(self):
        bookID=self.data_hb()
        url_hbx = '/v1/book/book-content'
        data_hbc = {
                      "book_id": bookID
                    }
        with self.client.post(url_hbx,headers=self.header, json=data_hbc ,catch_response=True) as responsec:
            if responsec.status_code == 200:
                responsec.success()
            else:
                responsec.failure('Failed!')




    @task(4)
    def data_hbx(self):

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




    @task(2)
    def data_dc(self):

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
    # 设置运行过程中的间隔时间，需要在locust中引入between
    wait_time = between(1,10)
    #声明执行压测的类
    tasks = [tlj_pressure]
    min_wait = 1000
    max_wait = 2000



if __name__ == '__main__':

    # --no - web - ui：启动Locust而不启动Web界面，这个参数需要与 - c和 - r一起使用，因为没有Web界面，这两个参数就没有存在的意义了。

    # -H, --host：指定被测试的网站的地址。

    # -f, --config - file：指定一个Python文件来导入配置。

    # -c, --num - clients：设置并发用户的数量。

    # -r, --hatch - rate：设置并发用户启动的速度。

    # -t, --run - time：设置测试的持续时间。

    # --csv：保存测试结果到CSV文件。

    # --logfile：保存测试过程的日志。

    # --print - stats：在测试结束后，打印测试结果到控制台。

    # --only - summary：只在测试结束后打印总结性的统计信息。


    os.system("locust -f test_locust_tlj.py --host=http://hear-dev.abctime.com")
    # locust -f dept_list.py --worker(从节点)/--master（主节点） --master-host=192.168.x.xx
    # os.system("locust -f locustForEmqx.py  --master --master-host =http://emqx-dev.xiongmaoboshi.com")

