#coding:utf-8
import requests
'''
curl -H 'PANDA-USE-NEW-VERSION: 2' -H 'PANDA-UID: 136' -H 'PANDA-TOKEN: 654a074f405d9' -H 'channel: 2' -H 'versionCode: 351' -H 'versionName: 6.5.1' -H 'xh-debug: 1' -H 'Content-Type: application/json; charset=utf-8' -H 'Host: api-dev.abctime.com' -H 'User-Agent: okhttp/4.8.0' --data-binary '{"dict_type":2,"sign":"e77aad175cf3c1531177df2e52a5094545a7d5e18bb0f14b1d354c714d89031d"}' --compressed 'http://api-dev.abctime.com/v5/book/book-config-map'

'''
map1={
		"list": [{
			"id": 75,
			"dictName": "aa",
			"dictCode": 3,
			"bookNum": 185,
			"wordNum": 615
		}, {
			"id": 76,
			"dictName": "A",
			"dictCode": 4,
			"bookNum": 93,
			"wordNum": 461
		}, {
			"id": 77,
			"dictName": "B",
			"dictCode": 5,
			"bookNum": 97,
			"wordNum": 514
		}, {
			"id": 78,
			"dictName": "C",
			"dictCode": 6,
			"bookNum": 95,
			"wordNum": 558
		}, {
			"id": 79,
			"dictName": "D",
			"dictCode": 7,
			"bookNum": 88,
			"wordNum": 559
		}, {
			"id": 80,
			"dictName": "E",
			"dictCode": 8,
			"bookNum": 86,
			"wordNum": 505
		}, {
			"id": 81,
			"dictName": "F",
			"dictCode": 9,
			"bookNum": 83,
			"wordNum": 491
		}, {
			"id": 82,
			"dictName": "G",
			"dictCode": 10,
			"bookNum": 83,
			"wordNum": 478
		}, {
			"id": 83,
			"dictName": "H",
			"dictCode": 11,
			"bookNum": 77,
			"wordNum": 430
		}, {
			"id": 84,
			"dictName": "I",
			"dictCode": 12,
			"bookNum": 70,
			"wordNum": 381
		}, {
			"id": 85,
			"dictName": "J",
			"dictCode": 13,
			"bookNum": 74,
			"wordNum": 414
		}, {
			"id": 86,
			"dictName": "K",
			"dictCode": 14,
			"bookNum": 69,
			"wordNum": 102
		}, {
			"id": 87,
			"dictName": "L",
			"dictCode": 15,
			"bookNum": 66,
			"wordNum": 133
		}, {
			"id": 88,
			"dictName": "M",
			"dictCode": 16,
			"bookNum": 52,
			"wordNum": 129
		}, {
			"id": 89,
			"dictName": "N",
			"dictCode": 17,
			"bookNum": 53,
			"wordNum": 136
		}, {
			"id": 90,
			"dictName": "O",
			"dictCode": 18,
			"bookNum": 49,
			"wordNum": 134
		}, {
			"id": 91,
			"dictName": "P",
			"dictCode": 19,
			"bookNum": 44,
			"wordNum": 166
		}, {
			"id": 92,
			"dictName": "Q",
			"dictCode": 20,
			"bookNum": 54,
			"wordNum": 180
		}, {
			"id": 93,
			"dictName": "R",
			"dictCode": 21,
			"bookNum": 54,
			"wordNum": 206
		}, {
			"id": 94,
			"dictName": "S",
			"dictCode": 22,
			"bookNum": 44,
			"wordNum": 213
		}, {
			"id": 95,
			"dictName": "T",
			"dictCode": 23,
			"bookNum": 43,
			"wordNum": 221
		}, {
			"id": 96,
			"dictName": "U",
			"dictCode": 24,
			"bookNum": 42,
			"wordNum": 246
		}, {
			"id": 97,
			"dictName": "V",
			"dictCode": 25,
			"bookNum": 32,
			"wordNum": 201
		}, {
			"id": 98,
			"dictName": "W",
			"dictCode": 26,
			"bookNum": 37,
			"wordNum": 243
		}, {
			"id": 99,
			"dictName": "X",
			"dictCode": 27,
			"bookNum": 41,
			"wordNum": 261
		}, {
			"id": 100,
			"dictName": "Y",
			"dictCode": 28,
			"bookNum": 45,
			"wordNum": 257
		}, {
			"id": 101,
			"dictName": "Z",
			"dictCode": 29,
			"bookNum": 112,
			"wordNum": 496
		}]}


listt=map1['list']
aaa=0
for i in listt:
    aaa+=i["bookNum"]
print(aaa)