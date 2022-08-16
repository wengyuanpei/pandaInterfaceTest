'''

这个地方封装的是接口的请求参数信息

'''
#   1  查询用户行为轨迹接口数据************************************************************************************


# def tags_type_add1():
#
#     paraMeter1=(
#         {'Authorization': tokenLate, 'customerId': nullParameter, 'code': "900"},
#         {'Authorization': tokenLate, 'customerId': nullParameter, 'code': "900"},
#         {'Authorization': tokenWrong, 'customerId': nullParameter, 'code': "900"},
#         {'Authorization': tokenLate, 'customerId': nullParameter, 'code': "900"},
#         {'Authorization': tokenRight, 'customerId': nullParameter, 'code': "200"},
#         {'Authorization': tokenRight, 'customerId': '480', 'code': "200"},
#         {'Authorization': tokenRight, 'customerId': '92233720368547758070', 'code': "500"},
#         {'Authorization': tokenRight, 'customerId': '你好', 'code': "500"},
#         {'Authorization': tokenRight, 'customerId': 'ABC', 'code': "500"}
#     )



# tags_type_add 添加标签类型请求参数格式  json
#     "timestamp":20321513231266,
#     "sign":"xxxx",
#     "body":{
#         "tagsTypeName":"百科标签"
#     }



timestamp_ok=20321513231266
sign_ok="xxxx"
body_ok="百科标签"
code_ok="200"



def tags_type_add():

     para_tags_type_add=(
        {"timestamp":timestamp_ok,"sign":sign_ok,"body":body_ok,"code":code_ok},
        {"timestamp": timestamp_ok, "sign": sign_ok, "body": body_ok, "code": code_ok}

    )
     return para_tags_type_add



