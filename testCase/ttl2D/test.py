from datetime import datetime, timedelta
import redis
def execute_redis(uid):
    """清空指定用户当天的学习记录缓存"""
    try:
        # 使用 redis-py 管道执行命令
        r = redis.Redis(
            host='xue-xi-yan-fa-redis-nextapp-twproxy.xesv5.com',
            port=2080,
            password='hSL18msdMCrxp5Z_',
            decode_responses=True
        )

        today = datetime.now().strftime("%Y%m%d")
        key = f"preschool:study:v2:user_today_finished_day:{uid}:{today}"

        # 使用管道执行命令
        pipe = r.pipeline()
        pipe.delete(key)
        result = pipe.execute()

        if result and result[0] > 0:
            print(f"redis已清空: 删除了 {result[0]} 个 key")
        else:
            print("redis已清空: key 不存在")

    except Exception as e:
        print(f"Redis操作失败: {e}")


if __name__ == '__main__':
    execute_redis(123)
