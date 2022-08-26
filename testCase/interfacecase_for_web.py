import unittest  # 单元测试模块
import requests,json,time,os,time
from ddt import ddt,data,unpack
from pandaInterfaceTest.common.interfaceurl_web import *
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
        '''创建平板礼包合集'''   #对当前接口进行描述

        print("接口测试参数：",giftBagGroupName,applyType,code)

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

        time.sleep(0.5)  #防止接口请求被限制

        print("返回参数："+request.text)


    @data(*gift_bag_group_list_para())
    @unpack
    def test_gift_bag_group_list(self, giftBagGroupCode, giftBagGroupStatus, code):
        '''平台礼包合集列表'''   #对当前接口进行描述

        print("接口测试参数：",giftBagGroupCode,giftBagGroupStatus,code)

        header = self.header
        url=gift_bag_group_list_url()
        print("测试地址",str(url))

        data = {
                  "timestamp":23143516166, #时间戳
                  "sign":"asdf234teqasdg", #签名
                  "body":{
                    "giftBagGroupCode": "P10", #礼包合集编码
                    "giftBagGroupStatus":giftBagGroupStatus, #0,0-待上架 1-上架中 2-已下架
                    "size":1, # 每页条数
                    "current":1  #第几页
                  }
                }

        data_json = json.dumps(data)
        request = requests.post(url=url, data=data_json, headers=header)
        codebase = str(request.json()["code"])
        self.assertEqual(code, codebase, '接口请求失败')

        time.sleep(0.5)  #防止接口请求被限制
        print("返回参数：" + request.text)


    @data(*gift_bag_add_para())
    @unpack
    def test_gift_bag_add_url(self,giftBagName,code):
        ''' 创建平板礼包'''
        print("接口参数：",giftBagName,code)
        header = self.header
        url=gift_bag_add_url()
        print("测试地址", str(url))
        data_gad = {
            "timestamp": 23143516166,
            "sign": "asdf234teqasdg",
            "body": {
                "giftBagName": giftBagName,
                "giftBagGroupId": 170,
                "giftBagOrder": 444,
                "goodsInfos": [{
                    "goodsId": 13415,
                    "goodsName": "(791)平板虚拟权限",
                    "goodsShowName": "(791)平板虚拟权限",
                    "goodsBgUrl": "www.baidu.com",
                    "gameId": "Pad Launcher",
                    "gameName": "Pad Launcher",
                    "goodsEffectivePeriod": 36}],
                "useRule": 0,
                "useRuleDesc": "全部",
                "useRuleChooseNum": 1
            }
        }
        # data_json = json.dumps(data)
        request = requests.post(url=url, json=data_gad, headers=header)
        codebase = str(request.json()["code"])
        self.assertEqual(code, codebase, '接口请求失败')

        time.sleep(0.5)  # 防止接口请求被限制
        print("返回参数：" + request.text)


    @data(*gift_bag_update_para())
    @unpack
    def test_gift_bag_update(self,giftBagName_up,code):
        ''' 编辑平板礼包'''
        print("接口参数：",giftBagName_up,code)
        header = self.header
        url=gift_bag_update_url()
        print("测试地址", str(url))
        data_updata = {
            "timestamp": 23143516166,
            "sign": "asdf234teqasdg",
            "body": {
                "id": 32,
                "giftBagName": giftBagName_up,
                "giftBagGroupId": 170,
                "giftBagOrder": 444,
                "goodsInfos": [{
                    "goodsId": 13415,
                    "goodsName": "(791)平板虚拟权限",
                    "goodsShowName": "(791)平板虚拟权限",
                    "goodsBgUrl": "www.baidu.com",
                    "gameId": "Pad Launcher",
                    "gameName": "Pad Launcher",
                    "goodsEffectivePeriod": 36}],
                "useRule": 0,
                "useRuleDesc": "全部",
                "useRuleChooseNum": 1
            }
        }
        request = requests.post(url=url, json=data_updata, headers=header)
        codebase = str(request.json()["code"])
        self.assertEqual(code, codebase, '接口请求失败')

        time.sleep(0.5)  # 防止接口请求被限制
        print("返回参数：" + request.text)

    @data(*gift_bag_delete_para())
    @unpack
    def test_gift_bag_delete(self,id_del,code):
        ''' 删除平板礼包'''
        print("接口参数：",id_del,code)
        header = self.header
        url=gift_bag_delete()
        print("测试地址", str(url))

        request = requests.post(url=url, params=id_del, headers=header)
        codebase = str(request.json()["code"])
        self.assertEqual(code, codebase, '接口请求失败')
        time.sleep(0.5)  # 防止接口请求被限制
        print("返回参数：" + request.text)




if "__name__"=="__main__":
    unittest.main()
