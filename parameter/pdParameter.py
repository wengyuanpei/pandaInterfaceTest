'''

这个地方封装的是接口的请求参数信息

'''
from pandaInterfaceTest.common.make_num_random import *
from pandaInterfaceTest.common.sql_for_para import *

#运行之前需要抓令牌
def auth():

    auth="Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ7XCJlbWFpbFwiOlwid2VuZ3l1YW5wZWlAZHJwYW5kYS5jb21cIixcImlkXCI6MjIzLFwibW9iaWxlXCI6XCIxNzM0NTA0MzM2NVwiLFwidXNlcm5hbWVcIjpcIndlbmd5dWFucGVpXCJ9IiwiZXhwIjoxNjYyMTAxNjMxfQ.UrsmdShTdFPbNq2qe1yv7ElUbmJs3N1QbOw0GnDsqQiuJqlfLVPY0_hEkTPLZGABq01wiAt7IMU6nncBZuU5_A"
    return auth



#状态码
code_ok="0"
code_f="-1"
code_f_1080="1080"
gift_app_type="P10"



'''*******************************************************************************************************'''


def gift_bag_group_add_para():
    num_gift = "礼包集合" + random_num()
    giftBagGroupName1 = num_gift


    para_tags_type_add= (
         {'giftBagGroupName': giftBagGroupName1,'applyType': gift_app_type, 'code': code_ok},
         {'giftBagGroupName': giftBagGroupName1,'applyType': gift_app_type, 'code': code_f}
     )
    return para_tags_type_add





'''*******************************************************************************************************'''
'''
{
  "timestamp":23143516166, #时间戳
  "sign":"asdf234teqasdg", #签名
  "body":{
    "giftBagGroupCode": "P10", #礼包合集编码
    "giftBagGroupStatus":0,0-待上架 1-上架中 2-已下架
    "size":1, # 每页条数
    "current":1  #第几页
  }
}
'''





def gift_bag_group_list_para():
    giftBagGroupStatus1 = "0"
    giftBagGroupStatus2 = "1"
    giftBagGroupStatus3 = "2"

    gift_bag_group_list=(
        {"giftBagGroupCode": gift_app_type, "giftBagGroupStatus": giftBagGroupStatus1, "code": code_ok},
        {"giftBagGroupCode": gift_app_type, "giftBagGroupStatus": giftBagGroupStatus2, "code": code_ok},
        {"giftBagGroupCode": gift_app_type, "giftBagGroupStatus": giftBagGroupStatus3, "code": code_ok}

    )

    return gift_bag_group_list


'''*******************************************************************************************************'''

'''
{
  "timestamp":23143516166, #时间戳
  "sign":"asdf234teqasdg", #签名
  "body":{
    "giftBagName": "识字启蒙大礼包", #礼包名称
    "giftBagGroupId": 12, #所属礼包合集ID
    "giftBagOrder": 444, #礼包顺序
    "goodsInfos":{[
      "goodsId": 13415, #商品编码
      "goodsName": "(791)平板虚拟权限", #商品名称
      "goodsShowName": "(791)平板虚拟权限", #商品展示名称
      "goodsBgUrl":"www.baidu.com",#商品背影图片url
      "gameId": "Pad Launcher", #项目ID 
      "gameName": "Pad Launcher", #项目名称
      "goodsEffectivePeriod": 36, #有效期，无表示永久,否则按月算 以接口为准，
    ]}, #--good 相关信息 @Dave
    "useRule": 0 , # 0-全部 1-部分
    "useRuleDesc": "全部" # 全部
    "useRuleChooseNum": 1 # 几选几 ，范围[1-goodInfoSize),在useRule=1时有效
  }
}
'''


def gift_bag_add_para():
    giftBagName = "new_gift" + random_num()
    gift_bag_add=(
        {'giftBagName':giftBagName,'code':code_ok},
        {'giftBagName': giftBagName, 'code': code_f}
    )

    return gift_bag_add



