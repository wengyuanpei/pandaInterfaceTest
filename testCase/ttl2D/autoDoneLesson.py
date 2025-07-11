import pymysql
import redis
from pymysql
def connect_redis():


    # 基本连接配置
    r = redis.Redis(
        host='xue-xi-yan-fa-redis-nextapp-twproxy.xesv5.com',
        port=2080,
        password='hSL18msdMCrxp5Z_',
        db=0,  # 默认数据库
        decode_responses=True  # 自动解码为字符串
    )
    # 测试连接
    try:
        if r.ping():
            print("✅ Redis连接成功")
            # 基本操作示例
            r.set("demo_key", "Hello Redis!")
            print("获取值:", r.get("demo_key"))
    except redis.ConnectionError as e:
        print(f"❌ 连接失败: {e}")


def connect_mysql(execute):
    # 打开数据库连接
    db = pymysql.connect(host='localhost',
                         user='testuser',
                         password='test123',
                         database='TESTDB')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(execute)
    # 关闭数据库连接
    db.close()





def planDone():
    pass

if __name__ == '__main__':
    connect_redis()

