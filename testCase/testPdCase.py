
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
from pandaInterfaceTest.common.interfaceUrl import *


@ddt
class testPdInterface(unittest.TestCase):
    def setUp(self):

        self.header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0",
                       "Accept": "application/json, text/plain, */*",
                       "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                       "Accept-Encoding": "gzip, deflate, br",
                       "Content-Type": "application/x-www-form-urlencoded",
                       "Authorization": ""}

    @unpack
    @data(
        * paraMeter1()
    )
    def testPdinterface01(self):
        def test_interface_1(self, Authorization, customerId, code):
            print('请求参数1:' + Authorization, '请求参数2:' + customerId, '请求参数3:' + code)
            self.header["Authorization"] = Authorization
            header = self.header

            url = pdurl01()

            params = {
                "customerId": customerId
            }
            rq_get = requests.get(url=url, params=params, headers=header)
            code_rq0 = rq_get.status_code
            print('请求状态码' + str(code_rq0))

            # 获取返回状态码
            # print(rq_get.text)

            code_rq1 = json.loads(rq_get.text).get('code')
            # print('1返回状态码' +code_rq1)
            # 断言
            self.assertEqual(code_rq1, code, '接口返回参数失败')
            print('服务端返回参数', rq_get.text)
            print('***********************************************************************************')

    def tearDown(self):
        pass

repot_path=saveReportPath()


#加载测试类
suite = unittest.TestSuite()
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(testPdInterface))
runner = unittest.TextTestRunner()

# 生成测试报告


repot_path_n = repot_path  + '.html'

fp = open(repot_path_n, 'wb')

reportRun=HTMLTestReport(stream=fp, title='接口测试报告',description='接口测试演示报告详情,脚本版本号V202202',tester='测试人员-翁远陪')


runner.run(suite)
fp.close()
