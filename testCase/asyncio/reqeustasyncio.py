import asyncio
import requests
from concurrent.futures import ThreadPoolExecutor


async def fetch(url, session, request_id, executor):
    try:
        print(f"请求 {request_id} 开始")
        response = await loop.run_in_executor(
            executor,
            lambda: session.get(url))
        print(f"请求 {request_id} 完成，状态码: {response.status_code}")
        return response.text
    except Exception as e:
        print(f"请求 {request_id} 出错: {str(e)}")
        return None


async def main():
    url = "https://httpbin.org/get"
    concurrency = 10

    # 创建线程池
    executor = ThreadPoolExecutor(max_workers=concurrency)

    # 每个线程使用独立的Session
    session = requests.Session()

    tasks = []
    for i in range(concurrency):
        task = asyncio.create_task(fetch(url, session, i + 1, executor))
        tasks.append(task)

    responses = await asyncio.gather(*tasks)
    print(f"总共完成 {len(responses)} 个请求")

    # 清理资源
    executor.shutdown(wait=True)
    session.close()


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()