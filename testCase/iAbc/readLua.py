import lua_decoder
import json


# 解析Lua文件的函数
def parse_lua_file(lua_file_path):
    with open(lua_file_path, 'r') as file:
        lua_code = file.read()

    # 使用lua_decoder解析Lua代码
    lua_data = lua_decoder.decode(lua_code)
    return lua_data


# 将解析的Lua数据转换为JSON字符串的函数
def lua_to_json(lua_data):
    return json.dumps(lua_data, ensure_ascii=False)


# Lua文件路径
lua_file_path = 'example.lua'

# 解析Lua文件
lua_data = parse_lua_file(lua_file_path)

# 转换为JSON
json_data = lua_to_json(lua_data)

print(json_data)