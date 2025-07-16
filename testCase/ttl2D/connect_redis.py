


"""
redis-cli -h xue-xi-yan-fa-redis-nextapp-twproxy.xesv5.com -p 2080 -a hSL18msdMCrxp5Z_

10.176.5.171
"""


import socket
import redis

import requests

proxy = {
    'http': '10.85.35.144:8080',

}

# 注意：这不是真正的Redis协议，需要代理服务器支持原始TCP转发
response = requests.get(
    'http://10.176.5.171:2080',
    proxies=proxy,
    auth=('', 'hSL18msdMCrxp5Z_')  # 基本认证
)
print(response.status_code)