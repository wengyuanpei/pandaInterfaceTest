
from ddt import ddt,unpack,data
import requests
import json
import time
import os
import unittest
#导入接口参数包

from pandaInterfaceTest.parameter.pdParameter import *
#导入公共包
from pandaInterfaceTest.common.resultPath import saveReportPath
from pandaInterfaceTest.common import HTMLTestReport
from pandaInterfaceTest.common import interfaceUrl

baseurl=interfaceUrl.baseurl()

@ddt
class TestPdInterface(unittest.TestCase):
    def setUp(self):

        self.header = header={
                                "Accept": "application/json",
                                "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9",
                                "Content-Type": "application/json;charset=UTF-8"
                                }

    def test_gift_bag_group_add(self,):
        header = self.header
        gift_bag_group_add_url=interfaceUrl.gift_bag_group_add()
        url=baseurl+gift_bag_group_add_url
        print(url)
        data1={
              "timestamp":23143516166, #时间戳
              "sign":"asdf234teqasdg", #签名
              "body":{
                "giftBagGroupName": "熊猫平板P10礼包合集", #礼包合集名称-验重
                "applyType":"适用型号", # 适用型号 用于平板与权益关联
              }
                }

        request=requests.post(url=url,data=data1,headers=header)
        # request_code=request.status_code
        respose=request.json()
        a=respose["code"]
        self.assertEqual(a, 1080, '接口返回参数失败')
        # print(request_code,'###########################')



    @unpack
    @data(
        * tags_type_add()
    )
    def testPdinterface01(self, timestamp, sign, body,code):
            print(timestamp,sign,body,code)
            # self.header["Authorization"] = Authorization
            header = self.header
            url = interfaceUrl.tags_type_add_url()
            url_end=baseurl+url
            # params = {
            #         "timestamp":timestamp,
            #         "sign":sign,
            #         "body":{"tagsTypeName":body},
            #         }
            params={
                    "timestamp":20321513231266,
                    "sign":"xxxx",
                    "body":{
                        "tagsTypeName":"百科标签"
                    }
}
            rq_get = requests.post(url=url_end, data=params, headers=header)
            # print(rq_get.json())
            code_rq=rq_get.json()
            code_rq_end = str(code_rq["code"])

            # 断言
            self.assertEqual(code_rq_end, code, '接口返回参数失败')
            print('服务端返回参数', code_rq_end)


    def tearDown(self):
        pass




# 加载测试类
suite = unittest.TestSuite()
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestPdInterface))
runner = unittest.TextTestRunner()



# 生成测试报告
repot_path1 = saveReportPath()
print(repot_path1,'报告路径')
repot_path = repot_path1 + '.html'
fp = open(repot_path, 'wb')
reportRun = HTMLTestReport.HTMLTestRunner(title='接口测试报告', description='接口测试报告,脚本版本号V202208', stream=fp)
reportRun.run(suite)
fp.close()




















