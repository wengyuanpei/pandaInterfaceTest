'''

这个地方封装的是接口的请求参数信息

'''
from    pandaInterfaceTest.common.make_num_random import *


#运行之前需要抓令牌
def auth():

    auth="Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ7XCJlbWFpbFwiOlwid2VuZ3l1YW5wZWlAZHJwYW5kYS5jb21cIixcImlkXCI6MjIzLFwibW9iaWxlXCI6XCIxNzM0NTA0MzM2NVwiLFwidXNlcm5hbWVcIjpcIndlbmd5dWFucGVpXCJ9IiwiZXhwIjoxNjYxMjQyMDQ2fQ.jZXyn3oH0FuNgF6wdbkkKyPLR8n5Te2woGZIFdJ3RLyEPnMlOkIRicqDu7otCLREx3cIMUceEwvbd9q3Xmfrrw"
    return auth



#状态码
code_ok="0"
code_f="-1"
code_f_1080="1080"
gift_app_type="P10"



'''*******************************************************************************************************'''

num_gift="礼包集合"+random_num()
giftBagGroupName1=num_gift


giftBagGroupName2=num_gift
applyType2="P10"

def gift_bag_group_add_para():

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




giftBagGroupStatus1="0"
giftBagGroupStatus2="1"
giftBagGroupStatus3="2"


def gift_bag_group_list_para():
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
giftBagName="礼包" + random_num()
giftBagGroupId="171"
giftBagOrder="666"


def gift_bag_add_para():
    gift_bag_add=(
        {'giftBagName':giftBagName,'giftBagGroupId':giftBagGroupId,'giftBagOrder':giftBagOrder,}
    )






















tokenRight="Bearer 397a8491-ef14-4f8c-9844-5b1effa4c102" #测试之前抓取一个正确的token值(最好用登录接口抓取)

tokenLate="Bearer f36f1500-5216-428f-8f9a-4f56784f259f" #过期的token

nullParameter="" #空的token值

tokenWrong="Bearer ec608034-3fac-4a54-a4b3-239dcb76666" #错误的token值
def paraMeter1():

    paraMeter1=(
        {'Authorization': tokenLate, 'customerId': nullParameter, 'code': "900"},
        {'Authorization': tokenLate, 'customerId': nullParameter, 'code': "900"},
        {'Authorization': tokenWrong, 'customerId': nullParameter, 'code': "900"},
        {'Authorization': tokenLate, 'customerId': nullParameter, 'code': "900"},
        {'Authorization': tokenRight, 'customerId': nullParameter, 'code': "200"},
        {'Authorization': tokenRight, 'customerId': '480', 'code': "200"},
        {'Authorization': tokenRight, 'customerId': '92233720368547758070', 'code': "500"},
        {'Authorization': tokenRight, 'customerId': '你好', 'code': "500"},
        {'Authorization': tokenRight, 'customerId': 'ABC', 'code': "500"}
    )


    return paraMeter1