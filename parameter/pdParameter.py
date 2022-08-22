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


num_gift=random_num()
giftBagGroupName1=num_gift
applyType1="P10"




giftBagGroupName2=num_gift
applyType2="P10"




def gift_bag_group_add_para():

     para_tags_type_add= (
         {'giftBagGroupName': giftBagGroupName1,'applyType': applyType1, 'code': code_ok},
         {'giftBagGroupName': giftBagGroupName1,'applyType': applyType1, 'code': code_ok}
     )

     return para_tags_type_add






giftBagGroupCode1="P10"
giftBagGroupStatus1="0"


def gift_bag_group_list():
    gift_bag_group_list=(
        {"giftBagGroupCode": giftBagGroupCode1, "giftBagGroupStatus": giftBagGroupStatus1, "code": code_ok}

    )

    return gift_bag_group_list




























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