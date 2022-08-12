'''

这个地方封装的是接口的请求参数信息

'''
#   1  查询用户行为轨迹接口数据************************************************************************************

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