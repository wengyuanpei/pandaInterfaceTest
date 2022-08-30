
baseurl_web='https://pad-dev.xiongmaoboshi.com/'  #这个是后台的接口




baseurl_pad='https://pad-api-dev.xiongmaoboshi.com/'  #这个是pad的接口




#创建平板礼包合集-ok
def gift_bag_group_add():
    url=baseurl_web+"s/drpanda/pad/web/gift-bag-group-add"
    return url


#平台礼包合集列表-ok
def gift_bag_group_list_url():
    url=baseurl_web+"s/drpanda/pad/web/gift-bag-group-list"
    return url

#创建平板礼包-ok
def gift_bag_add_url():
    url=baseurl_web+"s/drpanda/pad/web/gift-bag-add"
    return url

#平板礼包编辑-ok
def gift_bag_update_url():
    url=baseurl_web+"s/drpanda/pad/web/gift-bag-update"
    return url


#平板礼包删除 -ok
def gift_bag_delete_url():
    url=baseurl_web+"s/drpanda/pad/web/gift-bag-delete?"
    return url



#平板礼包列表-ok
def gift_bag_list_url():
    url=baseurl_web+"s/drpanda/pad/web/gift-bag-list"
    return url

#SN码领取记录 -ok

def receive_record_list_url():
    url=baseurl_web+"s/drpanda/pad/web/application/receive/record/list"
    return url


#web端添加白名单 -ok
def white_list_add_url():
    url=baseurl_web+"s/drpanda/pad/web/application/white-list-add"
    return url



#web端白名单修改 -ok
def white_list_update_url():
    url=baseurl_web+"s/drpanda/pad/web/application/white-list-update"
    return url



#web端白名单删除-ok
def white_list_delete_url():
    url=baseurl_web+"s/drpanda/pad/web/application/white-list-delete?"
    return url



#web端白名单列表 -ok
def application_white_list_url():
    url=baseurl_web+"s/drpanda/pad/web/application/white-list"
    return url


#web端获取机型列表
def pad_type_list_url():
    url=baseurl_web+"s/drpanda/pad/web/pad-type-list"

    return url



