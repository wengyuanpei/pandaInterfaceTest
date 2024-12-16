from gevent import monkey
monkey.patch_all()
from gevent.pywsgi import WSGIServer
import urllib
import urllib.parse
from collections import defaultdict
import numpy as np
import json


def dict2default(oldDic, get=True):
    newDic = defaultdict(lambda: None)
    for key, value in oldDic.items():
        if get == True:
            if len(value) == 1:
                newDic[key] = value[0]
            else:
                newDic[key] = value
        else:
            newDic[key] = value
    return newDic


def parse_query(env):
    # post
    try:
        request_body_size = int(env.get('CONTENT_LENGTH', 0))
        request_body = env['wsgi.input'].read(request_body_size)
        request_body = request_body.decode('utf-8')
    except (ValueError):
        request_body = ''
        request_body_size = 0
    # get
    recv = env['QUERY_STRING']
    get_data = urllib.parse.parse_qs(recv)  # 没解析成功则返回一个空的字典

    if request_body != '':
        try:
            # post_data = ast.literal_eval(request_body)
            post_data = json.loads(request_body)
            recv_data = dict2default(post_data, get=False)
        except:
            post_data = urllib.parse.parse_qs(request_body)
            recv_data = dict2default(post_data)
    else:
        recv_data = dict2default(get_data)
    return recv_data


class NpEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)


def application(env, start_response):
    response_headers = [('Content-type', 'application/json'),
                        ('Access-Control-Allow-Origin', '*'),
                        ('Access-Control-Allow-Credentials', 'true'),
                        ('Access-Control-Allow-Methods', 'PUT,POST,GET,PATCH,DELETE,OPTIONS'),
                        ('Access-Control-Allow-Headers',
                         'Accept,Accept-Encoding,Accept-Language,Connection,Content-Length,Content-Type,Host,Origin,Referer,User-Agent'),
                        ]
    recv_data = parse_query(env)  # 接收到的字典
    print(recv_data)
    if env['PATH_INFO'] == '？':
        if recv_data['text']:
            try:
                query = recv_data['query']
                query *= 2
                result = {
                    "result": query,
                    "status_code": "200",
                }
                result = json.dumps(result, ensure_ascii=False, cls=NpEncoder)

                result = result.encode('utf-8')
                start_response('200 OK',
                               response_headers)
                return [result]
            except Exception as e:
                result = {
                    "result": None,
                    "status_code": "500",
                }
                result = json.dumps(result, ensure_ascii=False)
                result = result.encode('utf-8')
                start_response('500',
                               response_headers)
                return [result]

    result = {
        "result": '请求无法被解析！',
        "status_code": "500",
    }
    result = json.dumps(result, ensure_ascii=False)
    result = result.encode('utf-8')
    start_response('500', response_headers)
    return [result]


if __name__ == '__main__':
    WSGIServer(('127.0.0.1', 3365), application).serve_forever()