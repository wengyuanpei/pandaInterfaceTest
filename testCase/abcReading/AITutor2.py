import asyncio
import json
import struct
import websockets
import aioconsole


# seq = 10001
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
    print(f"Sent message with command_code {command_code}, seq {seq}, data {data}")


async def on_open(ws, seq):
    print("连接已打开")
    # 发送第一个类型的消息
    seq = seq + 1
    await send_message(ws, command_code=0x01, seq=seq, data='{"user_id":11221113}')
    # 开始一个新的对话 task_id 1-50 model: task/free?
    seq = seq + 1
    await send_message(ws, command_code=0x02, seq=seq, data='{"model":"task","task_id":4}')


headers = {
    "appVersion": "391",
    "platform": "python",
}


async def main():
    #gpt
    uri = "ws://ai-tutor-dev.xiongmaoboshi.com/ai_tutor"
    #千问
    # uri = "ws://api-dev-inner.abctime.com/ai_tutor"
    # uri = "ws://10.85.66.146:8911/ai_tutor"
    seq = 10001
    last_output = ""
    # user_input = await aioconsole.ainput("请输入内容: ")
    # print(user_input)
    async with websockets.connect(uri, extra_headers=headers) as websocket:
        await on_open(websocket, seq)
        async for message in websocket:
            print("收到消息:", message)
            first_byte = message[0]

            decoded_str = message.decode("utf-8")

            # 从解码后的字符串中提取JSON部分，假设JSON总是从第一个左大括号开始
            json_str = decoded_str[decoded_str.index('{'):]
            # 解析JSON字符串
            parsed_json = json.loads(json_str)
            if  first_byte!= 9:

                print(parsed_json)
            outputStr = parsed_json.get("output")
            available_count = parsed_json.get("available_count")
            #解析available_count
            # available_count = int(available_count)
            #转为int
            # available_count = int(available_count)
            print("available_count:", {available_count})
            last_output = outputStr
            # print(first_byte)
            # print("outputStr:", {outputStr})
            if outputStr:
                if first_byte == 2 or first_byte == 3 or first_byte == 4 or first_byte == 5 or first_byte == 6:

                    cmd = await aioconsole.ainput("输入1 只对话(默认task模式);输入2 只润色，输入3 只跟读，输入4翻译： 请输入:1,2,3,4其中一个数字  :")
                    if cmd == "1":

                        user_input = await aioconsole.ainput("用户输入: ")
                        await send_message(websocket, command_code=0x03, seq=seq, data=f'{{"input":"{user_input}"}}')
                        seq = seq + 1;
                    elif cmd == "2":
                        user_input = await aioconsole.ainput("用户输入")
                        question = await aioconsole.ainput("请输入问题")

                        await send_message(websocket, command_code=0x04, seq=seq, data=f'{{"input":"{user_input}",'
                                                                                       f'"question":"{question}"}}')
                        seq = seq + 1;
                    elif cmd == "3":
                        need_follow = await aioconsole.ainput("是否需要跟读?,输入系统的问题:")
                        await send_message(websocket, command_code=0x05, seq=seq, data=f'{{"question":"{need_follow}"}}')
                        seq = seq + 1;

                    elif cmd == "4":
                        translate = await aioconsole.ainput("是否需要翻译？输入需要的翻译内容:")
                        await send_message(websocket, command_code=0x06, seq=seq, data=f'{{"input":"{translate}","src":"cn","dst":"en"}}')
                        seq = seq + 1;
                    elif cmd == "5":
                        #开始新的对话
                        await send_message(websocket, command_code=0x02, seq=seq, data='{"task_id":4,"model":"free"}')
                    else:
                        print("输入错误,重新开始一个新的round对话")
                        # await send_message(websocket, command_code=0x02, seq=seq, data='{"task_id":4,"model":"free"}')
                        await send_message(websocket, command_code=0x02, seq=seq, data='{"task_id":4,"model":"free"}')


                    # 开始对话

                    # question = await aioconsole.ainput("请输入问题,不输入进入T1【0x03】,输入进入0x04【润色环节】:")
                    #
                    # need_follow = await aioconsole.ainput("是否需要跟读?,输入系统的问题:")
                    # translate = await aioconsole.ainput("是否需要翻译？输入需要的翻译内容:")
                    # # #
                    # # # # 获取点评 自己的问题 + 系统的问题
                    # # if  last_output:
                    # # 判断用户输入的问题长度是否大于3
                    #
                    # if len(question) > 2 and len(user_input) > 2:
                    #     await send_message(websocket, command_code=0x04, seq=seq, data=f'{{"input":"{user_input}",'
                    #                                                                    f'"question":"{question}"}}')
                    # elif len(user_input) > 2:
                    #     await send_message(websocket, command_code=0x03, seq=seq, data=f'{{"input":"{user_input}"}}')
                    #     seq = seq + 1;
                    # # await send_message(websocket,command_code=0x04, seq=12346,data=f'{{"input":"{user_input}",'
                    # #                                                                f'"question":"{question}"}}')
                    # # #获取两个跟读例句，在用户没有达对的情况下
                    # if len(need_follow) > 2:
                    #     await send_message(websocket, command_code=0x05, seq=seq, data=f'{{"question":"{need_follow}"}}')
                    #     seq = seq + 1;
                    # # await send_message(websocket,command_code=0x05, seq=12346,data=f'{{"question":"{user_input}"}}')
                    # # #翻译
                    # if len(translate) > 2:
                    #     await send_message(websocket, command_code=0x06, seq=seq, data=f'{{"input":"{translate}","src":"cn","dst":"en"}}')
                    #     seq = seq + 1;

                    # await send_message(websocket,command_code=0x06, seq=12346,data=f'{{"input":"{user_input}","src":"cn","dst":"en"}}')
                    # # 心跳
                    # await send_message(websocket,command_code=0x08, seq=12346,data={"{}"})


if __name__ == "__main__":
    asyncio.run(main())