'''***************************************************************************************************'''
'''

{
  "timestamp":23143516166, 
  "sign":"asdf234teqasdg", 
  "body":{
    "id":59, 
    "giftBagName": "识字启蒙大礼包", 
    "giftBagGroupId": 170, 
    "giftBagOrder": 444,
    "goodsInfos":[{
      "goodsId": 13415, 
      "goodsName": "(791)平板虚拟权限", 
      "goodsShowName": "(791)平板虚拟权限", 
      "goodsBgUrl":"www.baidu.com",
      "gameId": "Pad Launcher", 
      "gameName": "Pad Launcher", 
      "goodsEffectivePeriod": 36}], 
    "useRule": 0 , 
    "useRuleDesc": "全部",
    "useRuleChooseNum": 1 
  }
}

'''


#平板礼包编辑


def gift_bag_update_para():
    giftBagName_u = "编辑礼包" + random_num()
    bag_update_para=({'giftBagName_up':giftBagName_u,'code':code_ok}
    )
    return bag_update_para



# 平板礼包删除  数据库查礼包id实现



def gift_bag_delete_para():
    id_del_para = get_gift_bag_id()
    id_ddel=({'id_del':{'id':id_del_para},'code':code_ok},{'id_del':{'id':id_del_para},'code':code_f})
    return id_ddel



#平板礼包列表
'''
{
  "timestamp":23143516166, # 时间戳
  "sign":"asdf234teqasdg", # 签名
  "body":{
    "giftBagCode": "pad 0001", # 礼包Code
    "giftBagName": "张三", # 礼包名称,
    "giftBagGroupId":1 #礼包合集ID
  }
}
'''


def gift_bag_list_para():
    giftBagCode = 'pad0044'
    giftBagName_list = " "
    giftBagGroupId = " "
    gift_list=({'giftBagCode':giftBagCode,'giftBagName':giftBagName_list,'giftBagGroupId':giftBagGroupId,'code':code_ok},)
    return gift_list


'''
{
  "timestamp":23143516166, # 时间戳
  "sign":"asdf234teqasdg", # 签名
  "body":{
    "applicationName": "熊猫博士国学", # 应用名
    "packageName":"Dr.panda.com", # packageName
  }
}
'''



def white_list_add_para():
    applicationName = 'test_name'
    packageName = "Dr.panda.com" + random_num()
    white_list_add=({'applicationName_wht_add':applicationName,'packageName_add':packageName,'code':code_ok},
                    {'applicationName_wht_add':applicationName,'packageName_add':packageName,'code':code_f})
    return white_list_add




'''
{
  "timestamp":23143516166, # 时间戳
  "sign":"asdf234teqasdg", # 签名
  "body":{
    "id":1, #主键ID
    "applicationName": "熊猫博士国学", # 应用名
    "packageName":"Dr.panda.com", # packageName
  }
}

白名单修改
'''

def  white_list_update_para():
    update_par='熊猫'+random_num()
    packageName_para='Dr.'+random_num()
    white_update_para=({'applicationName_white_update': update_par,'packageName_para':packageName_para,'code':code_ok},
                       {'applicationName_white_update': update_par,'packageName_para':packageName_para,'code':code_f})
    return white_update_para

'''
{
  "code":0, #0-成功 其他 错误或失败
  "success":true,
  "msg":"success", # 非成功时可作为提示信息
  "traceId":"122135-t234t23-qewqt-qweq",  # traceId,用于排查问题
  "data":{} # 有需要返回结果时，会有data数据
}
白名单删除
'''


def white_list_delete_para():
    id_white_para01 = get_white_list_id()
    id_white=({'id_white_del':{'id':id_white_para01},'code':code_ok},{'id_white_del':{'id':id_white_para01},'code':code_f})
    return id_white



'''
{
  "timestamp":23143516166, # 时间戳
  "sign":"asdf234teqasdg", # 签名
  "body":{
    "applicatioName": "熊猫博士国学", # 应用名
    "packageName":"Dr.panda.com", # packageName
  }
}
web 白名单列表

'''



