# -*- coding: utf-8
from time import sleep

import requests


# 接口登录
def login_yapi():
    logurl = 'http://yapi.txbapp.com/api/user/login'
    data = {'email': "2829226204@qq.com", 'password': "guoguo250"}
    heaher = {
        'Accept': 'application/json, text/plain, */*',
        'Host': 'yapi.txbapp.com',
        'Origin': 'http://yapi.txbapp.com'
    }
    login = requests.post(url=logurl, json=data, headers=heaher)
    print(login.status_code)
    # print(login.cookies)
    return login.cookies


# 获取所有接口列表信息
def get_list_api():
    cookie = login_yapi()

    url = 'http://yapi.txbapp.com/api/interface/list?page=1&limit=1000&project_id=46'
    listt = requests.get(url=url, cookies=cookie)
    # print(listt.json())
    return listt.json()


# 获取接口详情
def getapiinfo(id):
    urlgetapiinfo = 'http://yapi.txbapp.com/api/interface/get?id=' + str(id)
    apiinfo = requests.get(url=urlgetapiinfo, cookies=login_yapi())

    return apiinfo.json()


if __name__ == '__main__':
    resposedata = get_list_api()['data']['list']
    list = []

    print(resposedata)
    for i in range(len(resposedata)):
        # print(resposedata[i]['title'])
        title = resposedata[i]['title']


        # print(resposedata[i]['path'])
        path = resposedata[i]['path']


        method = resposedata[i]['method']


        # print('%s接口地址为【%s】>>请求方式%s' % (title, path, method))
        baseinfo = '%s接口地址为【%s】>>请求方式%s' % (title, path, method)
        list.append([[title], [path], [method]])

        id = resposedata[i]['_id']
        apiinfo = getapiinfo(id)['data']

    print(list)
    # list=[['上报学习记录', '/v1/record/add', 'POST'], ['绘本等级tab栏', '/v1/book/level-map', 'POST'], ['首页-第n屏', '/v1/page/index/{:id}', 'GET'], ['音视频列表(用户,暂不需对接)', '/v1/record/media/list', 'POST'], ['课包列表(用户)', '/v1/record/lesson/list', 'POST'], ['栏目下课包列表', '/v1/page/lesson-list', 'POST'], ['学习记录', '/v1/record/lesson/recents', 'POST'], ['定级上报', '/v1/study/set-level', 'POST'], ['定级测试题', '/v1/study/level-test', 'GET'], ['级别信息', '/v1/study/level-list', 'GET'], ['错词记录', '/v1/wrong/get-word', 'POST'], ['获取今日计划(英语)', '/v1/study/plan-info', 'POST'], ['完成计划上报(英语)', '/v1/study/finish-plan', 'POST'], ['学习计划历史(英语)', '/v1/study/history', 'POST'], ['重置学习等级', '/v1/study/reset-level', 'POST'], ['我的计划页面(英语)', '/v1/study/my-plan', 'POST'], ['学情报告（周）', '/v1/study/week-report', 'POST'], ['我的积分', '/v1/record/integral', 'POST'], ['跟读作品', '/v1/record/reading', 'POST'], ['作品分享', '/v1/study/work-share', 'POST'], ['获取今日计划(语文)', '/v1/study-cn/plan-info', 'POST'], ['完成计划上报(语文)', '/v1/study-cn/finish-plan', 'POST'], ['[无用]学习计划历史(语文)', '/v1/study-cn/history', 'POST'], ['语音助手技能', '/v1/study/skills', 'POST'], ['汉字列表(用户)', '/v1/record/char-list', 'POST'], ['汉字信息', '/v1/char/info', 'POST'], ['我的计划页面(语文)', '/v1/study-cn/my-plan', 'POST'], ['通过资源ID获取音视频列表', '/v1/resource/media-list', 'POST'], ['汉字信息(用户)', '/v1/record/char-info', 'POST'], ['学情报告（总）', '/v1/study/general-report', 'POST'], ['用户绑定孩子', '/v1/study/add-relationship', 'POST'], ['查询用户孩子', '/v1/study/get-relationship', 'POST'], ['鹦鹉阅读L0-L6', '/v1/highlights/level', 'POST'], ['绘本音频列表', '/v1/highlights/book/:id', 'GET'], ['听写-RAZ列表', '/v1/dictation/raz-list', 'POST'], ['聊天问答', '/v1/openapi/request', 'POST'], ['设置偏好', '/v1/study/set-preference', 'POST'], ['全局配置', '/v1/config/global', 'GET'], ['音频信息(后台使用)', '/hear-admin/v1/media/audio/{id}', 'GET'], ['视频信息(后台使用)', '/hear-admin/v1/media/video/{id}', 'GET'], ['文案', '/v1/config/clerical', 'POST'], ['获取每天学习时长', '/v1/record/watching', 'POST'], ['批量获取音频信息', '/v1/media/audio-list', 'POST'], ['批量获取视频信息', '/v1/media/video-list', 'POST'], ['获取分类id（配置）', '/v1/media/classify', 'GET'], ['获取带学习记录的音频列表', '/v1/highlights/book-record', 'POST'], ['获取牛津树音频歌词学习记录', '/v1/record/oxford-audio', 'POST'], ['获取口语训练列表', '/v1/ai-oral-training/get-list', 'POST'], ['重点词汇', '/v1/ai-oral-training/key-words', 'POST'], ['句子跟读/角色扮演', '/v1/ai-oral-training/sentence', 'POST'], ['阅读理解题', '/v1/book/comprehension', 'POST'], ['获取单词详情', '/v1/flashcard/get_word_info', 'POST'], ['获取单词测试题', '/v1/flashcard/get_word_test', 'POST'], ['获取等级列表', '/v1/ai-oral-training/get-level-list', 'GET'], ['新版今日计划页面', '/v1/study/plan-info-new', 'POST'], ['上报磨耳朵时长', '/v1/study/report-listen', 'POST'], ['获取磨耳朵音频列表', '/v1/study/listen-list', 'POST'], ['百度网盘存储', '/v1/record/store-baidu-disk', 'POST'], ['百度网盘获取', '/v1/record/list-baidu-disk', 'POST'], ['百度网盘删除', '/v1/record/delete-baidu-disk', 'POST'], ['新版语文学习计划', '/v1/study-cn/plan-info-new', 'POST'], ['新版语文计划历史学习记录', '/v1/study-cn/history-new', 'POST'], ['重设语文本周计划', '/v1/study-cn/reset-week-plan', 'POST'], ['上报新版语文计划', '/v1/study-cn/report-plan-new', 'POST'], ['获取语文资源详情', '/v1/study-cn/resource-detail', 'POST'], ['英语Raz绘本历史记录', '/v1/study/raz-history', 'POST'], ['绘本列表', '/v1/book/book-list', 'POST'], ['课包列表（暂不用对接）', '/v1/resource/{id}', 'GET'], ['错词本', '/v1/wrong/get', 'POST'], ['听写-教材列表', '/v1/dictation/textbook', 'POST'], ['绘本内容', '/v1/book/book-content', 'POST'], ['音视频列表', '/v1/lesson/{id}', 'GET'], ['上报错词记录', '/v1/wrong/add', 'POST'], ['听写-教材资源列表', '/v1/dictation/rescourse', 'POST'], ['单词列表', '/v1/book/words-list', 'POST'], ['音频信息', '/v1/media/audio/{id}', 'GET'], ['选词', '/v1/dictation/select', 'POST'], ['绘本详情', '/v1/book/book-detail', 'POST'], ['视频信息', '/v1/media/video/{id}', 'GET'], ['上报听写记录', '/v1/dictation/add-dictation', 'POST'], ['获取单词已学未学数量', '/v1/book/words-num', 'POST'], ['音频播放进度', '/v1/record/audio', 'POST'], ['听写记录', '/v1/dictation/dictation-record', 'POST'], ['视频播放进度', '/v1/record/video', 'POST'], ['绘本互动单词', '/v1/book/interactive-word', 'POST'], ['扣词', '/v1/dictation/deduction', 'POST'], ['课包上次播放集数', '/v1/record/lesson/last', 'POST'], ['根据纳米获取单词数据', '/v1/dictation/grade-textbook', 'POST']]

    from common.excelreadwrite import *
    excelname=r'C:\Users\zhang\Desktop\pandaInterfaceTest\testCase\api\apiautotest.xlsx'
    for i in range(len(list)-1):
        print(i)
        for ii in range(len(list[i])):

            excel_write(list[i][0],2+i,'A',excelname,'Sheet1')
            excel_write(list[i][1],2+i, 'B', excelname, 'Sheet1')
            excel_write(list[i][2],2+i, 'C', excelname, 'Sheet1')



