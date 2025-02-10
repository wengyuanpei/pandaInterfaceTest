#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'weng'

import os,sys,json
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import requests

class SendRequests():
    """发送请求数据"""
    def sendRequests(self,s,apiData):
        try:
            #从读取的表格中获取响应的参数作为传递
            method = apiData["method"]
            url = apiData["url"]
            if apiData["params"] == "":
                par = None
            else:
                par = eval(apiData["params"])
            if apiData["headers"] == "":
                h = None
            else:
                h = eval(apiData["headers"])
            if apiData["body"] == "":
                body_data = None
            else:
                body_data = eval(apiData["body"])
            type = apiData["type"]
            fal = False #忽略证书
            if type == "data":
                body = body_data
            elif type == "json":
                body = json.dumps(body_data)
            else:
                body = body_data

            #发送请求
            re = s.request(method=method,url=url,headers=h,params=par,data=body,verify=fal)
            return re
        except Exception as e:
            print(e)


if __name__ == '__main__':
    req={'module': '订单查询', 'ID': 'event_query_001', 'UseCase': '订单id查询', 'url': 'https://api-ext.abctime.com/dev/market_service/admin/order/detail', 'method': 'post', 'params': '', 'headers': '{"workcode":"V0013750","x-api-uis-secret":"kC0q4jVixSFqL4UHlf39erFNShDrRqVD","Content-Type":"application/json"}', 'body': '{"order_no":"518b1909-f3fc-4fa6-a168-cc88866117c7"}', 'type': 'application/json', 'status_code': 200.0, 'msg': 'success', 'result': '', ' testers': ''}
    qqq=requests.Session()
    reqqq=SendRequests().sendRequests(qqq,req)
    print(reqqq.json())
    print(reqqq.status_code)