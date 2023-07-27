from time import sleep

import requests
#接口登录
def login_yapi():
    logurl='http://yapi.txbapp.com/api/user/login'
    data={'email': "2829226204@qq.com", 'password': "guoguo250"}
    heaher={
        'Accept':'application/json, text/plain, */*',
        'Host':'yapi.txbapp.com',
        'Origin':'http://yapi.txbapp.com'
    }
    login=requests.post(url=logurl,json=data,headers=heaher)
    print(login.status_code)
    # print(login.cookies)
    return login.cookies

#获取所有接口列表信息
def get_list_api():
    cookie=login_yapi()

    url='http://yapi.txbapp.com/api/interface/list?page=1&limit=100&project_id=46'
    listt=requests.get(url=url,cookies=cookie)
    # print(listt.json())
    return listt.json()

#获取接口详情
def getapiinfo(id):
    urlgetapiinfo='http://yapi.txbapp.com/api/interface/get?id='+str(id)
    apiinfo=requests.get(url=urlgetapiinfo,cookies=login_yapi())

    return apiinfo.json()

if __name__ == '__main__':
        resposedata=get_list_api()['data']['list']

        print(resposedata)
        for i in range(len(resposedata)):
            # print(resposedata[i]['title'])
            title=resposedata[i]['title']
            # print(resposedata[i]['path'])
            path=resposedata[i]['path']
            method=resposedata[i]['method']
            # print('%s接口地址为【%s】>>请求方式%s' % (title, path, method))
            baseinfo='%s接口地址为【%s】>>请求方式%s' % (title, path, method)


            id=resposedata[i]['_id']
            apiinfo=getapiinfo(id)['data']

            print(apiinfo)

            sleep(2)

            with open(r"C:\Users\zhang\Desktop\pandaInterfaceTest\testCase\api\api.txt", "a") as f:
                f.write('\n'+str(baseinfo)+'\n'+str(apiinfo))  # 自带文件关闭功能，不需要再写
        f.close()