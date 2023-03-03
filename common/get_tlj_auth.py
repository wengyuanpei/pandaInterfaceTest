import requests
import random
import time
from common.requestSimulationData import *


def getauth():
    phone_num_1 =phone_num()
    # UG=user_agent()
    # print("phone_num:",phone_num_1)
    phone_num_end="+86"+str(phone_num_1)
    # print("phone_num_end:",phone_num_end)
    url_log="https://staging-subs.xiongmaoboshi.com/uis/ns/account/mobile-login-register-bind"
    data_log={"bundleId":"com.drpanda.aural.launcher","code":"888888","key":phone_num_end}
    header={"X-USER-API-VERSION":"3",}
    req_log=requests.post(url_log,json=data_log,headers=header)
    auth_beare_token=req_log.headers["Authorization"]
    uid=req_log.json()["data"]["id"]
    tal_auth=req_log.headers['Tal-Token']
    # print(tal_auth)
    # print("uid:",uid)
    # print(req_log.text)
    # print(auth)
    return auth_beare_token,tal_auth,phone_num_1,uid

getauth()

