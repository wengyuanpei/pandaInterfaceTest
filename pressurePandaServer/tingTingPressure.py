#听力机压力测试
import os
import random

from locust import TaskSet, task, between, FastHttpUser


# from gevent._semaphore import Semaphore #集合点


# 创建任务类
class tingTingPressure(TaskSet):
    def on_start(self):
        self.header={

        }
        #初始化
        self.url_word_list = '/v1/book/words-list'
        self.url_book_detail = '/v1/book/book-detail'
        self.url_book_cont='/v1/book/book-content'
        self.url_book_list='/v1/book/book-list'
        self.url_media_list='/v1/record/lesson/list'#音视频列表
        self.url_char_info='/v1/record/char-info' # 汉字信息
        self.url_char_list='/v1/record/char-list' #汉字列表
        self.url_record_add='/v1/record/add'#上报学习记录
        self.url_audio='/v1/lesson/' #音频列表信息接口 /v1/lesson/{id}  get
        self.url_saudio_info='/v1/media/audio/'#音频信息 {id} get
        self.url_vidio='/v1/media/video/' #视频信息 {id}  get
        self.uidlist=[1561969032355688449,]
        self.auth1='Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNTYxOTY5MDMyMzU1Njg4NDQ5Iiwic3ViIjoie1wiaWRcIjoxNTYxOTY5MDMyMzU1Njg4NDQ5LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTY5MDYyMTkzOX0.xlLBKUKxR9KSPMbGsBu3jX_sRdK2yM5e7GuKURS8yHu59NZZtExZNYQnK8KDAkwHVVUb6naqjdG4k4tMqTUDJA'
        self.bookId=[
            1882,
            1877,
            1964,
            1878,
            1915,
            2819,
            1010,
            588,
            2096,
            2143,
            803,
            466,
            625,
            2801,
            539,
            812,
            631,
            564,
            633,
            671,
            605,
            2519,
            371,
            2535,
            992,
            2153,
            191,
            2904,
            544,
            2152,
            2898,
            2212,
            269,
            1838,
            2820,
            620,
            2440,
            2906,
            470,
            302,
            649,
            2090,
            2121,
            813,
            201,
            662,
            281,
            211,
            2917,
            1016,
            548,
            2195,
            1843,
            292,
            557,
            680,
            820,
            583,
            2101,
            1863,
            2909,
            2211,
            2135,
            2085,
            293,
            287,
            2895,
            2861,
]
        self.sesourceId=[
                    23,
                    24,
                    27,
                    28,
                    20,
                    21,
                    22,
                    29,
                    30,
                    31,
                    32,
                    33,
                    34,
                    48,
                    46,
                    45,
                    41,
                    39,
                    49,
                    51,
                    56,
                    57,
                    58,
                    59,
                    68,
                    60,
                    61,
                    14,
                    81,
                    82,
                    13,
                    85,
                    86,
                    89,
                    90,
                    91,
                    83,
                    84,
                    92,
                    44,
                    99,
                    100,
]
        self.char_list=[73,87,102,103,120,134,141,155,161,172,213,221,225,226,229,230,231,253,261,266,266,270,281,288,295,317,321,332,367,535,548,570,580,635,740,753,816,984,1043,1049,1055,1079]
    @task(1)
    def word_list(self):
        Authorization=self.auth1
        uid=random.choice(self.uidlist)
        header={'Authorization':Authorization,'Content-Type':'application/json; charset=UTF-8'}
        word_list_data = {"current":1,"size":1000,"status":2,"uid":uid}
        with self.client.post(self.url_word_list, headers=header, json=word_list_data, catch_response=True) as responsex:
            if responsex.status_code == 200:
                responsex.success()
            else:
                responsex.failure('Failed!')

    @task(1)
    def book_detail(self):
        Authorization = self.auth1
        book_id=random.choice(self.bookId)
        uid = random.choice(self.uidlist)
        header = {'Authorization': Authorization, 'Content-Type': 'application/json; charset=UTF-8'}
        book_detail_data={"book_id":book_id,"uid":uid}
        with self.client.post( self.url_book_detail, headers=header, json=book_detail_data, catch_response=True) as responsex:
            if responsex.status_code == 200:
                responsex.success()
            else:
                responsex.failure('Failed!')
    @task(1)
    def book_cont(self):
        Authorization = self.auth1
        book_id=random.choice(self.bookId)
        uid = random.choice(self.uidlist)
        header = {'Authorization': Authorization, 'Content-Type': 'application/json; charset=UTF-8'}
        book_cont_data={
                                "book_id": book_id,
                                "uid": uid
                            }
        with self.client.post(self.url_book_cont, headers=header, json=book_cont_data, catch_response=True) as responsex:
            if responsex.status_code == 200:
                responsex.success()
            else:
                responsex.failure('Failed!')
    @task(1)
    def book_list(self):
        Authorization = self.auth1
        uid = random.choice(self.uidlist)
        lower_level=random.randint(4,28)
        header = {'Authorization': Authorization, 'Content-Type': 'application/json; charset=UTF-8'}
        book_cont_data = {"current":1,"lower_level":lower_level,"size":50,"uid":uid}
        with self.client.post(self.url_book_list, headers=header, json=book_cont_data,
                              catch_response=True) as responsex:
            if responsex.status_code == 200:
                responsex.success()
            else:
                responsex.failure('Failed!')

    @task(1)
    def char_info(self):
        Authorization = self.auth1
        uid = random.choice(self.uidlist)
        char_id=random.choice(self.char_list)
        header = {'Authorization': Authorization, 'Content-Type': 'application/json; charset=UTF-8'}
        char_info_data = {"char_id":73,"uid":uid}
        with self.client.post(self.url_char_info, headers=header, json=char_info_data,
                              catch_response=True) as responsex:
            if responsex.status_code == 200:
                responsex.success()
            else:
                responsex.failure('Failed!')

    @task(1)
    def char_list(self):
        Authorization = self.auth1
        uid = random.choice(self.uidlist)
        header = {'Authorization': Authorization, 'Content-Type': 'application/json; charset=UTF-8'}
        lesson_list_data = {"resource_id": 18, "uid": uid}
        with self.client.post(self.url_char_list, headers=header, json=lesson_list_data,
                              catch_response=True) as responsex:
            if responsex.status_code == 200:
                responsex.success()
            else:
                responsex.failure('Failed!')

    @task(1)
    def record_add(self):
        Authorization = self.auth1
        uid = random.choice(self.uidlist)
        header = {'Authorization': Authorization, 'Content-Type': 'application/json; charset=UTF-8'}
        lesson_list_data = {"category_id":10,"content":"","content_id":73,"cost_time":0,"event_id":22,"extra":"","is_init":1,"play_place":0,"proportion":0,"score":0,"uid":uid}
        with self.client.post(self.url_record_add, headers=header, json=lesson_list_data,
                              catch_response=True) as responsex:
            if responsex.status_code == 200:
                responsex.success()
            else:
                responsex.failure('Failed!')

    def on_stop(self):
        # teardown
        print('清除数据')


# 创建用户类
class TljPressure(FastHttpUser):
    wait_time = between(1,10)   #设置运行过程中的间隔时间，需要在locust中引入between
    tasks = [tingTingPressure]
    min_wait = 1000
    max_wait = 2000

if __name__ == '__main__':
    #线上环境
    # os.system("locust -f tingTingPressure.py --host=https://hear.abctime.com  --run-time 10m")
    os.system("locust -f tingTingPressure.py --host=https://hear.abctime.com ")

