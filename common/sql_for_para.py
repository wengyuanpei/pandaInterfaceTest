'''**********************************数据库的操作方法卸载这******************************************'''

import pymysql
from random import randint

def get_gift_bag_id():

    randdd=randint(0,20)
    # print(randdd)
    # 1. 连接数据库，
    conn = pymysql.connect(
        host='rm-bp1qz4b7e260219h5ho.mysql.rds.aliyuncs.com',
        user='dppad',
        password='s$gQr0MJvuLA7#@H',
        db='dppad',
        charset='utf8',
           # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )
    # ****python, 必须有一个游标对象， 用来给数据库发送sql语句， 并执行的.
    # 2. 创建游标对象，
    cur = conn.cursor()

    # 4). **************************数据库查询*****************************
    sqli = "select id from t_pad_gift_bag_info;"
    cur.execute(sqli)  # 默认不返回查询结果集， 返回数据记录数。
    result=cur.fetchall()
    print("gift—num：",result[randdd][0])

    # 4. 关闭游标
    cur.close()
    # 5. 关闭连接
    conn.close()
    return str(result[0][0])



def get_white_list_id():

    randdd=randint(0,20)
    # print(randdd)
    # 1. 连接数据库，
    conn = pymysql.connect(
        host='rm-bp1qz4b7e260219h5ho.mysql.rds.aliyuncs.com',
        user='dppad',
        password='s$gQr0MJvuLA7#@H',
        db='dppad',
        charset='utf8',
           # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )
    # ****python, 必须有一个游标对象， 用来给数据库发送sql语句， 并执行的.
    # 2. 创建游标对象，
    cur = conn.cursor()

    # 4). **************************数据库查询*****************************
    sqli = "select id from t_pad_application_white_list;"
    cur.execute(sqli)  # 默认不返回查询结果集， 返回数据记录数。
    result=cur.fetchall()
    print("white—num：",result[randdd][0])

    # 4. 关闭游标
    cur.close()
    # 5. 关闭连接
    conn.close()
    return str(result[0][0])

def get_sn_num():

    randdd=randint(0,5)
    # print(randdd)
    # 1. 连接数据库，
    conn = pymysql.connect(
        host='rm-bp1qz4b7e260219h5ho.mysql.rds.aliyuncs.com',
        user='dppad',
        password='s$gQr0MJvuLA7#@H',
        db='dppad',
        charset='utf8',
           # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )
    # ****python, 必须有一个游标对象， 用来给数据库发送sql语句， 并执行的.
    # 2. 创建游标对象，
    cur = conn.cursor()

    # 4). **************************数据库查询*****************************
    sqli = "select sn_num from t_pad_sn_info;"
    cur.execute(sqli)  # 默认不返回查询结果集， 返回数据记录数。
    result=cur.fetchall()
    print("SN—num：",result[randdd][0])

    # 4. 关闭游标
    cur.close()
    # 5. 关闭连接
    conn.close()
    return str(result[0][0])


# get_gift_bag_id()
# get_white_list_id()
# get_sn_num()

