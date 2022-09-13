import time
from locust import HttpUser, task, between, events
from locust.contrib.fasthttp import FastHttpUser
import random
import paho.mqtt.client as mqtt
from pandaInterfaceTest.parameter.getMqttToken import getmqtttoeken


@events.test_start.add_listener
def on_test_start(**kwargs):
    print('===测试开始===')


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    print('===测试结束===')


class TestTask(HttpUser):
    wait_time = between(1, 5)
    broker_url = 'emqx-dev.xiongmaoboshi.com'

    def on_start(self):
        broker_url = 'emqx-dev.xiongmaoboshi.com'
        print('这是SETUP，每次实例化User前都会执行！')
        mqttpara = getmqtttoeken()
        self.mqtttoeken = mqttpara[0]
        self.mqttsn = mqttpara[1]
        self.broker_url = 'emqx-dev.xiongmaoboshi.com'
        self.port = 1883


        def on_connect(client, userdata, flags, rc):
            print("Connected with result code :0 表示连接成功  其它表示失败，rc：" + str(rc))
            client.subscribe("chanel_01")

    @task(1)
    def getBaidu(self):
        broker_url = 'emqx-dev.xiongmaoboshi.com'
        port = 1883
        self = str(random.randint(0, 1000)) + 'test'
        HOST = broker_url
        PORT = port
        def on_connect(client, userdata, flags, rc):
            print("Connected with result code :0 表示连接成功  其它表示失败" + str(rc))
            client.subscribe("chanel_01")

        def main():
            client = mqtt.Client(client_id)
            client.connect(HOST, PORT, 60)
            client.on_connect = on_connect
            client.username_pw_set(client_id, password=self.mqtttoeken)
            client.loop_forever()  # 长连接

    def on_stop(self):
        print('这是TEARDOWN，每次销毁User实例时都会执行！')




class MyLocust(FastHttpUser):

    task_set = TestTask
    min_wait = 1000
    max_wait = 60000


if __name__ == "__main__":

    import os

    os.system("locust -f locustForPanda.py --host=emqx-dev.xiongmaoboshi.com")
#  locust -f dept_list.py --worker(从节点)/--master（主节点） --master-host=192.168.x.xx