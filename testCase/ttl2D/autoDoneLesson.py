
import redis
import pymysql
import time
def connect_redis(common,method):
    r = redis.Redis(
        host='xue-xi-yan-fa-redis-nextapp-twproxy.xesv5.com',
        port=2080,
        password='hSL18msdMCrxp5Z_',
        db=0,  # 默认数据库
        decode_responses=True  # 自动解码为字符串
    )
    # 测试连接
    if method =="del":
        r.delete(common)
    if method=='set':
        value=r.get(common)
        r.set(common,value)


def connect_mysql(execute):
    # 打开数据库连接
    db = pymysql.connect(host='localhost',
                         user='testuser',
                         password='test123',
                         database='TESTDB')

    cursor = db.cursor()
    cursor.execute(execute)
    db.close()





def planDone():
    pass

if __name__ == '__main__':
    connect_redis()

