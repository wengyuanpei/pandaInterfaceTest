import unittest  # 单元测试模块
import requests,json,time,os,time
from ddt import ddt,data,unpack
from pandaInterfaceTest.common.interfaceUrl import *
from pandaInterfaceTest.parameter.pdParameter import *



@ddt
class TestPandaInterface(unittest.TestCase):
    def setUp(self):

        # 令牌
        self.auth = auth()

        #请求头部信息
        self.header = {
            "Authorization": self.auth,
            "Content-Type": "application/json;charset=UTF-8"
        }
        #  请求方式



    @data(*gift_bag_group_add_para())
    @unpack
    def test_gift_bag_group_add(self, giftBagGroupName, applyType, code):

        print(giftBagGroupName,applyType,code)

        header = self.header

        url=gift_bag_group_add()
        print("测试地址",str(url))


        data = {
            "timestamp": "",
            "sign": "",
            "body": {
                "giftBagGroupName": giftBagGroupName,  # 礼包合集名称-验重
                "applyType": applyType,  # 适用型号 用于平板与权益关联
            }
        }

        data_json = json.dumps(data)
        request = requests.post(url=url, data=data_json, headers=header)
        codebase = str(request.json()["code"])
        self.assertEqual(code, codebase, '接口请求失败')
        print('接口描述')
        time.sleep(0.5)


    def testaa(self):
        '''这个是第二个测试用例'''
        self.assertEqual(1, 1)
        print('第二个用例')

    def testdd(self):
        '''用例描述3'''
        print('第三个用例')

    def testbb(self):
        '''用例描述4'''
        print('第四个用例')


if "__name__"=="__main__":
    unittest.main()
