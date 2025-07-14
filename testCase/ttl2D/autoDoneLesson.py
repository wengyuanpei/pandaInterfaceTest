
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
    print(r.ping())
    if method =="daytoday":
        r.delete(common)
    elif method=='daytounit':
        value=r.get(common)
        #处理时间为上一天
        r.set(common,value)
    elif method=="get":
        value=r.get(common)
        return value
    return None
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

"""Add-Content -Path "C:\Windows\System32\drivers\etc\hosts" -Value "10.176.5.171  xue-xi-yan-fa-redis-nextapp-twproxy.xesv5.com" -Force

Add-Content -Path "C:\Windows\System32\drivers\etc\hosts" -Value "10.176.5.167 oceanbase.next.oceanbase-next-test.rw.local.db.tal.com" -Force

ipconfig /flushdns

redis-cli -h xue-xi-yan-fa-redis-nextapp-twproxy.xesv5.com -p 2080 -a hSL18msdMCrxp5Z_"""

if __name__ == '__main__':
    print(redis.__version__)  # 确保 redis-py >= 3.0
    redis_del_methd="get"  #切换天

    cmd_today="preschool:study:user_today_finished_day:1090022461:20250714"
    try:
        a = connect_redis(cmd_today, redis_del_methd)
        print(a)
    except redis.AuthenticationError:
        print("Redis 认证失败！")
    except redis.ConnectionError as e:
        print("Redis 连接失败:", e)
    print(a)
