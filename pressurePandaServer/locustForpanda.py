import time
from locust import HttpUser, task, between, events
from locust import FastHttpUser,TaskSet
import paho.mqtt.client as mqtt

from pandaInterfaceTest.common.make_num_random import random_num
from pandaInterfaceTest.parameter.getMqttToken import getmqtttoeken



class My_task_set(TaskSet):



    def on_start(self):

        print('开始初始化！！')

        mqttpara = getmqtttoeken()
        self.mqtttoeken = mqttpara[0]
        self.mqttsn = mqttpara[1]
        self.clientID = self.mqttsn
        self.broker_url = 'emqx-dev.xiongmaoboshi.com'
        self.port = 1883

    @task(1)
    def mqtt1(self):
        def on_connect(client, userdata, flags, rc):
            print("Connected with result code :0 表示连接成功  其它表示失败，rc：" + str(rc))
            client.subscribe("chanel_01")
            print('mqtt1')

        client = mqtt.Client(self.clientID)
        client.connect(self.broker_url, self.port, 60000)
        time.sleep(1)
        client.on_connect = on_connect
        client.username_pw_set(self.mqttsn, password=self.mqtttoeken)
        client.loop_forever()  # 长连接

    @task(2)
    def mqtt2(self):
        def on_connect(client, userdata, flags, rc):
            print("Connected with result code :0 表示连接成功  其它表示失败，rc：" + str(rc))
            client.subscribe("chanel_01")
            print('mqtt2')

        client = mqtt.Client(self.clientID)
        client.connect(self.broker_url, self.port, 60000)
        time.sleep(1)
        client.on_connect = on_connect
        client.username_pw_set(self.mqttsn, password=self.mqtttoeken)
        client.loop_forever()  # 长连接

    @task(2)
    def mqtt3(self):
        def on_connect(client, userdata, flags, rc):
            print("Connected with result code :0 表示连接成功  其它表示失败，rc：" + str(rc))
            client.subscribe("chanel_01")
            print('mqtt3')

        client = mqtt.Client(self.clientID)
        client.connect(self.broker_url, self.port, 60000)
        time.sleep(1)
        client.on_connect = on_connect
        client.username_pw_set(self.mqttsn, password=self.mqtttoeken)
        client.loop_forever()  # 长连接
    @task(5)
    def mqtt4(self):
        def on_connect(client, userdata, flags, rc):
            print("Connected with result code :0 表示连接成功  其它表示失败，rc：" + str(rc))
            client.subscribe("chanel_01")
            print('mqtt4')

        client = mqtt.Client(self.clientID)
        client.connect(self.broker_url, self.port, 60000)
        time.sleep(1)
        client.on_connect = on_connect
        client.username_pw_set(self.mqttsn, password=self.mqtttoeken)
        client.loop_forever()  # 长连接



class WebSite(HttpUser):

    tasks = [My_task_set,]
    min_wait = 1000
    max_wait = 2000



if __name__ == "__main__":

    import os

    os.system("locust -f locustForPanda.py --host=http://emqx-dev.xiongmaoboshi.com")
#  locust -f dept_list.py --worker(从节点)/--master（主节点） --master-host=192.168.x.xx