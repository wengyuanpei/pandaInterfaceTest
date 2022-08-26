
import pymysql

# 1. 连接数据库，
conn = pymysql.connect(
    host='rm-bp1qz4b7e260219h5ho.mysql.rds.aliyuncs.com',
    user='dppad',
    password='s$gQr0MJvuLA7#@H',
    db='dev',
    charset='utf8',
       # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
)
# ****python, 必须有一个游标对象， 用来给数据库发送sql语句， 并执行的.
# 2. 创建游标对象，
cur = conn.cursor()

# 4). **************************数据库查询*****************************
sqli = "select * from hello;"
result = cur.execute(sqli)  # 默认不返回查询结果集， 返回数据记录数。
print(result)
print(cur.fetchone())     # 1). 获取下一个查询结果集;

# 4. 关闭游标
cur.close()
# 5. 关闭连接
conn.close()
