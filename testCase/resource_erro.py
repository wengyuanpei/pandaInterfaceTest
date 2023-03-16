import requests

list=[
    8160,
8161,
8162,
8163,
8164,
8165,
8166,
8167,
8168,
8169,
8170,
8171,
8172,
8173,
8174,
8175,
8176,
8177,
8178,
8179,
8180,
8181,
8182,
8183,
8184,
8185,
8186,
8187,
8188,
8189,
8190,
8191,
8192,
8193,
8194,
8195,
8196,
8197,
8198,
8199,
8200,
8201,
8202,
8203,
8204,
8205,
8206,
8207,
8208,
8209,
8210,
8211,
8212,
8213,
8214,
8215,
8216,
8217,
8218,
8219
]
headerss={"Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNTYxOTY5MDMyMzU1Njg4NDQ5Iiwic3ViIjoie1wiaWRcIjoxNTYxOTY5MDMyMzU1Njg4NDQ5LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTY5NDQzMTUwNH0.9ToNPthEBzk602y4XeCSxQdzo7csBunc-nqFCHZExaVoS0XJia75q7Zf5kvLele85mOcDyUDv5H4rGN777V06A"}

url="https://hear-pre.abctime.com/v1/media/audio/"
for resource in list:
    errolist=[]
    url_end=url+str(resource)
    print("请求地址",url_end)
    reqqq=requests.get(url=url_end,headers=headerss)
    print(reqqq.json())



