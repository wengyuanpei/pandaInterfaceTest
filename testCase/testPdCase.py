
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
from pandaInterfaceTest.common.HTMLTestReport import *
from pandaInterfaceTest.common import interfaceUrl



@ddt
class testPdInterface(unittest.TestCase):
    def setUp(self):

        self.header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0",

                       }

    @unpack
    @data(
        * tags_type_add()
    )
    def testPdinterface01(self, timestamp, sign, body,code):
            # self.header["Authorization"] = Authorization
            header = self.header
            baseurl=interfaceUrl.baseurl()
            url = interfaceUrl.tags_type_add_url()
            url_end=baseurl+url
            params = {
                    "timestamp":timestamp,
                    "sign":sign,
                    "body":body,
                    }
            rq_get = requests.post(url=url_end, data=params, headers=header)
            # print(rq_get.json())
            code_rq=rq_get.json()
            code_rq_end = json.loads(code_rq)["code"]

            # 断言
            self.assertEqual(code_rq_end, code, '接口返回参数失败')
            print('服务端返回参数', code_rq_end)


    def tearDown(self):
        pass




repot_path = saveReportPath()

# 加载测试类
suite = unittest.TestSuite()
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(testPdInterface))
runner = unittest.TextTestRunner()

# 生成测试报告

repot_path_n = repot_path + '.html'

fp = open(repot_path_n, 'wb')

reportRun = HTMLTestRunner(stream=fp, title='接口测试报告', description='接口测试报告,脚本版本号V202208', tester='测试人员-翁远陪')

runner.run(suite)
fp.close()













