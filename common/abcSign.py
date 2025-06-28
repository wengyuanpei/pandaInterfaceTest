'''

这个是公共方法构造请求参数签名

'''

from hashlib import sha256

import json
def generate_sha256_hashCode(plainText):
    plainTextBytes = plainText.encode('utf-8')  # 字符串在哈希之前，需要编码
    encryptor = sha256()
    encryptor.update(plainTextBytes)
    hashCode = encryptor.hexdigest()
    # print(hashCode)
    return hashCode

def signABC():
    sign_dev='GriE93gIGp$5bDjQ4rc20FzxWGghTIau'
    sign_live_pre='hkf%t5SMv1HtrVS!Y%B!NPNS!!0cWgy'
    return sign_dev,sign_live_pre

# str_origin：源字符串  pos：插入位置  str_add：待插入的字符串

def str_insert(str_origin, pos, str_add):
    str_list = list(str_origin)    # 字符串转list
    str_list.insert(pos, str_add)  # 在指定位置插入字符串
    str_out = ''.join(str_list)    # 空字符连接
    return str_out


def flatten_json_to_str(data):
    """将JSON键值对拼接为连续字符串"""
    result = []

    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                # 处理嵌套字典或列表
                nested = flatten_json_to_str(value)
                if nested:  # 只有当嵌套结果非空时才添加
                    result.append(f"{key}{nested}")
            elif value is not None:  # 忽略None值
                # 特殊处理extra字段(已经是字符串的JSON)
                if key == "extra":
                    try:
                        extra_data = json.loads(value)
                        extra_str = flatten_json_to_str(extra_data)
                        result.append(f"{key}{extra_str}")
                    except json.JSONDecodeError:
                        result.append(f"{key}{value}")
                else:
                    result.append(f"{key}{value}")
    elif isinstance(data, list):
        for item in data:
            nested = flatten_json_to_str(item)
            if nested:
                result.append(nested)

    return "".join(result)
#
def getSignEnd(requestData,env:str):
    if env=='dev':
        text1 = flatten_json_to_str(requestData)
        text2 = signABC()[0]
        tend = text1 + text2
        sign = generate_sha256_hashCode(tend)

        requestData.update({'sign':sign})
        # print('生成签名成功！')
        print('生成签名成功！当前签名是dev')
    if env=='pre' or env=='live':
        text1 = flatten_json_to_str(requestData)
        text2 = signABC()[1]
        tend = text1 + text2
        sign = generate_sha256_hashCode(tend)

        requestData.update({'sign': sign})
        # print('生成签名成功！')
        print('生成签名成功！当前签名是pre')
    return requestData

if __name__ == '__main__':
    js = {
        "ab_study_flow3": 1,
        "again_coin": 5,
        "challenges_id": 208,
        "continue_true_num": 0,
        "cost_time": 1,
        "extra": "{\"allCount\":0,\"challengeRate\":1,\"correctCount\":0,\"currentCorrectCount\":0,\"maxCorrentCount\":0,\"maxScore\":0,\"openCount\":0}",
        "false_num": 0,
        "is_again": "false",

        "proportion": 25,
        "repair_date": 0,
        "score": 0,
        "stage": -1,
        "stage_num": 3,
        "stage_type": 1,
        "true_num": 0,
        "true_proportion": 0,
        "uid": 73279,
        "video_urls": []}

a=getSignEnd(js,'dev')
#验证签名

print(a)
