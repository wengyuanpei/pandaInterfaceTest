'''

这个是公共方法构造请求参数签名

'''

from hashlib import sha256


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


def get_json_map(jsonnn):

    aa = ''
    posision=0
    bb=''
    result = sorted(jsonnn.items())
    for i in result:
        for ii in i:
            if type(ii) != dict:
                aa += str(ii)
            else:
                posision=len(aa)
                # print('当前的位置：',posision)
                result1 = sorted(ii.items())
                # print(result1)

                for k in result1:
                    for kk in k:
                        if type(kk) != dict:
                            bb += str(kk)

    textend0=str_insert(aa, posision, bb)
    # print(textend0)

    endaa = textend0.replace("[", "")
    endaa = endaa.replace("]", "")
    endText = endaa.replace(" ", "")

    return endText
#
def getSignEnd(requestData,env:str):
    if env=='dev':
        text1 = get_json_map(requestData)
        text2 = signABC()[0]
        tend = text1 + text2
        sign = generate_sha256_hashCode(tend)

        requestData.update({'sign':sign})
        # print('生成签名成功！')
        print('生成签名成功！当前签名是dev')
    if env=='pre' or env=='live':
        text1 = get_json_map(requestData)
        text2 = signABC()[1]
        tend = text1 + text2
        sign = generate_sha256_hashCode(tend)

        requestData.update({'sign': sign})
        # print('生成签名成功！')
        print('生成签名成功！当前签名是pre')
    return requestData

if __name__ == '__main__':
    js={
    "stage_num": 5,
    "is_again": bool(0),
    "cost_time": 61430,
    "timestamp": "1711357187",
    "true_proportion": 88,
    "proportion": 100,
    "uuid": "Y2E4MTZhNTljZWRkYWM5MTIyNjQ2ODc5MjhmM2UyYTU=",
    "token": "660133ed33d6c",
    "extra": "{\"currentCorrectCount\":5,\"allCount\":23,\"maxScore\":100,\"challengeRate\":4,\"openCount\":17,\"correctCount\":15,\"maxCorrentCount\":6}",
    "stage": 4,
    "challenges_id": 9,
    "uid": 63080,
    "source": "2",
    "open_num": 4,
    "score": 81,
    "continue_true_num": 6,
    "video_urls": [],
    "stage_type": 3,
    "false_num": 1,
    "again_coin": 0,
    "true_num": 8,
    "version": "400",
    "member_id": 63080,
    "answer_num": 9
}
    a=getSignEnd(js,'dev')
    #验证签名

    print(a)
