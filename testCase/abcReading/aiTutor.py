import asyncio
import json
import struct
import websockets
import aioconsole

async def send_message(ws, command_code, seq, data):
    """
    发送消息给服务器。
    :param ws: WebSocket连接
    :param command_code: 命令代码，用于区分不同类型的消息
    :param seq: 消息序列号
    :param data: 消息内容，预期为JSON字符串
    """
    # 编码消息内容
    original_data = data.encode('utf-8')

    # 构造消息
    mutable_data = bytearray()
    mutable_data.append(command_code)
    seq_bytes = struct.pack('>I', seq)
    mutable_data.extend(seq_bytes)
    mutable_data.extend(original_data)

    # 发送消息
    await ws.send(mutable_data)
    print(f"Sent message with command_code {command_code}, seq {seq}")

async def on_open(ws):
    print("连接已打开")
    # 发送第一个类型的消息
    await send_message(ws, command_code=0x01, seq=12345, data='{"user_id":1}')
    # 开始一个新的对话 task_id 1-50 model: task/free?
    await send_message(ws, command_code=0x02, seq=12346, data='{"task_id":3,"model":"task"}')

async def main():
    uri = "ws://ai-tutor-dev.xiongmaoboshi.com/ai_tutor"
    # user_input = await aioconsole.ainput("请输入内容: ")
    # print(user_input)
    async with websockets.connect(uri) as websocket:
        await on_open(websocket)
        async for message in websocket:
            print("收到消息:", message)
            first_byte = message[0]

            decoded_str = message.decode("utf-8")

            # 从解码后的字符串中提取JSON部分，假设JSON总是从第一个左大括号开始
            json_str = decoded_str[decoded_str.index('{'):]

            # 解析JSON字符串
            parsed_json = json.loads(json_str)
            print(parsed_json)
            outputStr = parsed_json.get("output")
            print(first_byte)
            if  outputStr:
                if  first_byte == 2 or first_byte == 3:
                    user_input = await aioconsole.ainput("用户输入: ")
                    # 开始对话
                    await send_message(websocket,command_code=0x03, seq=12346,data=f'{{"input":"{user_input}"}}')
                    # question = await aioconsole.ainput("请输入问题: ")
                    #
                    # # 获取点评 自己的问题 + 系统的问题
                    # await send_message(websocket,command_code=0x04, seq=12346,data=f'{{"input":"{user_input}",'
                    #                                                                f'"question":"{question}"}}')
                    # #获取两个跟读例句，在用户没有达对的情况下
                    # await send_message(websocket,command_code=0x05, seq=12346,data=f'{{"question":"{user_input}"}}')
                    # #翻译
                    # await send_message(websocket,command_code=0x06, seq=12346,data=f'{{"input":"{user_input}","src":"cn","dst":"en"}}')
                    # # 心跳
                    # await send_message(websocket,command_code=0x08, seq=12346,data={"{}"})



if __name__ == "__main__":
    asyncio.run(main())
