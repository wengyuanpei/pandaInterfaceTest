import asyncio
import requests
from concurrent.futures import ThreadPoolExecutor


def make_request(url, request_id):
    """
    独立的请求处理函数
    """
    try:
        print(f"请求 {request_id} 开始")
        response = requests.get(url)
        print(f"请求 {request_id} 完成，状态码: {response.status_code}")
        return response.text
    except Exception as e:
        print(f"请求 {request_id} 出错: {str(e)}")
        return None


async def fetch(url, request_id, executor, loop):
    """
    异步获取请求结果
    """
    try:
        response_text = await loop.run_in_executor(
            executor,
            make_request,
            url,
            request_id
        )
        return response_text
    except Exception as e:
        print(f"异步执行请求 {request_id} 出错: {str(e)}")
        return None


async def main():

    url = "https://httpbin.org/get"
    concurrency = 100  # 合理设置并发数，避免过高

    # 创建线程池
    executor = ThreadPoolExecutor(max_workers=20)  # 限制线程池大小

    # 为每个请求创建独立的session会带来额外开销，这里使用统一处理函数
    tasks = []
    for i in range(concurrency):
        task = asyncio.create_task(fetch(url, i + 1, executor, asyncio.get_event_loop()))
        tasks.append(task)

    responses = await asyncio.gather(*tasks)
    print(f"总共完成 {len(responses)} 个请求")

    # 清理资源
    executor.shutdown(wait=True)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
