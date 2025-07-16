import asyncio
#并发携程

# 定义一个协程函数
async def simple_coroutine(name, delay):
    print(f"{name} 开始执行，将等待 {delay} 秒")
    await asyncio.sleep(delay)  # 模拟IO操作
    print(f"{name} 执行完成")


# 创建事件循环并运行协程
async def main():
    # 创建多个协程任务
    task1 = simple_coroutine("协程A", 2)
    task2 = simple_coroutine("协程B", 1)
    task3 = simple_coroutine("协程C", 3)

    # 并发执行多个协程
    await asyncio.gather(task1, task2, task3)


# 运行主协程
asyncio.run(main())