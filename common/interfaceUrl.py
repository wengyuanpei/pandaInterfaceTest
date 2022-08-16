
def baseurl():
    baseurl='https://pad-api-dev.xiongmaoboshi.com/'
    return baseurl

#创建平板礼包合集
def gift_bag_group_add():
    url="s/drpanda/pad/web/gift-bag-group-add"
    return url


#平台礼包合集列表
def gift_bag_group_list():
    url="s/drpanda/pad/web/gift-bag-group-list"
    return url

#创建平板礼包
def gift_bag_add():
    url="s/drpanda/pad/web/gift-bag-add"
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





# 灯塔接口

def tags_type_add_url():
    url01='s/**/tags-type-add'
    return url01

