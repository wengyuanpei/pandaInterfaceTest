
baseurl_web='https://pad-dev.xiongmaoboshi.com/'  #这个是后台的接口




baseurl_pad='https://pad-api-dev.xiongmaoboshi.com/'  #这个是pad的接口




#创建平板礼包合集
def gift_bag_group_add():
    url=baseurl_web+"s/drpanda/pad/web/gift-bag-group-add"
    return url


#平台礼包合集列表
def gift_bag_group_list_url():
    url=baseurl_web+"s/drpanda/pad/web/gift-bag-group-list"
    return url

#创建平板礼包
def gift_bag_add_url():
    url=baseurl_web+"s/drpanda/pad/web/gift-bag-add"
    return url

#平板礼包编辑
def gift_bag_update():
    url="s/drpanda/pad/web/gift-bag-update"
    return url

#平板礼包删除
def gift_bag_delete():
    url="s/drpanda/pad/web/gift-bag-delete?id={id}"
    return url



#平板礼包列表
def gift_bag_list():
    url="s/drpanda/pad/web/gift-bag-list"
    return url


#SN码领取记录   特殊字符

def sn_list():
    url='s/drpanda/pad/web/application/'

#小程序判断平板是否已经发放权益
def receive():
    url ='ns/drpanda/pad/min-app/judge/receive'
    return url

# 平板判断是否已经发放权益

#小程序端扫码绑定领取权益
def equity():
    url='ns/drpanda/pad/min-app/bind/equity'
    return

#小程序端查看平板权益
def equity_see():
    url='ns/drpanda/pad/min-app/query/equity'
    return url

#pad端查看权益
def equity_pad_see():
    url='ns/drpanda/pad/pad/application/query/equity'
    return url

#小程序激活已经领取的权益
def equity_live():
    url='ns/drpanda/pad/min-app/active/equity'
    return url

#web端添加白名单
def white_list_add():
    url="s/drpanda/pad/web/application/white-list-add"
    return url

#web端白名单修改
def white_list_update():
    url="s/drpanda/pad/web/application/white-list-update"
    return url

#web端白名单删除
def white_list_delete():
    url="s/drpanda/pad/web/application/white-list-delete?id={id}"
    return url

#web端白名单列表
def white_list():
    url="s/drpanda/pad/web/application/white-list"
    return url

#pad端获取所有白名单
def white_list_pad():
    url="ns/drpanda/pad/pad/application/white-list"
    return url

#平台礼包合集上下架
def white_list_release():
    url="s/drpanda/pad/web/gift-bag-group/release"

    return url

#B端-平板SN激活详情
def pad_sn():
    url="s/drpanda/pad/web/application/receive/record/detail"

    return url

#web端获取机型列表
def pad_type_list():
    url="s/drpanda/pad/web/pad-type-list"

    return url



# 灯塔接口

def tags_type_add_url():
    url01='s/**/tags-type-add'
    return url01

