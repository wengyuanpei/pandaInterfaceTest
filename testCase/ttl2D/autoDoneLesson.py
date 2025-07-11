
import redis
import pymysql
import time
def connect_redis(common,method):
    r = redis.Redis(
        host='10.176.5.171',
        port=2080,
        password='hSL18msdMCrxp5Z_',
        db=0,  # 默认数据库
        decode_responses=True  # 自动解码为字符串
    )
    if method =="daytoday":
        r.delete(common)
    if method=='daytounit':
        value=r.get(common)
        r.set(common,value)


def connect_mysql(execute):
    # 打开数据库连接
    db = pymysql.connect(host='10.176.5.167',
                         user='testuser',
                         password='test123',
                         database='TESTDB')

    cursor = db.cursor()
    cursor.execute(execute)
    db.close()


def planDone():
    pass

if __name__ == '__main__':

    redis_del_methd="daytoday"  #切换天
    redis_set_methd="daytounit" #切换unit或book

    connect_redis(redis_del,redis_del_methd)

