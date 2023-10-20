#coding:UTF-8
import requests

tag={
25:"未参加打卡",
26:"注册用户",
27:"注册时间固定期限",
28:"打卡相关",
30:"单渠道测试",
31:"多渠道测试",
32:"注册时间距今时间段",
33:"当前是VIP",
34:"用户活跃",
70:"月卡在生效用户",
81:"用户表-全条件",
82:"老用户待续费",
84:"老用户已续费(至少2个年卡)",
85:"有年卡且有月卡",
86:"有过期VIP",
87:"有过期畅玩年卡",
88:"用户&付费商品关联",
89:"用户&付费商品&过期商品关联",
90:"年卡付费未打卡 付费商品&打卡 关联",
91:"最近30天注册未打卡的用户",
92:"最近60天注册关联打卡",
93:"年卡付费未打卡",
94:"有效年卡&过期月卡&未打卡",
96:"3表关联&未打卡",
97:"3表关联&打卡",
98:"7月注册最近30天活跃的免费用户",
99:"60-90天内注册最近30天活跃的免费用户(当前不是VIP&无过期VIP)",
100:"首次购买年卡VIP用户(无过期VIP)",
101:"无过期VIP用户",
110:"新增付费人群",
223:"411过期后6天",
224:"月卡过期后1-10天",
235:"新版本用户",
236:"老版标签",
237:"新版vip用户",
239:"过期VIP注册小于100天",
240:"老版vip用户",
242:"新版vip",
243:"老版本用户",
244:"2",
245:"免费用户",
246:"购买后2-12个月内（for乐途2）",
247:"非首日免费用户",
248:"全部非VIP用户",
249:"在籍会员",
}
def getTagInfo(mid):
    url="http://api-dev.abctime.com/v2/member/member/get-member-tags"
    header={'Content-Type':'application/x-www-form-urlencoded'}
    data={'member_id':mid}
    req=requests.post(url=url,data=data,headers=header)
    print(req.json())
    return req.json()


if __name__ == '__main__':

    idlist=[55012]

    for id in idlist:

        reqinfo=getTagInfo(id)['data']['app_tags_ids']
