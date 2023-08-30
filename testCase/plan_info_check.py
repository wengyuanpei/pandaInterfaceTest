# coding:utf-8
import requests
from common.finish_plan_urlenverment import *
from time import sleep

uidlist=[1111231209041,
1673521949928181761,
0,
166446229794493644,
166446229794,
1677514107694317569,
1678207612001759234,
1678227575164940290,
1676943285946519554,
1676844684280958978,
1678207524214976513,
1637341169567461377,
1678207524214976513,
1677473850718388225,
1673598015506329602,
1638058141213868033,
1675413898159820802,
1676146704968159234,
1678227568391139329,
1637695993316982785,
1636614095216947201,
1675781638886576129,
1679463055549345794,
1675413899353313281,
1664162981414031361,
1638853113282564098,
1641618904969633793,
1674327776284381186,
1546105642325368833,
1666617549487390722,
1675047406538231809,
1247907987132846082,
1676848479706775554,
1664654809299734530,
1676146702884966401,
1225777926203047938,
1675413899353313281,
1642870024736940034,
1640605899060744194,
1268544820929695746,
1659456360795811842,
1637695993316982785,
1678751258579361794,
1679456022412767234,
1678207524214976513,
1679680037914464257,
1678207524214976513,
1256454727823896577,
1256454727823896577,
1665571208138379265,
1629327922231590914,
1677473850718388225,
1651466220789227522,
1638742075413311490,
1674327776284381186,
1669256795623886850,
1676146704968159234,
1678576102153363457,
1675413899353313281,
1679842151442341889,
1678667075295174658,
1361822399788204034,
1635992926515752962,
1679716102238015490,
1636240895752646658,
1638058141213868033,
1680118680011374594,
1638469154437656578,
1669875586240147458,
1679479275656491009,
1679479275656491009,
1676146704968159234,
1638058141213868033,
1636320814648324098,
1599006485522726914,
1641028573283557378,
1679032708885983233,
1679414495917486081,
1653634968558567425,
1680463533856649217,
1674327776284381186,
1651208348735619075,
1659008420402900993,
1676146704968159234,
1674334222992543746,
1674731838139109378,
1631192545830281217,
1674327776284381186,
1629327920028094465,
1260868789673070593,
1235182607167569921,
1650383637250252801,
1638369987719655426,
1679997960135766017,
1680493390832263170,
1544576343172005890,
1654690603707305985,
1677487683599962114,
1664264253089632257,
1681579433639731201,
1678573583465422850,
1675104111371063298,
1679108988318855169,
1637695992738168834,
1664190411472822273,
1637261358637363201,
1606177770294083585,
1678227554396504066,
1544576343172005890,
1675781635979923458,
1678241418018004994,
1681207014391980033,
1637342223387148290,
1635994087151480833,
1680058685487181826,
1606177769817821185,
1665571208138379265,
1679033756941889538,
1676056997510156289,
1377927205900120065,
1670341517103325186,
1603346282996490241,
1650693813828136962,
1681937677969186818,
1631176728467660801,
1682299360185081858,
1682301765047193601,
1681604541229887490,
1682215101301952514,
1682209004025450498,
1682207657528844290,
1624237122540400642,
1640006667286650881,
1682222624890593281,
1434385448378503170,
1629327926655393793,
1651490295611207682,
1682206350437425154,
1640943121039429634,
1679690942869049346,
1682222624890593281,
1588076404861239298,
1675047738427936769,
1436988742638682113,
1682040172120018945,
1654392206910881794,
1680522671463563266,
1682252439035224066,
1557685650197581825,
1681107680184340481,
1673957753231683586,
1678222575849930753,
1636576260917145601,
1684739595322433538,
1684744744565080066,
1638744717883609090,
1637823970402975746,
1636648354571153409,
1679855774466236418,
1641353325659258882,
1684500117511901186,
1636609568780906498,
1683507341161586689,
1650351097394290690,
1684914667143876609,
1683999333821898753,
1587057475944685569,
1680771877348540417,
1682215205930180610,
1684369299616100354,
1665546184354738178,
1679760832158142466,
1678964440312897538,
1641802534757933058,
1664525870595428353,
1681521501642264577,
1684875447040905218,
1682211193561190402,
1677093826412642305,
1684875444080406530,
1635991323477360641,
1638576273859407873,
1683022567942713345,
1678254000309248001,
1684875450870304770,
1683090548302712834]


listt=[1481461004571475970,
1568474100482093058,
1599742732982231042,
1601016285109014530,
1611229848665759746,
1624977807136649217,
1636535337036607490,
1636648354022506497,
1637102815958921217,
1637695993170182145,
1639953416937541633,
1641067697910546434,
1641356034700730371,
1641720742398885889,
1650693813664559106,
1652578208417824770,
1655954113232093186,
1665986725842194433,
1669244629847367681,
1673957756262916098,
1674718033432096769,
1674731838508208130,
1674767253169934338,
1675413897766932482,
1675413899579805697,
1675781637389209601,
1676146700333580290,
1676146706717310978,
1676866832514875393,
1678553444279885825,
1682210098727018498,
1684209468275331074,
1684497862377926658,
1684875444915707905,
1686229094816210946,
1686282611232919553,
1686282612012126209,
1686282614139318273,
1686282615791194113,
1686282617854791682,
1686639504580190210,
1686685594510888962,
1687035837938343938]

def checkuerplaninfo(uid):
    baseurl=urlenverment(2)
    url=baseurl+'v1/study/my-plan'
    anthpre='Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjg2NjM5NTA0NTgwMTkwMjEwIiwic3ViIjoie1wiaWRcIjoxNjg2NjM5NTA0NTgwMTkwMjEwLFwibW9iaWxlXCI6XCIrODYxODM4NDI1MzUwNlwifSIsImV4cCI6MTcwNjUxMzE2OX0.c8ch4WBbE6raEe8PKSkMcf5-GcO-TNis81sAcrE6RveVntoxUtVB076l8lhfA1IqshgF1u7msB9Q9uUlmIVhRw'
    header = {'Authorization': anthpre}

    data={
        "uid": uid
    }

    req=requests.post(url=url,json=data,headers=header)

    return req.json()


if __name__ == '__main__':
    errorlist = []
    for uid in listt:

        info=checkuerplaninfo(1676844684280958978)['data']
        sleep(1.5)
        # print(info)
        if info['level'] == '' or info['week_plan'] == None or info['study_time'] == '':
            errorlist.append(uid)
            print('uid：%s，用户异常!' %uid)
        else:
            print('正常用户信息>>>>>>>>>',info)

    print('异常用户列表：',errorlist)
