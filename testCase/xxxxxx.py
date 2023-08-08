import json

def create_nested_json():
    # 创建一个空字典
    nested_json = {}

    # 添加第一层键值对
    nested_json['key1'] = 'value1'
    nested_json['key2'] = 'value2'

    # 创建一个嵌套的字典
    nested_dict = {}
    nested_dict['nested_key1'] = 'nested_value1'
    nested_dict['nested_key2'] = 'nested_value2'

    # 将嵌套字典添加到第一层字典中
    nested_json['nested_dict'] = nested_dict

    # 创建一个嵌套的列表
    nested_list = ['item1', 'item2', 'item3']

    # 将嵌套列表添加到第一层字典中
    nested_json['nested_list'] = nested_list

    # 将字典转换为 JSON 字符串
    json_str = json.dumps(nested_json, indent=4)

    return json_str

# 调用函数生成多层 JSON 结构
nested_json_str = create_nested_json()
print(nested_json_str)