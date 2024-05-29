import re


def lua_reader(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        data = file.read()
    return data


# 文件地址自行修改
if __name__ == '__main__':
    filepath = r'C:\Users\zhang\Desktop\听力机\pandaInterfaceTest\testCase\iAbc\lua\Draws.lua'  # Lua文件路径
    lua_data = lua_reader(filepath)
    # print(lua_data)
    # 绘本id匹配
    pattern = r"\[([^\]]+)\]"
    matches_id = re.findall(pattern, lua_data)
    # print(matches_id)
    #匹配绘本名
    start='name_ ='
    end='resCover_'
    #匹配绘本名称
    pattern_name=rf"{start}\s*(.+?)\s*{end}"
    matches_name = re.findall(pattern_name, lua_data)
    # print(matches_name)


    #绘本ID 匹配
    listBook=[]
    for id,name in zip(matches_id,matches_name):
        listBook.append([id,name])
    # print(listBook)
    #根据id输出绘本名字
    id='3205'
    for i in listBook:
        if id in i:
            print("id是%s的绘是" % id,i[1])
