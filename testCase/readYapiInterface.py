#  读YAPI 接口


import json
import re
import requests


class Yapi(object):
    def __init__(self):
        self.local_url = "http://yapi.xxx.com"  # yapi对应的域名
        self.email = "账号"
        self.password = "密码"
        self.loginUrl = "登录的真实url"
        self.group_id = "产品id"

    def login(self):
        # 模拟登录
        data = {
            "email": self.email,
            "password": self.password
        }
        login_info = requests.request("POST", url=self.local_url + self.loginUrl, json=data)
        if login_info.status_code != 200: return ""
        v_cookie = login_info.headers.get("Set-Cookie")
        if not v_cookie: return ""
        cookie_ = re.compile('\_yapi_(.*?)\;').findall(v_cookie)
        v_cookie = "_yapi_" + cookie_[0] + ";" + "_yapi_" + cookie_[1]
        return v_cookie

    def get_path_data(self, v_cookie):
        """根据产品id,获取对应的模块id"""

        headers = {'Cookie': v_cookie}
        getid = {'project_id': self.group_id, 'page': '1', 'limit': '1000000'}
        resp = requests.request("GET", url=self.local_url + "/api/interface/list?", params=getid, headers=headers)
        data_lst = resp.json().get("data").get("list")
        apikey_dit = {}
        for i in range(0, len(data_lst)):
            path_url = data_lst[i].get("path")  # 获取path
            path_id = data_lst[i].get("_id")  # 获取_id
            apikey_name = path_url.split('=')[-1] if path_url.find("apiKey=") != -1 else ''  # 获取path中的apikey,若无,则为空
            sample_lst = self.get_data_byid(headers, path_id, apikey_name)
            apikey_dit[path_url] = sample_lst
        return apikey_dit


def get_data_byid(self, headers, path_id, apikey_name=""):
    # 根据path_id获取每个样本的信息
    details = requests.request("GET",
                               url=self.local_url + "/api/plugin/advmock/case/list?interface_id=%s" % path_id,
                               headers=headers).json()
    data_lst = details.get("data")
    # data为空处理
    if not data_lst:
        return []
    # data不为空处理
    sample_lst = []
    for sample_ in data_lst:
        sample_dit = {}
        sample_dit["api_key"] = apikey_name  # apikey
        sample_dit["interface_id"] = path_id  # path_id
        sample_dit["yapi_id"] = sample_.get("_id")  # 样本id
        sample_dit["sample_name"] = sample_.get("name")  # 样本名称
        sample_dit["param_filter"] = sample_.get("params")  # 参数过滤
        json_ = self.json_deal(sample_.get("res_body"))  # 自定义函数处理数据并判断是否是json
        if json_ == -1: continue
        sample_dit["json_sample"] = json_  # 样本json
        sample_dit["create_user"] = sample_.get("username")  # 创建者
        sample_lst.append(sample_dit)
    return sample_lst
