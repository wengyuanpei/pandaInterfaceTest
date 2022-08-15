from locust import HttpUser, TaskSet, task
import json

# 定义每个用户的任务集合
class DeptList(TaskSet):

    # 任务A--GET示例
    @task(7)        # 权重 7/ 10
    def t_login(self):
        url = '/api/ip/ipdept/deptList'
        h = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
             "Cookie": "sessionToken=2e183b7bb566461d"}
        data = {'draw': '5',
                'start': '0',
                'length': '13',
                'deptTypes': '[]',
                'defunctInd': 'N',
                'searchStr': 'FSK_01',
                '_': '1597112917355'}

        # catch_response =True：允许该请求被标记为失败
        with self.client.get(url, headers=h, params=data, catch_response=True) as response:
            if response.status_code == 200:
                response.success()

    # 任务B--POST示例
    @task(3)        # 权重 3/ 10
    def t_query_dept(self):
        url = '/api/ip/entity/save'
        h = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
             "Content-Length": "355",
             "Cookie": "sessionToken=6b67c3bfd60c4008"}
        entity = {"ipEntityMstrId": 7233101,
                      "entityCode": "BLL1",
                      "entityDesc": "BLL2019",
                      "entityDescLang1": "BLL2019#",
                      "shortCode": "BLL",
                      "seqNo": "1",
                      "entityNameAlias": "BL",
                      "entityNameAlias1": "BL#",
                      "addressDetail": "详细地址111"}

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
    host = "10.227.253.226:7000"
