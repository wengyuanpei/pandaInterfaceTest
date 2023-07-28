# -*- coding: utf-8 -*-
import unittest

import requests

from common.finish_plan_urlenverment import *

class ServeceIterfaceTestCase(unittest.TestCase):
    def setUp(self) :

        self.header={'Authorization':'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjc5NjkzMzAwNDE1NzcwNjI1Iiwic3ViIjoie1wiaWRcIjoxNjc5NjkzMzAwNDE1NzcwNjI1LFwibW9iaWxlXCI6XCIrODYxODM4NDI1MzUwNlwifSIsImV4cCI6MTcwNDg3MjE4NH0.kR_S20qzXP7S0wNMoBEa98CgngD6qqxtTMoJo-sLMviphT8B80Wdnbpm-FM_hN2roPMrAsY2NtsSRue2OiD2eg'}

        self.baseurl=urlenverment(3)

        self.timersp=[]

    def test_book_detail(self):
        baseurl=self.baseurl
        url_book_detail=baseurl+'v1/book/book-detail'
        databookdetail={
                          "uid": 1640976882862985217,
                          "book_id": 2757
                        }

        req=requests.post(url=url_book_detail,headers=self.header,json=databookdetail)

        self.assertEqual(req.status_code, 200)

        self.responsetime_book_detail=req.elapsed.total_seconds()
        self.timersp.append([url_book_detail+'请求响应时间（s）：'+str(self.responsetime_book_detail)])




if __name__ == '__main__':
    unittest.main()
