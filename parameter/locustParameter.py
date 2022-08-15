

def headerForRequests():
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0",
                   "Accept": "application/json, text/plain, */*",
                   "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                   "Accept-Encoding": "gzip, deflate, br",
                   "Content-Type": "application/x-www-form-urlencoded",
                   }
    return header




def url_001():
    url=''
    return url


def dataForGet():
    data={'draw': '5',
                'start': '0',
                'length': '13',
                'deptTypes': '[]',
                'defunctInd': 'N',
                'searchStr': 'FSK_01',
                '_': '1597112917355'}
def dataForPost():

    data= {"ipEntityMstrId": 7233101,
      "entityCode": "BLL1",
      "entityDesc": "BLL2019",
      "entityDescLang1": "BLL2019#",
      "shortCode": "BLL",
      "seqNo": "1",
      "entityNameAlias": "BL",
      "entityNameAlias1": "BL#",
      "addressDetail": "详细地址111"}